TEXTO = """ Ejercicio 8 - Clasificación Discriminante vs Probabilística 🌷🌷🌷🌷

■ Objetivo: Evaluar las diferencias entre LDA y Naive Bayes en condiciones reales.

■ Enunciado del Reto: 
• Entrena un clasificador LDA y uno Naive Bayes sobre el dataset Iris. 
• Determina cuál de los dos comete menos errores en el conjunto de prueba y
• reflexiona sobre si la suposición de independencia de variables de Naive Bayes afecta los resultados. """

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from colorama import Fore, Style
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
test_size=0.4, random_state=42)
# ■ Entrenamiento
lda = LinearDiscriminantAnalysis().fit(X_train, y_train)
print(f'\nPARAMETROS DEL MODELO Linea (LDA): {lda.get_params(deep=True)}')
print("•••••••••••• Entrenamiento/fit [ lda ] Cargado OK")

gnb = GaussianNB().fit(X_train, y_train)
print(f'\nPARAMETROS DEL MODELO GaussianNB: {gnb.get_params(deep=True)}')
print("•••••••••••• Entrenamiento/fit [ gnb ] Cargado OK")

# ■ Reporte de resultados
print("\n████ Rendimiento LDA ---")
print(classification_report(y_test, lda.predict(X_test), target_names=iris.target_names))

print("\n████ Rendimiento Naive Bayes ---")
print(classification_report(y_test, gnb.predict(X_test), target_names=iris.target_names))

print(""" Justificación: El alumno evalúa supuestos teóricos comparando métricas de precisión: 
recall y F1-score para dos paradigmas distintos de clasificación. """)