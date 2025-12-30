train = pd.read_csv('/kaggle/input/mercor-cheating-detection/train.csv')
test = pd.read_csv('/kaggle/input/mercor-cheating-detection/test.csv')
target = 'is_cheating'
train = train.drop(columns=[target])
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

def convert_all_to_numeric(train, test):
    """
    Converts ALL columns in train/test to numeric (LabelEncoding for objects),
    safely handling columns that exist only in one dataset.
    """
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder

    tr, te = train.copy(), test.copy()
    encoders = {}

    # unify columns intersection (ignore target like Dropout that’s train-only)
    common_cols = sorted(set(tr.columns).intersection(set(te.columns)))

    for col in common_cols:
        if tr[col].dtype == "O" or str(tr[col].dtype).startswith("category"):
            le = LabelEncoder()
            combined = pd.concat([tr[col].astype(str), te[col].astype(str)], axis=0)
            le.fit(combined)
            tr[col] = le.transform(tr[col].astype(str))
            te[col] = le.transform(te[col].astype(str))
            encoders[col] = le
        else:
            tr[col] = pd.to_numeric(tr[col], errors="coerce")
            te[col] = pd.to_numeric(te[col], errors="coerce")

    # handle train-only numeric columns like target
    for col in set(tr.columns) - set(te.columns):
        if tr[col].dtype == "O":
            le = LabelEncoder()
            tr[col] = le.fit_transform(tr[col].astype(str))
        else:
            tr[col] = pd.to_numeric(tr[col], errors="coerce")

    # clean infinities / NaNs
    tr.replace([np.inf, -np.inf], np.nan, inplace=True)
    te.replace([np.inf, -np.inf], np.nan, inplace=True)
    tr.fillna(tr.mean(numeric_only=True), inplace=True)
    te.fillna(te.mean(numeric_only=True), inplace=True)

    num_cols = tr.select_dtypes(include="number").columns.tolist()
    return tr, te, num_cols


def dist_plots(train, test, num_features):
    """
    Plot KDE + Boxplots for numeric columns.
    """
    print("\nDistribution analysis (all numeric/object columns converted)\n")
    df = pd.concat(
        [train[num_features].assign(Source="Train"),
         test[num_features].assign(Source="Test")],
        axis=0, ignore_index=True
    )

    n = len(num_features)
    fig, axes = plt.subplots(
        n, 2,
        figsize=(18, n * 4),
        gridspec_kw={"hspace": 0.3, "wspace": 0.2, "width_ratios": [0.70, 0.30]}
    )
    if n == 1:
        axes = np.array([axes])

    for i, col in enumerate(num_features):
        # KDE
        ax = axes[i, 0]
        sns.kdeplot(data=df, x=col, hue="Source",
                    palette=["#3cb371", "#0483ff"], ax=ax, linewidth=2)
        ax.set(xlabel="", ylabel="")
        ax.set_title(f"{col}")
        ax.grid()

        # Boxplot
        ax = axes[i, 1]
        sns.boxplot(data=df, y=col, x="Source", width=0.5,
                    linewidth=1, fliersize=1, ax=ax, palette=["#3cb371", "b"])
        ax.set(xlabel="", ylabel="")
        ax.set_title(f"{col}")
        ax.set_xticklabels(["Train", "Test"])

    plt.tight_layout()
    plt.show()
    
# 1️⃣ Convert everything to numeric
tr_all, te_all, numeric_cols = convert_all_to_numeric(train, test)

print("Numeric columns used for distribution plots:")
print(numeric_cols)

# 2️⃣ Plot all feature distributions
dist_plots(tr_all, te_all, [c for c in numeric_cols if c != target])
