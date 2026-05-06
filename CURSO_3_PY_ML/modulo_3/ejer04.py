""" Ejercicio 4 - Reducción de Dimensiones con LDA
Objetivo: Analizar cómo el Análisis Discriminante Lineal (LDA) ayuda a separar clases visualmente.
Enunciado del Reto: Visualizar datos en 4 dimensiones (Iris) es complejo. Utiliza LDA para reducir el dataset a
2 componentes principales que maximicen la separabilidad de las clases y genera un gráfico de dispersión
(scatter plot) para observar cómo se agrupan las especies. """


import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets

# Carga de datos
iris = datasets.load_iris()
X, y = iris.data, iris.target
# Reducción a 2 dimensiones usando LDA
# LDA busca maximizar la distancia entre medias de clases y minimizar la varianza interna
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit(X, y).transform(X)
# Visualización de los resultados
plt.figure(figsize=(8, 6))
colors = ['navy', 'turquoise', 'darkorange']
for i, color, name in zip([0, 1, 2], colors, iris.target_names):plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], color=color, alpha=.8,
label=name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA: Proyección del dataset Iris en 2D')
plt.show()

""" Justificación: El alumno analiza la capacidad de LDA para proyectar datos preservando la información de
clase, diferenciándolo de un simple análisis estadístico. """