import re
from collections import Counter

def contar_palabras(texto):
    # Normalización
    texto = texto.lower()
    
    # Limpieza de puntuación
    texto = re.sub(r'[^\w\s]', '', texto)
    
    # Filtrado de stopwords
    stopwords = {'el', 'la', 'de', 'y', 'en', 'que', 'se', 'no', 'con', 'por'}
    palabras = [palabra for palabra in texto.split() if palabra not in stopwords]
    
    # Conteo
    conteo = Counter(palabras)
    
    # Devolver las 5 palabras más frecuentes
    return dict(conteo.most_common(5))

