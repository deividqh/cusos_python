# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  
# ■ Plan basico:
# crear los datos sinteticos.
# decidir ssobre los valores que faltan.
# gestionar los valores atipicos.
# escalar y normalizar los datos

import numpy as np
import pandas as pd
from  sklearn.preprocessing import StandardScaler, MinMaxScaler


def tarea7():
    np.random.seed(12)      # Para reproducibilidad
    n_muestras = 50         # Tamaño muestral

    # Sensores de temperatura
    temperatura = np.random.uniform(low=-10, high=40, size=n_muestras)  # Temperatura en grados Celsius
    presion = np.random.uniform(low=10000, high=50000, size=n_muestras)    # Presión en hPa

    df_sensores = pd.DataFrame({
        'temperatura': temperatura,
        'presion': presion
    })

    # Introducir valores problematicos:
    # a) valores nulos
    for col in df_sensores.columns:
        indices_nulos = np.random.choice(df_sensores.index, size=int(n_muestras*0.05), replace=False)
        df_sensores.loc[indices_nulos, col] = np.nan
        
        # n_nulos = np.random.randint(1, 5)  # Número aleatorio de valores nulos por columna
    # b) valores criticos (atipicos)
    # c) valores fuera de rango
    print('fin ejercicio')

