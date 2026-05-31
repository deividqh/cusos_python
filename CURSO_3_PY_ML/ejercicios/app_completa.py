# ■■■■■■■■■■■■■■■■■■ EJECUCION ■■■■■■■■■■■■■■■■■ 
# (cmd) ► streamlit run app_completa.py 
# (cmd) ► python -m streamlit run app_completa.py   |  directamente desde python.
# ■■■■■■■■■■■■■■■■■■ EJECUCION ■■■■■■■■■■■■■■■■■
import streamlit as st

# --- NUEVO: Texto Markdown en el panel izquierdo ---
# Puedes ponerlo arriba de la navegación
st.sidebar.markdown("# Modulo 3 REGRESIÓN")
st.sidebar.divider() # Añade una línea divisoria visual

# 1. Configuración global de la plataforma
st.set_page_config(layout="wide", page_title="Modulo 3 Ejercicios Propuestos de Regresión.")

# 2. Mapeamos de forma nativa los archivos sin usar subprocesos de la consola
ejercicios = {
    "Actividad 1: Rendimiento Académico": st.Page("ejercicios_modulo_3/st_regresion/st_reg_01.py", title="EJ1 • Rendimiento Académico", icon="🧮"),
    "Actividad 2: Satisfacción Laboral": st.Page("ejercicios_modulo_3/st_regresion/st_reg_02.py", title="EJ2 • Satisfacción Laboral", icon="📊"),
    "Actividad 3: El Algoritmo desde Cero": st.Page("ejercicios_modulo_3/st_regresion/st_reg_03.py", title="EJ3 • El Algoritmo desde Cero", icon="🤖"),
    "Actividad 4: Tasación de Vehículos": st.Page("ejercicios_modulo_3/st_regresion/st_reg_04.py", title="EJ4 • Tasación de Vehículos", icon="🚗"),
    "Actividad 5: Eficiencia Energética": st.Page("ejercicios_modulo_3/st_regresion/st_reg_05.py", title="EJ5 • Eficiencia Energética", icon="🏠"),
    "Actividad 6: Trayectoria de Mercado": st.Page("ejercicios_modulo_3/st_regresion/st_reg_06.py", title="EJ6 • Trayectoria de Mercado", icon="📈"),
    "Actividad 7: Prevención del Overfitting": st.Page("ejercicios_modulo_3/st_regresion/st_reg_07.py", title="EJ7 • Prevención del Overfitting", icon="📉"),
    "Actividad 8: Diagnóstico Médico": st.Page("ejercicios_modulo_3/st_regresion/st_reg_08.py", title="EJ8 • Diagnóstico Médico", icon="🩺"),
    "Actividad 9: Auditoría de Fraude": st.Page("ejercicios_modulo_3/st_regresion/st_reg_09.py", title="EJ9 • Auditoría de Fraude", icon="🚨"),
    "Actividad 10: Rendimiento Agrícola": st.Page("ejercicios_modulo_3/st_regresion/st_reg_10.py", title="EJ10 • Rendimiento Agrícola", icon="🌱"),
}

# 3. Renderizamos el menú lateral automático de Streamlit
pg = st.navigation(list(ejercicios.values()))

# 4. Ejecutar. Streamlit limpia la pantalla y cambia de código automáticamente al hacer clic
pg.run()
