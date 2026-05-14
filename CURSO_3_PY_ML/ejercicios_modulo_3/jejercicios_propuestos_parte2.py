from colorama import Fore, Style

def ejercicio_01():
    ENUNCIADO = """ El Misterio de los Kernels: Genera un dataset no lineal (usando make_circles o
make_moons de Scikit-Learn) y demuestra cómo un SVM con kernel 'linear' fracasa mientras que uno
con kernel 'rbf' logra una separación casi perfecta. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_02():
    ENUNCIADO = """ Actividad 2 - Clasificador de Spam (Naive Bayes): Crea un pequeño conjunto de datos sintético
donde las características representen la frecuencia de palabras como "oferta", "gratis" o "urgente".
Entrena un modelo de Naive Bayes para clasificar si un mensaje es "Spam" o "Legítimo". """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_03():
    ENUNCIADO = """ Actividad 3 - Reducción de Ruido con PCA: Utiliza el dataset digits (números escritos a mano) de
Scikit-Learn. Aplica PCA para determinar cuántos componentes principales son necesarios para
mantener al menos el 90% de la varianza original. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_04():
    ENUNCIADO = """ Actividad 4 - Búsqueda del Vecino Óptimo: Implementa un bucle que pruebe valores de k (de 1 a 20)
para un modelo KNN. Grafica la precisión en el conjunto de prueba para identificar el valor de k que
ofrece el mejor equilibrio. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

def ejercicio_05():
    ENUNCIADO = """ Actividad 5 - Poda de Árboles (Pruning): Entrena un Árbol de Decisión sobre un dataset complejo y
observa su profundidad. Luego, aplica restricciones de min_samples_leaf y max_depth para
simplificarlo y explica cómo esto ayuda a la generalización.
 """
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
        "Ejercicio_01. ": ejercicio_01, 
        "Ejercicio_02. ": ejercicio_02 , 
        "Ejercicio_03. ": ejercicio_03,
        "Ejercicio_04. ": ejercicio_04,
        "Ejercicio_05. ": ejercicio_05,
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
    print("Ejercicios de Analisis de Datos - Modulo 2")
    main()
