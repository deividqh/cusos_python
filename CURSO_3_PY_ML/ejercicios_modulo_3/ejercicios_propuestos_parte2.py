from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from  colorama import Fore, Style
import os           # Para Limpiar la terminal con  os.system('cls') 
# ■■■■■■■■■ mias
import  menuDvd     # Funcion que crea un menu y devuelve un int(opcion)
from modulos.datos import get_d_datos

def ejercicio_01():
    ENUNCIADO = """ El Misterio de los Kernels: 
    • Genera un dataset no lineal (usando make_circles o make_moons de Scikit-Learn) y 
    • demuestra cómo un SVM con kernel 'linear' fracasa mientras que uno con kernel 'rbf' logra una 
    separación casi perfecta. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    import matplotlib.pyplot as plt
    from sklearn.datasets import make_circles
    from sklearn.svm import SVC
    import numpy as np
    X, y = make_circles(n_samples=500, noise=0.05, factor=0.5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    algoritmos = {'lineal':SVC(kernel='linear'), 'rbf':SVC(kernel='rbf')}

    fig, ax_es = plt.subplots(1, len(algoritmos), figsize=(12, 5))

    for i, (kernel, algoritmo) in enumerate(algoritmos.items()):
        
        modelo = algoritmo.fit(X_train,y_train)        
        prediccion = modelo.predict(X_test)
        precision = modelo.score(X_test, y_test)
        
        # LOG
        print(f"Precisión Kernel {kernel}: {precision:.2f} ")

        # ■ UI
        if ax_es[i]: 
            ax_es[i].scatter(X_test[:, 0], X_test[:, 1], c = prediccion, edgecolors='k')
            ax_es[i].set_title(f'Kernel {kernel} ')
    pass
    plt.show()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from colorama import Fore, Style

def generar_dataset(muestras=100, random_state=42):
    rng = np.random.default_rng(random_state)
    # ■ Creamos etiquetas primero: 0 para Legítimo, 1 para Spam
    target = rng.integers(0, 2, size=muestras)
    
    # ■ Creamos una matriz de ceros para los datos
    data = np.zeros((muestras, 3))    
    for i in range(muestras):
        if target[i] == 1:  # Si es SPAM, más frecuencia de estas palabras
            data[i] = rng.integers(3, 10, size=3)  # Frecuencias entre 3 y 10
        else:               # Si es LEGÍTIMO, menos frecuencia
            data[i] = rng.integers(0, 4, size=3)   # Frecuencias entre 0 y 4

    return {
        'data': data,
        'target': target,
        'target_names': np.array(['Legitimo', 'Spam']),
        'feature_names': ['oferta', 'gratis', 'urgente'],
        'size': muestras
    }

def ejercicio_02():
    ENUNCIADO = """ Actividad 2 - Clasificador de Spam (Naive Bayes): 
    • Crea un pequeño conjunto de datos sintético donde las características representen la 
      frecuencia de palabras como "oferta", "gratis" o "urgente".
    • Entrena un modelo de Naive Bayes para clasificar si un mensaje es "Spam" o "Legítimo". """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import classification_report, accuracy_score
    
    # ■ datos
    correo = generar_dataset(150, 123)
    X = correo['data']
    y = correo['target']
    
    # ■ ■ ■ ■ ■ ■ ■ Aquí tendría que haber Exploraciópn de los datos para ver correlaciones etc,...
    
    # ■ Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # ■ Fit
    algoritmo = MultinomialNB()
    modelo = algoritmo.fit(X=X_train, y=y_train)
    
    # ■ ■ ■ ■ ■ ■ ■ Aquí tendría que haber metricas y re-evaluación del modelo 

    # ■ Predict
    prediccion = modelo.predict(X=X_test)
    
    # ■ MÉTRICAS Y LOGS
    print(f"{Fore.GREEN}Resultados del Modelo:{Style.RESET_ALL}")
    print(f"Precisión: {accuracy_score(y_true=y_test, y_pred=prediccion):.2%}")
    print("\nReporte de Clasificación:")
    print(classification_report(y_true = y_test, y_pred = prediccion, target_names = correo['target_names']))

    # ■ Prueba rápida con datos nuevos
    test_mensaje = [[8, 7, 9]] 
    prediccion = modelo.predict(test_mensaje) # Corregido de 'clf' a 'modelo'
    print(f"\nPrueba mensaje sospechoso {test_mensaje}:")
    print(f"Resultado --> {Fore.RED if prediccion[0] == 1 else Fore.CYAN}{correo['target_names'][prediccion[0]]}")

    print(f"\n{Fore.YELLOW} DUDA: No entiendo el Reporte de Clasificación ni, si quisiera cambiar la precisión que tengo que hacer?  {Style.RESET_ALL}:")


def ejercicio_03():
    ENUNCIADO = """ Actividad 3 - Reducción de Ruido con PCA: 
    • Utiliza el dataset digits (números escritos a mano) de Scikit-Learn. 
    • Aplica PCA para determinar cuántos componentes principales son necesarios para 
      mantener al menos el 90% de la varianza original. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    from sklearn.decomposition import PCA

    digits = get_d_datos('digits')    
    if not digits: return
    # Las columnas de la dimensión son el numero de componentes total del dataset
    _, columnas = digits.data.shape

    numero_componentes = columnas   # aquí lo igualo para que tenga sentido
    varianza_final = 0              # acumulador de varianza, empieza en 0.
    candidato = 0                   # el resultado buscado. 
    for i in range(1, numero_componentes + 1):
        pca = PCA(n_components = i)
        X_pca = pca.fit_transform(digits.data)
        
        # Varianza-Explicada
        varianza_explicada = pca.explained_variance_ratio_
        total_varianza = varianza_explicada.sum()

        print(f"Varianza x componente: {[f'{v:.2f}' for v in varianza_explicada]}")
        print(f"Varianza total retenida: {total_varianza:.2%}")

        distancia = abs(total_varianza - 0.9) 
        if total_varianza >= 0.9:
            varianza_final = total_varianza
            candidato = i
            break
    
    print(f"{Fore.YELLOW}RESULTADO:{Style.RESET_ALL}")
    print(f"Necesitamos {candidato} componentes para tener un {varianza_final:.2%} de varianza.")

def ejercicio_04():
    ENUNCIADO = """ Actividad 4 - Búsqueda del Vecino Óptimo: 
    • Implementa un bucle que pruebe valores de k (de 1 a 20) para un modelo KNN. 
    • Grafica la precisión en el conjunto de prueba para identificar el valor de k 
      que ofrece el 'mejor equilibrio'. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    
    from sklearn.neighbors import KNeighborsClassifier as KNN

    (X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names) = get_d_datos('iris', 30, True)    
    # dd = get_d_datos('iris', 30)    
    # if not dd: return
    print("\n■■■■■■■■■ ")
    
    lista_k = []            # para k
    lista_p = []    # para_las precisiones
    # compilado = {'k':i, 'p':precision}
    for i in range(1, 21):
        algoritmo = KNN(n_neighbors=i)
        modelo = algoritmo.fit(X = X_train,  y = y_train)
        precision = modelo.score(X = X_test, y = y_test)        
        print(f'Precision modelo KNN entrenado  con k = {i} vecinos = {precision:.2f}')
        pass
        # Cacho para la grafica
        lista_k.append(i)
        lista_p.append(precision)
    pass
    # 2. Graficamos los resultados
    plt.plot(X = lista_k, y = lista_p, marker='o' )
    plt.xlabel('Valor de K (n_neighbors)')
    plt.ylabel('Precisión (Score)')
    plt.xticks(range(1, 21))
    plt.show()

def ejercicio_05():
    ENUNCIADO = """ Actividad 5 - Poda de Árboles (Pruning): 
    • Entrena un Árbol de Decisión sobre un dataset complejo y observa su profundidad. 
    • Luego, aplica restricciones de min_samples_leaf y max_depth para simplificarlo y 
    • explica cómo esto ayuda a la generalización. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")



def ejercicio_06():
    ENUNCIADO = """  Actividad 6 - Estabilidad del Bosque: Compara un único Árbol de Decisión frente a un Random Forest
de 500 árboles. Evalúa ambos modelos 10 veces con diferentes particiones de datos (seeds) y analiza
cuál de los dos presenta una varianza menor en sus resultados """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")



def ejercicio_07():
    ENUNCIADO = """ Actividad 7 - Visualización Comparativa (LDA vs PCA): Toma un dataset con 3 clases y aplica LDA y
PCA para reducirlo a 2D. Genera ambos gráficos uno al lado del otro y explica por qué LDA suele
mostrar grupos de clases mucho más definidos. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_08():
    ENUNCIADO = """ Actividad 8 - Arquitectura de Neuronas: Diseña una Red Neuronal (MLP) para un problema de
clasificación multiclase. Experimenta variando el número de capas ocultas (ej. una capa de 50 neuronas
vs. tres capas de 10 neuronas) y reporta cuál converge más rápido. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_09():
    ENUNCIADO = """ Actividad 9 - Análisis de Falsos Alarmas: En un sistema de detección de intrusos (0: Seguro, 1:
Intruso), un Falso Positivo (alarma falsa) genera un coste operativo alto. Utiliza la Matriz de Confusión
para ajustar el umbral de decisión de un modelo y minimizar estas falsas alarmas. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_10():
    ENUNCIADO = """  Actividad 10 - Proyecto Integrador: Scoring Bancario: Desarrolla un Pipeline profesional para
predecir si se debe aprobar un préstamo. El flujo debe: 1. Escalar los datos, 2. Aplicar PCA para eliminar
redundancia, 3. Entrenar un Random Forest y 4. Mostrar un informe de métricas completo (Precision,
Recall y F1-Score).
 """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ejercicio_01. (circles) El Misterio de los Kernels": ejercicio_01, 
        "Ejercicio_02. (custom)  Clasificador de Spam (Naive Bayes)": ejercicio_02 , 
        "Ejercicio_03. (digits)  Reducción de Ruido con PCA": ejercicio_03,
        "Ejercicio_04. 🌷🌷🌷🌷 Búsqueda del Vecino Óptimo": ejercicio_04,
        "Ejercicio_05. Poda de Árboles (Pruning)": ejercicio_05,
        "Ejercicio_06. ": ejercicio_06,
        "Ejercicio_07. ": ejercicio_07,
        "Ejercicio_08. ": ejercicio_08,
        "Ejercicio_09. ": ejercicio_09,
        "Ejercicio_10. ": ejercicio_10,
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
    print("Ejercicios de  Modulo 3 - Algoritmos - Metricas Parte 2")
    main()
