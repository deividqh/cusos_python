""" Ejercicio 6 - Selección de Kernel en SVM
Objetivo: Evaluar la eficacia de diferentes fronteras de decisión (lineales vs no lineales).
Enunciado del Reto: En el dataset de cáncer de mama, las relaciones entre variables pueden no ser lineales.
Evalúa el rendimiento de un SVM con kernel 'linear' frente a uno 'rbf' utilizando validación cruzada (Cross-
Validation) para determinar cuál generaliza mejor. """

from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
cancer = load_breast_cancer()
# Definimos los modelos a comparar
modelos = {
"SVM Lineal": SVC(kernel='linear'),
"SVM RBF (No lineal)": SVC(kernel='rbf')
}
print("Resultados de Validación Cruzada (CV=5):")
for nombre, modelo in modelos.items():puntuaciones = cross_val_score(modelo, cancer.data, cancer.target, cv=5)
print(f"- {nombre}: {puntuaciones.mean():.4f} (+/- {puntuaciones.std() *
2:.4f})")

""" Justificación: Al evaluar resultados estadísticos, el alumno decide críticamente qué configuración matemática
es superior para un conjunto de datos específico. """