!pip install pandarallel
import pandas as pd
import re
from bnunicodenormalizer import Normalizer
from num2bangla import TakaConverter
from pandarallel import pandarallel
import multiprocessing

# 1. Initialize Parallelization
# use_memory_fs=False is safer for Kaggle/Colab to avoid memory issues
num_cores = multiprocessing.cpu_count()
pandarallel.initialize(nb_workers=num_cores, progress_bar=True, use_memory_fs=False)

# 2. Global Initialization (Each worker will get access to these)
bnorm = Normalizer()
taka = TakaConverter()

def convert_number_to_words(text):
    def verbalize(match):
        num_str = match.group().replace(',', '')
        
        # Standardize digits
        b_digits = "০১২৩৪৫৬৭৮৯"
        e_digits = "0123456789"
        trans = str.maketrans(b_digits, e_digits)
        num_str = num_str.translate(trans)

        try:
            if '.' in num_str:
                parts = num_str.split('.')
                int_word = taka.convert(parts[0]).replace("টাকা", "").replace("পয়সা", "").strip()
                frac_word = taka.convert(parts[1]).replace("টাকা", "").replace("পয়সা", "").strip()
                return f"{int_word} দশমিক {frac_word}"
            else:
                return taka.convert(num_str).replace("টাকা", "").replace("পয়সা", "").strip()
        except:
            return num_str
    return re.sub(r'[0-9০-৯,]+(?:\.[0-9০-৯]+)?', verbalize, text)

def master_asr_cleaner(text):
    if not isinstance(text, str) or text.strip() == "":
        return ""

    # Step 1: Remove [tags] and >>
    text = re.sub(r'\[.*?\]', '', text)
    text = text.replace(">>", "")

    # Step 2: Verbalize Numbers
    text = convert_number_to_words(text)

    # Step 3: Word-by-word Normalization (Avoiding the "hultiple" error)
    words = text.split()
    normalized_words = []
    for word in words:
        try:
            res = bnorm(word)
            # Handle different return types of the library
            if hasattr(res, 'refined'):
                normalized_words.append(res.refined)
            elif isinstance(res, list) and len(res) > 0:
                normalized_words.append(res[0].refined)
            else:
                normalized_words.append(word)
        except:
            normalized_words.append(word)
    
    text = " ".join(normalized_words)

    # Step 4: Keep only Bengali characters and spaces
    text = re.sub(r'[^\u0980-\u09FF\s]', ' ', text)

    # Step 5: Clean extra whitespace
    return " ".join(text.split())

# --- THE FAST IMPORT/EXECUTION ---
print(f"🚀 Starting parallel cleaning on {num_cores} CPU cores...")

# Instead of .apply(), we use .parallel_apply()
df['transcription'] = df['transcription'].parallel_apply(master_asr_cleaner)

print("✅ Cleaning Complete!")
print(df[['transcription', 'cleaned_transcription']].head())
