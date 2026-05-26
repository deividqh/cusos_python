import streamlit as st
from streamlit_sortables import sort_items

# Configuración de la página
st.set_page_config(page_title="Índice Interactivo", layout="centered")

st.title("🗂️ Índice Interactivo (Drag & Drop)")
st.write("Arrastra y suelta los módulos para reorganizar el orden del índice:")

# 1. Definir los elementos iniciales de tu índice
elementos_indice = [
    "Introducción a Python",
    "Variables y Estructuras de Datos",
    "Programación Orientada a Objetos",
    "Desarrollo Web con Python",
    "Bases de Datos y APIs",
    "Despliegue en la Nube"
]

# 2. Crear el componente Drag & Drop
# Al arrastrar, 'orden_actualizado' guarda la nueva lista de forma automática
orden_actualizado = sort_items(elementos_indice)

# 3. Mostrar el resultado del nuevo orden en tiempo real
st.subheader("📌 Orden de salida en tiempo real (Python):")

# Recorremos el resultado final para mostrarlo numerado
for i, modulo in enumerate(orden_actualizado, 1):
    st.write(f"**{i}.** {modulo}")
