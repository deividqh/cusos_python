import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Configurar semilla para reproducibilidad
np.random.seed(42)

# 1. Generación de Datos de Línea de Base (Entrenamiento)
n_samples = 1000
X_baseline = np.random.normal(loc=10, scale=2, size=(n_samples, 1))
noise = np.random.normal(loc=0, scale=1, size=(n_samples, 1))
y_baseline = 3.5 * X_baseline + noise

# Entrenamiento del modelo inicial
model = LinearRegression()
model.fit(X_baseline, y_baseline)

# 2. Simulación de Escenarios en Producción

# Escenario A: Sin Deriva (No Drift)
X_test_no_drift = np.random.normal(loc=10, scale=2, size=(n_samples, 1))
y_test_no_drift = 3.5 * X_test_no_drift + np.random.normal(loc=0, scale=1, size=(n_samples, 1))

# Escenario B: Deriva de Datos (Data Drift) - Desplazamiento de la característica X
X_test_data_drift = np.random.normal(loc=18, scale=2, size=(n_samples, 1)) # La media cambia de 10 a 18
y_test_data_drift = 3.5 * X_test_data_drift + np.random.normal(loc=0, scale=1, size=(n_samples, 1)) # La relación matemática es idéntica

# Escenario C: Deriva de Concepto (Concept Drift) - Cambio en la relación entre X e Y
X_test_concept_drift = np.random.normal(loc=10, scale=2, size=(n_samples, 1)) # La distribución de X es idéntica
y_test_concept_drift = 1.5 * X_test_concept_drift + np.random.normal(loc=0, scale=1, size=(n_samples, 1)) # La pendiente pasa de 3.5 a 1.5

# 3. Evaluación del modelo en producción
y_pred_no_drift = model.predict(X_test_no_drift)
y_pred_data_drift = model.predict(X_test_data_drift)
y_pred_concept_drift = model.predict(X_test_concept_drift)

# Cálculo de métricas
mae_no_drift = mean_absolute_error(y_test_no_drift, y_pred_no_drift)
r2_no_drift = r2_score(y_test_no_drift, y_pred_no_drift)

mae_data_drift = mean_absolute_error(y_test_data_drift, y_pred_data_drift)
r2_data_drift = r2_score(y_test_data_drift, y_pred_data_drift)

mae_concept_drift = mean_absolute_error(y_test_concept_drift, y_pred_concept_drift)
r2_concept_drift = r2_score(y_test_concept_drift, y_pred_concept_drift)

print("--- RESULTADOS DE EVALUACIÓN DEL MODELO ---")
print(f"Escenario: Sin Deriva (No Drift)")
print(f"  MAE: {mae_no_drift:.4f}")
print(f"  R2: {r2_no_drift:.4f}")
print(f"Escenario: Deriva de Datos (Data Drift)")
print(f"  MAE: {mae_data_drift:.4f}")
print(f"  R2: {r2_data_drift:.4f}")
print(f"Escenario: Deriva de Concepto (Concept Drift)")
print(f"  MAE: {mae_concept_drift:.4f}")
print(f"  R2: {r2_concept_drift:.4f}")

# 4. Creación de gráficos explicativos
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Subgráfico 1: Histograma de Características (Data Drift)
axes[0].hist(X_baseline, bins=30, alpha=0.6, label='Línea de Base (Entrenamiento)', color='#1f77b4')
axes[0].hist(X_test_data_drift, bins=30, alpha=0.6, label='Nuevos Datos (Data Drift)', color='#ff7f0e')

axes[0].set_title('Deriva de Datos (Data Drift):\nCambio en la Distribución de la Característica X')
axes[0].set_xlabel('Valor de la Característica X')
axes[0].set_ylabel('Frecuencia')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.5)

# Subgráfico 2: Relación X contra Y (Concept Drift)
axes[1].scatter(X_test_no_drift[:100], y_test_no_drift[:100], color='#1f77b4', alpha=0.6, label='Sin Deriva (Reales)')
axes[1].scatter(X_test_concept_drift[:100], y_test_concept_drift[:100], color='#d62728', alpha=0.6, label='Con Deriva de Concepto (Reales)')

x_range = np.linspace(5, 15, 100).reshape(-1, 1)
y_range_pred = model.predict(x_range)

axes[1].plot(x_range, y_range_pred, color='black', linewidth=3, linestyle='--', label='Predicción del Modelo Entrenado')

axes[1].set_title('Deriva de Concepto (Concept Drift):\nCambio en la Relación Y = f(X)')
axes[1].set_xlabel('Característica X')
axes[1].set_ylabel('Variable Objetivo Y')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()