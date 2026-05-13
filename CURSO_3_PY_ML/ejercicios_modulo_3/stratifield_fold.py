# Configuramos 3 Folds
import numpy as np
from sklearn.model_selection import StratifiedKFold, KFold

# Creamos datos: 12 muestras (9 de clase 0, 3 de clase 1)
X = np.ones(12)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1])

# Configuramos 3 Folds
skf = StratifiedKFold(n_splits=3)

print(f"Proporción original: {np.bincount(y)[0]} ceros, {np.bincount(y)[1]} unos\n")

for i, (train_index, test_index) in enumerate(skf.split(X, y)):
    y_train, y_test = y[train_index], y[test_index]
    
    print(f"--- FOLD {i+1} ---")
    print(f"  Entrenamiento: {np.bincount(y_train)} (ceros/unos)")
    print(f"  Test:          {np.bincount(y_test)} (ceros/unos)")