from sklearn.datasets import load_breast_cancer
from colorama import Fore, Style
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

TEXTO = f""" Ejercicio 3 - Diagnóstico Médico con SVM (Breast Cancer) 🦀🦀🦀🦀 (METRICAS)

■ Objetivo: Aplicar [ Técnicas de Clasificación ] en un  Entorno de Alta Criticidad  (Salud).

■ Enunciado del Reto: Un hospital digital desea una herramienta de soporte para diagnosticar cáncer de mama (Maligno/Benigno). 
    • Utiliza el dataset 'UCI Breast Cancer' para entrenar un [ modelo SVM ]. 
    • Asegúrate de 'Evaluar' el modelo con el conjunto de prueba y mostrar el 'Porcentaje de Aciertos / Acuracy'.\n """

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

# 1. Carga del dataset de cáncer de mama UCI
cancer = load_breast_cancer()
print("•••••••••••• dataset [ load_breast_cancer ] Cargado OK")

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)
print("•••••••••••• train y entrenamiento Load Ok")

# 2. Configuración del modelo SVC
# Usamos parámetros por defecto para observar el rendimiento base
clf = SVC()

print("•••••••••••• algoritmo SVC Cargado OK")
clf.fit(X_train, y_train)

print(f'PARAMETROS DEL MODELO: {clf.get_params(deep=True)}')
print("•••••••••••• Entrenamiento/Fit Cargado OK")

# 3. Predicción y evaluación
y_pred = clf.predict(X_test)
print("•••••••••••• Predicción Cargada OK")

acc = accuracy_score(y_test, y_pred)
print(f"\n██•██ Precisión/accuracy_score en el diagnóstico médico: {acc*100:.2f}% \n")

print(""" Justificación: Evalúa la transferencia de conocimientos de un dataset simple (Iris) a uno con más dimensiones
(30 características) y un impacto social real. """)