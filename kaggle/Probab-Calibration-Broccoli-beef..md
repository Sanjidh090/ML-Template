# Probability calibration can improve your score
```https://www.kaggle.com/competitions/playground-series-s5e7/discussion/587685```
Most models predict probabilities that would then be thresholded to give label predictions. The default threshold is 0.5 but you can tune it to optimize the accuracy score. In scikit-learn, you can use the meta-class TunedThresholdClassifierCV for that purpose (requires version 1.5+).

A different approach is to keep the threshold fixed at 0.5 and calibrate the probabilities instead.

```python
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.calibration import CalibratedClassifierCV

X = pd.read_csv('/kaggle/input/playground-series-s5e7/train.csv', index_col='id')
y = X.pop('Personality').map({'Introvert':1, 'Extrovert':0})
X['Stage_fear'] = X['Stage_fear'].map({'No':0, 'Yes':1})
X['Drained_after_socializing'] = X['Drained_after_socializing'].map({'No':0, 'Yes':1})

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

base_models = {
    'xgb': XGBClassifier(n_jobs=4, random_state=0),
    'lgb': LGBMClassifier(n_jobs=4, random_state=0, verbose=-1),
    'cb': CatBoostClassifier(thread_count=4, random_state=0, verbose=0)
}

for m in base_models:
    model = base_models[m]
    y_pred = cross_val_predict(model, X, y, cv=kfold)
    score = accuracy_score(y, y_pred)
    print(F'{m}: {score:.6f}')
    model = CalibratedClassifierCV(
        model, cv=kfold
    )
    y_pred = cross_val_predict(model, X, y, cv=kfold)
    score = accuracy_score(y, y_pred)
    print(F'calibrated {m}: {score:.6f}')    
```
```python
xgb: 0.967664
calibrated xgb: 0.968149
lgb: 0.968797
calibrated lgb: 0.968851
cb: 0.968311
calibrated cb: 0.968473
```

