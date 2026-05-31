import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, recall_score, precision_score

# Configuración de página en modo ancho estándar
# st.set_page_config(layout="wide", page_title="Actividad 9 - Auditoría de Fraude")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Ejercicio 09: Auditoría de Modelos: Matriz de Confusión y Recall")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE ■■■■■
ENUNCIADO = """Actividad 9 - Auditoría de Modelos de Fraude: Has entrenado un modelo para
detectar transacciones fraudulentas. Genera la Matriz de Confusión y el reporte de
clasificación. Explica por qué, en este caso, el “Recall” (Sensibilidad) es más importante
que la “Accuracy” (Exactitud).
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ 3. PANEL DE CONTROLES ■■■■■
st.markdown("### 🎛️ Panel de Simulación de Auditoría")
with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        n_transacciones = st.number_input("Volumen de Transacciones:", min_value=1000, max_value=50000, value=10000, step=1000)
    with c2:
        tasa_fraude = st.slider("Tasa Real de Fraude (%):", min_value=0.5, max_value=15.0, value=2.0, step=0.5)
    with c3:
        # Este slider es la clave didáctica del ejercicio
        umbral = st.slider("Umbral de Decisión del Modelo (Paranoia):", min_value=0.1, max_value=0.9, value=0.5, step=0.05)

# ■■■■■ 4. PROCESAMIENTO DE DATOS (Simulación de un Modelo Evaluado) ■■■■■
np.random.seed(42)

# Calculamos cuántas transacciones son normales y cuántas fraude
n_fraudes = int(n_transacciones * (tasa_fraude / 100))
n_normales = n_transacciones - n_fraudes

# Simulamos la "Probabilidad de Fraude" que arrojaría un modelo logístico ya entrenado.
# Los normales suelen tener probabilidad baja, los fraudes alta, pero HAY SOLAPAMIENTO.
prob_normales = np.random.normal(loc=0.2, scale=0.15, size=n_normales)
prob_fraudes = np.random.normal(loc=0.75, scale=0.2, size=n_fraudes)

# Unimos los arrays y limitamos las probabilidades entre 0 y 1
y_prob = np.clip(np.concatenate([prob_normales, prob_fraudes]), 0, 1)

# Etiquetas reales: 0 para normal, 1 para fraude
y_true = np.concatenate([np.zeros(n_normales), np.ones(n_fraudes)])

# El modelo clasifica como "Fraude" (1) solo si la probabilidad supera el Umbral de Decisión
y_pred = (y_prob >= umbral).astype(int)

# ■■■■■ 4. CÁLCULO DE MÉTRICAS ■■■■■
cm = confusion_matrix(y_true, y_pred)
# Extraemos los cuadrantes (True Negative, False Positive, False Negative, True Positive)
TN, FP, FN, TP = cm.ravel()

exactitud = accuracy_score(y_true, y_pred)
sensibilidad = recall_score(y_true, y_pred) # Recall
precision_fraude = precision_score(y_true, y_pred, zero_division=0)


# ■■■■■ 4. DOS COLUMNAS (REPORTE Y MATRIZ VISUAL EN PLOTLY) ■■■■■
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 Reporte de Clasificación")
    
    st.metric("Exactitud Global (Accuracy)", f"{exactitud*100:.2f}%")
    
    st.markdown("#### Métricas Clave (Clase 1: Fraude)")
    st.metric("🔴 Recall (Sensibilidad)", f"{sensibilidad*100:.2f}%", 
              help="De todos los fraudes reales que hubo, ¿cuántos atrapó el modelo?")
    st.metric("🎯 Precision (Precisión)", f"{precision_fraude*100:.2f}%", 
              help="De todas las veces que el modelo gritó 'Fraude', ¿cuántas era fraude real?")
    
    # Reporte de texto clásico de Scikit-Learn (muy usado en la industria)
    with st.expander("Ver reporte crudo de Scikit-Learn"):
        reporte_crudo = classification_report(y_true, y_pred, target_names=['0: Normal', '1: Fraude'])
        st.text(reporte_crudo)

with col_grafico:
    st.markdown("### 📉 Matriz de Confusión (Plotly)")
    
    # Preparamos los textos enriquecidos para cada celda de la matriz
    textos_cm = [[f"Verdaderos Negativos (TN)<br><b>{TN:,.0f}</b><br>Normales bloqueados correctamente", 
                  f"Falsos Positivos (FP)<br><b>{FP:,.0f}</b><br>¡Normales bloqueados por error!"],
                 [f"Falsos Negativos (FN)<br><b>{FN:,.0f}</b><br>¡Fraudes que se escaparon!", 
                  f"Verdaderos Positivos (TP)<br><b>{TP:,.0f}</b><br>Fraudes detectados con éxito"]]

    # Matriz Z invertida verticalmente para que Plotly pinte el Real(1) arriba y Real(0) abajo
    z = [[FN, TP], [TN, FP]]
    textos_z = [textos_cm[1], textos_cm[0]]
    
    # Usamos Figure Factory para crear un heatmap anotado súper limpio
    fig = ff.create_annotated_heatmap(
        z=z, 
        x=['Predicho: Normal (0)', 'Predicho: Fraude (1)'],
        y=['Real: Fraude (1)', 'Real: Normal (0)'],
        annotation_text=textos_z,
        colorscale='Blues',
        showscale=False
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=400,
        xaxis=dict(title='Lo que predijo nuestro Modelo', side='bottom'),
        yaxis=dict(title='La Realidad (Etiqueta Verdadera)')
    )
    
    # Truco para cambiar el color de la fuente en celdas oscuras/claras automáticamente
    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 14
        
    st.plotly_chart(fig, width='stretch')

# ■■■■■ 5. PANEL INFERIOR (CONCLUSIONES DIDÁCTICAS) ■■■■■
st.markdown("---")
st.markdown("### 📊 ¿Por qué el Recall es el rey en la Detección de Fraude?")

c_acc, c_rec = st.columns(2)

with c_acc:
    st.error("**El engaño de la Exactitud (Accuracy)**")
    st.write("""
    Fíjate en el panel de la izquierda. Incluso con el umbral mal configurado, el modelo puede tener una **Exactitud del 98%**. 
    
    ¿Por qué? Porque en un mundo donde el 98% de las transacciones son legítimas, un modelo "tonto" que simplemente diga que *todo es normal* acertará el 98% de las veces. Sin embargo, **dejará pasar el 100% de los fraudes**, llevando a la empresa a la quiebra. La exactitud no sirve en conjuntos de datos desbalanceados.
    """)

with c_rec:
    st.success("**El poder del Recall (Sensibilidad) y el Umbral**")
    st.write("""
    En problemas de fraude médico o bancario, **un Falso Negativo (dejar escapar a un estafador o a un enfermo) es muchísimo más caro** que un Falso Positivo (llamar al cliente para confirmar si él hizo el pago). 
    
    **El truco interactivo:** Sube a los controles y baja el **Umbral de Decisión a 0.20**. Verás cómo el *Recall* sube radicalmente, los fraudes atrapados (TP) aumentan y los fraudes escapados (FN) se reducen casi a cero. Sacrificamos un poco de comodidad de los clientes normales (FP) para blindar el negocio.
    """)