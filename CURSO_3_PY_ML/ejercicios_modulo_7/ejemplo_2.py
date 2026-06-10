import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 1. Simulación de un Registrador de Experimentos (Mini MLflow)
class MiniMLflowTracker:
    def __init__(self):
        self.runs = []
        self.current_run = None

    def start_run(self, run_name):
        self.current_run = {
            "run_name": run_name,
            "params": {},
            "metrics": {},
            "model": None
        }

    def log_param(self, key, value):
        if self.current_run:
            self.current_run["params"][key] = value

    def log_metric(self, key, value):
        if self.current_run:
            self.current_run["metrics"][key] = value

    def log_model(self, model, model_name):
        if self.current_run:
            self.current_run["model"] = (model, model_name)

    def end_run(self):
        if self.current_run:
            self.runs.append(self.current_run)
            self.current_run = None

    def get_results_table(self):
        records = []
        for r in self.runs:
            row = {"run_name": r["run_name"]}
            for k, v in r["params"].items():
                row[f"param_{k}"] = v
            for k, v in r["metrics"].items():
                row[f"metric_{k}"] = v
            records.append(row)
        return pd.DataFrame(records)

# Helper para imprimir en Markdown sin dependencias externas
def to_markdown_manual(df):
    cols = df.columns
    header = "| " + " | ".join(map(str, cols)) + " |"
    separator = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        # Arreglado el salto de línea que rompía esta instrucción
        row_str = "| " + " | ".join(map(lambda val: f"{val:.4f}" if isinstance(val, float) else str(val), row)) + " |"
        rows.append(row_str)
    return "\n".join([header, separator] + rows)

# 2. Generación de Datos de Regresión
X, y = make_regression(n_samples=800, n_features=10, noise=15.0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
tracker = MiniMLflowTracker()

# 3. Entrenamiento y Tracking de Experimentos
hyperparameter_grid = [
    {"n_estimators": 10, "max_depth": 3},
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 10, "max_depth": 8},
    {"n_estimators": 50, "max_depth": 8},
    {"n_estimators": 100, "max_depth": 8},
    {"n_estimators": 100, "max_depth": 15}
]

for idx, config in enumerate(hyperparameter_grid):
    run_name = f"RF_Run_{idx+1}"
    tracker.start_run(run_name)

    tracker.log_param("n_estimators", config["n_estimators"])
    tracker.log_param("max_depth", config["max_depth"])

    # Entrenamiento del Algoritmo
    rf = RandomForestRegressor(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        random_state=42
    )
    rf.fit(X_train, y_train)

    # Predicciones y Métricas
    y_pred = rf.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Registro de Métricas y Modelo
    tracker.log_metric("RMSE", rmse)
    tracker.log_metric("MAE", mae)
    tracker.log_metric("R2", r2)
    tracker.log_model(rf, f"random_forest_v{idx+1}")
    tracker.end_run()

# 4. Mostrar la tabla de resultados
df_results = tracker.get_results_table()
print("--- TABLA DE EXPERIMENTOS (REGISTRO) ---")
print(to_markdown_manual(df_results))