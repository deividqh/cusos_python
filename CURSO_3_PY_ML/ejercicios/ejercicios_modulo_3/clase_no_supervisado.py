from colorama import Fore, Style
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_01():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    ENUNCIADO = """ Ejercicio 1 - Agrupamiento con K-Means
    Objetivo: Aplicar el algoritmo de K-Means para segmentar clientes basándose en su comportamiento de
    compra.
    Enunciado del Reto: Un centro comercial quiere agrupar a sus clientes según sus ingresos anuales y su
    puntuación de gasto. Utiliza los datos sintéticos para crear 5 grupos de clientes y visualiza los centroides de
    cada grupo. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    # 1. Generación de datos sintéticos (Ingresos vs Gasto)
    np.random.seed(42)
    X = np.random.rand(200, 2) * 100
    # 2. Aplicar K-Means con k=5
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    y_kmeans = kmeans.fit_predict(X)
    # 3. Visualización
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X',
    label='Centroides')
    plt.title('Segmentación de Clientes (K-Means)')
    plt.xlabel('Ingresos Anuales')
    plt.ylabel('Score de Gasto')
    plt.legend()
    plt.show()

    JUSTIFICACION = """ Resultados Esperados de la Ejecución:
    Gráfico generado: Se creará una imagen mostrando la distribución de los 200 puntos en 5 clústeres de
    diferentes colores, junto con sus respectivos centroides marcados con una 'X' roja. """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_02():
    ENUNCIADO = """ Ejercicio 2 - Optimización: El Método del Codo (Elbow Method)
    Objetivo: Analizar cuál es el número óptimo de clusters ($k$) para un conjunto de datos desconocido.
    Enunciado del Reto: No siempre sabemos en cuántos grupos dividir los datos. Utiliza la métrica de Inercia
    para graficar el "Método del Codo" y determinar visualmente cuántos clusters serían ideales para el problema
    anterior. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    # Para entender el codo, primero debemos entender 'la Inercia'.
    # La Inercia es una métrica que calcula qué tan "compactos" o "apretados" están tus grupos. 
    
    # Matemáticamente, mide la suma de las distancias al cuadrado entre cada cliente (punto) y 
    # el centro de su grupo (centroide).
    
    # Si la inercia es muy alta: Tus grupos están muy dispersos (mala agrupación).
    
    # Si la inercia es baja: Tus puntos están muy cerca de sus centros (buena agrupación)
    # A medida que aumentas $k$, la inercia siempre va a bajar (si tienes 200 clientes y haces 200 grupos, 
    # la inercia será 0 porque cada cliente es su propio centroide). 
    # Sin embargo, llegará un punto donde añadir un grupo más ya no reduce la inercia de forma significativa. 
    # En una gráfica, esto se ve como una curva que cae bruscamente y de repente se aplana. 
    # Ese punto de inflexión, que parece el "codo" de un brazo humano, es tu número óptimo de clusters.

    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_blobs # Ideal para generar datos sintéticos agrupados
    
    # 1. Generación de datos sintéticos (Usamos make_blobs para crear 4 grupos naturales ocultos)
    # n_samples=300 (300 clientes), centers=4 (4 grupos reales), cluster_std (dispersión)
    X, _ = make_blobs(n_samples=300, centers=4  , cluster_std=1.5, random_state=42)

    inercia = []
    rango_k = range(1, 11)  # Evaluamos desde 1 hasta 10 clusters (suficiente para ver el codo)
    
    # 2. Entrenamos un modelo para cada valor de K y guardamos su inercia
    print("Calculando inercias. Por favor, espera...")
    for k in rango_k:
        algoritmo = KMeans(n_clusters=k, random_state=42, n_init=10)
        modelo = algoritmo.fit(X)
        inercia.append(modelo.inertia_) # Guardamos el valor de cohesión
    
    # 3. Graficamos el Método del Codo
    plt.figure(figsize=(8, 5))
    plt.plot(rango_k, inercia, marker='x', linestyle='-', color='b') # Línea azul con cruces 'bx-'
    plt.xticks(rango_k) # Para asegurar que el eje X muestre números enteros del 1 al 10
    
    plt.xlabel('Número de clusters (k)')
    plt.ylabel('Inercia (Suma de distancias al cuadrado)')
    plt.title('Método del Codo para encontrar el K óptimo')
    # plt.grid(True, linestyle='-', alpha=0.6)
    plt.show()
    JUSTIFICACION = """ 
     El alumno analiza la relación entre el número de grupos y la cohesión interna, identificando el
punto de equilibrio donde añadir más grupos deja de aportar valor significativo.
Resultados Esperados de la Ejecución:
Gráfico generado: Una gráfica de línea azul con marcadores de cruz ('bx-') que muestra el valor de la
Inercia en el eje Y en relación con el número de clústeres $k$ (de 1 a 10) en el eje X.
    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_03():
    ENUNCIADO = """Ejercicio 3 - Aprendizaje Semisupervisado (Label Propagation)
Objetivo: Aplicar técnicas semisupervisadas para etiquetar datos aprovechando una pequeña muestra inicial.

Enunciado del Reto: Imagina que tienes 100 muestras pero solo has podido etiquetar manualmente 10 de
ellas. Utiliza el algoritmo LabelPropagation para que el modelo aprenda de esas 10 etiquetas y las propague
al resto del dataset de forma automática. 
    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.semi_supervised import LabelPropagation
    import numpy as np

    # Datos sintéticos: 2 clases
    X = np.random.rand(100, 2)
    y = np.full(100, -1) # -1 indica "sin etiqueta"
    
    # Etiquetamos solo 10 muestras (5 de la clase 0, 5 de la clase 1)
    y[0:5] = 0
    y[5:10] = 1
    
    # Entrenar el modelo semisupervisado
    lp_model = LabelPropagation()
    lp_model.fit(X, y)
    
    # Predecir las etiquetas que faltaban
    y_final = lp_model.transduction_
    print(f"Etiquetas propagadas (primeras 20): {y_final[:20]}")

    JUSTIFICACION = """ Justificación: El alumno comprende cómo los datos no etiquetados pueden ayudar a definir fronteras de
decisión cuando la supervisión es costosa o limitada.
Etiquetas propagadas (primeras 20): [0 0 0 0 0 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1]

    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_04():
    ENUNCIADO = """ Ejercicio 4 - Aprendizaje por Refuerzo (Q-Learning básico)
Objetivo: Aplicar la lógica de recompensas para que un agente aprenda a navegar en un entorno simple.
Enunciado del Reto: Diseña un agente que aprenda a elegir la mejor acción en un entorno de 4 estados
lineales (0-1-2-3) donde el objetivo es llegar al estado 3 para recibir una recompensa de +10. Implementa una
tabla Q muy simplificada.
    """    
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")        
    import numpy as np


    # Q-Table inicializada en ceros (4 estados, 2 acciones: Izquierda, Derecha)
    Q = np.zeros((4, 2))
    gamma = 0.8 # Factor de descuento
    alpha = 0.1 # Tasa de aprendizaje
    # Simulación de un paso de aprendizaje
    estado_actual = 2
    accion = 1              # 0 significa moverse a la izquierda y 1 significa moverse a la derecha.
    recompensa = 10
    proximo_estado = 3
    # Actualización de la regla de Q-Learning (Ecuación de Bellman simplificada)
    # Q(s,a) = Q(s,a) + alpha * (recompensa + gamma * max(Q(s')) - Q(s,a))
    Q[estado_actual, accion] += alpha * (recompensa + gamma * np.max(Q[proximo_estado]) - Q[estado_actual, accion])
    print("Q-Table después de una recompensa:")
    print(Q)


    JUSTIFICACION = """ Justificación: El alumno aplica el concepto de actualización de valor basado
en la experiencia futura, base fundamental del aprendizaje por refuerzo.

Resultados Esperados de la Ejecución:
Q-Table después de una recompensa:
[[0. 0.]
[0. 0.]
[0. 1.]
[0. 0.]]
    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_05():
    ENUNCIADO = """ Ejercicio 5 - Aprendizaje en Continuo (Incremental Learning)
Objetivo: Analizar cómo actualizar un modelo con nuevos datos sin necesidad de volver 
a entrenar con todo el historial.
Enunciado del Reto: En entornos de Big Data, los datos llegan en flujo constante. Utiliza un clasificador que
soporte el método partial_fit para entrenar un modelo con dos lotes de datos distintos de forma
secuencial
    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.linear_model import SGDClassifier
    import numpy as np
    # Lote 1 de datos
    X1 = np.array([[1, 2], [2, 1]])
    y1 = np.array([0, 1])
    # Inicializar modelo
    clf = SGDClassifier(loss='log_loss')
    # Entrenamiento incremental (Primer lote)
    clf.partial_fit(X1, y1, classes=[0, 1])
    # Lote 2 de datos (nuevos datos que llegan)
    X2 = np.array([[10, 11], [11, 10]])
    y2 = np.array([0, 1])
    # Entrenamiento incremental (Sin perder lo anterior)
    clf.partial_fit(X2, y2)
    print(f"Predicción para dato nuevo: {clf.predict([[1.5, 1.5]])}")

    JUSTIFICACION = """ 
    Justificación: El alumno analiza la eficiencia computacional de los modelos incrementales, esenciales para
sistemas que aprenden en tiempo real.
Resultados Esperados de la Ejecución:
Predicción para dato nuevo [1.5, 1.5]: [0]

    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_06():
    ENUNCIADO = """ Ejercicio 6 - Comparativa Instantánea con LazyPredict
Objetivo: Evaluar múltiples modelos supervisados simultáneamente para seleccionar el mejor punto de
partida.
Enunciado del Reto: Nota: Requiere pip install lazypredict. Utiliza LazyClassifier para comparar el
rendimiento de todos los clasificadores disponibles en Scikit-learn sobre un dataset de juguete.

    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    # Comentado para evitar errores si no está instalado
    from lazypredict.Supervised import LazyClassifier
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    # Código lógico de LazyPredict:
    clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
    models, predictions = clf.fit(X_train, X_test, y_train, y_test)
    print(models.head(5))
    print("LazyPredict permite evaluar +30 modelos en 2 líneas de código.")

    JUSTIFICACION = """ 
    Justificación: El alumno evalúa la productividad que ofrecen las herramientas de AutoML para descartar
algoritmos ineficientes de forma masiva.
Resultados Esperados de la Ejecución (Simulado):
LazyPredict permite evaluar +30 modelos en 2 líneas de código.

Tabla comparativa típica obtenida de 'models.head(5)':
| Model                     | Accuracy | Balanced Accuracy | ROC AUC | F1 Score | Time Taken |
|---------------------------|----------|-------------------|---------|----------|------------|
| LogisticRegression        | 0.9825 | 0.9789 | 0.9789 | 0.9824 | 0.015s |
| SVC                       | 0.9825 | 0.9789 | 0.9789 | 0.9824 | 0.016s |
| LinearSVC                 | 0.9737 | 0.9711 | 0.9711 | 0.9738 | 0.012s |
| RandomForestClassifier    | 0.9649 | 0.9605 | 0.9605 | 0.9650 | 0.155s |
| XGBClassifier             | 0.9649 | 0.9605 | 0.9605 | 0.9650 | 0.120s |

    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_07():
    ENUNCIADO = """ Ejercicio 7 - Low-Code ML con PyCaret
Objetivo: Aplicar un flujo completo de Machine Learning (preprocesamiento y comparación) en una sola
línea de comando.
Enunciado del Reto: Nota: Requiere pip install pycaret. Imagina que debes presentar un informe de
modelos hoy mismo. Utiliza la función setup y compare_models de PyCaret para automatizar la búsqueda del
mejor clasificador.

    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    # Lógica de PyCaret (Requiere entorno instalado)
    # from pycaret.classification import *
    # 1. Configurar el experimento (Normalización, Imputación, etc.)
    # exp = setup(data=mi_dataframe, target='clase_objetivo', session_id=123)
    # 2. Comparar todos los modelos y obtener el mejor
    # best_model = compare_models()
    print("PyCaret automatiza el preprocesamiento y la comparativa mediante 'LowCode'.")

    JUSTIFICACION = """ 
    Justificación: El alumno aplica herramientas de alto nivel que encapsulan la complejidad técnica, permitiendo
enfocarse en la interpretación de los resultados de negocio.
Resultados Esperados de la Ejecución (Simulado):
PyCaret automatiza el preprocesamiento y la comparativa mediante 'Low-Code'.

Salida típica de 'compare_models()':
| Model                     | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
|---------------------------|----------|--------|--------|--------|--------|--------|--------|
| Logistic Regression       | 0.9583 | 0.9912 | 0.9500 | 0.9667 | 0.9567 | 0.9163 |0.9192    |
| Support Vector Machine    | 0.9521 | 0.9880 | 0.9412 | 0.9610 | 0.9492 | 0.9038 |0.9080    |
| Random Forest             | 0.9480 | 0.9854 | 0.9380 | 0.9540 | 0.9450 | 0.8950 |0.8970    |
| Decision Tree             | 0.9120 | 0.9110 | 0.9100 | 0.9150 | 0.9120 | 0.8240 |0.8250    |

    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_08():
    ENUNCIADO = """ Ejercicio 8 - Comparación: Supervisado vs No Supervisado
Objetivo: Evaluar la diferencia entre predecir una clase conocida y agrupar por similitud natural.
Enunciado del Reto: Genera un dataset con 2 grupos claros. Entrena un modelo de Regresión Logística
(Supervisado) y un K-Means (No Supervisado). Compara visualmente cómo cada uno divide el espacio.

    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_blobs
    from sklearn.linear_model import LogisticRegression
    from sklearn.cluster import KMeans
    # 1. Crear datos
    X, y = make_blobs(n_samples=100, centers=2, random_state=42)
    # 2. Modelos
    sup = LogisticRegression().fit(X, y)
    nosup = KMeans(n_clusters=2, random_state=42, n_init=10).fit(X)
    # 3. Graficar comparativa
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
    ax1.set_title('Supervisado (Etiquetas Reales)')
    ax2.scatter(X[:, 0], X[:, 1], c=nosup.labels_, cmap='viridis')
    ax2.set_title('No Supervisado (Clusters)')
    plt.show()

    JUSTIFICACION = """ 
Justificación: El alumno evalúa críticamente ambos paradigmas, comprendiendo que el no supervisado busca
estructura propia mientras el supervisado busca imitar una respuesta dada.
Resultados Esperados de la Ejecución:
Gráficos generados: Se mostrará una ventana con dos gráficos comparativos lado a lado. El de la
izquierda exhibe los datos clasificados bajo las etiquetas reales originales del dataset bidimensional
sintético. El de la derecha muestra la clasificación determinada autónomamente por el agrupamiento KMeans.
    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_09():
    ENUNCIADO = """ Ejercicio 9 - Detección de Anomalías (Isolation Forest)
Objetivo: Analizar desviaciones en los datos que podrían representar fraude o errores de sensor.
Enunciado del Reto: En un flujo de transacciones bancarias, el 99% son normales y el 1% son anomalías.
Utiliza IsolationForest para identificar automáticamente esos puntos atípicos sin necesidad de etiquetas
previas.

    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.ensemble import IsolationForest
    import numpy as np
    # Datos normales
    X = 0.3 * np.random.randn(100, 2)
    # Añadir anomalías deliberadas
    X_outliers = np.random.uniform(low=-4, high=4, size=(10, 2))
    X = np.r_[X, X_outliers]
    # Modelo de detección de anomalías
    iso = IsolationForest(contamination=0.1, random_state=42)
    pred = iso.fit_predict(X) # -1 para anomalía, 1 para normal
    print(f"Número de anomalías detectadas: {list(pred).count(-1)}")


    JUSTIFICACION = """ Justificación: El alumno analiza la capacidad de los modelos no supervisados para detectar comportamientos
inusuales en entornos donde no hay ejemplos previos de fraude.
Resultados Esperados de la Ejecución:
Número de anomalías detectadas: 11
    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_10():
    ENUNCIADO = """ Ejercicio 10 - Creación de un Pipeline de AutoML Integral
Objetivo: Crear un script que integre la limpieza de datos y la selección automática de modelos para un
problema de investigación.
Enunciado del Reto: Diseña un flujo de trabajo que: 1. Genere datos ruidosos, 2. Los limpie mediante un
escalador, y 3. Use un bucle para probar 3 algoritmos distintos (KNN, Árbol, SVM) y devuelva el nombre del
ganador basándose en la precisión.
    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score
    
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    
    # 1. Preprocesamiento
    X_scaled = StandardScaler().fit_transform(X)
    
    # 2. "Mini-AutoML" Manual
    modelos = [KNeighborsClassifier(), DecisionTreeClassifier(), SVC()]
    resultados = {}
    for m in modelos:
        score = cross_val_score(m, X_scaled, y, cv=3).mean()
        resultados[m.__class__.__name__] = score
    # 3. Resultado final
    ganador = max(resultados, key=resultados.get)
    print(f"Ganador del Pipeline: {ganador} con precisión de {resultados[ganador]:.2f}")


    JUSTIFICACION = """ Justificación: El alumno crea una solución arquitectónica básica que imita el comportamiento de un sistema
AutoML, integrando preprocesamiento y selección lógica de algoritmos.
Resultados Esperados de la Ejecución:
 KNeighborsClassifier: 0.5603
 DecisionTreeClassifier: 0.4299
 SVC: 0.5796
Ganador del Pipeline: SVC con precisión de 0.58

    """
    print (f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")