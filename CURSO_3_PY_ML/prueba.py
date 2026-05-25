import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuración del título de la página web
st.title("📊 Cuadro de Mando de Ciencia de Datos")
st.markdown("Este es un ejemplo de cómo reemplazar Tkinter por una interfaz web moderna.")

# 2. Creación de datos simulados (Simulamos un EDA o métricas de negocio)
@st.cache_data # Optimiza la carga de datos
def cargar_datos():
    np.random.seed(42)
    fechas = pd.date_range(start="2026-01-01", periods=100)
    datos = pd.DataFrame({
        "Fecha": fechas,
        "Ventas": np.random.randint(100, 1000, size=100),
        "Visitas_Web": np.random.randint(1000, 5000, size=100),
        "Categoría": np.random.choice(["Electrónica", "Ropa", "Hogar"], size=100)
    })
    return datos

df = cargar_datos()

# =========================================================================
# COMPONENTES INTERACTIVOS (Los equivalentes a tus widgets de Tkinter)
# =========================================================================

# Creamos una barra lateral (Sidebar) para organizar los controles
st.sidebar.header("🎛️ Filtros y Controles")

# EQUIVALENTE AL RADIOBUTTON: Selector de métrica principal
metrica = st.sidebar.radio(
    "Selecciona la métrica a visualizar:",
    options=["Ventas", "Visitas_Web"]
)

# EQUIVALENTE AL SPINBOX: Selector numérico para filtrar filas
filas_a_mostrar = st.sidebar.number_input(
    "Cantidad de filas a ver en la tabla:",
    min_value=5,
    max_value=50,
    value=10, # Valor inicial
    step=5
)

# =========================================================================
# RENDERIZADO DE MÉTRICAS Y GRÁFICAS (EDA / Visualización)
# =========================================================================

# Mostramos métricas clave estilo "Dashboard"
st.subheader("📈 Resumen Ejecutivo")
col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"Total {metrica}", value=f"{df[metrica].sum():,}")
with col2:
    st.metric(label=f"Promedio Diario", value=f"{int(df[metrica].mean()):,}")

# Generamos una gráfica interactiva con Plotly basada en el "Radiobutton"
st.subheader(f"Evolución Temporal de {metrica}")
fig = px.line(df, x="Fecha", y=metrica, color="Categoría", title=f"Tendencia de {metrica} por Categoría")
st.plotly_chart(fig, width="stretch")

# Mostramos la tabla de datos limitada por el "Spinbox"
st.subheader("📄 Vista previa de los Datos")
st.dataframe(df.head(filas_a_mostrar),  width="stretch")

# EQUIVALENTE AL PROGRESSBAR: Simulación de carga de un modelo
if st.sidebar.button("🤖 Entrenar Modelo IA"):
    barra_progreso = st.sidebar.progress(0)
    for porcentaje_completo in range(100):
        # Simula tiempo de cómputo
        import time
        time.sleep(0.01)
        barra_progreso.progress(porcentaje_completo + 1)
    st.sidebar.success("¡Modelo entrenado con éxito!")
