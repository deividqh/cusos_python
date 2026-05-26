import streamlit as st
from streamlit_sortables import sort_items
import json
import os
import signal

st.set_page_config(page_title="Índice Multi-Nivel", layout="centered")
st.title("🗂️ Índice Jerárquico Vertical (Drag & Drop)")
st.write("Gestiona el orden de tus contenidos arrastrando los bloques verticales:")

# Caracteres especiales para forzar la indentación en la web
ind1 = "\u2002\u2002\u2002\u2002"  # Grado 1 de indentación
ind2 = "\u2002\u2002\u2002\u2002\u2002\u2002\u2002\u2002"  # Grado 2 de indentación

# 1. Base de datos del índice con múltiples grados de anidación
# Formato: Contenedor Principal -> Sub-lista con Grado 1 y Grado 2 combinados en vertical
estructura_profunda = [
    {
        "header": "📁 1. Fundamentos de IA",
        "items": [
            f"{ind1}├── 📝 1.1 Introducción al Aprendizaje Automático",
            f"{ind2}└── 🔍 1.1.1 ¿Qué es una neurona artificial?",
            f"{ind1}└── 📝 1.2 Configuración del Entorno",
            f"{ind2}├── 🔍 1.2.1 Instalación de dependencias",
            f"{ind2}└── 🔍 1.2.2 Verificación de GPU con CUDA"
        ]
    },
    {
        "header": "📁 2. Redes Neuronales",
        "items": [
            f"{ind1}├── 📝 2.1 Perceptrón Multicapa",
            f"{ind2}└── 🔍 2.1.1 Funciones de activación (ReLU, Sigmoid)",
            f"{ind1}└── 📝 2.2 Optimización",
            f"{ind2}└── 🔍 2.2.1 Descenso del gradiente estocástico (SGD)"
        ]
    }
]

# 2. Renderizado interactivo en vertical con 'multi_containers'
# Esto genera los bloques del menú ordenables en un flujo vertical limpio
orden_actualizado = sort_items(estructura_profunda, multi_containers=True)

st.write("---")

# BOTÓN DE RETORNO: Limpia todas las sangrías y niveles para devolver un JSON limpio a tu flujo principal
if st.button("💾 Finalizar y Procesar Índice", type="primary"):
    datos_limpios = []
    
    for bloque in orden_actualizado:
        elementos_procesados = []
        for item in bloque["items"]:
            # Identificamos el grado de anidación analizando el texto antes de limpiarlo
            if ind2 in item:
                nivel = 3
            elif ind1 in item:
                nivel = 2
            else:
                nivel = 1
                
            # Limpieza exhaustiva de caracteres visuales
            texto_limpio = item.replace(ind2, "").replace(ind1, "").replace("├── ", "").replace("└── ", "").strip()
            
            elementos_procesados.append({
                "texto": texto_limpio,
                "nivel_jerarquia": nivel
            })
            
        datos_limpios.append({
            "categoria_principal": bloque["header"].replace("📁 ", "").strip(),
            "sub_elementos": elementos_procesados
        })

    # Guardamos el mapa jerárquico estructurado
    with open("orden_final.json", "w", encoding="utf-8") as f:
        json.dump(datos_limpios, f, ensure_ascii=False, indent=4)
        
    st.success("¡Índice jerárquico guardado con éxito!")
    os.kill(os.getpid(), signal.SIGINT)
