import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Configuración de página en modo ancho estándar
st.set_page_config(layout="wide", page_title="Actividad 5 - Diseño Limpio")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD (EL PRIMER ELEMENTO) ■■■■■
st.markdown("### Ejercicio 05: Regresión con Variables Categóricas (OHE)")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE (Letras normales) ■■■■■
ENUNCIADO = """ Actividad 5 - Eficiencia Energética con Categorías: 
Predice el gasto en calefacción de una vivienda usando los metros cuadrados y la 
variable categórica “Tipo de Aislamiento” (Pobre, Medio, Excelente). No olvides usar One-Hot Encoding.

• En este ejercicio, la magia está en el One-Hot Encoding. Como los modelos matemáticos no entienden la palabra "Excelente" o "Pobre", tenemos que convertir esa columna en múltiples columnas de ceros y unos.
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)


# ■■■■■ 3. PANEL DE CONTROLES (UBICADO SOBRE LAS COLUMNAS, NO FIJO) ■■■■■
st.markdown("### 🎛️ Panel de Simulación y Control")
# Usamos border=True para enmarcar los controles de forma elegante y limpia
with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        n_viviendas = st.number_input("Número de Viviendas:", min_value=50, max_value=500, value=150)
    with c2:
        ruido = st.slider("Variabilidad climática (€):", 10, 150, 40, 5)
    with c3:
        area_test = st.number_input("Metros Cuadrados (Predicción):", 40, 300, 100, 5)
    with c4:
        aisl_test = st.selectbox("Aislamiento (Predicción):", ['Pobre', 'Medio', 'Excelente'])


# ■■■■■ PROCESAMIENTO DE DATOS Y MODELADO (Background) ■■■■■
np.random.seed(42)

# Generación del Dataset Sintético
area = np.random.uniform(50, 250, n_viviendas)
aislamientos = np.random.choice(['Pobre', 'Medio', 'Excelente'], n_viviendas)

costo = area * 5.0
costo += np.where(aislamientos == 'Pobre', area * 3.5, 0)
costo -= np.where(aislamientos == 'Excelente', area * 2.0, 0)
costo += np.random.normal(0, ruido, n_viviendas)
costo = np.clip(costo, 50, None)

df = pd.DataFrame({
    'Metros Cuadrados': area,
    'Aislamiento': aislamientos,
    'Gasto Calefacción (€)': costo
})

# Transformación One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['Aislamiento'], dtype=int)

X = df_encoded.drop('Gasto Calefacción (€)', axis=1)
y = df_encoded['Gasto Calefacción (€)']

# Entrenamiento
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# Predicción del caso del Panel de Control
input_test = pd.DataFrame(columns=X.columns)
input_test.loc[0] = 0 
input_test['Metros Cuadrados'] = area_test
columna_activa = f'Aislamiento_{aisl_test}'
if columna_activa in input_test.columns:
    input_test[columna_activa] = 1

prediccion_test = modelo.predict(input_test)[0]


# --- 4. DOS COLUMNAS (DATOS A LA IZQUIERDA, GRÁFICO INTERACTIVO A LA DERECHA) ---
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 Histórico de Datos")
    tab1, tab2 = st.tabs(["Datos OHE (Modelo)", "Datos Originales"])
    with tab1:
        st.dataframe(df_encoded.style.format({'Metros Cuadrados': '{:.1f}', 'Gasto Calefacción (€)': '{:.2f} €'}), height=400)
    with tab2:
        st.dataframe(df.style.format({'Metros Cuadrados': '{:.1f}', 'Gasto Calefacción (€)': '{:.2f} €'}), height=400)

with col_grafico:
    st.markdown("### 📉 Impacto del Aislamiento: Metros vs Gasto (Plotly)")
    
    # Creación del gráfico interactivo con Plotly
    fig = go.Figure()
    colores = {'Pobre': '#d62728', 'Medio': '#ff7f0e', 'Excelente': '#2ca02c'}
    
    for categoria in ['Pobre', 'Medio', 'Excelente']:
        mask = df['Aislamiento'] == categoria
        
        # Nube de puntos (Scatter)
        fig.add_trace(go.Scatter(
            x=df[mask]['Metros Cuadrados'],
            y=df[mask]['Gasto Calefacción (€)'],
            mode='markers',
            marker=dict(color=colores[categoria], size=7, opacity=0.6),
            name=f'Casas: {categoria}',
            hovertemplate='<b>Área:</b> %{x:.1f} m²<br><b>Gasto:</b> %{y:.2f} €<extra></extra>'
        ))
        
        # Líneas de tendencia calculadas por el modelo para cada categoría
        X_linea = pd.DataFrame(columns=X.columns)
        X_linea['Metros Cuadrados'] = np.linspace(50, 250, 10)
        for col in X.columns:
            if 'Aislamiento' in col:
                X_linea[col] = 1 if col == f'Aislamiento_{categoria}' else 0
        
        y_linea = modelo.predict(X_linea)
        
        fig.add_trace(go.Scatter(
            x=X_linea['Metros Cuadrados'],
            y=y_linea,
            mode='lines',
            line=dict(color=colores[categoria], width=2.5),
            name=f'Recta {categoria}',
            hoverinfo='skip'
        ))

    # Marcador de la simulación actual del usuario
    fig.add_trace(go.Scatter(
        x=[area_test],
        y=[prediccion_test],
        mode='markers',
        marker=dict(color='black', size=14, symbol='star', line=dict(color='white', width=1)),
        name='Tu Predicción',
        hovertemplate='<b>Tu Simulación:</b><br>Área: %{x} m²<br>Est. Gasto: %{y:.2f} €<extra></extra>'
    ))

    # Estilizado de Plotly
    fig.update_layout(
        xaxis_title='Superficie de la Vivienda (Metros Cuadrados)',
        yaxis_title='Gasto en Calefacción (€)',
        margin=dict(l=10, r=10, t=10, b=10),
        hovermode='closest',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=400
    )
    
    st.plotly_chart(fig, width='stretch')


# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
st.markdown("---")
st.markdown("### 📊 Conclusiones y Métricas del Modelo")

m1, m2, m3 = st.columns(3)
m1.metric("Gasto Estimado (Tu Simulación)", f"{prediccion_test:,.2f} €")
m2.metric("Precisión del Modelo (R²)", f"{r2_score(y, y_pred):.3f}")
m3.metric("Error Medio (MAE)", f"{mean_absolute_error(y, y_pred):,.2f} €")

st.info("💡 **Estructura del Dashboard:** Este orden de lectura respeta el estándar natural. El título nos da el contexto del ejercicio, el enunciado se oculta para no estorbar una vez leído, los controles modifican los parámetros globales y de predicción, y de un solo vistazo podemos comparar la tabla de datos a la izquierda con el comportamiento gráfico interactivo a la derecha, concluyendo con las métricas del modelo en el pie de página.")