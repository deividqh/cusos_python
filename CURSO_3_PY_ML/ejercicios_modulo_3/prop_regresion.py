
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_01():
    ENUNCIADO = """ Actividad 1 - Rendimiento Académico: 
    Una academia desea predecir la nota final de un alumno basada únicamente en las horas de estudio semanales. 
    Genera un dataset sintético y aplica una Regresión Lineal Simple. Visualiza el resultado.
""" 
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_02():
    ENUNCIADO = """ Actividad 2 - Satisfacción Laboral (Inferencia): 
Utiliza Statsmodels para analizar si el número de días de teletrabajo al mes influye significativamente en 
el “Score de Felicidad” de los empleados. 
Interpreta el p-valor para una confianza del 95%.
"""  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_03():
    ENUNCIADO = """ Actividad 3 - El Algoritmo desde Cero: 
Calcula manualmente los parámetros de una recta que relacione los “Minutos de uso de una App” con la “Batería consumida”. 
Valida tus cálculos comparándolos con el resultado de Scikit-Learn.
"""  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_04():
    ENUNCIADO = """ Actividad 4 - Tasación de Vehículos: 
Crea un modelo de Regresión Múltiple para estimar el precio de venta de coches usados 
considerando: Años de antigüedad, Kilometraje y Caballos de fuerza (HP).
    """  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_05():
    ENUNCIADO = """ Actividad 5 - Eficiencia Energética con Categorías: 
Predice el gasto en calefacción de una vivienda usando los metros cuadrados y la 
variable categórica “Tipo de Aislamiento” (Pobre, Medio, Excelente). No olvides usar One-Hot Encoding.
""" 
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_06():
    ENUNCIADO = """ Actividad 6 - Trayectoria de Mercado: Un producto nuevo presenta una curva de
ventas que aumenta rápido y luego se estabiliza. Aplica una Regresión Polinomial de
grado 2 y grado 3, y elige visualmente cuál captura mejor la tendencia.
"""  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_07():
    ENUNCIADO = """Actividad 7 - Prevención del Overfitting: Genera un conjunto de datos con mucho
ruido que represente la temperatura horaria. Entrena modelos polinomiales de grado 1 al 15
y detecta en qué punto el modelo empieza a “memorizar” el ruido en lugar de la tendencia.
"""  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_08():
    ENUNCIADO = """Actividad 8 - Diagnóstico Médico (Logística): Entrena un modelo de Regresión
Logística para predecir si un paciente tiene riesgo de hipertensión (1: Riesgo, 0: Normal)
basado en su nivel de estrés y edad.
"""  
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_09():
    ENUNCIADO = """Actividad 9 - Auditoría de Modelos de Fraude: Has entrenado un modelo para
detectar transacciones fraudulentas. Genera la Matriz de Confusión y el reporte de
clasificación. Explica por qué, en este caso, el “Recall” (Sensibilidad) es más importante
que la “Accuracy” (Exactitud).
"""     
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_10():
    ENUNCIADO = """Actividad 10 - Proyecto Final: Rendimiento Agrícola: Desarrolla un Pipeline completo
para predecir las toneladas de cosecha por hectárea. Debes incluir: carga de datos
(sintéticos), división Train/Test, entrenamiento de una regresión múltiple (usando agua,
fertilizante y horas de sol) y reporte de métricas MSE y R2. """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
