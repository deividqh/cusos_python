from colorama import Fore, Style
def ejer_1():
    ENUNCIADO = """ Ejercicio 1 - Regresión Lineal Simple (Scikit-Learn)
    Objetivo: Aplicar un modelo de regresión lineal simple para identificar la relación entre una variable
    independiente y una dependiente en un contexto de marketing.
    Enunciado del Reto: Una empresa de e-commerce quiere entender cómo su inversión mensual en publicidad
    en redes sociales (en miles de dólares) afecta sus ventas totales. Utiliza los datos generados sintéticamente
    para entrenar un modelo que prediga las ventas basadas en la inversión publicitaria """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    from sklearn.linear_model import LinearRegression 
    # 1. Generación de datos sintéticos 
    np.random.seed(42) 
    inversion = np.random.normal(50, 15, 100).reshape(-1, 1) 
    ventas = 5 + 2.5 * inversion + np.random.normal(0, 10, (100, 1)) 
    # 2. Creación e entrenamiento del modelo 
    modelo = LinearRegression() 
    modelo.fit(inversion, ventas) 
    # 3. Predicción y visualización 
    ventas_pred = modelo.predict(inversion) 
    plt.scatter(inversion, ventas, color='blue', label='Datos reales') 
    plt.plot(inversion, ventas_pred, color='red', linewidth=2, label='Línea de regresión') 
    plt.title('Impacto de la Publicidad en las Ventas') 
    plt.xlabel('Inversión (Miles $)') 
    plt.ylabel('Ventas (Unidades)') 
    plt.legend() 
    plt.show() 
    print(f"Coeficiente (Pendiente): {modelo.coef_[0][0]:.2f}") 
    print(f"Intercepto: {modelo.intercept_[0]:.2f}") 

    JUSTIFICACION = """ Justificación: El alumno demuestra su capacidad para instanciar, ajustar y visualizar un modelo básico de
    Scikit-learn, traduciendo una relación teórica en una representación matemática funcional """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    
def ejer_2():
    ENUNCIADO = """ Ejercicio 2 - Regresión Lineal con Statsmodels
    Objetivo: Analizar la significancia estadística de los coeficientes de un modelo para validar hipótesis de
    negocio.
    Enunciado del Reto: El departamento de RRHH sospecha que los años de experiencia son el factor
    determinante en la productividad de los empleados. Utiliza Statsmodels para realizar una regresión y analiza
    el valor p (p-value) para confirmar si esta relación es estadísticamente significativa """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import statsmodels.api as sm 
    import numpy as np 

    # 1. Datos sintéticos: Años de experiencia vs Score de productividad 
    np.random.seed(42) 
    experiencia = np.random.randint(1, 20, 50) 
    productividad = 20 + 3.5 * experiencia + np.random.normal(0, 5, 50) 
    # 2. Preparación de los datos para Statsmodels (añadir constante para el     intercepto) 
    X = sm.add_constant(experiencia)  
    y = productividad 
    # 3. Ajuste del modelo por Mínimos Cuadrados Ordinarios (OLS) 
    modelo_stats = sm.OLS(y, X).fit() 
    # 4. Mostrar el resumen estadístico 
    print(modelo_stats.summary())
    JUSTIFICACION = """ 
    # Análisis del resultado (Comentario didáctico)
    # Si P > |t| para la variable x1 es < 0.05, la relación es significativa
    Justificación: Esta tarea obliga al alumno a ir más allá de la predicción, interpretando métricas estadísticas
    críticas como el R-cuadrado y el p-valor para sustentar decisiones corporativas. """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    pass

def ejer_3():
    ENUNCIADO = """ Ejercicio 3 - Ajuste de Mínimos Cuadrados (Fundamentos)
    Objetivo: Aplicar la fundamentación matemática de la regresión mediante el cálculo manual de los
    parámetros en un escenario de consumo energético.
    Enunciado del Reto: Imagina que no tienes acceso a librerías de alto nivel. Calcula manualmente la pendiente
    ($m$) y el intercepto ($b$) de la recta de regresión $y = mx + b$ para predecir el consumo eléctrico de un
    edificio basado en la temperatura exterior, utilizando las fórmulas de mínimos cuadrados """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np 
    # Datos: Temperatura (X) vs Consumo Kw/h (y) 
    X = np.array([15, 20, 25, 30, 35]) 
    y = np.array([120, 150, 190, 240, 300]) 
    # Cálculo de medias 
    x_media = np.mean(X) 
    y_media = np.mean(y) 
    # Cálculo de la pendiente (m = sum((x-mx)(y-my)) / sum((x-mx)^2)) 
    numerador = np.sum((X - x_media) * (y - y_media)) 
    denominador = np.sum((X - x_media)**2) 
    m = numerador / denominador 
    # Cálculo del intercepto (b = y_media - m * x_media) 
    b = y_media - m * x_media 
    print(f"Ecuación calculada manualmente: y = {m:.2f}x + {b:.2f}") 
    # Predicción para 40 grados 
    prediccion = m * 40 + b 
    print(f"Predicción para 40°C: {prediccion:.2f} Kw/h")
    JUSTIFICACION = """ Justificación: Al implementar la lógica subyacente sin abstracciones, el alumno consolida la comprensión del
    proceso de optimización que ocurre dentro de las librerías estándar """
    pass
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")

def ejer_4():
    ENUNCIADO = """ Ejercicio 4 - Regresión Lineal Múltiple
    Objetivo: Aplicar el concepto de regresión con múltiples variables predictoras para resolver un problema de
    valoración inmobiliaria.
    AlgoritmosML_Regresión.md
    2026-04-30
    Enunciado del Reto: Desarrolla un modelo que prediga el precio de una vivienda considerando tres factores:
    Metros cuadrados, número de habitaciones y antigüedad de la propiedad """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import pandas as pd 
    from sklearn.linear_model import LinearRegression 
    # 1. Crear dataset sintético 
    data = { 
    'Metros': [60, 80, 100, 120, 150, 200], 
    'Habitaciones': [1, 2, 3, 3, 4, 5], 
    'Antiguedad': [30, 20, 15, 10, 5, 2], 
    'Precio': [120000, 180000, 250000, 310000, 450000, 600000] 
    } 
    df = pd.DataFrame(data) 
    # 2. Separar variables 
    X = df[['Metros', 'Habitaciones', 'Antiguedad']] 
    y = df['Precio'] 
    # 3. Entrenar modelo 
    modelo_mult = LinearRegression() 
    modelo_mult.fit(X, y) 
    # 4. Predicción para un nuevo caso: 110m2, 3 habs, 12 años 
    nuevo_hogar = [[110, 3, 12]] 
    pred_precio = modelo_mult.predict(nuevo_hogar) 
    print(f"Precio estimado para el nuevo hogar: ${pred_precio[0]:,.2f}")
    JUSTIFICACION = """ 
    Justificación: El alumno aprende a manejar estructuras de datos multidimensionales y a entender cómo
    múltiples características contribuyen simultáneamente a un resultado único """
    pass
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")

def ejer_5():
    ENUNCIADO = """ Ejercicio 5 - Tratamiento de Variables Categóricas en Regresión
    import pandas as pd 
    from sklearn.linear_model import LinearRegression 
    Objetivo: Aplicar técnicas de preprocesamiento (One-Hot Encoding) para integrar variables no numéricas en
    un modelo de regresión.
    Enunciado del Reto: En un estudio de costes médicos, el género (Masculino/Femenino) influye en los gastos.
    Transforma esta variable categórica en numérica y entrena un modelo de regresión para predecir el coste
    sanitario """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import pandas as pd 
    from sklearn.linear_model import LinearRegression 
    # 1. Datos con variable categórica 
    df_med = pd.DataFrame({ 
        'Edad': [20, 30, 40, 50, 60], 
        'Genero': ['M', 'F', 'M', 'F', 'M'], 
        'Coste': [2000, 2500, 4200, 5100, 6800] 
    }) 
    # 2. Transformación: One-Hot Encoding 
    df_encoded = pd.get_dummies(data= df_med, columns=['Genero'], drop_first=True) 
    # 3. Entrenamiento 
    X = df_encoded.drop('Coste', axis=1) 
    y = df_encoded['Coste'] 
    model = LinearRegression().fit(X, y) 
    print("Dataset transformado:") 
    print(df_encoded) 
    print(f"\nCoeficientes: {dict(zip(X.columns, model.coef_))}")
    
    JUSTIFICACION = """ Justificación: Esta competencia es vital, ya que los modelos matemáticos solo aceptan números; el alumno
    demuestra que sabe preparar datos del mundo real para el análisis. """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    pass

def ejer_6():
    ENUNCIADO = """ Ejercicio 6 - Regresión Polinomial
    Objetivo: Evaluar cuándo una relación lineal no es suficiente y aplicar una transformación polinomial para
    modelar crecimientos curvos (ej. crecimiento bacteriano).
    Enunciado del Reto: Un biólogo observa que la población de una bacteria crece de forma acelerada. Los
    modelos lineales subestiman el crecimiento. Utiliza PolynomialFeatures de grado 2 para ajustar mejor los
    datos. """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np 
    import matplotlib.pyplot as plt 
    from sklearn.preprocessing import PolynomialFeatures 
    from sklearn.linear_model import LinearRegression 
    # 1. Datos no lineales 
    horas = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1) 
    poblacion = np.array([2, 5, 12, 25, 48, 80]) 
    # 2. Transformación Polinomial (Grado 2) 
    poly = PolynomialFeatures(degree=2) 
    horas_poly = poly.fit_transform(horas) 
    # 3. Ajuste de regresión lineal sobre los datos transformados 
    modelo_poly = LinearRegression().fit(horas_poly, poblacion) 
    # 4. Visualización 
    plt.scatter(horas, poblacion, label='Observaciones') 
    plt.plot(horas, modelo_poly.predict(horas_poly), color='green', label='Ajuste  Polinomial') 
    plt.title('Crecimiento de Población Bacteriana') 
    plt.legend() 
    plt.show() 
    JUSTIFICACION = """ Justificación: El alumno identifica la limitación del modelo lineal y selecciona una herramienta más compleja
    para capturar la naturaleza no lineal de los fenómenos biológicos. """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")

def ejer_7():
    ENUNCIADO = """ Ejercicio 7 - Análisis de Complejidad y Sobreajuste (Overfitting)
    Objetivo: Evaluar el rendimiento de diferentes grados polinomiales para encontrar el equilibrio entre sesgo y
    varianza (predicción de temperatura).
    Enunciado del Reto: Prueba modelos polinomiales de grado 1, 3 y 10 para predecir la temperatura a lo largo
    del día. Identifica visualmente cuál de ellos sufre de "overfitting" (se ajusta demasiado al ruido de los datos). """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np 
    import matplotlib.pyplot as plt 
    from sklearn.pipeline import make_pipeline 
    from sklearn.preprocessing import PolynomialFeatures 
    from sklearn.linear_model import LinearRegression 
    # Datos con ruido 
    x = np.linspace(0, 10, 15).reshape(-1, 1) 
    y = np.sin(x).ravel() + np.random.normal(0, 0.2, 15) 
    grados = [1, 3, 10] 
    plt.figure(figsize=(12, 4)) 
    for i, grado in enumerate(grados): 
        ax = plt.subplot(1, 3, i + 1) 
        modelo = make_pipeline(PolynomialFeatures(grado), LinearRegression()) 
        modelo.fit(x, y) 
        x_plot = np.linspace(0, 10, 100).reshape(-1, 1) 
        plt.scatter(x, y, color='black', s=20) 
        plt.plot(x_plot, modelo.predict(x_plot), label=f'Grado {grado}') 
        plt.title(f"Grado {grado}") 
    plt.tight_layout() 
    plt.show() 
    JUSTIFICACION = """Justificación: La capacidad de discernir entre un buen ajuste y el sobreajuste es lo que diferencia a un
    especialista en IA de un usuario básico de herramientas.  """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    pass
def ejer_8():
    ENUNCIADO = """ Ejercicio 8 - Regresión Logística (Introducción)
    Objetivo: Aplicar un modelo de regresión logística para resolver un problema de clasificación binaria basado
    en probabilidades.
    Enunciado del Reto: Un banco quiere predecir si un cliente aprobará un examen de solvencia basado en sus
    ingresos. Aunque se llama "regresión", genera una frontera de decisión para clasificar (Pasa / No Pasa). """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.linear_model import LogisticRegression 
    import numpy as np 
    # 1. Datos: Ingresos vs Solvencia (0: No, 1: Sí) 
    ingresos = np.array([10, 15, 20, 25, 40, 45, 50, 60, 70]).reshape(-1, 1) 
    solvencia = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1]) 
    # 2. Entrenar modelo 
    log_reg = LogisticRegression() 
    log_reg.fit(ingresos, solvencia) 
    # 3. Predicción de probabilidad para un cliente que gana 30k 
    prob = log_reg.predict_proba([[30]]) 
    clase = log_reg.predict([[30]]) 
    print(f"Cliente con 30k:") 
    print(f"Probabilidad de solvencia: {prob[0][1]*100:.2f}%") 
    print(f"Resultado final: {'Solvente' if clase[0]==1 else 'No Solvente'}") 
    JUSTIFICACION = """Justificación: El alumno entiende el cambio de paradigma de predecir un valor continuo a predecir la
    probabilidad de una categoría.  """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    pass
def ejer_9():
    ENUNCIADO = """  Ejercicio 9 - Evaluación de Regresión Logística
    Objetivo: Analizar el rendimiento de un clasificador mediante la Matriz de Confusión y el Reporte de
    Clasificación.
    Enunciado del Reto: Evalúa el modelo anterior utilizando un conjunto de datos de prueba. ¿Cuántos errores
    cometió el modelo? ¿Cuál es su precisión?"""
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.metrics import confusion_matrix, classification_report 
    import seaborn as sns 
    import matplotlib.pyplot as plt 
    # Datos de prueba reales vs predicciones simuladas 
    y_test = [0, 0, 1, 1, 0, 1, 0, 1] 
    y_pred = [0, 1, 1, 1, 0, 1, 0, 0] # El modelo falló en 2 casos 
    # Matriz de Confusión 
    cm = confusion_matrix(y_test, y_pred) 
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues') 
    plt.xlabel('Predicho') 
    plt.ylabel('Real') 
    plt.show() 
    # Reporte detallado 
    print(classification_report(y_test, y_pred)) 
    JUSTIFICACION = """ Justificación: El alumno demuestra que sabe interpretar si un modelo es útil en la práctica analizando falsos
    positivos y negativos, no solo la exactitud global """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")

def ejer_10():
    ENUNCIADO = """ Ejercicio 10 - Creación de un Pipeline de Regresión Completo
    Objetivo: Crear un flujo de trabajo completo que incluya división de datos, entrenamiento y validación de
    una regresión múltiple.
    Enunciado del Reto: Desarrolla un script profesional para predecir las emisiones de CO2 de vehículos
    basándose en el tamaño del motor y los cilindros. El script debe dividir los datos en entrenamiento (80%) y
    prueba (20%), entrenar el modelo y reportar el Error Cuadrático Medio (MSE). """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import pandas as pd 
    from sklearn.model_selection import train_test_split 
    from sklearn.linear_model import LinearRegression 
    from sklearn.metrics import mean_squared_error, r2_score 
    # 1. Dataset Sintético 
    data = { 
    'Motor_Size': [2.0, 2.4, 3.0, 3.5, 1.5, 4.0, 5.0, 2.0, 3.2, 1.6], 
    'Cylinders': [4, 4, 6, 6, 4, 8, 8, 4, 6, 4], 
    'CO2_Emissions': [196, 221, 244, 270, 160, 320, 390, 200, 260, 175] 
    } 
    df = pd.DataFrame(data) 
    # 2. División de datos 
    X = df[['Motor_Size', 'Cylinders']] 
    y = df['CO2_Emissions'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
    # 3. Entrenamiento 
    modelo_final = LinearRegression() 
    modelo_final.fit(X_train, y_train) 
    # 4. Evaluación 
    predicciones = modelo_final.predict(X_test)
    mse = mean_squared_error(y_test, predicciones) 
    r2 = r2_score(y_test, predicciones) 
    print("--- Informe Final del Modelo ---") 
    print(f"Error Cuadrático Medio (MSE): {mse:.2f}") 
    print(f"R-Cuadrado (Precisión): {r2:.2f}")  
    
    JUSTIFICACION = """ Justificación: Este ejercicio final integra todas las piezas: gestión de datos, validación cruzada y métricas de
    error, demostrando que el alumno puede orquestar un proyecto de IA desde cero. """
    print (f"\n{Fore.BLUE}{JUSTIFICACION}{Style.RESET_ALL}")
    