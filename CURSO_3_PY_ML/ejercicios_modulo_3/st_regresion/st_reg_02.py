import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Configuración de diseño ancho
# st.set_page_config(layout="wide")

# Cabecera
st.title("Inferencia Estadística con Statsmodels")
# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### ejercicio 2: Inferencia Estadística con Statsmodels")


# Enunciado exacto y visible
ENUNCIADO = """ Actividad 2 - Satisfacción Laboral (Inferencia): 
Utiliza Statsmodels para analizar si el número de días de teletrabajo al mes influye significativamente en 
el “Score de Felicidad” de los empleados. 
Interpreta el p-valor para una confianza del 95%.
"""
st.code(ENUNCIADO, language="text")

# ■■■■■ PANEL IZQUIERDO (Controles en la Sidebar) ■■■■■
st.sidebar.header("🎛️ Panel Izquierdo: Controles")

n_empleados = st.sidebar.slider("Número de Empleados:", min_value=30, max_value=500, value=150, step=10)
# Este control es clave para aprender: permite simular si existe una relación real o si es puro ruido
impacto_real = st.sidebar.slider("Impacto real del teletrabajo (Coeficiente oculto):", min_value=-1.0, max_value=3.0, value=1.2, step=0.1)
ruido = st.sidebar.slider("Variabilidad (Ruido):", min_value=5.0, max_value=30.0, value=15.0, step=1.0)


# --- PROCESAMIENTO DE DATOS ---
np.random.seed(42)

# Generamos X: Días de teletrabajo al mes (de 0 a 20 días hábiles)
dias_teletrabajo = np.random.randint(0, 21, n_empleados)

# Generamos Y: Score de Felicidad (Base de 40 + impacto del teletrabajo + ruido)
felicidad = 40 + (impacto_real * dias_teletrabajo) + np.random.normal(0, ruido, n_empleados)
felicidad = np.clip(felicidad, 0, 100) # Aseguramos que el score se mantenga entre 0 y 100

df_datos = pd.DataFrame({
    'Días Teletrabajo (X)': dias_teletrabajo,
    'Score Felicidad (Y)': felicidad
})

# --- MODELADO CON STATSMODELS ---
X = df_datos['Días Teletrabajo (X)']
y = df_datos['Score Felicidad (Y)']

# Statsmodels requiere que añadamos manualmente la constante (el punto de corte en el eje Y)
X_const = sm.add_constant(X)

# Ajuste del modelo de Mínimos Cuadrados Ordinarios (OLS)
modelo = sm.OLS(y, X_const).fit()

# Extracción de métricas clave
p_valor = modelo.pvalues['Días Teletrabajo (X)']
r_cuadrado = modelo.rsquared
coeficiente = modelo.params['Días Teletrabajo (X)']
intercepto = modelo.params['const']


# --- PANEL DERECHO (Resultados, Datos y Gráfico de Pyplot) ---
col_datos, col_resultados = st.columns([1, 2])

with col_datos:
    st.subheader("📋 Datos de Trabajo")
    st.write("Muestra de empleados:")
    st.dataframe(
        df_datos.style.format({'Score Felicidad (Y)': '{:.1f}'}),
        height=500
    )

with col_resultados:
    st.subheader("📊 Panel Derecho: Inferencia y P-Valor")
    
    # Mostrar métricas
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Coeficiente Estimado", value=f"{coeficiente:.2f}")
    m2.metric(label="P-Valor", value=f"{p_valor:.4f}")
    m3.metric(label="R-Cuadrado (R²)", value=f"{r_cuadrado:.2f}")
    
    # Lógica de interpretación del P-Valor (Confianza 95% -> Alfa = 0.05)
    st.markdown("### 🧠 Interpretación (Nivel de Confianza 95%)")
    alfa = 0.05
    
    if p_valor < alfa:
        st.success(f"""
        **Resultado Significativo:** El p-valor ({p_valor:.4f}) es **menor que {alfa}**. 
        
        Rechazamos la hipótesis nula. Tenemos evidencia estadística suficiente (al 95% de confianza) para afirmar que el número de días de teletrabajo **SÍ influye significativamente** en la felicidad de los empleados.
        """)
    else:
        st.warning(f"""
        **Resultado NO Significativo:** El p-valor ({p_valor:.4f}) es **mayor o igual que {alfa}**. 
        
        No podemos rechazar la hipótesis nula. No hay evidencia estadística suficiente (al 95% de confianza) para afirmar que el teletrabajo influya en la felicidad. La ligera inclinación de la línea podría deberse simplemente a la casualidad.
        """)
    
    st.markdown("### 📉 Visualización del Ajuste OLS")
    
    # Gráfico con Pyplot
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Nube de puntos
    ax.scatter(X, y, color='#2ca02c', alpha=0.6, edgecolors='white', label='Empleados')
    
    # Línea de regresión
    X_linea = np.linspace(0, 20, 100)
    y_linea = intercepto + coeficiente * X_linea
    ax.plot(X_linea, y_linea, color='#d62728', linewidth=2.5, label='Línea de Tendencia (OLS)')
    
    ax.set_xlabel('Días de Teletrabajo al Mes')
    ax.set_ylabel('Score de Felicidad (0-100)')
    ax.set_xlim(-1, 21)
    ax.set_ylim(0, 105)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper left')
    
    st.pyplot(fig)
    
    # Extra: Añadimos un desplegable para ver el reporte clásico de Statsmodels (muy útil para aprender)
    with st.expander("Ver Reporte Completo de Statsmodels (summary)"):
        st.text(modelo.summary())