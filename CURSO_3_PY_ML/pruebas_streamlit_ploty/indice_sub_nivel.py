import streamlit as st
from streamlit_sortables import sort_items
import json
import os
import signal

st.set_page_config(page_title="Índice con Sub-niveles", layout="wide")
st.title("🗂️ Índice con Sub-niveles (Drag & Drop)")
st.write("Organiza los temas arrastrándolos dentro de sus módulos o muévelos entre ellos:")

# 1. NUEVA ESTRUCTURA: Lista de diccionarios con 'header' e 'items'
estructura_indice = [
    {
        "header": "📌 Módulo 1: Introducción",
        "items": ["1.1 Instalación de Python", "1.2 Sintaxis básica", "1.3 Primer script"]
    },
    {
        "header": "📌 Módulo 2: Estructuras",
        "items": ["2.1 Listas y Diccionarios", "2.2 Bucles y Condicionales", "2.3 Funciones"]
    },
    {
        "header": "📌 Módulo 3: Avanzado",
        "items": ["3.1 Programación Orientada a Objetos", "3.2 Manejo de Excepciones"]
    }
]

# 2. Ahora pasamos la lista de contenedores correctamente configurada
orden_actualizado = sort_items(estructura_indice, multi_containers=True)

st.write("---")

# BOTÓN DE RETORNO: Guarda la nueva estructura de lista/diccionarios y vuelve a Python
if st.button("💾 Finalizar y Continuar Flujo Python", type="primary"):
    # Guardamos la lista con su nuevo orden
    with open("orden_final.json", "w", encoding="utf-8") as f:
        json.dump(orden_actualizado, f, ensure_ascii=False, indent=4)
    
    st.success("¡Estructura guardada! Retornando al flujo...")
    
    # Detiene el servidor Streamlit para devolver el control a main.py
    os.kill(os.getpid(), signal.SIGINT)
