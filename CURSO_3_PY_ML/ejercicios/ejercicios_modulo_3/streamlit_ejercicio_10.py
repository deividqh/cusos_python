import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score

# --- Interfaz de Streamlit ---
st.title("🤖 Mini-AutoML para Regresión")
st.write("""
**Actividad 10**: Este script genera datos ruidosos, los escala y prueba automáticamente tres modelos de regresión para encontrar el que tiene el menor **Error Absoluto Medio (MAE)**.
""")

# 1. Generación y Preprocesamiento de datos
# Generamos X (características) y una 'y' continua (variable objetivo)
X = np.random.rand(100, 5)
# Creamos una relación lineal con algo de ruido para que los modelos tengan algo que aprender
y = (X[:, 0] * 10) + (X[:, 1] * 5) + (np.random.randn(100) * 2)

X_scaled = StandardScaler().fit_transform(X)

# 2. "Mini-AutoML" Manual para Regresión
modelos = [LinearRegression(), DecisionTreeRegressor(), SVR()]
resultados_mae = {}

for m in modelos:
    # Usamos neg_mean_absolute_error y lo multiplicamos por -1 para tener el MAE positivo
    scores = cross_val_score(m, X_scaled, y, cv=3, scoring='neg_mean_absolute_error')
    mae = -1 * scores.mean()
    resultados_mae[m.__class__.__name__] = mae

# 3. Resultado final (Buscamos el menor MAE)
ganador = min(resultados_mae, key=resultados_mae.get)

st.subheader("🏆 Modelo Ganador")
st.success(f"El ganador es **{ganador}** con un MAE de **{resultados_mae[ganador]:.2f}**")

# 4. Visualización con Pyplot
st.subheader("Comparativa de Rendimiento")

fig, ax = plt.subplots(figsize=(8, 5))
nombres = list(resultados_mae.keys())
valores = list(resultados_mae.values())

# Coloreamos el ganador de verde y el resto de gris para resaltarlo
colores = ['#2e7d32' if nombre == ganador else '#9e9e9e' for nombre in nombres]

ax.bar(nombres, valores, color=colores)
ax.set_ylabel('MAE (Menor es mejor)')
ax.set_title('Error Absoluto Medio por Modelo')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica en Streamlit
st.pyplot(fig)