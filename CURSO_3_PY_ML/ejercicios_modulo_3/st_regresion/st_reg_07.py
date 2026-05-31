import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error

# Configuración de página en modo ancho estándar
# st.set_page_config(layout="wide", page_title="Actividad 7 - Overfitting")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Prevención del Overfitting (Sobreajuste)")

# ■■■■■ 2. ENUNCIADO EN COLLAPSE ■■■■■
ENUNCIADO = """Actividad 7 - Prevención del Overfitting: Genera un conjunto de datos con mucho
ruido que represente la temperatura horaria. Entrena modelos polinomiales de grado 1 al 15
y detecta en qué punto el modelo empieza a “memorizar” el ruido en lugar de la tendencia.

• Nos enfrentamos a uno de los conceptos más importantes en Machine Learning: el Overfitting (Sobreajuste). Para demostrarlo visualmente de forma espectacular, vamos a generar una curva de temperatura teórica (una onda suave que sube por la tarde y baja de madrugada) y le añadiremos ruido.

• Al usar un control para subir el grado del polinomio de 1 a 15, verás cómo el modelo pasa de ser demasiado rígido (Underfitting) a ajustarse perfectamente, y finalmente "enloquece" intentando tocar todos los puntos ruidosos (Overfitting), arruinando por completo la predicción real.
"""
with st.expander("📖 Ver el Enunciado del Ejercicio"):
    st.write(ENUNCIADO)

# ■■■■■ 3. PANEL DE CONTROLES ■■■■■
with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        # El control clave de este ejercicio: el grado del polinomio
        grado_poly = st.slider("Complejidad del Modelo (Grado Polinomial):", min_value=1, max_value=15, value=1, step=1)
    with c2:
        ruido = st.slider("Nivel de Ruido en Sensores (ºC):", min_value=1.0, max_value=8.0, value=3.0, step=0.5)
    with c3:
        n_puntos = st.slider("Número de mediciones (Puntos):", min_value=15, max_value=40, value=24)

# ■■■■■ 4. PROCESAMIENTO DE DATOS Y MODELADO ■■■■■
np.random.seed(42)
X_raw = np.linspace(0, 24, n_puntos).reshape(-1, 1)     # Generamos X (Horas del día, de 0 a 24)

# Generamos Y_ideal (La tendencia real: una onda senoidal suave simulando la temperatura)
# Temp mínima a las 6am, máxima a las 18pm.
y_ideal = 20 + 8 * np.sin((X_raw.flatten() - 12) * np.pi / 12)

# Generamos Y_real (Los datos que el modelo realmente ve: ideal + ruido del sensor)
y_ruidoso = y_ideal + np.random.normal(0, ruido, n_puntos)

# Transformación Polinomial según el grado seleccionado por el usuario
poly = PolynomialFeatures(degree=grado_poly)
X_poly = poly.fit_transform(X_raw)

# Entrenamiento del Modelo
modelo = LinearRegression()
modelo.fit(X_poly, y_ruidoso)

# 1. Predicción sobre los puntos de entrenamiento (Para calcular el Error de Entrenamiento)
y_pred_train = modelo.predict(X_poly)
error_entrenamiento = mean_absolute_error(y_ruidoso, y_pred_train)

# 2. Predicción sobre una línea continua (Para dibujar la curva y calcular el Error Real)
X_plot = np.linspace(0, 24, 200).reshape(-1, 1)
y_plot_ideal = 20 + 8 * np.sin((X_plot.flatten() - 12) * np.pi / 12)
y_plot_pred = modelo.predict(poly.transform(X_plot))

# El "Error Real" mide cuánto se desvía la curva del modelo de la temperatura teórica perfecta
error_real = mean_absolute_error(y_plot_ideal, y_plot_pred)

# Preparamos el DataFrame para la columna izquierda
df_resultados = pd.DataFrame({
    'Hora': X_raw.flatten(),
    'Temp. Ideal (Tendencia)': y_ideal,
    'Temp. Medida (Ruido)': y_ruidoso,
    f'Predicción (Grado {grado_poly})': y_pred_train
})


# ■■■■■ 4. DOS COLUMNAS (DATOS Y GRÁFICO PLOTLY) ■■■■■
st.markdown("---")
col_datos, col_grafico = st.columns([1, 2.5])

with col_datos:
    st.markdown("### 📋 Registros del Sensor")
    st.dataframe(
        df_resultados.style.format({
            'Hora': '{:.1f} h', 
            'Temp. Ideal (Tendencia)': '{:.2f} ºC', 
            'Temp. Medida (Ruido)': '{:.2f} ºC', 
            f'Predicción (Grado {grado_poly})': '{:.2f} ºC'
        }), 
        height=450
    )

with col_grafico:
    st.markdown(f"### 📉 Ajuste vs Tendencia (Grado {grado_poly})")
    
    fig = go.Figure()
    
    # 1. La Tendencia Ideal (Oculta al modelo, pero la dibujamos para el estudiante)
    fig.add_trace(go.Scatter(
        x=X_plot.flatten(), y=y_plot_ideal,
        mode='lines', line=dict(color='rgba(44, 160, 44, 0.4)', width=6),
        name='Tendencia Real (Ideal)', hoverinfo='skip'
    ))

    # 2. Los datos ruidosos (Lo que el modelo intenta aprender)
    fig.add_trace(go.Scatter(
        x=df_resultados['Hora'], y=df_resultados['Temp. Medida (Ruido)'],
        mode='markers', marker=dict(color='#1f77b4', size=9, opacity=0.8, line=dict(color='white', width=1)),
        name='Sensores (Con Ruido)',
        hovertemplate='<b>Hora:</b> %{x:.1f} h<br><b>Medición:</b> %{y:.1f} ºC<extra></extra>'
    ))
    
    # 3. La curva predictiva del modelo polinomial
    fig.add_trace(go.Scatter(
        x=X_plot.flatten(), y=y_plot_pred,
        mode='lines', line=dict(color='#d62728', width=3),
        name=f'Modelo (Grado {grado_poly})', hoverinfo='skip'
    ))

    # Forzamos un límite en el eje Y para evitar que el gráfico colapse visualmente 
    # cuando los polinomios altos (grado 14-15) se disparen al infinito
    fig.update_layout(
        xaxis_title='Hora del Día',
        yaxis_title='Temperatura (ºC)',
        yaxis=dict(range=[0, 40]), # Congelamos el eje Y para ver cómo el modelo se escapa
        margin=dict(l=10, r=10, t=10, b=10),
        hovermode='x unified',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450
    )
    
    st.plotly_chart(fig, width='stretch')

# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
st.markdown("---")
st.markdown("### 📊 Conclusiones del Experimento")

m1, m2, m3 = st.columns(3)

# Mostramos el error de entrenamiento (que engañosamente baja)
m1.metric("Error de Entrenamiento (MAE)", f"{error_entrenamiento:.2f} ºC", delta="Lo que el modelo cree", delta_color="off")
# Mostramos el error real contra la curva ideal (que explota en overfitting)
m2.metric("Error Real contra Tendencia", f"{error_real:.2f} ºC", delta="El error verdadero", delta_color="off")

with m3:
    st.markdown(f"**Estado Actual:**")
    if grado_poly == 1:
        st.warning("⚠️ **Underfitting:** Una línea recta no puede capturar la curva del clima.")
    elif 2 <= grado_poly <= 4:
        st.success("✅ **Buen Ajuste:** El modelo captura la onda térmica e ignora el ruido.")
    elif 5 <= grado_poly <= 9:
        st.warning("⚠️ **Alerta:** El modelo empieza a zigzaguear buscando los puntos ruidosos.")
    else:
        st.error("🚨 **Overfitting Severo:** El modelo ha memorizado el ruido. Las predicciones entre puntos son absurdas.")

st.info("""
💡 • La trampa matemática del Overfitting:** Desliza el **Grado Polinomial del 1 al 15** observando los errores de arriba. Notarás algo aterrador: a medida que subes el grado, el *Error de Entrenamiento* disminuye constantemente, haciéndote creer que el modelo está mejorando. Sin embargo, mira el gráfico: la línea roja empieza a hacer curvas imposibles y oscilaciones violentas solo para "tocar" los puntos ruidosos, alejándose por completo de la suave curva de temperatura real (el *Error Real* se dispara). **Un buen modelo generaliza la tendencia, no memoriza los datos.**

• La trampa visual (Congelar el eje Y): En Plotly, he forzado yaxis=dict(range=[0, 40]). Si no hiciéramos esto, al seleccionar grado 15 el modelo predeciría temperaturas de 2000ºC y el gráfico haría tanto zoom inverso que los puntos se verían como una línea plana. Al congelar la escala, el estudiante verá la línea roja salirse violentamente del gráfico hacia arriba y hacia abajo, demostrando el efecto devastador de memorizar el ruido.

• Doble Métrica (Entrenamiento vs Realidad): El panel de conclusiones muestra cómo el modelo cree que está acertando (el MAE de entrenamiento baja), pero te avisa del desastre porque la métrica real (que mide la distancia contra la curva verde) se dispara.
""")