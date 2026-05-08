"""  Ejercicio 7 - Análisis de Errores con Matriz de Confusión
Objetivo: Evaluar el coste de los errores en un modelo de clasificación.
Enunciado del Reto: No todos los errores pesan igual. En el diagnóstico de cáncer, un Falso Negativo es
mucho más grave que un Falso Positivo. Genera una Matriz de Confusión para el clasificador de cáncer de
mama e identifica cuántos casos malignos fueron erróneamente clasificados como benignos. """

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
test_size=0.3, random_state=0)
# Entrenar modelo (usamos kernel lineal por su estabilidad en este dataset)
clf = SVC(kernel='linear').fit(X_train, y_train)
y_pred = clf.predict(X_test)
# Generar y mostrar la matriz
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
display_labels=data.target_names)
disp.plot(cmap='Reds')
plt.title("Matriz de Confusión: Diagnóstico Oncológico")
plt.show()

""" Justificación: El alumno evalúa la utilidad real del modelo mediante el análisis detallado de la matriz,
reconociendo la diferencia entre precisión y seguridad. """