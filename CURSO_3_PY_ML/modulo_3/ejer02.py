""" Ejercicio 2 - Probabilidades con Naive Bayes (Iris)
Objetivo: Aplicar modelos probabilísticos para entender la pertenencia a clases.
Enunciado del Reto: En un estudio genético, se requiere no solo clasificar la especie, sino conocer el nivel de
confianza de la predicción. Implementa el algoritmo Gaussian Naive Bayes sobre el dataset Iris y muestra las
probabilidades exactas de que una flor con medidas [6.7, 3.1, 4.4, 1.4] pertenezca a cada una de las
tres categorías. """

from sklearn.naive_bayes import GaussianNB
from sklearn import datasets

# Carga de datos
iris = datasets.load_iris()
X, y = iris.data, iris.target
print("•••••••••••• dataset Iris Cargado OK")

# Inicializar y entrenar el clasificador Naive Bayes
gnb = GaussianNB()
print("•••••••••••• Algoritmo GaussianNB Cargado OK")
gnb.fit(X, y)
print("•••••••••••• Entrenamiento/fit Cargado OK")

# Definir la muestra a evaluar
muestra = [[6.7, 3.1, 4.4, 1.4]]
print(f"•••••••••••• Muestra {muestra}")

# Obtener las probabilidades de pertenencia a cada clase
probabilidades = gnb.predict_proba(muestra)
print(f"•••••••••••• predict-proba")
 
print("Probabilidades por especie:")
for i, nombre in enumerate(iris.target_names):
    print(f"- {nombre.capitalize()}: {probabilidades[0][i]:.4f}") 


print ("""\nJustificación: La solución requiere que el alumno utilice predict_proba, demostrando que comprende que
Naive Bayes se basa en el teorema de Bayes para asignar pesos probabilísticos. 
El ejercicio va más allá de la clasificación simple, exigiendo una interpretación de los resultados en términos de confianza, lo que es crucial en aplicaciones reales. La presentación clara de las probabilidades por especie muestra una comprensión completa del modelo. 
 """)
