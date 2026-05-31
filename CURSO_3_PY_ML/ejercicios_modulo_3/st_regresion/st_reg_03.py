import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configuración de diseño ancho para simular los paneles izquierdo/derecho
# st.set_page_config(layout="wide")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### ejercicio 3: El Algoritmo desde Cero")

# Enunciado exacto y visible sin adaptaciones
ENUNCIADO = """ Actividad 3 - El Algoritmo desde Cero: 
Calcula manualmente los parámetros de una recta que relacione los “Minutos de uso de una App” con la “Batería consumida”. 
Valida tus cálculos comparándolos con el resultado de Scikit-Learn.

• El truco del "Reshaped" en Scikit-LearnExplicación: El paso X.reshape(-1, 1) es obligatorio y crucial en tu explicación.Motivo técnico: NumPy maneja X como un vector unidimensional (un array de 1D con forma (n,)). Scikit-Learn está diseñado para regresiones lineales múltiples, por lo que exige estrictamente una matriz bidimensional (n_muestras, n_características). El -1 le dice a NumPy que calcule automáticamente el número de filas basándose en el tamaño del array original, y el 1 fuerza la creación de una sola columna.
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ PANEL IZQUIERDO (Controles en la Sidebar) ■■■■■
st.sidebar.header("🎛️ Panel Izquierdo: Controles")

# Controles para manipular el tamaño del dataset y la dispersión del experimento
n_muestras = st.sidebar.slider("Cantidad de registros (Dispositivos):", min_value=5, max_value=150, value=25, step=5)
pendiente_teorica = st.sidebar.slider("Tasa teórica de consumo (mAh/min):", min_value=0.5, max_value=4.0, value=1.8, step=0.1)
ruido_bateria = st.sidebar.slider("Variabilidad/Ruido en el consumo:", min_value=0.0, max_value=20.0, value=8.0, step=0.5)


# ■■■■■ PROCESAMIENTO Y CÁLCULOS MATEMÁTICOS ■■■■■
np.random.seed(42)

# X: Minutos de uso continuo de la aplicación (entre 5 y 90 minutos)
X = np.random.uniform(5, 90, n_muestras)
# Y: Batería consumida en mAh (Ecuación base + ruido aleatorio)
y = 12.0 + (pendiente_teorica * X) + np.random.normal(0, ruido_bateria, n_muestras)
y = np.clip(y, 0, None)  # Evitamos consumos negativos por excesos de ruido

# Dataframe requerido para visualizar los datos con los que se trabaja
df_datos = pd.DataFrame({
    'Minutos de Uso (X)': X,
    'Batería Consumida (Y)': y
})

# 1️⃣ CÁLCULO MANUAL (Desde cero aplicando fórmulas analíticas)
X_media = np.mean(X)
y_media = np.mean(y)

# Fórmula de la pendiente: Beta_1 = Cov(X,Y) / Var(X)
numerador = np.sum((X - X_media) * (y - y_media))
denominador = np.sum((X - X_media) ** 2)

beta_1_manual = numerador / denominador
# Fórmula del intercepto: Beta_0 = Y_media - Beta_1 * X_media
beta_0_manual = y_media - (beta_1_manual * X_media)

# 2️⃣ VALIDACIÓN CON SCIKIT-LEARN
modelo_sklearn = LinearRegression()
X_reshaped = X.reshape(-1, 1)  # Scikit-learn requiere matriz 2D para las características
modelo_sklearn.fit(X_reshaped, y)

beta_1_sklearn = modelo_sklearn.coef_[0]
beta_0_sklearn = modelo_sklearn.intercept_


# ■■■■■ PANEL DERECHO (Resultados, Datos y Gráfico de Pyplot) ■■■■■
col_datos, col_resultados = st.columns([1, 2])

with col_datos:
    st.subheader("📋 Datos de Trabajo")
    st.write("Mediciones del consumo de batería:")
    st.dataframe(
        df_datos.style.format({'Minutos de Uso (X)': '{:.1f}', 'Batería Consumida (Y)': '{:.2f}'}),
        height=500
    )

with col_resultados:
    st.subheader("📊 Panel Derecho: Validación del Algoritmo")
    
    # Distribución en dos columnas internas para contrastar los parámetros calculados
    c_manual, c_sklearn = st.columns(2)
    
    with c_manual:
        st.markdown("#### ✍️ Ecuaciones Manuales")
        st.metric(label="Intercepto ($\\beta_0$)", value=f"{beta_0_manual:.4f}")
        st.metric(label="Pendiente ($\\beta_1$)", value=f"{beta_1_manual:.4f}")
        
    with c_sklearn:
        st.markdown("#### 🤖 Biblioteca Scikit-Learn")
        st.metric(label="`intercept_` ($\\beta_0$)", value=f"{beta_0_sklearn:.4f}")
        st.metric(label="`coef_[0]` ($\\beta_1$)", value=f"{beta_1_sklearn:.4f}")
        
    # Mensaje dinámico de comparación matemática
    if np.isclose(beta_0_manual, beta_0_sklearn) and np.isclose(beta_1_manual, beta_1_sklearn):
        st.success("✅ **¡Validación Perfecta!** Los parámetros obtenidos mediante las fórmulas matemáticas manuales coinciden de manera idéntica con los coeficientes optimizados de Scikit-Learn.")
    else:
        st.error("⚠️ Existe una diferencia numérica en las aproximaciones.")

    st.markdown("### 📉 Visualización de Ajustes con Pyplot")
    
    # Generación de la gráfica
    fig, ax = plt.subplots(figsize=(8, 4.2))
    
    # Dispersión de los puntos reales
    ax.scatter(X, y, color='#bcbd22', alpha=0.8, edgecolors='black', linewidth=0.7, label='Dispositivos Medidos')
    
    # Generar la línea recta de predicción
    X_linea = np.linspace(0, 100, 100)
    y_recta_manual = beta_0_manual + (beta_1_manual * X_linea)
    y_recta_sklearn = beta_0_sklearn + (beta_1_sklearn * X_linea)
    
    # Dibujamos ambas líneas (una sólida y otra discontinua ligeramente más delgada para notar el solapamiento perfecto)
    ax.plot(X_linea, y_recta_manual, color='#1f77b4', linewidth=3.5, label='Recta Analítica (Manual)')
    ax.plot(X_linea, y_recta_sklearn, color='#d62728', linewidth=1.5, linestyle='--', label='Recta Scikit-Learn')
    
    # Estilizado del gráfico
    ax.set_xlabel('Minutos de Uso Continuo de la App')
    ax.set_ylabel('Batería Consumida (mAh)')
    ax.set_xlim(0, 100)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left')
    
    # Despliegue en Streamlit
    st.pyplot(fig)