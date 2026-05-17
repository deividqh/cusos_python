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

def generar_dataset_2(muestras=100, random_state=42):
    # ■ Generamos la semilla... seed la pone global, defalult_rng es local y mejor.
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
    correo = generar_dataset_2(150, 123)
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
    
    lista_k = []    # para k(nuemro de vecinos)
    lista_p = []    # para_las precisiones
    # compilado = {'k':i, 'p':precision}
    for i in range(1, 21):
        algoritmo = KNN(n_neighbors=i)
        modelo = algoritmo.fit(X = X_train,  y = y_train)
        precision = modelo.score(X = X_test, y = y_test)        
        print(f'Precision modelo KNN entrenado  con k = {i} vecinos = {precision:.2f}')
        pass
        # Cacho los valores para la grafica
        lista_k.append(i)
        lista_p.append(precision)
    pass
    # 2. Graficamos los resultados
    plt.plot(lista_k, lista_p, marker='o' )
    plt.xlabel('Valor de K (n_neighbors)')
    plt.ylabel('Precisión (Score)')
    plt.xticks(range(1, 21))
    plt.show()

    print(f"{Fore.YELLOW}NO ENTIENDO POR QUÉ SALE ESTE RESULTADO{Style.RESET_ALL}")
    

def ejercicio_05():
    ENUNCIADO = """ Actividad 5 - Poda de Árboles (Pruning): 
    • Entrena un Árbol de Decisión sobre un dataset complejo y observa su profundidad. 
    • Luego, aplica restricciones de min_samples_leaf y max_depth para simplificarlo y 
    • explica cómo esto ayuda a la generalización. 
    max_depth: Limita la longitud del camino más largo desde la raíz a una hoja. Un árbol demasiado profundo captura relaciones espurias (ruido).
    min_samples_leaf: Establece el número mínimo de muestras que deben quedar en un nodo terminal. Si un nodo tiene muy pocas muestras, la decisión tomada en él no es estadísticamente representativa.
    """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    
    # Datos
    (X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names) = get_d_datos('cancer', 30, True)    
    print("\n■■■■■■■■■ ")

    # FASE 1: El Árbol de Decisión.
    # Sin restricciones, el árbol crecerá hasta que todas las hojas sean puras
    arbol_de_decision = DecisionTreeClassifier(random_state=42)

    arbol_de_decision.fit(X_train, y_train)

    profundidad_arbol = arbol_de_decision.get_depth()
    precision_arbol_train = arbol_de_decision.score(X_train, y_train)
    precision_arbol_test  = arbol_de_decision.score(X_test, y_test)

    print(f"Árbol Complejo - Profundidad: {profundidad_arbol}")
    print(f"Precisión Entrenamiento: {precision_arbol_train:.4f} | Test: {precision_arbol_test:.4f}")

    # --- FASE 2: Aplicación de Poda (Pruning) ---
    # Restringimos el crecimiento para mejorar la generalización
    arbol_poda = DecisionTreeClassifier(
        max_depth=3, 
        min_samples_leaf=5, 
        random_state=42
    )
    # Entrenamiento del arbol podado
    arbol_poda.fit(X_train, y_train)

    profundidad_poda = arbol_poda.get_depth()
    precision_poda_train = arbol_poda.score( X_train , y_train )
    precision_poda_test  = arbol_poda.score( X_test , y_test )

    print(f"\nÁrbol Podado - Profundidad: {profundidad_poda}")
    print(f"Precisión Entrenamiento: {precision_poda_train:.4f} | Test: {precision_poda_test:.4f}")



import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def _get_decission_tree(seed, X_train, X_test, y_train, y_test):
    # Árbol sin límite de profundidad para ver su varianza real
    algoritmo = DecisionTreeClassifier(random_state=seed)
    algoritmo.fit(X_train, y_train)
    return algoritmo.score(X_test, y_test)

def _get_random_forest(n_estimators, seed, X_train, X_test, y_train, y_test):
    algoritmo = RandomForestClassifier(n_estimators=n_estimators, random_state=seed)
    algoritmo.fit(X_train, y_train)
    return algoritmo.score(X_test, y_test)

def ejercicio_06():
    # Datos
    (X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names) = get_d_datos('cancer', 30, True)    
    print("\n■■■■■■■■■ ")
    
    seeds = [10, 12, 234, 355, 467, 589, 56, 73, 28, 29]
    resultados_dt = []
    resultados_rf = []

    print(f"{'Seed':<10} | {'Acc. Árbol':<15} | {'Acc. Forest':<15}")
    print("-" * 45)

    for s in seeds:
        precision_dt = _get_decission_tree(s, X_train, X_test, y_train, y_test)
        precision_rf = _get_random_forest(500, s, X_train, X_test, y_train, y_test)
        
        resultados_dt.append(precision_dt)
        resultados_rf.append(precision_rf)
        
        print(f"{s:<10} | {precision_dt:<15.4f} | {precision_rf:<15.4f}")

    # ■■■■■■■■■ ■ ■  ANÁLISIS DE VARIANZA 
    var_dt = np.var(resultados_dt)
    var_rf = np.var(resultados_rf)

    print("\n" + "="*45)
    print(f"{'Modelo':<20} | {'Varianza (Estabilidad)':<20}")
    print("-" * 45)
    print(f"{'Decision Tree':<20} | {var_dt:<20.6f}")
    print(f"{'Random Forest (500)':<20} | {var_rf:<20.6f}")
    print("="*45)

    if var_rf < var_dt:
        print("\nCONCLUSIÓN: El Random Forest es más ESTABLE (menor varianza).")
    else:
        print("\nCONCLUSIÓN: El Árbol de Decisión es más ESTABLE (poco probable).")

    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ PLUS TEORIA
    # Definición de anchos de columna
    m, p, d, f = 16, 18, 15, 60
    # Encabezado
    print()
    print('■'*60)
    print(f"+{'-'*(m+2)}+{'-'*(p+2)}+{'-'*(d+2)}+{'-'*(f+2)}+")
    print(f"| {'Modelo':<{m}} | {'Parámetro':<{p}} | {'Defecto':<{d}} | {'Función Principal':<{f}} |")
    print(f"+{'='*(m+2)}+{'='*(p+2)}+{'='*(d+2)}+{'='*(f+2)}+")
    print(f"| {'DT / RF':<{m}} | {'max_depth':<{p}} | {'None':<{d}} | {'Limita los niveles de profundidad para evitar sobreajuste.':<{f}} |")
    print(f"| {'DT / RF':<{m}} | {'min_samples_split':<{p}} | {'2':<{d}} | {'Mínimo de datos requeridos en un nodo para dividirlo.':<{f}} |")
    print(f"| {'DT / RF':<{m}} | {'min_samples_leaf':<{p}} | {'1':<{d}} | {'Mínimo de datos que deben quedar en una hoja terminal.':<{f}} |")
    print(f"| {'DT / RF':<{m}} | {'criterion':<{p}} | {'gini/sq_error':<{d}} | {'Métrica para medir la calidad de cada división.':<{f}} |")
    print(f"| {'DT / RF':<{m}} | {'max_features':<{p}} | {'None / sqrt':<{d}} | {'Variables evaluadas para elegir la mejor división.':<{f}} |")
    print(f"| {'Random Forest':<{m}} | {'n_estimators':<{p}} | {'100':<{d}} | {'Número total de árboles que se van a crear en el bosque.':<{f}} |")
    print(f"| {'Random Forest':<{m}} | {'bootstrap':<{p}} | {'True':<{d}} | {'Activa el muestreo aleatorio con reemplazo por árbol.':<{f}} |")
    # Cierre
    print(f"+{'-'*(m+2)}+{'-'*(p+2)}+{'-'*(d+2)}+{'-'*(f+2)}+")
    print("\n* DT: DecisionTreeClassifier | RF: RandomForestClassifier")


def generar_dataset_3(muestras=100, random_state=42):
    rng = np.random.default_rng(random_state)    
    
    target = rng.integers(0, 3, size = muestras)

    data = np.zeros((muestras, 3))    
    for i in range(muestras):
        if target[i] ==  2:             # FRECUENCIA ALTA ( ALERTA )
            data[i] = rng.integers(7, 12, size=3)  
        elif target[i] == 1:            # FRECUENCIA MEDIA ( MEDIO )
            data[i] = rng.integers(4, 7, size=3)   
        else:                           # FRECUENCIA BAJA ( LEGITIMO )
            data[i] = rng.integers(0, 4, size=3)
    return {
        'data': data,
        'target': target,
        'target_names': np.array(['Legitimo', 'Medio', 'Alerta']),
        'feature_names': ['oferta', 'gratis', 'urgente'],
        'size': muestras
    }
def ejercicio_07():
    ENUNCIADO = """ Actividad 7 - Visualización Comparativa (LDA vs PCA): 
    • Toma un dataset con 3 clases y aplica LDA y PCA para reducirlo a 2D. 
    • Genera ambos gráficos uno al lado del otro y 
    • explica por qué LDA suele mostrar grupos de clases mucho más definidos. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.decomposition import PCA

    dataset = generar_dataset_3(muestras=100, random_state=88)
    X = dataset['data']
    y = dataset['target']
    # ■ Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ Reducción a 2 dimensiones usando LDA
    # ■ LDA busca maximizar la distancia entre medias de clases y minimizar la varianza interna
    algoritmo_lda = LinearDiscriminantAnalysis( n_components = 2 )
    X_lda = algoritmo_lda.fit(X, y).transform(X)
    
    df_lda = pd.DataFrame(X_lda, columns=dataset['feature_names'])
    print("\nPrimeras muestras en el nuevo espacio 2D:")
    print(df_lda.head())

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ Aplicar PCA para reducir a 2 componentes
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    df_pca = pd.DataFrame(X_pca, columns=dataset['feature_names'])
    print("\nPrimeras muestras en el nuevo espacio 2D:")
    print(df_pca.head())

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    fig, (ax_lda, ax_pca) = plt.subplots(1, 2, figsize=(12, 5))
    ax_lda.scatter(X_lda[:, 0], X_lda[:, 1], c = y, edgecolors='k')
    ax_lda.set_title(f'LDA ')

    ax_pca.scatter(X_pca[:, 0], X_pca[:, 1], c = y, edgecolors='k')
    ax_pca.set_title(f'PCA ')

    plt.show()

    print(f"{Fore.YELLOW}HE TENIDO QUE PREGUNTAR A LA IA QUE TIPO DE GRAFICO TENGO QUE SACAR{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}NO PUEDO DAR EXPLICACIONES, SOLO SACO DATOS{Style.RESET_ALL}")
    
def ejercicio_08():
    ENUNCIADO = """ Actividad 8 - Arquitectura de Neuronas: 
    • Diseña una Red Neuronal (MLP) para un problema de clasificación multiclase. 
    • Experimenta variando el número de capas ocultas 
    (ej. una capa de 50 neuronas vs. tres capas de 10 neuronas) y reporta cuál converge más rápido. """

    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    print (f"\n{Fore.CYAN}{TEORIA}{Style.RESET_ALL}")

    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn import datasets
    
    # Carga y escalado (importante para Redes Neuronales)
    iris = datasets.load_iris()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(iris.data)
        
    # ■■■■■■■■■■ Creación de la Red Neuronal
    # Una capa de 50 vs Tres capas de 10
    configuraciones = {
        "Capa única (50 neuronas)": (50,),
        "Tres capas (10 neuronas cada una)": (10, 10, 10)
    }
    print(f"{'Arquitectura':<35} | {'Precisión':<10} | {'Iteraciones':<12}")
    print("■" * 65)
    for nombre, capas in configuraciones.items():
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        mlp = MLPClassifier(hidden_layer_sizes=capas, max_iter=2000, random_state=1)        
        mlp.fit(X_scaled, iris.target)        
        precision = mlp.score(X_scaled, iris.target)
        iteraciones = mlp.n_iter_ # Aquí obtenemos cuándo convergió        
        print(f"{nombre:<35} | {precision:<10.4f} | {iteraciones:<12}")

def ejercicio_09():
    ENUNCIADO = """ Actividad 9 - Análisis de Falsos Alarmas: 
    • En un sistema de detección de intrusos (0: Seguro, 1: Intruso), un Falso Positivo (alarma falsa) genera un coste operativo alto. 
    • Utiliza la Matriz de Confusión para ajustar el umbral de decisión de un modelo y minimizar estas falsas alarmas. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    from sklearn import datasets

    from sklearn.model_selection import cross_val_score

    # Datos
    (X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names) = get_d_datos('cancer', 30, True)    
    print("\n■■■■■■■■■ ")

    # ■■■■■■■■■■■■■■■■■ Random Forest
    algoritmo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo_rf = algoritmo_rf.fit(X_train, y_train)
    
    # ■ ■ ■ En lugar de usar 'predict', uso 'predict_proba' para manipular el umbral( el mayor % )
    # ■ ■ ■ En cancer, la columna 1 es Maligno
    probabilidades = algoritmo_rf.predict_proba(X_test)[:, 1]
    UMBRAL = 0.75 
    prediccion_rf = [1 if p >= UMBRAL else 0 for p in probabilidades]

    # ■■■■■■■■■■■■■■■■ Generar la matriz de confusion
    matrix = confusion_matrix(y_test, prediccion_rf)
    matrix_UI = ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = target_names)
    # ■ ■ ■     
    matrix_UI.plot(cmap='Reds')
    plt.title("Matriz de Confusión: Diagnóstico Oncológico")
    plt.show()

    # ■■■■■■■■■■■■■■■■ intento sacar todas las matrices para diferentes umbrales.
    UMBRALES = [0.70 , 0.75, 0.77, 0.8 ]
    fig, ax_s = plt.subplots(1, len(UMBRALES), figsize=(12, 5))
    for i, u in enumerate(UMBRALES):
        prediccion_rf = [1 if p >= u else 0 for p in probabilidades]
        matrix = confusion_matrix(y_test, prediccion_rf)        
        matrix_UI = ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = target_names)

        matrix_UI.plot(cmap='Reds', ax=ax_s[i])
        ax_s[i].set_title(f"Umbral {u}")
    plt.show()

def ejercicio_10():
    ENUNCIADO = """  Actividad 10 - Proyecto Integrador: Scoring Bancario: 
    • Desarrolla un Pipeline profesional para predecir si se debe aprobar un préstamo. 
      El flujo debe: 1. Escalar los datos, 
                     2. Aplicar PCA para eliminar redundancia, 
                     3. Entrenar un Random Forest 
                     4. Mostrar un informe de métricas completo (Precision, Recall y F1-Score).  """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")
    
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.ensemble import RandomForestClassifier

    # ■■■■■■■■■■■ DATOS
    (X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names) = get_d_datos('cancer', 30, True)        
    # ■■■■■■■■■■■ PIPELINE: ESCALADO / PCA / ALGORITMO
    PIPELIN = Pipeline([
        ('escalador', StandardScaler()),
        ('PCA', PCA(n_components=2)),
        ('RandomF', RandomForestClassifier(n_estimators=100, random_state=42)),
    ])
    # ■■■■■■■■■■■ Entrenamiento
    modelo = PIPELIN.fit(X_train, y_train)
    # ■■■■■■■■■■■ METRICAS
    import modulos.metricas as MT    
    # ■■
    exactitud = MT.get_accuracy_score(PIPELIN, X_test, y_test)    
    # ■■
    MT.get_reporte_completo(PIPELIN, X_test, y_test, target_names)    
    # ■■
    disp = MT.get_matriz_confusion(PIPELIN, X_test, y_test, target_names)
    disp.plot(cmap='Reds') # Un color diferente para variar
    plt.show()

    


def parametros_teoria():
    RANDOMFOREST = """
    INFORMACIÓN DE PARÁMETROS: RandomForestClassifier (Bosque Aleatorio)
    • n_estimators: (Por defecto: 100) ► Define el número total de árboles de decisión individuales que se construirán en el bosque.
    • criterion: (Por defecto: 'gini') ► Función métrica utilizada para medir la calidad de la división de los nodos ('gini' o 'entropy').
    • max_depth: (Por defecto: None) ► Profundidad máxima que pueden alcanzar los árboles. Si es None, se expanden hasta que las hojas sean puras.
    • min_samples_split: (Por defecto: 2) ► Número mínimo de muestras requeridas que debe tener un nodo antes de poder dividirse en subnodos.
    • min_samples_leaf: (Por defecto: 1) ► Número mínimo de muestras que obligatoriamente deben quedar en un nodo hoja (terminal).
    • max_features: (Por defecto: 'sqrt') ► Cantidad de características (features) que se seleccionan al azar para buscar la mejor división en cada nodo.
    • class_weight: (Por defecto: None) ► Pesos asignados a las clases (ej. 'balanced'), sumamente útil para compensar datasets desbalanceados.
    • random_state: (Por defecto: None) ► Semilla numérica que garantiza que el proceso de aleatorización y el experimento sean exactamente reproducibles.
    """
    MLP = """
    INFORMACIÓN DE PARÁMETROS: MLPClassifier (Red Neuronal Multicapa)
    • hidden_layer_sizes: [ Por defecto: (100,) ] ► 1 capa 100 neuronas. IF ( 10, 14 ) ► 2 capas, una de 10 neuronas y otra de 14.
    • activation: (Por defecto: 'relu') ► Función de activación que añade no-linealidad al aprendizaje del modelo.
    • solver: (Por defecto: 'adam') ► Algoritmo de optimización encargado de ajustar los pesos de las conexiones.
    • alpha: (Por defecto: 0.0001) ► Fuerza de la regularización L2 utilizada para evitar el sobreajuste (overfitting).
    • learning_rate_init: (Por defecto: 0.001) ► Tamaño del paso inicial al actualizar los pesos durante el entrenamiento.
    • max_iter: (Por defecto: 200) ► Límite de épocas o vueltas máximas permitidas para el proceso de entrenamiento.
    • random_state: (Por defecto: None) ► Semilla numérica que garantiza que el experimento sea exactamente reproducible.
    """
    import pyfiglet
    rf = pyfiglet.figlet_format("Random ForestClassifier", font="small", width=120) 
    print(f'{rf}')
    print (f"{Fore.CYAN}{RANDOMFOREST}{Style.RESET_ALL}")
    
    mlp = pyfiglet.figlet_format("Redes Neuronales MLP", font="small" , width=120) 
    print(f'{mlp}')
    print (f"{Fore.BLUE}{MLP}{Style.RESET_ALL}")
    

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL  ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ejercicio_01. (circles) El Misterio de los Kernels": ejercicio_01, 
        "Ejercicio_02. (custom)  Clasificador de Spam (Naive Bayes)": ejercicio_02 , 
        "Ejercicio_03. (digits)  Reducción de Ruido con PCA": ejercicio_03,
        "Ejercicio_04. 🌷🌷🌷🌷 Búsqueda del Vecino Óptimo": ejercicio_04,
        "Ejercicio_05. 🦀🦀     Poda de Árboles (Pruning)": ejercicio_05,
        "Ejercicio_06. 🦀🦀     Estabilidad del Bosque": ejercicio_06,
        "Ejercicio_07. (custom) Visualización Comparativa (LDA vs PCA)": ejercicio_07,
        "Ejercicio_08. Arquitectura de Neuronas 🧠 🧠 ": ejercicio_08,
        "Ejercicio_09. (custom) Análisis de Falsos Alarmas ": ejercicio_09,
        "Ejercicio_10. Proyecto Integrador: Scoring Bancario": ejercicio_10,
        "TEORIA. parametros de randomForest y MLP(Redes Neuronales)": parametros_teoria,
    }
    while (True):
        i = menuDvd.MenuDiccionario(menu, tituloMenu='Ejercicios de Analisis de Datos - Modulo 2', num_char=60)
        
        if i == 0: break  #PRIMERO LA DE SALIDA
        
        for index ,ejer in enumerate(menu):
            if i == index + 1:
                menu[ejer]() 
                # print ("_"*30)

    # ■■■■■■■■■ SALIDA 
    import pyfiglet
    texto_small = pyfiglet.figlet_format("That's Folks", font="small") 
    print ('\n\t\t🐰')
    print(texto_small)
    


# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    print("Ejercicios de  Modulo 3 - Algoritmos - Metricas Parte 2")
    main()
    