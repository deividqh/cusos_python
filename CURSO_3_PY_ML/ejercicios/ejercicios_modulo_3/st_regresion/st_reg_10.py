import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Configuración de página en modo ancho estándar
# st.set_page_config(layout="wide", page_title="Actividad 10 - Pipeline Final")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Ejercicio 10: Proyecto Final: Pipeline de Rendimiento Agrícola")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE ■■■■■
ENUNCIADO = """Actividad 10 - Proyecto Final: Rendimiento Agrícola: Desarrolla un Pipeline completo
para predecir las toneladas de cosecha por hectárea. Debes incluir: carga de datos
(sintéticos), división Train/Test, entrenamiento de una regresión múltiple (usando agua,
fertilizante y horas de sol) y reporte de métricas MSE y R2.
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ 3. PANEL DE CONTROLES ■■■■■
st.markdown("### 🎛️ Configuración del Pipeline y Predicción")
with st.container(border=True):
    st.markdown("**1. Parámetros del Experimento (Train/Test)**")
    c1, c2 = st.columns(2)
    with c1:
        n_parcelas = st.number_input("Total de Parcelas (Dataset):", min_value=100, max_value=2000, value=500, step=100)
    with c2:
        test_size = st.slider("Porcentaje para Test (Validación):", min_value=0.1, max_value=0.5, value=0.2, step=0.05, 
                              help="Porcentaje de datos que el modelo NO verá durante el entrenamiento.")
    
    st.markdown("---")
    st.markdown("**2. Tu Parcela (Predicción Interactiva)**")
    c3, c4, c5 = st.columns(3)
    with c3:
        agua_test = st.slider("Agua de Riego (L/m²):", 100, 1000, 450, 10)
    with c4:
        fert_test = st.slider("Fertilizante (Kg/ha):", 10, 200, 80, 5)
    with c5:
        sol_test = st.slider("Horas de Sol (Mensual):", 100, 350, 220, 10)

# ■■■■■ 4. PROCESAMIENTO DE DATOS: EL PIPELINE ■■■■■
np.random.seed(42)

# 1. Generación de Datos Sintéticos (3 variables independientes)
agua = np.random.uniform(100, 1000, n_parcelas)
fertilizante = np.random.uniform(10, 200, n_parcelas)
sol = np.random.uniform(100, 350, n_parcelas)

# Ecuación teórica: Rendimiento Base + Aportes - Excesos + Ruido
# Supongamos que demasiada agua ahoga la planta (relación ligeramente penalizada si es extrema, pero la haremos lineal simple aquí)
rendimiento = 2.5 + (0.015 * agua) + (0.04 * fertilizante) + (0.02 * sol) + np.random.normal(0, 1.5, n_parcelas)
rendimiento = np.clip(rendimiento, 0.5, None)

df_agricola = pd.DataFrame({
    'Agua (L/m²)': agua,
    'Fertilizante (Kg/ha)': fertilizante,
    'Horas Sol': sol,
    'Cosecha (Ton/ha)': rendimiento
})

X = df_agricola[['Agua (L/m²)', 'Fertilizante (Kg/ha)', 'Horas Sol']]
y = df_agricola['Cosecha (Ton/ha)']

# 2. División Train / Test (Paso crucial del Pipeline)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# 3. Entrenamiento del Modelo (Solo con Train)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. Evaluación del Modelo (Solo con Test)
y_pred_test = modelo.predict(X_test)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

# Predicción del usuario
parcela_usuario = np.array([[agua_test, fert_test, sol_test]])
prediccion_usuario = modelo.predict(parcela_usuario)[0]


# ■■■■■ 4. DOS COLUMNAS (DATOS Y GRÁFICO PLOTLY) ■■■■■
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 División de Datos")
    tab_train, tab_test = st.tabs([f"Datos Train ({len(X_train)})", f"Datos Test ({len(X_test)})"])
    
    with tab_train:
        st.write("El modelo aprendió de estos datos:")
        df_train_show = X_train.copy()
        df_train_show['Cosecha (Ton/ha)'] = y_train
        st.dataframe(df_train_show.style.format('{:.1f}'), height=400)
        
    with tab_test:
        st.write("Datos ocultos para el examen final:")
        df_test_show = X_test.copy()
        df_test_show['Cosecha (Ton/ha)'] = y_test
        st.dataframe(df_test_show.style.format('{:.1f}'), height=400)

with col_grafico:
    st.markdown("### 📉 Evaluación en Test: Real vs Predicción (Plotly)")
    
    fig = go.Figure()
    
    # Puntos de Prueba (Test Data)
    fig.add_trace(go.Scatter(
        x=y_test, y=y_pred_test,
        mode='markers', marker=dict(color='#8c564b', size=8, opacity=0.7),
        name='Parcelas de Prueba (Test)',
        hovertemplate='<b>Real:</b> %{x:.2f} Ton/ha<br><b>Predicho:</b> %{y:.2f} Ton/ha<extra></extra>'
    ))
    
    # Línea Ideal de Ajuste Perfecto
    min_val = min(y_test.min(), y_pred_test.min())
    max_val = max(y_test.max(), y_pred_test.max())
    fig.add_trace(go.Scatter(
        x=[min_val, max_val], y=[min_val, max_val],
        mode='lines', line=dict(color='#2ca02c', width=3, dash='dash'),
        name='Precisión Perfecta (100%)', hoverinfo='skip'
    ))

    # Marcador de la Simulación del Usuario (Posicionado sobre la línea ideal teórica para referencia)
    fig.add_trace(go.Scatter(
        x=[prediccion_usuario], y=[prediccion_usuario],
        mode='markers', 
        marker=dict(color='#ff7f0e', size=16, symbol='star', line=dict(color='black', width=1.5)),
        name='Tu Cosecha Estimada',
        hovertemplate='<b>Tu Parcela</b><br>Rendimiento Estimado: %{y:.2f} Ton/ha<extra></extra>'
    ))

    fig.update_layout(
        xaxis_title='Cosecha Real Histórica (Ton/ha)',
        yaxis_title='Cosecha Predicha por el Modelo (Ton/ha)',
        margin=dict(l=10, r=10, t=10, b=10),
        hovermode='closest',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450
    )
    
    # st.plotly_chart(fig, width='stretch')
    st.plotly_chart(fig, width='stretch')

# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
st.markdown("---")
st.markdown("### 📊 Conclusiones del Pipeline")

m1, m2, m3 = st.columns(3)

m1.metric("Tu Cosecha Estimada", f"{prediccion_usuario:.2f} Ton/ha", "Basado en tu clima/riego")
m2.metric("R² en Validación (Test)", f"{r2_test:.3f}", "Capacidad de generalización")
# El MSE suele ser alto numéricamente, por lo que a veces se usa RMSE, pero mostraremos el MSE pedido
m3.metric("Error Cuadrático Medio (MSE)", f"{mse_test:.2f}", "Penaliza errores grandes", delta_color="inverse")

st.success("""
🎉 **¡Proyecto Final Completado!** Has implementado un flujo de trabajo profesional. Dividir los datos en Train y Test garantiza que el $R^2$ que ves abajo no sea producto de "memorizar" (Overfitting), sino que refleja la capacidad real del modelo para predecir sobre parcelas agrícolas que jamás había visto antes.
""")