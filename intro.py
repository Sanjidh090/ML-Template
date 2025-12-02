import numpy as nnp
import pandas as pd
import os
# Loop through all directories and filenames in the input folder
for dirname, _, filenames in os.walk('/kaggle/input'):
    # Print the first 10 filenames
    for i, filename in enumerate(filenames):
        if i >= 5:
            break
        print(os.path.join(dirname, filename))
