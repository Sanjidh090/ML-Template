# 🧰 ML Collections

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)

**A curated collection of ready-to-use ML/Data Science code snippets and utilities**

*Stop rewriting the same exploratory data analysis code — just copy, paste, and explore!* 🚀

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Scripts](#-scripts) • [Kaggle Resources](#-kaggle-resources) • [Contributing](#-contributing)

</div>

---

## 📖 About

ML Collections is a practical repository containing reusable Python scripts and utilities for machine learning and data science workflows. Whether you're working on Kaggle competitions or exploring datasets, this collection provides battle-tested code snippets that save time and reduce repetitive coding.

### 💡 Why This Repository?

- **⚡ Quick Start**: Copy-paste ready code for common ML tasks
- **🎯 Practical**: Real-world utilities used in actual Kaggle competitions
- **📊 Exploratory**: Tools focused on dataset exploration and visualization
- **🔧 Modular**: Each script is self-contained and easy to integrate
- **📚 Educational**: Learn from curated Kaggle resources and techniques

---

## ✨ Features

- **Data Exploration Tools**: Quickly analyze datasets with unique value counting and visualizations
- **Distribution Analysis**: Compare train/test distributions with KDE and box plots
- **Dataset Utilities**: Print directory trees and explore Kaggle dataset structures
- **Kaggle Resources**: Curated collection of valuable discussions and notebooks
- **TensorFlow Setup**: Pre-configured environment setup scripts

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Required Libraries

Install the necessary dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

For TensorFlow-based scripts:

```bash
pip install tensorflow
```

### Clone the Repository

```bash
git clone https://github.com/Sanjidh090/ml-collections.git
cd ml-collections
```

---

## 📝 Usage

### Quick Start: Dataset Exploration

The simplest way to explore a dataset:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load your dataset
df = pd.read_csv('path/to/your/dataset.csv')

# Analyze unique values
for column in df.columns:
    print(f"="*100)
    print(f" Unique values in {column}:")
    print(df[column].value_counts())

print(f"=="*50)
print(f" Unique Value Report:")
print(df.nunique())

# Visualize distributions
df.hist(figsize=(16, 16), bins=30)
plt.tight_layout()
plt.show()
```

---

## 📦 Scripts

### 1. `unique.py` - Unique Value Analysis

**Purpose**: Quickly analyze unique values and distributions in your dataset.

**Features**:
- Count unique values per column
- Display value frequency distributions
- Generate histogram visualizations

**Usage**:
```python
# Analyze any CSV file
df = pd.read_csv('/path/to/dataset.csv')
# Run the unique value analysis (see script for details)
```

---

### 2. `plot_train_test_csv.py` - Train/Test Distribution Comparison

**Purpose**: Compare feature distributions between training and test sets to detect data drift.

**Features**:
- Automatic label encoding for categorical variables
- KDE (Kernel Density Estimation) plots
- Box plots for outlier detection
- Train vs Test comparison for all features

**Key Functions**:

- `convert_all_to_numeric(train, test)`: Converts all columns to numeric format
- `dist_plots(train, test, num_features)`: Generates distribution comparison plots

**Usage**:
```python
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Convert and get numeric columns
tr_all, te_all, numeric_cols = convert_all_to_numeric(train, test)

# Plot distributions
dist_plots(tr_all, te_all, numeric_cols)
```

---

### 3. `intro.py` - Environment Setup

**Purpose**: Standard setup script for TensorFlow-based Kaggle notebooks.

**Features**:
- TensorFlow version upgrade
- Protobuf compatibility fix
- CPU-only mode (CUDA disabled)
- Log level configuration
- Dataset file exploration

**Usage**:
```python
# Run at the start of your Kaggle notebook
# Automatically lists first 5 files in /kaggle/input
```

---

### 4. `prompt_style_dataset.py` - Directory Tree Visualization

**Purpose**: Print dataset directory structure in a clean ASCII tree format.

**Features**:
- Recursive directory traversal
- Beautiful ASCII tree formatting
- Error handling for permissions and missing paths

**Usage**:
```python
from prompt_style_dataset import print_tree

# Print dataset structure
print_tree("/path/to/dataset")
```

**Output Example**:
```
Dataset structure for: /kaggle/working/
├── data
│   ├── train.csv
│   └── test.csv
└── models
    └── model_v1.pkl
```

---

## 📚 Kaggle Resources

The [`kaggle/`](./kaggle) directory contains a curated collection of valuable Kaggle discussions, notebooks, and insights:

- **Pseudo-labelling Techniques** ([Pseudo-labelling___Chris_Deotte.md](./kaggle/Pseudo-labelling___Chris_Deotte.md))
- **Probability Calibration** ([Probab-Calibration-Broccoli-beef..md](./kaggle/Probab-Calibration-Broccoli-beef..md))
- **Code Robustness Tips** ([Code_robust?.md](./kaggle/Code_robust?.md))

These resources serve as a personal knowledge base for:
- 💡 Competition strategies and winning approaches
- 🔍 Advanced ML techniques
- 🛠️ Practical tips discovered across various competitions
- 📖 Concepts to revisit when they become relevant

Check out the [Kaggle README](./kaggle/readme.md) for more details!

---

## 🛠️ Additional Resources

- **[Markdown Cheatsheet](./Markdown_cheatsheet.md)**: Quick reference for Markdown syntax

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-utility`)
3. **Commit** your changes (`git commit -m 'Add amazing utility'`)
4. **Push** to the branch (`git push origin feature/amazing-utility`)
5. **Open** a Pull Request

### Guidelines

- Keep scripts self-contained and well-documented
- Add usage examples in comments
- Follow existing code style
- Test your code before submitting

---

## 📄 License

This project is open source and available for educational and personal use.

---

## 🙏 Acknowledgments

- Inspired by common Kaggle workflows and community best practices
- Built for the data science community to reduce repetitive coding
- Special thanks to Kaggle competition participants for sharing insights

---

## 📬 Contact

**Author**: Sanjidh090

**Repository**: [github.com/Sanjidh090/ml-collections](https://github.com/Sanjidh090/ml-collections)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for the Data Science Community

</div>
