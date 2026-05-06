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

# ■■■■■■■■■■■■■■■■■■■■■■■■■■
# 1. Cargar el dataset ( de 1930 )
iris = datasets.load_iris()   
print("■ type Iris:", type(iris) )
print("■ keys:", iris.keys())

X, y = iris.data, iris.target

print("■ type X:", type(X))
print("■ type y:", type(y))
print(X[2])

# df = pd.DataFrame({'datas':1})

# ■■■■■■■■■■■■■■■■■■■■■■■■■■
# 2. Dividir en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f'■ type x train: {type(X_train)} \n■ type y train: {type(y_train)}')

# ■■■■■■■■■■■■■■■■■■■■■■■■■■
# 3. Crear y entrenar el modelo (Kernel Lineal)
# modelo_svm = SVC(kernel='linear', verbose=True)
# modelo_svm = SVC(kernel='rbf', verbose=True)
# modelo_svm = SVC(kernel='poly', verbose=True)
modelo_svm = SVC(kernel='sigmoid', verbose=True)
print("■ type modelo:", type(modelo_svm))

fit = modelo_svm.fit(X_train, y_train)
print("■ type fit:", type(fit))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■
# 4. Evaluación básica
precision = modelo_svm.score(X_test, y_test)
print("■ type precision:", type(precision))
print(f"■■■■■ Precisión del modelo: {precision:.2f}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■
# 5. Predicción de una nueva muestra desconocida
nueva_flor = np.array([[111115.1, 3.5, 1.4, 0.2], [5.1, 4.5, 2.4, 0.2], [6.1, 3.5, 3.4, 0.2]])
prediccion = modelo_svm.predict(nueva_flor)

print(f'■ type Prediccion : {type(prediccion)}')
print(f'■ type target_names : {type(iris.target_names)}')
# print(iris.target_names[1][::-1])


for i, flor in enumerate(prediccion):
    print(f"► La flor pertenece a la especie: {Fore.CYAN}  {iris.target_names[prediccion][i]}  {Style.RESET_ALL})")
    print(flor)
    print(iris.target_names[flor])


""" Justificación: El alumno demuestra capacidad de aplicación al integrar el flujo básico de Scikit-Learn (Carga,
Split, Fit, Predict) en un problema de clasificación estándar. 
La elección de SVM con kernel lineal es adecuada para el dataset Iris, y la evaluación se realiza de forma
sencilla pero efectiva, mostrando comprensión de la precisión como métrica. La predicción de nuevas muestras añade un toque práctico al ejercicio. 
"""
