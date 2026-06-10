import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# CONFIGURACIÓN DE LA INTERFAZ
# ==========================================
st.set_page_config(
    page_title="Predicción de Viviendas - California",
    page_icon="🏠",
    layout="wide"
)

st.title("Plataforma Interactiva de Regresión: Viviendas en California")
st.markdown("""
Esta herramienta interactiva permite cargar datos reales de viviendas, analizar
visualmente sus correlaciones y entrenar dinámicamente un modelo de **Regresión Lineal Múltiple**
para predecir precios.
""")

# ==========================================
# CARGA DE DATOS (SIDEBAR)
# ==========================================
st.sidebar.header("Gestión de Datos")
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV personalizado", type=["csv"])

@st.cache_data
def cargar_datos_california():
    california = fetch_california_housing(as_frame=True)
    df = california.frame.copy()
    # Traducir los nombres de las columnas para mayor claridad pedagógica
    df.columns = [
        'IngresoMedio', 'EdadVivienda', 'PromHabitaciones', 'PromDormitorios',
        'Poblacion', 'PromOcupantes', 'Latitud', 'Longitud', 'ValorMedioVivienda'
    ]
    return df

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("¡Datos cargados con éxito!")
else:
    df = cargar_datos_california()
    st.sidebar.info("Utilizando el California Housing Dataset por defecto.")

# ==========================================
# PESTAÑAS DE NAVEGACIÓN
# ==========================================
tab_eda, tab_model = st.tabs(["Análisis Exploratorio (EDA)", "Modelado y Simulación"])

# ------------------------------------------
# PESTAÑA 1: ANÁLISIS EXPLORATORIO DE DATOS
# ------------------------------------------
with tab_eda:
    st.header("Análisis Exploratorio de Datos (EDA)")

    col_prev, col_slide = st.columns([7, 3])
    with col_slide:
        filas = st.slider("Filas a visualizar en la tabla inferior:", 5, 50, 10)

    st.subheader("Muestra de Datos (Head)")
    st.dataframe(df.head(filas), use_container_width=True)

    col_des, col_map = st.columns([4, 6])

    with col_des:
        st.subheader("Estadísticas Descriptivas del Dataset")
        st.dataframe(df.describe().T, use_container_width=True)

    with col_map:
        st.subheader("Matriz de Correlación Lineal")
        # Creamos mapa de calor interactivo con Matplotlib puro
        fig, ax = plt.subplots(figsize=(10, 8))
        corr = df.corr()
        im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')
        fig.colorbar(im, ax=ax)

        ticks = np.arange(len(corr.columns))
        ax.set_xticks(ticks)
        ax.set_xticklabels(corr.columns, rotation=45, ha='right', fontsize=9)
        ax.set_yticks(ticks)
        ax.set_yticklabels(corr.columns, fontsize=9)

        for i in range(len(corr.columns)):
            for j in range(len(corr.columns)):
                val = corr.iloc[i, j]
                text_color = "white" if abs(val) > 0.6 else "black"
                ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=text_color, fontweight='bold', fontsize=8)

        plt.tight_layout()
        st.pyplot(fig)

# ------------------------------------------
# PESTAÑA 2: MODELADO Y INFERENCIA INTERACTIVA
# ------------------------------------------
with tab_model:
    st.header("Entrenamiento y Simulación del Modelo")

    st.subheader("Configuración del Entrenamiento")
    features = st.multiselect(
        "Selecciona las características de entrada (X):", 
        options=[col for col in df.columns if col != 'ValorMedioVivienda'],
        default=['IngresoMedio', 'EdadVivienda', 'PromHabitaciones']
    )

    target = 'ValorMedioVivienda'

    if len(features) == 0:
        st.warning("Debes seleccionar al menos una característica explicativa para ajustar el modelo.")
    else:
        # 1. División de datos y entrenamiento
        X = df[features]
        y = df[target]

        # Muestreo representativo para simular consistencia con el entorno de pruebas
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)

        # 2. Evaluación del rendimiento
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Coeficiente de Determinación (R²)", f"{r2:.4f}")
        col_m2.metric("Error Cuadrático Medio (MSE)", f"{mse:.4f}")
        col_m3.metric("Raíz del MSE (RMSE)", f"{rmse:.4f}")

        st.subheader("Ecuación Obtenida e Interpretación de Coeficientes")
        coef_data = pd.DataFrame({
            "Característica": features,
            "Coeficiente (Peso Beta)": modelo.coef_
        })
        st.dataframe(coef_data, use_container_width=True)
        st.markdown(f"**Intercepto ($\\beta_0$ / Sesgo):** `{modelo.intercept_:.4f}`")

        # 3. Formulario para inferencia en tiempo real
        st.subheader("Calculadora del Valor de la Vivienda (Predicción)")
        st.markdown("Ajusta los parámetros para estimar el valor medio en tiempo real:")

        user_data = {}
        inputs_columns = st.columns(len(features))

        for idx, feat in enumerate(features):
            min_val = float(df[feat].min())
            max_val = float(df[feat].max())
            mean_val = float(df[feat].mean())

            with inputs_columns[idx]:
                user_data[feat] = st.slider(
                    f"{feat}",
                    min_value=min_val,
                    max_value=max_val,
                    value=mean_val
                )

        # Crear input para el modelo
        df_input = pd.DataFrame([user_data])
        pred_val = modelo.predict(df_input)[0]

        # Mostrar predicción
        st.success(f"### Valor Predicho de la Vivienda: **${pred_val * 100000:,.2f} USD**")
        st.caption(f"(Salida cruda del modelo: {pred_val:.4f} centenas de miles de dólares)")

        # 4. Gráfica de ajuste real vs predicción
        st.subheader("Ajuste del Modelo en Datos de Test")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.scatter(y_test, y_pred, alpha=0.6, color='#1f77b4', edgecolors='k')
        ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Ajuste Perfecto (y=x)')
        ax2.set_xlabel('Valor Real ($100k)')
        ax2.set_ylabel('Valor Predicho ($100k)')
        ax2.grid(True, linestyle='--', alpha=0.5)
        ax2.legend()
        plt.tight_layout()
        st.pyplot(fig2)