# https://www.kaggle.com/code/joeportilla/analisis-exploratorio-de-datos-dataset-iris
# https://rpubs.com/jigbadouin/EDAIRIS01
""" Ejercicio 1 - Clasificación Básica con SVM (Iris)
Objetivo: Aplicar los conceptos fundamentales de Support Vector Machines para una clasificación multiclase.
Enunciado del Reto: Un equipo de botánicos necesita automatizar la identificación de la especie Iris
basándose en medidas físicas. Tu tarea es cargar el dataset Iris de Scikit-Learn, dividirlo en entrenamiento y
prueba, y entrenar un modelo SVM con kernel lineal para predecir la especie de una muestra desconocida. """

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from  colorama import Fore, Style
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 
# ■■■■■■■■■ 1. 🌷 Cargar el dataset ( Finsher - 1930 )
iris = datasets.load_iris()   
X, y = iris.data, iris.target
print(y)
# ■■■■■■■■■ 📉 Analisis de los datos :::

# ■ Crear el DataFrame con los nombres de las columnas
df = pd.DataFrame(data = X, columns = iris.feature_names)

# ■ Añadir la columna de especie (traducida de número a nombre)
df['species'] = [iris.target_names[i] for i in y]
print("■ Vista previa del DataFrame:")
print(df.head())

# ■ 
sns.set_theme(style="ticks")
grafico = sns.pairplot(data=df, hue="species", palette="bright" )
grafico.fig.suptitle("Dispersión de Especies Iris", y=1.02)

plt.show()

sns.displot(df, x="petal width (cm)", hue="species", kind="kde", fill=True)
plt.show()



# ■■■■■■■■■ 2. ✂️ Dividir en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ■■■■■■■■■ 3. 🧠 Crear el modelo sobre el algoritmo SVC con Kernel Lineal (byDef 'rbf')
modelo_svm = SVC(kernel='linear', probability=True)
# modelo_svm = SVC(kernel='rbf', verbose=True)
# modelo_svm = SVC(kernel='poly', verbose=True)
# modelo_svm = SVC(kernel='sigmoid', verbose=True)

# ■■■■■■■■■ 👟 Entrenar el Modelo SVC
fit = modelo_svm.fit(X_train, y_train)

# ■■■■■■■■■ 🎲 Probabilidad (siempre despues de 'fit')
probabilidades = modelo_svm.predict_proba( X = X_test )
print(f"■■■■■ Probabilidades: {probabilidades}")

# ■■■■■■■■■ 🎯 Precisión/score: El modelo se auto-analiza.
precision = modelo_svm.score(X_test, y_test)
print(f"■■■■■ Precisión del modelo: {precision:.2f}")

# ■■■■■■■■■ 🔮🔮 PREDICCION ... Con los elementos a 'predict', hago una consulta a la bolita magica
# ■ 🌷 Creo unos elementos (dentro del rango probable) con numpy
nueva_flor = np.array([[5000, 5800, 5000, 5000], [5.1, 4.5, 2.4, 0.2], [6.1, 3.5, 3.4, 0.2]])

# ■ 🔮 Predict ... hago una consulta a la bolita magica
predicciones_nuevas = modelo_svm.predict(nueva_flor)

# ■ 🎲 PROBABILIDAD Por cada nueva flor o array de flores, hay nuevas probabilidades
probabilidades_nuevas = modelo_svm.predict_proba(nueva_flor)

# ■■■■■■■■■ 🖥️ Visualización por Consola.
for i, clase_idx in enumerate(predicciones_nuevas):
    nombre = iris.target_names[clase_idx]
    porcentaje = np.max(probabilidades_nuevas[i]) * 100
    
    print(f"► Flor {i+1}: {Fore.CYAN}{nombre}{Style.RESET_ALL} "
          f"(Confianza: {porcentaje:.2f}%)")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■          
print(f'\n {'■'*30}')
print("■ type Iris:", type(iris) )
print("■ keys:", iris.keys())
print("■ type X:", type(X))
print("■ type y:", type(y))
print(f'■ type x train: {type(X_train)} \n■ type y train: {type(y_train)}')
print("■ type fit:", type(fit))
print("■ type precision:", type(precision))
print("■ type modelo:", type(modelo_svm))
print(f'■ type Prediccion: {type(predicciones_nuevas)}')
print(f'■ type target_names: {type(iris.target_names)}')

""" Justificación: El alumno demuestra capacidad de aplicación al integrar el flujo básico de Scikit-Learn (Carga,
Split, Fit, Predict) en un problema de clasificación estándar. 
La elección de SVM con kernel lineal es adecuada para el dataset Iris, y la evaluación se realiza de forma
sencilla pero efectiva, mostrando comprensión de la precisión como métrica. La predicción de nuevas muestras añade un toque práctico al ejercicio. 
"""
