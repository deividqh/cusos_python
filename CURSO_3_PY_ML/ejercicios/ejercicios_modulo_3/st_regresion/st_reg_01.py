import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Configuración de diseño ancho para simular perfectamente los paneles izq/der
# st.set_page_config(layout="wide")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### ejercicio 1: Regresión Lineal Simple")

# Enunciado exacto y visible tal cual lo solicitaste
ENUNCIADO = """ Actividad 1 - Rendimiento Académico: 
    Una academia desea predecir la nota final de un alumno basada únicamente en las horas de estudio semanales. 
    Genera un dataset sintético y aplica una Regresión Lineal Simple. Visualiza el resultado.

    A diferencia de Scikit-Learn, statsmodels asume por defecto que la línea pasa por el origen $(0,0)$. Por eso debemos usar explícitamente sm.add_constant(X) para calcular el intercepto ($\beta_0$).
"""
st.code(ENUNCIADO, language="text")

# ■■■■■ PANEL IZQUIERDO (Controles en la Sidebar) ■■■■■
st.sidebar.header("🎛️ Panel Izquierdo: Controles")

# Controles interactivos para manipular el dataset sintético
n_muestras = st.sidebar.slider("Número de Alumnos (Muestras):", min_value=10, max_value=300, value=100, step=10)
ruido = st.sidebar.slider("Dispersión/Ruido de los datos:", min_value=0.0, max_value=3.0, value=1.2, step=0.1)

st.sidebar.markdown("---")
st.sidebar.subheader("🔮 Predicción Individual")
horas_test = st.sidebar.slider("Simular horas de estudio para un alumno:", min_value=0.0, max_value=24.0, value=12.0, step=0.5)


# ■■■■■ PROCESAMIENTO DE DATOS EN BACKGROUND ■■■■■
np.random.seed(42)  # Semilla para consistencia al mover controles

# Generamos X (Horas de estudio semanales entre 2 y 22 horas)
X = np.random.uniform(2, 22, n_muestras).reshape(-1, 1)

# Generamos Y (Nota final basada en una ecuación lineal teórica + ruido)
# Ecuación base: Nota = 1.5 + 0.4 * Horas
y = 1.5 + 0.4 * X.flatten() + np.random.normal(0, ruido, n_muestras)
y = np.clip(y, 0, 10)  # Aseguramos que las notas reales estén en el rango de 0 a 10

# Construcción del DataFrame para cumplir con "visualizar los datos con los que se trabaja"
df_datos = pd.DataFrame({
    'Horas de Estudio (X)': X.flatten(),
    'Nota Final Real (Y)': y
})

# Ajuste del modelo de Regresión Lineal Simple
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# Cálculo de métricas requeridas para el análisis
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Predicción interactiva basada en el control del usuario
nota_predicha = modelo.predict([[horas_test]])[0]
nota_predicha = np.clip(nota_predicha, 0, 10)


# ■■■■■ PANEL DERECHO (Resultados, Datos y Gráfico de Pyplot) ■■■■■
# Dividimos el área principal en dos columnas: Datos a la izquierda y Gráfico/Métricas a la derecha
col_datos, col_resultados = st.columns([1, 2])

with col_datos:
    st.subheader("📋 Datos de Trabajo")
    st.write("Tabla completa del dataset sintético generado:")
    # Mostramos el dataframe formateado
    st.dataframe(
        df_datos.style.format({'Horas de Estudio (X)': '{:.1f}', 'Nota Final Real (Y)': '{:.2f}'}),
        height=500
    )

with col_resultados:
    st.subheader("📊 Panel Derecho: Resultados del Modelo")
    
    # Visualización de métricas clave
    m1, m2 = st.columns(2)
    m1.metric(label="Error Absoluto Medio (MAE)", value=f"{mae:.2f}")
    m2.metric(label="Precisión del Modelo (R²)", value=f"{r2:.2f}")
    
    # Cuadro informativo de la predicción realizada mediante el panel de control
    st.info(f"**Resultado de Predicción:** Un alumno que estudie **{horas_test} horas** obtendrá una nota estimada de **{nota_predicha:.2f}/10**")
    
    st.markdown("### 📉 Visualización con Pyplot")
    
    # Generación del gráfico estadístico con Matplotlib (Pyplot)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    # 1. Nube de puntos de los datos del DataFrame
    ax.scatter(X, y, color='#1f77b4', alpha=0.7, edgecolors='none', label='Alumnos Reales')
    
    # 2. Línea de tendencia estimada por la regresión
    X_linea = np.linspace(0, 24, 100).reshape(-1, 1)
    y_linea = modelo.predict(X_linea)
    ax.plot(X_linea, y_linea, color='#d62728', linewidth=2.5, label='Línea de Regresión')
    
    # 3. Marcador del alumno interactivo seleccionado en los controles
    ax.scatter([[horas_test]], [[nota_predicha]], color='#ff7f0e', s=150, zorder=5, edgecolor='black', label='Alumno Simulado')
    
    # Estilizado básico y limpio del gráfico
    ax.set_xlabel('Horas de Estudio Semanales')
    ax.set_ylabel('Nota Final (0-10)')
    ax.set_xlim(0, 24)
    ax.set_ylim(-0.5, 10.5)
    ax.grid(True, linestyle='-', alpha=0.5)
    ax.legend(loc='upper left')
    
    # Despliegue del gráfico en la interfaz de Streamlit
    st.pyplot(fig)