# Tarea 6 Evaluacion de un dataset de los precios de la vivienda.

import numpy as np
import pandas as pd

np.random.seed(123)     # Para reproducibilidad
n_viviendas = 1000      # Tamaño muestral

def prueba():    
    df_viviendas = pd.DataFrame({
        'id_vivienda': np.random.randint( low=1, high=6, size=n_viviendas ),  # Número de habitaciones
        'precio': np.random.normal(loc=200000, scale=50000, size=n_viviendas),  # Precio en dólares
        # superficies de 20 a 100 metros 
        'superficie': np.random.normal(loc=100, scale=20, size=n_viviendas),  # Área en metros cuadrados
        'zona':   np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=n_viviendas),  # Zona geográfica
    })

    print(type(df_viviendas))
    precios_base=np.random.normal(loc=200000, scale=50000, size=n_viviendas)



    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Valores atipicos(se añaden al numero de viviendas)
    n_outliers = 20
    outliers = np.random.uniform(low=800000, high=1500000, size=n_outliers)  # Precios de outliers

    # Combinamos los valores de ambos grupos
    precios_finales = np.concatenate([precios_base, outliers])                  

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Limitar precios entre 50k y 500k
    precios_finales = np.clip(precios_finales, a_min=50000, a_max=None)                 

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # Área en metros cuadrados
    superficie = np.random.normal(loc=100, scale=40, size=len(precios_finales)).clip(40, 500)     
    # Número de habitaciones
    habitaciones = np.random.randint(1, 6, len(precios_finales))                        

prueba()                                  

df = pd.read_csv('viviendas.csv')  # Cargar el dataset desde un archivo CSV
# Tendencia Central(media, mediana, moda)
media_precio = df['precio'].mean()
mediana_precio = df['precio'].median()

# dispersion:
varianza_precio = df['precio'].var()
desviacion_estandar_precio = df['precio'].std()

# Interpretacion 
limite_inferior = media_precio - desviacion_estandar_precio
limite_superior = media_precio + desviacion_estandar_precio

# Imprimir resultados
print(f"Media del precio: {media_precio:,.2f}")
print(f"Mediana del precio: {mediana_precio:,.2f}")
print(f"Varianza del precio: {varianza_precio:,.2f}")
print(f"Desviación estándar del precio: {desviacion_estandar_precio:,.2f}")
print(f"Límite inferior: {limite_inferior:,.2f}")
print(f"Límite superior: {limite_superior:,.2f}")

# Mediana: Es el punto medio. Si ordenas los datos de menor a mayor, es el valor que deja al 50% por arriba.
# No le afectan los valores externos.

# Varianza: Es el promedio de los cuadrados de las distancias de cada datos respecto a la media. Nos dice qué tan dispersos están los datos. Si es alta, los datos están más dispersos; si es baja, están más agrupados..
# Es dificil interpretar directamente la varianza, por eso se usa la desviación estándar.

# Desviación estándar: Es la raíz cuadrada de la varianza. Nos da una medida de dispersión 
# en las mismas unidades que los datos originales. 
# Si es alta, los datos están más dispersos; si es baja, están más agrupados.

import matplotlib.pyplot as plt
import seaborn as sns

# Configuracion de la estetica del grafico
sns.set_theme(style="whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
ax1.set_title("Distribución del Precio de las Viviendas")
ax1.set_xlabel("Precio", fontsize=12)

#boxplot de valores, de precio.
sns.boxplot(x=df['precio'], ax=ax1, color='skyblue' , flierprops={'marker': 'o', 'markerfacecolor': 'red', 'markersize': 12})
ax2.set_title("Analisis de Outliers en el Precio de las Viviendas", fontsize=14, fontweight='bold')
ax2.set_xlabel("Precio", fontsize=12)

plt.tight_layout()

plt.show()

