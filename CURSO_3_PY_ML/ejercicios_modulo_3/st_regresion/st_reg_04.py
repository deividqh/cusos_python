import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Configuración de diseño ancho para simular paneles izquierdo/derecho
# st.set_page_config(layout="wide")

# Cabecera original tal cual fue provista
st.markdown("### Ejercicio 04: Regresión Lineal Múltiple")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE (Letras normales) ■■■■■
ENUNCIADO = """ Actividad 5 - Eficiencia Energética con Categorías: 
Predice el gasto en calefacción de una vivienda usando los metros cuadrados y la 
variable categórica “Tipo de Aislamiento” (Pobre, Medio, Excelente). No olvides usar One-Hot Encoding.

En este ejercicio pasamos de la regresión simple a la Regresión Lineal Múltiple. 
Dado que ahora manejamos tres variables predictoras independientes (Antigüedad, Kilometraje y HP), 
la visualización óptima cambia: en lugar de trazar una única línea en dos dimensiones, utilizaremos un gráfico de "Valores Reales vs. Valores Predichos", que es el estándar en ciencia de datos para evaluar visualmente el ajuste de modelos de múltiples dimensiones

Al pasar a una regresión múltiple, la función matemática optimiza un plano (o hiperplano) en lugar de una simple línea recta. La gráfica de Valores Reales vs. Valores Predichos implementada aquí te permite verificar visualmente la calidad de la predicción general: cuanto más estrecha y cercana esté la nube de puntos a la línea diagonal discontinua roja, más preciso será tu modelo multivariable.
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ PANEL IZQUIERDO (Controles en la Sidebar) ■■■■■
st.sidebar.header("🎛️ Panel Izquierdo: Controles")

# Parámetros del Dataset Sintético
n_vehiculos = st.sidebar.slider("Número de Vehículos en el Historial:", min_value=30, max_value=500, value=120, step=10)
ruido_mercado = st.sidebar.slider("Volatilidad del Mercado (Ruido en €):", min_value=500, max_value=5000, value=2000, step=100)

st.sidebar.markdown("---")
st.sidebar.subheader("🚗 Tasador Interactivo")
# Controles para la predicción de un caso individual
antiguedad_test = st.sidebar.slider("Antigüedad del coche (Años):", min_value=0, max_value=20, value=6, step=1)
km_test = st.sidebar.slider("Kilometraje acumulado (Km):", min_value=0, max_value=300000, value=90000, step=5000)
hp_test = st.sidebar.slider("Potencia del motor (HP):", min_value=60, max_value=400, value=140, step=10)


# ■■■■■ PROCESAMIENTO DE DATOS ■■■■■
np.random.seed(42)

# Generación de variables independientes realistas y correlacionadas
antiguedad = np.random.uniform(0, 18, n_vehiculos)
# El kilometraje suele depender de la antigüedad del vehículo
km = (antiguedad * np.random.uniform(10000, 18000, n_vehiculos)) + np.random.uniform(0, 12000, n_vehiculos)
hp = np.random.uniform(70, 320, n_vehiculos)

# Ecuación teórica de tasación: Precio Base de 30,000€
# Pierde 1,100€ por año, pierde 0.05€ por kilómetro y gana 95€ por cada HP de potencia.
precio = 30000 - (1100 * antiguedad) - (0.05 * km) + (95 * hp) + np.random.normal(0, ruido_mercado, n_vehiculos)
# Limitamos los precios para evitar valores negativos sinsentido en el mercado real
precio = np.clip(precio, 700, 95000)

# Estructuración del DataFrame para visualización de los datos de trabajo
df_coches = pd.DataFrame({
    'Antigüedad (Años)': antiguedad,
    'Kilometraje (Km)': km,
    'Potencia (HP)': hp,
    'Precio Real (€)': precio
})

# Separación de características (X) y variable objetivo (y)
X = df_coches[['Antigüedad (Años)', 'Kilometraje (Km)', 'Potencia (HP)']]
y = df_coches['Precio Real (€)']

# Ajuste del modelo multivariable
modelo_multiple = LinearRegression()
modelo_multiple.fit(X, y)
y_pred = modelo_multiple.predict(X)

# Extracción de Coeficientes e Indicadores
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
coefs = modelo_multiple.coef_
intercepto = modelo_multiple.intercept_

# Predicción del coche configurado en el panel izquierdo
coche_usuario = np.array([[antiguedad_test, km_test, hp_test]])
tasacion_estimada = max(700, modelo_multiple.predict(coche_usuario)[0])


# ■■■■■ PANEL DERECHO (Resultados, Datos y Gráfico de Pyplot) ■■■■■
col_datos, col_resultados = st.columns([1.3, 2])

with col_datos:
    st.subheader("📋 Datos de Trabajo")
    st.write("Historial de vehículos utilizados para entrenar el tasador:")
    st.dataframe(
        df_coches.style.format({
            'Antigüedad (Años)': '{:.1f}', 
            'Kilometraje (Km)': '{:,.0f}', 
            'Potencia (HP)': '{:.0f}', 
            'Precio Real (€)': '{:,.2f} €'
        }),
        height=520
    )

with col_resultados:
    st.subheader("📊 Panel Derecho: Resultados de la Regresión Múltiple")
    
    # Despliegue de métricas globales de evaluación
    m1, m2 = st.columns(2)
    m1.metric(label="Error Absoluto Medio (MAE)", value=f"{mae:,.2f} €")
    m2.metric(label="Coeficiente de Determinación (R²)", value=f"{r2:.2f}")
    
    # Cuadro de tasación personalizada basada en el panel de control
    st.info(f"✨ **Valoración Estimada:** Un coche con **{antiguedad_test} años**, **{km_test:,} Km** y **{hp_test} HP** tiene un valor estimado de mercado de **{tasacion_estimada:,.2f} €**")
    
    # Desglose de la ecuación matemática calculada automáticamente
    with st.expander("🔍 Ver Impacto Individual de las Variables (Coeficientes)"):
        st.write(f"**Intercepto (Precio base teórico):** {intercepto:,.2f} €")
        st.write(f"📉 **Por cada año de antigüedad:** El precio disminuye `{coefs[0]:,.2f} €` de forma neta.")
        st.write(f"📉 **Por cada kilómetro recorrido:** El precio disminuye `{coefs[1]:,.4f} €` (aproximadamente {coefs[1]*10000:,.2f} € cada 10,000 Km).")
        st.write(f"📈 **Por cada unidad de HP adicional:** El precio incrementa `{coefs[2]:,.2f} €` de forma neta.")

    st.markdown("### 📉 Evaluación Visual del Ajuste (Reales vs Predichos)")
    
    # Generación de la gráfica matemática con Pyplot
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Graficamos el valor real contra la predicción del modelo para cada punto del dataset
    ax.scatter(y, y_pred, color='#9467bd', alpha=0.6, edgecolors='white', label='Vehículos del Historial')
    
    # Línea ideal de referencia a 45 grados (donde Real == Predicho)
    limites = [int(min(y.min(), y_pred.min())), int(max(y.max(), y_pred.max()))]
    ax.plot(limites, limites, color='#d62728', linestyle='-', linewidth=2, label='Ajuste Perfecto (Ideal)')
    
    # Añadir el punto que el usuario está cotizando desde el panel de control
    ax.scatter([tasacion_estimada], [tasacion_estimada], color='#ff7f0e', s=180, zorder=5, edgecolor='black', label='Tu Vehículo Simulado')
    
    # Estilizado del gráfico multivariable
    ax.set_xlabel('Precio Real Registrado (€)')
    ax.set_ylabel('Precio Predicho por el Modelo (€)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend(loc='upper left')
    
    st.pyplot(fig)