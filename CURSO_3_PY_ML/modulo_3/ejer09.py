TEXTO = """ Ejercicio 9 - Optimización de Hiperparámetros (C y Gamma) 🦀🦀🦀🦀

■ Objetivo: Crear un proceso de sintonización (tuning) para encontrar la mejor configuración de un SVM.

■ Enunciado del Reto: 
• El rendimiento de SVM depende de los parámetros C (regularización) y gamma (influencia de muestras). 
• Crea un proceso automatizado usando GridSearchCV que pruebe múltiples combinaciones de
estos parámetros sobre el dataset de cáncer de mama y  Reporte la 'Mejor configuración encontrada'. """


from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from colorama import Fore, Style

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

data = load_breast_cancer()

X_scaled = StandardScaler().fit_transform(data.data)

# Definir la rejilla de parámetros (Grid)
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf']
}
# Crear y ejecutar la búsqueda
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=0, cv=5)
grid.fit(X_scaled, data.target)
print(f'PARAMETROS DEL MODELO: {grid.get_params(deep=True)}')

print(f"Mejores parámetros encontrados: {grid.best_params_}")
print(f"Mejor precisión obtenida: {grid.best_score_:.4f}")

print(""" Justificación: El alumno crea un sistema de búsqueda exhaustiva, demostrando que puede orquestar
herramientas de optimización para mejorar modelos existentes. """)
