import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss

# Configuración de página en modo ancho estándar
# st.set_page_config(layout="wide", page_title="Actividad 8 - Regresión Logística")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Ejercicio 08: Regresión Logística: Diagnóstico Médico de Hipertensión")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE ■■■■■
ENUNCIADO = """Actividad 8 - Diagnóstico Médico (Logística): Entrena un modelo de Regresión
Logística para predecir si un paciente tiene riesgo de hipertensión (1: Riesgo, 0: Normal)
basado en su nivel de estrés y edad.

Aunque el nombre empiece por "Regresión", la Regresión Logística es en realidad un algoritmo de Clasificación. Esto significa un cambio de paradigma emocionante respecto a los ejercicios anteriores: ya no predecimos un valor continuo (como el dinero o la temperatura), sino la probabilidad de pertenecer a una categoría discreta (0 o 1).

Para adaptarnos perfectamente a este problema de clasificación manteniendo nuestra estructura de diseño interactivo con Plotly, la mejor visualización posible ya no es una línea de tendencia, sino un Gráfico de Dispersión con Frontera de Decisión. El modelo trazará una línea divisoria en el plano cartesiano (Nivel de Estrés vs. Edad) que separará la zona de "Riesgo" de la zona "Normal".
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)


# ■■■■■ 3. PANEL DE CONTROLES ■■■■■
st.markdown("### 🎛️ Panel de Simulación y Control")
with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        n_pacientes = st.number_input("Número de Pacientes:", min_value=30, max_value=500, value=150)
    with c2:
        ruido_clinico = st.slider("Solapamiento/Ruido Clínico:", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
    with c3:
        edad_test = st.slider("Edad del Paciente (Predicción):", min_value=18, max_value=90, value=50)
    with c4:
        estres_test = st.slider("Nivel de Estrés (0-10) (Predicción):", min_value=0.0, max_value=10.0, value=6.0, step=0.5)


# ■■■■■ 4. PROCESAMIENTO DE DATOS Y MODELADO (Background) ■■■■■
np.random.seed(42)

# Generación de variables independientes aleatorias pero realistas
edad = np.random.uniform(20, 85, n_pacientes)
estres = np.random.uniform(1, 10, n_pacientes)

# Ecuación logística interna (log-odds): a mayor edad y estrés, más probabilidad de riesgo
# log_odds = beta_0 + beta_1 * edad + beta_2 * estres
log_odds = -6.5 + (0.07 * edad) + (0.45 * estres) + np.random.normal(0, ruido_clinico, n_pacientes)

# Aplicamos la función sigmoide para convertir log-odds en probabilidades (0 a 1)
probabilidad_real = 1 / (1 + np.exp(-log_odds))

# Si la probabilidad es > 0.5 el paciente tiene riesgo (1), de lo contrario normal (0)
hipertension = (probabilidad_real > 0.5).astype(int)

df_pacientes = pd.DataFrame({
    'Edad': edad,
    'Nivel de Estrés': estres,
    'Diagnóstico (Hipertensión)': hipertension
})

# Entrenamiento de la Regresión Logística
X = df_pacientes[['Edad', 'Nivel de Estrés']]
y = df_pacientes['Diagnóstico (Hipertensión)']

modelo = LogisticRegression()
modelo.fit(X, y)

# Predicciones globales y métricas
y_pred = modelo.predict(X)
y_prob = modelo.predict_proba(X)[:, 1] # Extraemos solo la probabilidad del evento '1' (Riesgo)

precision = accuracy_score(y, y_pred)
perdida = log_loss(y, y_prob)

# Predicción interactiva para el paciente seleccionado por el usuario en el Panel de Control
paciente_nuevo = np.array([[edad_test, estres_test]])
diagnostico_test = modelo.predict(paciente_nuevo)[0]
probabilidad_test = modelo.predict_proba(paciente_nuevo)[0][1]


# --- 4. DOS COLUMNAS (DATOS A LA IZQUIERDA, GRÁFICO INTERACTIVO A LA DERECHA) ---
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 Historial Clínico (Dataset)")
    # Mapeamos los 0 y 1 a texto solo para la visualización del DataFrame
    df_visual = df_pacientes.copy()
    df_visual['Diagnóstico (Hipertensión)'] = df_visual['Diagnóstico (Hipertensión)'].map({1: '🔴 Riesgo', 0: '🟢 Normal'})
    st.dataframe(
        df_visual.style.format({'Edad': '{:.0f} años', 'Nivel de Estrés': '{:.1f}/10'}),
        height=450
    )

with col_grafico:
    st.markdown("### 📉 Mapa de Diagnóstico y Frontera de Decisión (Plotly)")
    
    fig = go.Figure()
    
    # 1. Puntos: Pacientes Normales (0)
    normales = df_pacientes[df_pacientes['Diagnóstico (Hipertensión)'] == 0]
    fig.add_trace(go.Scatter(
        x=normales['Edad'], y=normales['Nivel de Estrés'],
        mode='markers', marker=dict(color='#2ca02c', size=8, opacity=0.7),
        name='Pacientes Normales',
        hovertemplate='<b>Paciente Normal</b><br>Edad: %{x:.0f} años<br>Estrés: %{y:.1f}/10<extra></extra>'
    ))
    
    # 2. Puntos: Pacientes con Riesgo (1)
    riesgo = df_pacientes[df_pacientes['Diagnóstico (Hipertensión)'] == 1]
    fig.add_trace(go.Scatter(
        x=riesgo['Edad'], y=riesgo['Nivel de Estrés'],
        mode='markers', marker=dict(color='#d62728', size=8, opacity=0.7),
        name='Pacientes con Riesgo',
        hovertemplate='<b>Paciente en Riesgo</b><br>Edad: %{x:.0f} años<br>Estrés: %{y:.1f}/10<extra></extra>'
    ))

    # 3. Cálculo matemático de la Línea Frontera de Decisión
    # En la Regresión Logística la frontera ocurre cuando la probabilidad es exactamente 0.5,
    # lo cual matemáticamente equivale a: intercepto + b1*Edad + b2*Estrés = 0
    # Despejando el Estrés (Eje Y): Estrés = -(intercepto + b1*Edad) / b2
    b0 = modelo.intercept_[0]
    b1, b2 = modelo.coef_[0][0], modelo.coef_[0][1]
    
    edad_linea = np.linspace(20, 85, 100)
    estres_linea = -(b0 + b1 * edad_linea) / b2
    
    fig.add_trace(go.Scatter(
        x=edad_linea, y=estres_linea,
        mode='lines', line=dict(color='black', width=2.5, dash='dash'),
        name='Frontera de Decisión', hoverinfo='skip'
    ))

    # 4. Marcador del paciente simulado actual
    color_simulado = '#d62728' if diagnostico_test == 1 else '#2ca02c'
    fig.add_trace(go.Scatter(
        x=[edad_test], y=[estres_test],
        mode='markers',
        marker=dict(color=color_simulado, size=15, symbol='star', line=dict(color='white', width=1.5)),
        name='Tu Paciente Simulado',
        hovertemplate='<b>Consulta Actual:</b><br>Edad: %{x} años<br>Estrés: %{y:.1f}/10<extra></extra>'
    ))

    # Estilizado del Layout del mapa médico
    fig.update_layout(
        xaxis_title='Edad del Paciente',
        yaxis_title='Nivel de Estrés (0 a 10)',
        xaxis=dict(range=[15, 90]),
        yaxis=dict(range=[0, 11]),
        margin=dict(l=10, r=10, t=10, b=10),
        hovermode='closest',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450
    )
    
    st.plotly_chart(fig, width='stretch')


# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
st.markdown("---")
st.markdown("### 📊 Conclusiones Clínicas y Métricas de Clasificación")

m1, m2, m3 = st.columns(3)

# Formateamos el cartel del paciente interactivo usando código HTML sutil nativo de Streamlit
if diagnostico_test == 1:
    m1.metric("Predicción del Paciente", "🔴 RIESGO ALTURADO", f"Probabilidad: {probabilidad_test*100:.1f}%")
else:
    m1.metric("Predicción del Paciente", "🟢 NORMAL", f"Probabilidad: {probabilidad_test*100:.1f}%")

m2.metric("Exactitud Global (Accuracy)", f"{precision*100:.1f} %", delta="Porcentaje de aciertos nulos")
m3.metric("Función de Pérdida (Log Loss)", f"{perdida:.3f}", delta="Menor entropía es mejor", delta_color="inverse")

st.info(f"""
💡 **Inferencia del Modelo de Clasificación:** A diferencia de la regresión tradicional que dibuja curvas sobre los puntos, la **Regresión Logística** calcula la probabilidad de riesgo y traza una frontera espacial (línea discontinua negra). 
* Si modificas los controles superiores y tu **Paciente Simulado (Estrella)** cruza hacia arriba de la línea, el algoritmo automáticamente cambiará el diagnóstico a **Riesgo** porque la probabilidad matemática superó el umbral del 50%.
* Prueba a subir el control de 'Solapamiento/Ruido Clínico'. Verás cómo los puntos rojos y verdes se mezclan en el mapa simulando historiales médicos complejos, provocando que la precisión global (Accuracy) disminuya.
""")