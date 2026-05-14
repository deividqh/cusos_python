import menuDvd
from colorama import Fore, Style

def ejercicio_01():
    ENUNCIADO = """ Ejercicio 1 - PCA: Reducción de Dimensionalidad
• Objetivo: Analizar cómo la reducción de dimensiones preserva la varianza de los datos.
Enunciado del Reto: Una empresa de biotecnología necesita simplificar el análisis de sus muestras de flores
para reducir costes de almacenamiento de datos. 
• Tu tarea es aplicar el Análisis de Componentes Principales
(PCA) al dataset Iris para reducir las 4 variables originales a solo 2, informando qué porcentaje de la
información total (varianza) se ha logrado retener.
"""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.decomposition import PCA
    from sklearn import datasets
    import pandas as pd

    # 1. Carga de datos
    iris = datasets.load_iris()
    X = iris.data
    # 2. Aplicar PCA para reducir a 2 componentes
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # 3. Calcular la varianza explicada
    varianza_explicada = pca.explained_variance_ratio_

    # AlgoritmosML_Clasificacion2 copy.md 2026-05-13
    total_varianza = varianza_explicada.sum()
    print(f"Varianza por componente: {varianza_explicada}")
    print(f"Varianza total retenida: {total_varianza:.2%}")
    
    # Mostramos las primeras 5 filas transformadas
    df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
    print("\nPrimeras muestras en el nuevo espacio 2D:")
    print(df_pca.head())

def ejercicio_02():
    ENUNCIADO = """ Ejercicio 2 - 
Objetivo: Aplicar el algoritmo de vecinos más cercanos para clasificar nuevasK-Nearest Neighbors (KNN): Clasificación Espacial muestras.
Enunciado del Reto: Un sistema de clasificación automática en invernaderos requiere identificar especies en
tiempo real. Implementa un modelo KNN con 3 vecinos (k=3) sobre el dataset Iris y predice la clase de una
flor cuyas medidas son [5.5, 2.4, 3.8, 1.1]. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    
    # Datos
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
    test_size=0.2, random_state=42)
    
    # Modelo KNN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # Predicción de nueva muestra
    nueva_muestra = [[5.5, 2.4, 3.8, 1.1]]
    prediccion = knn.predict(nueva_muestra)
    nombre_especie = iris.target_names[prediccion][0]
    print(f"Resultado de clasificación: {nombre_especie}")
    print(f"Precisión en el set de prueba: {knn.score(X_test, y_test):.2f}")

def ejercicio_03():
    ENUNCIADO = """ Ejercicio 3 - Árboles de Decisión: Interpretación de Reglas
Objetivo: Analizar y extraer las reglas de decisión lógicas generadas por un modelo.
Enunciado del Reto: El departamento legal de una empresa exige que los modelos de IA sean "explicables".
Entrena un Árbol de Decisión con el dataset Iris y genera una representación en texto de las reglas que el
modelo utiliza para clasificar una flor como 'Setosa', 'Versicolor' o 'Virginica'. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.tree import DecisionTreeClassifier, export_text
    from sklearn import datasets
    
    # Carga y entrenamiento
    iris = datasets.load_iris()
    clf = DecisionTreeClassifier(max_depth=3, random_state=1)
    clf.fit(iris.data, iris.target)
    
    # Extracción de reglas en formato texto
    reglas = export_text(clf, feature_names=iris.feature_names)
    print("Árbol de Decisión - Reglas de Clasificación:")
    print(reglas)

def ejercicio_04():
    ENUNCIADO = """ Ejercicio 4 - Bosque Aleatorio (Random Forest): Ensambles
Objetivo: Aplicar modelos de ensamble para mejorar la robustez de la clasificación.
Enunciado del Reto: Para evitar que el modelo se aprenda los datos de memoria (overfitting), se decide
utilizar un Bosque Aleatorio. Crea un bosque con 100 árboles para clasificar el dataset Iris e informa de la
precisión media obtenida """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn import datasets
    # Datos
    iris = datasets.load_iris()
    # Bosque Aleatorio con 100 estimadores
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Evaluación mediante validación cruzada
    scores = cross_val_score(rf, iris.data, iris.target, cv=5)
    print(f"Precisión por cada fold: {scores}")
    print(f"Precisión media del Bosque Aleatorio: {scores.mean():.4f}")


def ejercicio_05():
    ENUNCIADO = """ Ejercicio 5 - Redes Neuronales: Perceptrón Multicapa (MLP)
Objetivo: Aplicar una red neuronal básica para la clasificación de patrones complejos.
Enunciado del Reto: Como introducción al Deep Learning, implementa una red neuronal tipo MLP con una
capa oculta de 10 neuronas para clasificar las especies de Iris. Asegúrate de limitar las iteraciones a 1000 para
controlar el tiempo de entrenamiento.
 """    
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn import datasets
    
    # Carga y escalado (importante para Redes Neuronales)
    iris = datasets.load_iris()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(iris.data)
    
    # Creación de la Red Neuronal
    mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=1)
    mlp.fit(X_scaled, iris.target)
    print(f"Precisión de la Red Neuronal: {mlp.score(X_scaled, iris.target):.4f}")


def ejercicio_06():
    ENUNCIADO = """ Ejercicio 6 - PCA + KNN: Impacto de la Reducción
Objetivo: Analizar cómo afecta la reducción de dimensiones al rendimiento de un clasificador.
Enunciado del Reto: ¿Es mejor clasificar con todos los datos o con los componentes principales? Compara la
precisión de un KNN usando los datos originales de Iris frente a un KNN usando solo los 2 primeros
componentes de PCA.
 """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.decomposition import PCA
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import datasets

    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    
    # 1. KNN con datos originales
    knn_orig = KNeighborsClassifier(n_neighbors=5).fit(X, y)
    acc_orig = knn_orig.score(X, y)
    
    # 2. KNN con PCA (2 componentes)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    knn_pca = KNeighborsClassifier(n_neighbors=5).fit(X_pca, y)
    acc_pca = knn_pca.score(X_pca, y)
    print(f"Precisión (Datos 4D): {acc_orig:.4f}")
    print(f"Precisión (Datos 2D PCA): {acc_pca:.4f}")


def ejercicio_07():
    ENUNCIADO =""" Ejercicio 7 - Importancia de Características (Feature Importance)
Objetivo: Evaluar qué variables son determinantes en el proceso de clasificación.
Enunciado del Reto: Un botánico desea saber qué medida de la flor (largo/ancho de sépalo/pétalo) es la más
útil para diferenciar especies. Utiliza un modelo de Random Forest para extraer y mostrar el ranking de
importancia de las características del dataset Iris."""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import datasets
    import matplotlib.pyplot as plt
    iris = datasets.load_iris()
    rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(iris.data,
    iris.target)
    # Obtener importancia
    importancias = rf.feature_importances_
    # Mostrar resultados
    for nombre, imp in zip(iris.feature_names, importancias):
        print(f"Variable: {nombre} | Importancia: {imp:.4f}")
    
    # Gráfico rápido
    plt.barh(iris.feature_names, importancias)
    plt.title("Importancia de Variables en Iris")
    plt.show()

def ejercicio_08():
    ENUNCIADO ="""Ejercicio 8 - Optimización de Hiperparámetros en Árboles
Objetivo: Evaluar el efecto de la profundidad del árbol en la generalización.
Enunciado del Reto: Los árboles muy profundos tienden a sobreajustar. Compara un Árbol de Decisión con
profundidad infinita (None) frente a uno limitado a 2 niveles (max_depth=2) usando el dataset Iris. ¿Cuál
elegirías para un entorno de producción?"""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)
    
    # Árbol profundo vs Árbol podado
    profundo = DecisionTreeClassifier(max_depth=None).fit(X_train, y_train)
    podado = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    print(f"Profundo - Entrenamiento: {profundo.score(X_train, y_train):.2f} | Test:{profundo.score(X_test, y_test):.2f}")
    print(f"Podado - Entrenamiento: {podado.score(X_train, y_train):.2f} | Test:{podado.score(X_test, y_test):.2f}")

def ejercicio_09():
    ENUNCIADO = """ Ejercicio 9 - Comparativa Maestra de Modelos
Objetivo: Evaluar múltiples arquitecturas para seleccionar el mejor algoritmo para un caso de uso.
Enunciado del Reto: Se te pide recomendar un único algoritmo para clasificar flores en una app móvil.
Compara KNN, Árbol de Decisión y Random Forest. Muestra una tabla comparativa de precisión y selecciona
el ganador.
"""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn import datasets

    iris = datasets.load_iris()
    modelos = {
    "KNN": KNeighborsClassifier(),"Árbol": DecisionTreeClassifier(), "Random Forest": RandomForestClassifier()}
    for nombre, mod in modelos.items():
        res = cross_val_score(mod, iris.data, iris.target, cv=5)
        print(f"Algoritmo: {nombre:15} | Precisión: {res.mean():.4f}")

def ejercicio_10():
    ENUNCIADO ="""Ejercicio 10 - Creación de un Clasificador Inteligente (Ensemble)
Objetivo: Crear una solución compleja que integre preprocesamiento y selección de modelos.
Enunciado del Reto: Crea un script final que reciba una muestra desconocida, la normalice, aplique PCA para
visualizarla y luego use el mejor modelo de los anteriores para clasificarla, imprimiendo un informe completo
del proceso.
"""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np
    from sklearn import datasets

    iris = datasets.load_iris()

    # 1. Crear el Pipeline (Flujo de trabajo)
    flujo_ia = Pipeline([
        ('escalado', StandardScaler()),
        ('pca', PCA(n_components=2)),
        ('clasificador', RandomForestClassifier(n_estimators=100))
    ])
    
    # 2. Entrenar con todos los datos
    flujo_ia.fit(iris.data, iris.target)
    
    # 3. Nueva muestra y diagnóstico
    muestra = np.array([[5.1, 3.5, 1.4, 0.2]])
    diagnostico = flujo_ia.predict(muestra)
    probabilidad = flujo_ia.predict_proba(muestra).max()
    print("--- INFORME DE DIAGNÓSTICO INTELIGENTE ---")
    print(f"Especie Detectada: {iris.target_names[diagnostico][0].upper()}")
    print(f"Confianza del modelo: {probabilidad:.2%}")
    print("Proceso: Escalado -> PCA(2D) -> Random Forest")


# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ej_01. PCA: Reducción de Dimensionalidad": ejercicio_01, 
        "Ej_02. K-Nearest Neighbors (KNN): Clasificación Espacial ": ejercicio_02 , 
        "Ej_03. Árboles de Decisión: Interpretación de Reglas": ejercicio_03,
        "Ej_04. Bosque Aleatorio (Random Forest): Ensambles": ejercicio_04,
        "Ej_05. Redes Neuronales: Perceptrón Multicapa (MLP)": ejercicio_05,
        "Ej_06. PCA + KNN: Impacto de la Reducción": ejercicio_06,
        "Ej_07. Importancia de Características (Feature Importance)": ejercicio_07,
        "Ej_08. Ejercicio 8 - Optimización de Hiperparámetros en Árboles": ejercicio_08,
        "Ej_09. Comparativa Maestra de Modelos": ejercicio_09,
        "Ej_10. Creación de un Clasificador Inteligente (Ensemble)": ejercicio_10,
    }
    while (True):
        i = menuDvd.MenuDiccionario(menu, tituloMenu='Ejercicios de Analisis de Datos - Modulo 2', num_char=60)
        if i == 0: break  #PRIMERO LA DE SALIDA        
        for index ,ejer in enumerate(menu):
            if i == index + 1:
                menu[ejer]() 
                # print ("_"*30)

    # ■■■■■■■■■ SALIDA 
    print("\n Bye Bye   🐝  🐝 ")


# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    print("Ejercicios de Analisis de Datos - Modulo 2")
    main()
