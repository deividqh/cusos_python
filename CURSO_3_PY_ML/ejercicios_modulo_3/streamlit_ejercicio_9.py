import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Variable con el texto exacto del enunciado
ENUNCIADO = """ 
Actividad 9 - Mantenimiento Predictivo: En una fábrica, los sensores de una máquina suelen dar
valores estables. Usa Isolation Forest para detectar picos extraños que podrían indicar una avería
inminente antes de que ocurra.
"""

# Configuración de la cabecera en Streamlit mostrando el enunciado
st.title("Ejercicio Resuelto")        
st.info(ENUNCIADO)

# Generación de datos
np.random.seed(42) 
sensor_data = np.random.normal(loc=0, scale=1, size=1000)     
# Introducimos algunos picos anómalos
sensor_data[::100] += np.random.normal(loc=10, scale=5, size=10) 
# Entrenamiento del modelo
algoritmo = IsolationForest(contamination=0.01, random_state=42)
modelo = algoritmo.fit(sensor_data.reshape(-1, 1))
anomalias = modelo.predict(sensor_data.reshape(-1, 1)) 
# Obtención de índices anómalos
indices_anomalos = np.where(anomalias == -1)
# Mostrar resultados de texto en Streamlit
st.subheader("Resultados del Análisis")
st.write("**Índices de datos anómalos detectados:**")
st.code(str(indices_anomalos[0].tolist()))
# Creación del gráfico con Pyplot
fig, ax = plt.subplots(figsize=(10, 4))    
# Dibujar todos los datos
ax.plot(sensor_data, label="Datos del Sensor", color="teal", alpha=0.6)    
# Resaltar las anomalías en el gráfico
ax.scatter(indices_anomalos[0], sensor_data[indices_anomalos], color="red", label="Anomalías Detectadas", zorder=5)
ax.set_title("Datos del Sensor con Anomalías")
ax.set_xlabel("Tiempo / Muestra")
ax.set_ylabel("Valor del Sensor")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
# Mostrar el gráfico en la interfaz de Streamlit
st.pyplot(fig)