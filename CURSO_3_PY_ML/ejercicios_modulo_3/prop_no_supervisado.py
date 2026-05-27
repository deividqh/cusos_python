
from colorama import Fore, Style
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_01():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    ENUNCIADO = """ Actividad 1 - Segmentación por Edad y Gasto: 
Un restaurante desea agrupar a sus clientes para ofrecer promociones personalizadas. 
Utiliza el algoritmo de K-Means para crear 3 grupos basados en:
"Edad" y el "Gasto promedio por visita" 
(genera datos sintéticos)  """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    # K-Means es un algoritmo de agrupamiento (clustering) que tiene como objetivo particionar un conjunto 
    # de datos en $k$ grupos distintos (clusters). Es "no supervisado" porque los datos originales 
    # no tienen etiquetas previas; el algoritmo descubre los patrones por sí mismo basándose en la similitud
    #  de las características (en este caso, Edad y Gasto).

    # ■ Generación de datos sintéticos (Ingresos Gasto)
    np.random.seed(42)
    X = np.random.rand(200, 2) * 100                    # 200 clientes, 2 características (Edad y Gasto)
    edad: X[:, 0] = np.random.randint(18, 70, size=200)  # Edad entre 18 y 70 años
    gasto: X[:, 1] = np.random.randint(10, 500, size=200)  # Gasto promedio entre $10 y $500

    # ■ Aplica K-Means y "Encuéntrame 3 grupos, 
    # ■ y haz 10 intentos internos para asegurarte de darme la mejor agrupación posible"
    algoritmo = KMeans(n_clusters=3 , random_state=42, n_init=10)
    modelo = algoritmo.fit(X)

    etiquetas = modelo.labels_              # Etiquetas de grupo asignadas a cada cliente, para saber a qué grupo pertenece cada uno.
    centroides = modelo.cluster_centers_ # Extraemos el centro de cada grupo

    plt.figure(figsize=(10, 6))
    # scatter = plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', alpha=0.6, edgecolors='w')
    
    plt.scatter(X[:, 0], X[:, 1], c=etiquetas)
    # se ponen centroides en rojo, con un tamaño grande (s=200)
    plt.scatter(centroides[:, 0], centroides[:, 1], s=200, label='Centroides')

    plt.title('Segmentación de Clientes: Edad vs Gasto Promedio')
    plt.xlabel('Edad')
    plt.ylabel('Gasto Promedio ($)')
    plt.legend()
    plt.show()

    JUSTIFICACION = """  """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_02():
    ENUNCIADO = """ Actividad 2 - Optimización de K en Redes Sociales: 
    • Tienes un conjunto de datos de seguidores de una marca. 
    • Aplica el 'Método del Codo' para determinar si es mejor dividirlos en 2, 4 o 6 comunidades de interés.
     """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    
    from sklearn.datasets import make_blobs # Ideal para generar datos sintéticos agrupados
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    import numpy as np
    
    # 1. Generación de datos sintéticos (Usamos make_blobs para crear 4 grupos naturales ocultos)
    # n_samples=300 (300 clientes), centers=4 (4 grupos reales), cluster_std (dispersión)
    X, _ = make_blobs(n_samples=300, centers=4  , cluster_std=1.5, random_state=42)
    inercia = []
    rango_k = range(1, 10)  # Probamos desde 1 hasta 9 comunidades
    
    # 2. Aplicamos K-Means guardando la Inercia
    print("Analizando el comportamiento de los seguidores...")
    for k in rango_k:
        algoritmo = KMeans(n_clusters=k, random_state=42, n_init=10)
        modelo = algoritmo.fit(X)
        inercia.append(modelo.inertia_)
    
    plt.plot(rango_k, inercia)
    plt.xlabel('k')
    plt.ylabel('Inercia')
    plt.show()
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_03():
    ENUNCIADO = """ Actividad 3 - Etiquetado de Mensajes de Soporte: 
    • Dispones de 500 correos de clientes. 
    • Solo has etiquetado 20 como "Reclamación" o "Consulta". 
    • Usa Label Propagation para predecir la intención de los 480 restantes.
    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    # ■
    from sklearn.semi_supervised import LabelPropagation
    import numpy as np

    # ■ Generación de datos sintéticos (500 mensajes, 2 características)
    np.random.seed(42)
    X = np.random.rand(500, 2) * 100
    # ■ Etiquetado de solo 20 mensajes (0: Reclamación, 1: Consulta)
    y = np.full(500, -1)  # Inicializamos todas las etiquetas como -1 (desconocidas)
    y[:10] = 0  # 10 Reclamaciones
    y[10:20] = 1  # 10 Consultas
    # ■ Aplicamos Label Propagation para 'predecir' las etiquetas de los 480 mensajes restantes
    algoritmo = LabelPropagation()
    modelo = algoritmo.fit(X, y)
    etiquetas_predichas = modelo.transduction_  # Etiquetas predichas para todos los mensajes
    print("Etiquetas predichas para los mensajes no etiquetados:")
    print(etiquetas_predichas[20:30])  # Mostramos las primeras 10 predichas
    # ■
    JUSTIFICACION = """  """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

def ejercicio_04():
    ENUNCIADO = """ Actividad 4 - Laberinto Unidimensional: 
    Crea un agente de Q-Learning que aprenda a moverse en una línea de 5 posiciones. (0, 1, 2, 3, 4)
    El agente empieza en la posición 0 y recibe una recompensa si llega a la posición 4. 
    ¿Cuántas iteraciones necesita para aprender el camino más corto? """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    import numpy as np
    import random
    # 1. Configuración del Entorno y Agente
    np.random.seed(42)
    random.seed(42)
    
    Q = np.zeros((5, 2)) # 5 estados (0 al 4), 2 acciones (0: Izquierda, 1: Derecha)
    
    alpha = 0.1    # Tasa de aprendizaje (qué tanto aprende de cada paso)
    gamma = 0.9    # Factor de descuento (visión a largo plazo)
    epsilon = 0.3  # Tasa de exploración (30% del tiempo se mueve al azar)

    episodios_totales = 100
    historial_pasos = []
    
    print("Iniciando entrenamiento...\n")

    # 2. Bucle de Entrenamiento (Jugando múltiples partidas)
    for episodio in range(1, episodios_totales + 1):
        estado_actual = 0  # En cada nueva partida, el agente vuelve a la casilla de salida
        pasos = 0
        
        while estado_actual != 4: # Mientras no llegue a la meta...
            
            # --- TOMA DE DECISIÓN (Epsilon-Greedy) ---
            # El 30% de las veces elige al azar para explorar. El 70% usa su Q-Table para ganar.
            if random.uniform(0, 1) < epsilon:
                accion = random.randint(0, 1) # Acción aleatoria
            else:
                # np.argmax elige la columna con el número más alto en la fila del estado actual
                accion = np.argmax(Q[estado_actual])                 
            # --- EL ENTORNO RESPONDE ---
            if accion == 0: # Intenta ir a la izquierda
                proximo_estado = max(0, estado_actual - 1) # max(0) evita que atraviese la pared inicial
            else:           # Intenta ir a la derecha
                proximo_estado = min(4, estado_actual + 1)                
            # --- EVALUACIÓN Y RECOMPENSA ---
            if proximo_estado == 4:
                recompensa = 10 # ¡Llegó a la meta!
            else:
                recompensa = 0  # No hay premio por caminar                
            # --- APRENDIZAJE (Ecuación de Bellman) ---
            mejor_futuro = np.max(Q[proximo_estado])
            Q[estado_actual, accion] += alpha * (recompensa + gamma * mejor_futuro - Q[estado_actual, accion])            
            # Avanzamos al siguiente paso
            estado_actual = proximo_estado
            pasos += 1            
        historial_pasos.append(pasos)

    # 3. Análisis de Resultados
    print(f"Entrenamiento finalizado tras {episodios_totales} episodios.")
    print("\nQ-Table Final (Fila=Estado, Columna=Izquierda/Derecha):")
    # Redondeamos para que sea fácil de leer
    print(np.round(Q, 2)) 

    # Buscamos cuándo aprendió a hacerlo en 4 pasos seguidos
    episodio_exito = 0
    for i in range(len(historial_pasos) - 5):
        # Si logra hacer la ruta en exactamente 4 pasos durante 5 partidas seguidas, consideramos que aprendió.
        if all(p == 4 for p in historial_pasos[i:i+5]):
            episodio_exito = i + 1
            break
    
    # ■
    JUSTIFICACION = """ Una vez que ha aprendido sigue fallando el 30% de las veces por el epsilon.  """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_05():
    ENUNCIADO = """ 
    . Actividad 5 - Actualización Semanal de Modelo: Simula un flujo de datos de ventas semanales.
Entrena un modelo inicial con la "Semana 1" y utiliza partial_fit para actualizarlo con los datos de la
"Semana 2" sin perder el aprendizaje previo.
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_06():
    ENUNCIADO = """ 
    Actividad 6 - Torneo de Clasificadores: Utiliza LazyPredict sobre el dataset Iris de Scikit-learn.
Muestra el TOP 3 de algoritmos con mejor F1-Score y reflexiona sobre por qué el ganador es superior
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_07():
    ENUNCIADO = """ 
    Actividad 7 - Auditoría de Calidad con PyCaret: Configura un experimento en PyCaret para un
dataset de "Calidad de Vinos". Utiliza el parámetro de normalización en el setup y compara qué
modelo es el más preciso para detectar vinos de alta calidad.
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_08():
    ENUNCIADO = """ 
    Actividad 8 - El Experimento del Daltónico: Genera un dataset con puntos de colores (coordenadas
RGB). Usa K-Means para agruparlos sin usar las etiquetas de color. ¿Coinciden los grupos encontrados
por el modelo con los colores reales? Evalúa la diferencia entre ambos paradigmas.
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def ejercicio_09():
    ENUNCIADO = """ 
    Actividad 9 - Mantenimiento Predictivo: En una fábrica, los sensores de una máquina suelen dar
valores estables. Usa Isolation Forest para detectar picos extraños que podrían indicar una avería
inminente antes de que ocurra.
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

def ejercicio_10():
    ENUNCIADO = """ 
    Actividad 10 - Mini-AutoML para Regresión: Diseña un script similar al del Ejercicio 10, pero para un
problema de regresión. El script debe probar automáticamente una Regresión Lineal, un Árbol de
Decisión y un SVR, informando cuál tiene el menor MAE.
    """
    print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    import numpy as np
    # ■


    # ■
    JUSTIFICACION = """ 
    
    """
    print(f"\n{Fore.CYAN}{JUSTIFICACION}{Style.RESET_ALL}")