TEXTO = """ Ejercicio 4 - Reducción de Dimensiones con LDA  🌷🌷🌷🌷 (EDA)

■ Objetivo: Analizar cómo el Análisis Discriminante Lineal (LDA) ayuda a separar clases visualmente.

■ Enunciado del Reto: Visualizar datos en 4 dimensiones (Iris) es complejo. 
    • Utiliza LDA para reducir el dataset a 2 componentes principales que maximicen la separabilidad de las clases.
    • genera un 'gráfico de dispersión' (scatter plot) para observar cómo se agrupan las especies. """


import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets
from colorama import Fore, Style

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    
# Carga de datos
iris = datasets.load_iris()
X, y = iris.data, iris.target

# ■ Nombres de las categorias (setosa, verdicolor, virginica)
cat_names = iris.target_names
for name in cat_names:
    print(name)

# ■ Reducción a 2 dimensiones usando LDA
# ■ LDA busca maximizar la distancia entre medias de clases y minimizar la varianza interna
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit(X, y).transform(X)

# Visualización de los resultados
plt.figure(figsize=(8, 6))
colors = ['navy', 'turquoise', 'darkorange']

# Dibuja 3 Graficos. Uno encima de otro
for i, color, name in zip([0, 1, 2], colors, iris.target_names):
    col_0 = X_lda[y == i, 0]    # de las filas encontradas(y==i, selecciona la columna 0)
    col_1 = X_lda[y == i, 1]    # de las filas encontradas(y==i, selecciona la columna 1)
    plt.scatter( x = X_lda[y == i, 0], y = X_lda[y == i, 1], color=color, alpha=.8, label=name)

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA: Proyección del dataset Iris en 2D')
plt.show()

print(""" Justificación: El alumno analiza la capacidad de LDA para proyectar datos preservando la información de
clase, diferenciándolo de un simple análisis estadístico. """)