import os
import json
import subprocess

# ================= CONFIGURATION =================
# 1. Credentials
# Based on your path, I assume your username is 'rlsalvi'. Change if incorrect.
KAGGLE_USERNAME = secret_value_1

# I removed the 'KGAT_' prefix to get the standard 32-char key. 
# If your key actually includes 'KGAT_', put it back.
KAGGLE_KEY = secret_value_0

# 2. Dataset Info
DATASET_TITLE = "16GB_0.4_corrputed"
DATASET_SLUG = "corrpted_chunk-processed" # URL friendly name (letters, numbers, hyphens)

# 3. Directories
# The folder containing your processed wav files and metadata.csv
UPLOAD_DIR = "/kaggle/working/corrupted"
# =================================================

def upload_dataset():
    # --- Step 1: Set Authentication Environment Variables ---
    os.environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME
    os.environ['KAGGLE_KEY'] = KAGGLE_KEY

    print(f"Authenticated as: {KAGGLE_USERNAME}")

    # --- Step 2: Create dataset-metadata.json ---
    # This file is required by Kaggle to know what you are uploading.
    metadata = {
        "title": DATASET_TITLE,
        "id": f"{KAGGLE_USERNAME}/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}], # Public Domain
        "subtitle": "Processed 16kHz WAV chunks + Metadata CSV for Bengali ASR"
    }

    metadata_path = os.path.join(UPLOAD_DIR, "dataset-metadata.json")
    
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
        
    print(f"Created metadata file at: {metadata_path}")

    # --- Step 3: Run the Kaggle Upload Command ---
    print("Starting upload... this might take a while depending on file size.")
    
    # We use 'create' for a new dataset. 
    # If you run this again later to update it, change 'create' to 'version'
    command = f"kaggle datasets create -p {UPLOAD_DIR} --dir-mode zip"
    
    try:
        # Run the command line tool from Python
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode('utf-8'))
        print("\nSUCCESS! Dataset uploaded.")
        print(f"View it at: https://www.kaggle.com/{KAGGLE_USERNAME}/{DATASET_SLUG}")
    except subprocess.CalledProcessError as e:
        print("\nERROR during upload:")
        print(e.output.decode('utf-8'))

if __name__ == "__main__":
    # Ensure the directory exists
    if os.path.exists(UPLOAD_DIR):
        upload_dataset()
    else:
        print(f"Error: Directory {UPLOAD_DIR} does not exist. Run the processing scripts first.")
