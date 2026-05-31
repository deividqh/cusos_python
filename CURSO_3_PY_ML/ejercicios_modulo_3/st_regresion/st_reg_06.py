import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, r2_score

# Configuración de página en modo ancho estándar
# st.set_page_config(layout="wide", page_title="Actividad 6 - Polinomial")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Ejercicio 06: Regresión Polinomial para Series Temporales")

# ■■■■■ 2. PANEL DE CONTROLES ■■■■■
st.markdown("### 🎛️ Panel de Simulación y Control")
with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        n_meses = st.slider("Meses de histórico (Tiempo):", min_value=12, max_value=60, value=36, step=1)
    with c2:
        ruido = st.slider("Volatilidad del mercado:", min_value=10, max_value=200, value=60, step=10)
    with c3:
        mes_test = st.number_input("Mes a predecir (Prueba extrapolación):", min_value=1, max_value=100, value=40)

# ■■■■■ 3. ENUNCIADO EN COLLAPSE (Debajo de los controles) ■■■■■
ENUNCIADO = """ Actividad 6 - Trayectoria de Mercado: 
Un producto nuevo presenta una curva de ventas que aumenta rápido y luego se estabiliza. 
Aplica una Regresión Polinomial de grado 2 y grado 3, y elige visualmente cuál captura mejor la tendencia.

• Para esta Actividad 6, vamos a introducir la Regresión Polinomial. Matemáticamente, esto se logra tomando nuestra variable $x$ (el tiempo) y elevándola al cuadrado ($x^2$) y al cubo ($x^3$) mediante PolynomialFeatures de Scikit-Learn, para luego aplicarle una Regresión Lineal estándar.Visualmente es un ejercicio fantástico para Plotly, ya que podremos ver cómo la curva de Grado 2 (parábola) inevitablemente empezará a caer al final, mientras que el Grado 3 o intenta estabilizarse o se dispara, demostrando el gran riesgo de usar polinomios para predecir el futuro.

• He configurado Plotly con hovermode='x unified'. 
Si pasas el ratón por el gráfico, te mostrará una línea vertical interactiva indicando el valor de los puntos exactos sobre la coordenada $x$, lo cual es perfecto para series temporales (meses).He añadido un pequeño bloque condicional en las conclusiones y la gráfica que proyecta la línea un poco más adelante del histórico de datos para que puedas enseñar qué pasa cuando un polinomio intenta adivinar el futuro (normalmente se hunden de golpe o salen disparados hacia el infinito).
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ PROCESAMIENTO DE DATOS Y MODELADO ■■■■■
np.random.seed(42)

# Generamos X (Meses)
X_raw = np.arange(1, n_meses + 1).reshape(-1, 1)

# Generamos Y (Ventas que suben rápido y se estabilizan simulando una función logarítmica)
# Ecuación teórica: Ventas = 500 * log(Mes) + Ruido
y = 500 * np.log(X_raw.flatten()) + np.random.normal(0, ruido, n_meses)
y = np.clip(y, 0, None)  # No hay ventas negativas

# Transformaciones Polinomiales
poly2 = PolynomialFeatures(degree=2)
poly3 = PolynomialFeatures(degree=3)

X_poly2 = poly2.fit_transform(X_raw)
X_poly3 = poly3.fit_transform(X_raw)

# Entrenamiento de Modelos
modelo_g2 = LinearRegression().fit(X_poly2, y)
modelo_g3 = LinearRegression().fit(X_poly3, y)

# Predicciones sobre el histórico
y_pred_g2 = modelo_g2.predict(X_poly2)
y_pred_g3 = modelo_g3.predict(X_poly3)

# DataFrame para la columna izquierda
df_resultados = pd.DataFrame({
    'Mes (X)': X_raw.flatten(),
    'Ventas Reales (Y)': y,
    'Predicción Grado 2': y_pred_g2,
    'Predicción Grado 3': y_pred_g3
})

# Predicción del mes interactivo seleccionado por el usuario
X_test = np.array([[mes_test]])
pred_test_g2 = modelo_g2.predict(poly2.transform(X_test))[0]
pred_test_g3 = modelo_g3.predict(poly3.transform(X_test))[0]

# Preparamos una línea más larga (hasta el mes de test) para trazar la curva completa en el gráfico
max_x_plot = max(n_meses, mes_test) + 5
X_plot = np.linspace(1, max_x_plot, 100).reshape(-1, 1)
y_plot_g2 = modelo_g2.predict(poly2.transform(X_plot))
y_plot_g3 = modelo_g3.predict(poly3.transform(X_plot))


# ■■■■■ 4. DOS COLUMNAS (DATOS Y GRÁFICO PLOTLY) ■■■■■
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 Tabla de Comparación")
    st.dataframe(
        df_resultados.style.format({
            'Mes (X)': '{:.0f}', 
            'Ventas Reales (Y)': '{:.1f}', 
            'Predicción Grado 2': '{:.1f}', 
            'Predicción Grado 3': '{:.1f}'
        }), 
        height=450
    )

with col_grafico:
    st.markdown("### 📉 Ajuste Polinomial (Interactivo)")
    
    fig = go.Figure()
    
    # Datos Reales
    fig.add_trace(go.Scatter(
        x=df_resultados['Mes (X)'], y=df_resultados['Ventas Reales (Y)'],
        mode='markers', marker=dict(color='#1f77b4', size=8, opacity=0.7),
        name='Ventas Históricas',
        hovertemplate='<b>Mes:</b> %{x}<br><b>Ventas:</b> %{y:.1f}<extra></extra>'
    ))
    
    # Curva Grado 2
    fig.add_trace(go.Scatter(
        x=X_plot.flatten(), y=y_plot_g2,
        mode='lines', line=dict(color='#ff7f0e', width=3, dash='dash'),
        name='Polinomio Grado 2', hoverinfo='skip'
    ))
    
    # Curva Grado 3
    fig.add_trace(go.Scatter(
        x=X_plot.flatten(), y=y_plot_g3,
        mode='lines', line=dict(color='#2ca02c', width=3),
        name='Polinomio Grado 3', hoverinfo='skip'
    ))

    # Marcadores de extrapolación (Tu Predicción)
    fig.add_trace(go.Scatter(
        x=[mes_test, mes_test], y=[pred_test_g2, pred_test_g3],
        mode='markers', 
        marker=dict(color=['#ff7f0e', '#2ca02c'], size=14, symbol='star', line=dict(color='black', width=1)),
        name=f'Predicción Mes {mes_test}',
        hovertemplate='<b>Extrapolación Mes %{x}</b><br>Estimado: %{y:.1f}<extra></extra>'
    ))

    fig.update_layout(
        xaxis_title='Tiempo (Meses)',
        yaxis_title='Volumen de Ventas',
        margin=dict(l=10, r=10, t=10, b=10),
        hovermode='x unified',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450
    )
    
    st.plotly_chart(fig, width='stretch')

# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
st.markdown("---")
st.markdown("### 📊 Conclusiones y Evaluación del Modelo")

c_g2, c_g3, c_conclu = st.columns([1, 1, 2])

with c_g2:
    st.markdown("#### 🟠 Modelo Grado 2 ($x^2$)")
    st.metric("Precisión (R²)", f"{r2_score(y, y_pred_g2):.3f}")
    st.metric("Error Medio (MAE)", f"{mean_absolute_error(y, y_pred_g2):.1f}")
    
with c_g3:
    st.markdown("#### 🟢 Modelo Grado 3 ($x^3$)")
    st.metric("Precisión (R²)", f"{r2_score(y, y_pred_g3):.3f}")
    st.metric("Error Medio (MAE)", f"{mean_absolute_error(y, y_pred_g3):.1f}")

with c_conclu:
    st.info("""
    💡 **El peligro de la extrapolación polinomial:** Observa el gráfico configurando el 'Mes a predecir' más allá de tu histórico (por ejemplo, el mes 50). Aunque ambos modelos puedan tener un R² muy alto en los datos conocidos, el **Polinomio de Grado 2** es una parábola ($y = ax^2+bx+c$) que terminará forzosamente cayendo hacia abajo, pronosticando un desplome de ventas irreal. 
    
    Visualmente, en curvas de saturación/estabilización, es crucial inspeccionar el comportamiento de la curva proyectada y no fiarse únicamente del error matemático (MAE).
    """)