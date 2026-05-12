TEXTO = """ Ejercicio 5 - Sensibilidad al Escalamiento en SVM  🦀🦀🦀🦀 (EDA)

■ Objetivo: Analizar la importancia del PRE-PROCESAMIENTO de datos en algoritmos basados en distancias.

■ Enunciado del Reto: Los modelos SVM son extremadamente sensibles a la escala de las variables. Demuestra
este impacto comparando el rendimiento de un modelo SVM entrenado con los datos de Cáncer de Mama
"crudos" frente a uno entrenado con los datos normalizados usando StandardScaler. 

■ Este conjunto de datos se utiliza para clasificación binaria (predecir si un tumor es maligno o benigno) 
y contiene información sobre características de núcleos celulares extraídas de imágenes
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from colorama import Fore, Style

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

# Datos
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,random_state=1)

# 1. Modelo sin escalado
svm_raw = SVC().fit(X_train, y_train)
score_raw = svm_raw.score(X_test, y_test)

# 2. Modelo con escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_scaled = SVC().fit(X_train_scaled, y_train)
print(f'PARAMETROS DEL MODELO: {svm_scaled.get_params(deep=True)}')

score_scaled = svm_scaled.score(X_test_scaled, y_test)

# ■ Resultado
print(f"Rendimiento sin escalado: {score_raw:.4f}")
print(f"Rendimiento con escalado: {score_scaled:.4f}")

print(""" Justificación: Analiza la importancia del preprocesamiento, comprendiendo que la arquitectura del algoritmo
(márgenes) depende de la magnitud de los vectores. """)