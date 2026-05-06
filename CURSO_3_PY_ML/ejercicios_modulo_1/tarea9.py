"""
• Normalización: Convierta todo el texto a minúsculas para que "Inteligencia" e "inteligencia" se cuenten como la misma palabra.
• Limpieza de Puntuación: Utilice expresiones regulares (re) o métodos de string para eliminar puntos, comas y caracteres especiales.
• Filtrado de Stopwords: Elimine las palabras "vacías" (artículos, preposiciones como "el", "de", "y") que no aportan valor semántico al análisis.
• Conteo: Devuelva un diccionario con las 5 palabras más frecuentes y su número de apariciones.
• Entrega: Script de Python que procese un párrafo de ejemplo sobre IA.
"""

import re
import tarea9contarpalabras as cp

text = "La inteligencia artificial es un campo de estudio que se centra en crear máquinas que pueden pensar y aprender como los humanos. La inteligencia artificial tiene muchas aplicaciones en la vida cotidiana, como los asistentes virtuales y los sistemas de recomendación."

# Procesar el texto
processed_text = cp.contar_palabras(text)
print("Palabras más frecuentes:")
for word, count in processed_text.items():
    print(f"  {word}: {count}")


