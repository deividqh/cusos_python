from colorama import Fore, Back, Style, init
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from  colorama import Fore, Style
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os           #Para Limpiar la terminal con  os.system('cls') 
# import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)
from XindeX import menuDvd          # Menu con diccionario de datos para mostrar en cada item


def ejercicio_01():
    # https://www.kaggle.com/code/joeportilla/analisis-exploratorio-de-datos-dataset-iris
    # https://rpubs.com/jigbadouin/EDAIRIS01
    TEXTO = """ Ejercicio 1 - Clasificación Básica con SVM (Iris) 🌷🌷🌷🌷
    Objetivo: Aplicar los conceptos fundamentales de Support Vector Machines para una clasificación multiclase.
    Enunciado del Reto: Un equipo de botánicos necesita automatizar la identificación de la especie Iris
    basándose en medidas físicas. Tu tarea es cargar el dataset Iris de Scikit-Learn, dividirlo en entrenamiento y
    prueba, y entrenar un modelo SVM con kernel lineal para predecir la especie de una muestra desconocida. """

    

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    # █████████ 1. 🌷 Cargar el dataset ( Finsher - 1930 )
    iris = datasets.load_iris()   
    X, y = iris.data, iris.target
    print("\n■■■■■■■■■ DATOS INICIALES")
    # print(y)

    # ■■■■■■■■■ 📉 Analisis de los datos ::: EDA
    # ■ Crear el DataFrame con los nombres de las columnas
    df = pd.DataFrame(data = X, columns = iris.feature_names)

    # ■ Añadir la columna de especie (traducida de número a nombre)
    df['species'] = [iris.target_names[i] for i in y]
    print("■ Vista previa del DataFrame Iris:")
    print(df.head())

    # ■ MENU 
    menu={  
        "Grafico pairplot": None, 
        "Grafico displot": None , 
    }
    sns.set_theme(style="ticks")

    while (True):
        i = menuDvd.MenuDiccionario(menu, tituloMenu='Mod3 - Ejercicio 1 -  Graficas EDA', num_char=60)
        if i == 0: break  #PRIMERO LA DE SALIDA
        for index , opt in enumerate(menu):
            if i ==  1:
                # grafico = sns.pairplot(data=df, hue="species", palette="bright" )
                grafico = sns.pairplot(data=df, hue="species" )
                # grafico.fig.suptitle("Dispersión de Especies Iris", y=1.02)
                plt.show()
                break

            elif i == 2:
                sns.displot(df, x="petal width (cm)", hue="species", kind="kde", fill=True)
                plt.show()
                break
            
            pass
    # ■■■■■■■■■ SALIDA MENU
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
    # ■ De aquí tenemos que salir con una idea de que 'Algoritmo' y 'Modelo'  queremos generar. 
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

    # █████████ ✂️ Dividir en entrenamiento (70%) y prueba (30%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    print("•••••••••••• SPLIT train/test/ ✔️")

    # █████████ 🧠 Crear el modelo sobre el algoritmo SVC con Kernel Lineal (byDef 'rbf')
    #   • Elige modelo : [SVC, Gaussian]               .... depende de la naturaleza de los datos 
    #   • Si SVC ... elige kernel : [linear, rbf, poly, sigmoid]  .... depende de la naturaleza de los datos
    modelo_svm = SVC(kernel='linear', probability=True)
    # modelo_svm = SVC(kernel='rbf', probability=True)
    # modelo_svm = SVC(kernel='poly', probability=True)
    # modelo_svm = SVC(kernel='sigmoid', probability=True)
    print("•••••••••••• Modelo Cargado/ ✔️")

    # █████████ 👟 Entrenar el Modelo SVC
    fit = modelo_svm.fit( X=X_train, y=y_train)
    # print(f'PARAMETROS DEL MODELO: {modelo_svm.get_params(deep=True)}')

    # ■ 🎲 Probabilidad (siempre despues de 'fit')
    # Mientras que predict() te dice "esto es una Setosa", predict_proba() te dice "hay un 90% de probabilidad de que sea Setosa y un 10% de Versicolor"
    # Devuelve un array de NumPy con una estructura de [n_samples, n_classes]
    probabilidades = modelo_svm.predict_proba( X = X_test )
    proba_view = probabilidades[:5]
    print(f"\n■■■■■ Probabilidades del Test: "
    f' \n[ % setosa(0), % versicolor(1) , % virginica ] ... hay que elegir el valor mayor(max)\n{proba_view.round(3)}' )

    #  🎯 Precisión/score: El modelo se auto-analiza.
    precision = modelo_svm.score(X=X_test, y=y_test)
    print(f"\n■■■■■ Precisión/ Score del modelo sobre el Test(score) despues de ser entrenado: {precision:.2f}")

    # █████████ 🔮 PREDICCION ... Con los elementos a 'predict', hago una consulta a la bolita magica
    # ■ 🌷 Creo unos elementos (dentro del rango probable) con numpy
    nueva_flor = np.array([[6.0, 5, 2, 1.2], [5.1, 4.5, 2.4, 0.2], [6.1, 3.5, 3.4, 0.2]])
    print(f"\n■■■■■ Muestras: \n{nueva_flor.round(3)}")

    # ■ 🔮 🔮 Predict ... hago una consulta a la bolita magica
    predicciones_nuevas = modelo_svm.predict(X=nueva_flor)
    print("•••••••••••• Prediccion Terminada ✔️")

    # ■ 🎲 PROBABILIDAD Por cada nueva flor o array de flores, hay nuevas probabilidades
    # ■ 🎲 Es un array de array np con la misma dimension que la nueva_flor
    probabilidades_nuevas = modelo_svm.predict_proba(X=nueva_flor)
    print(f'\n∟∟∟∟∟∟∟∟Predict Proba sobre Muestras:\n{probabilidades_nuevas.round(3)}\n')

    l_percent = [ probabilidades_nuevas[i] for i, new_p in enumerate(probabilidades_nuevas) ]
    np_l_percent = np.array(l_percent)*100
    np_l_percent = np_l_percent.round(3)
    new_percent = np.max(np_l_percent, axis=1)
    print(f'Calculo de procentajes con lista compresion: \n{new_percent}')

    # ■■■■■■■■■ 🖥️ Visualización por Consola.
    for i, clase_idx in enumerate(predicciones_nuevas):
        nombre = iris.target_names[clase_idx]
        porcentaje = np.max(probabilidades_nuevas[i]) * 100
        
        print(f"► Flor {i+1}: {Fore.CYAN}{nombre}{Style.RESET_ALL} "
            f"(Confianza: {porcentaje:.2f} %)")

    print(""" Justificación: El alumno demuestra capacidad de aplicación al integrar el flujo básico de Scikit-Learn (Carga,
    Split, Fit, Predict) en un problema de clasificación estándar. 
    La elección de SVM con kernel lineal es adecuada para el dataset Iris, y la evaluación se realiza de forma
    sencilla pero efectiva, mostrando comprensión de la precisión como métrica. La predicción de nuevas muestras añade un toque práctico al ejercicio. 
    """)

def ejercicio_02():
    TEXTO = """ Ejercicio 2 - Probabilidades con Naive Bayes (Iris) 🌷🌷🌷🌷  (ALGORITMO)
    ■ Objetivo: Aplicar modelos probabilísticos para entender la [Pertenencia a Clases].
    ■ Enunciado del Reto: En un estudio genético, se requiere no solo clasificar la especie, 
    sino conocer el nivel de confianza de la predicción. 
    • Implementa el algoritmo Gaussian Naive Bayes sobre el dataset Iris y muestra las
    • probabilidades exactas de que una flor con medidas [6.7, 3.1, 4.4, 1.4] pertenezca a cada una de las
    tres categorías. """

    from sklearn.naive_bayes import GaussianNB
    from sklearn import datasets
    from colorama import Fore, Style

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    
    # Carga de datos
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    # Inicializar y entrenar el clasificador Naive Bayes
    gnb = GaussianNB()
    gnb.fit(X, y)
    # print(f'\t• Parametros GaussianNB:  {gnb.get_params(deep=True)}')

    # Definir la muestra a evaluar
    muestra = [[6.7, 3.1, 4.4, 1.4]]
    # Obtener las probabilidades de pertenencia a cada clase
    probabilidades = gnb.predict_proba(muestra)
    for i, nombre in enumerate(iris.target_names):
        print(f"- {nombre.capitalize()}: {probabilidades[0][i]:.4f}") 

    print ("""\nJustificación: La solución requiere que el alumno utilice predict_proba, demostrando que comprende que
    Naive Bayes se basa en el teorema de Bayes para asignar pesos probabilísticos. 
    El ejercicio va más allá de la clasificación simple, exigiendo una interpretación de los resultados en términos de confianza, lo que es crucial en aplicaciones reales. La presentación clara de las probabilidades por especie muestra una comprensión completa del modelo. 
    """)

def ejercicio_03():
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
    print(f'\t• Parametros :  {clf.get_params(deep=True)}')

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



def ejercicio_04():
    TEXTO = """ Ejercicio 4 - Reducción de Dimensiones con LDA  🌷🌷🌷🌷 (EDA)
    ■ Objetivo: Analizar cómo el Análisis Discriminante Lineal (LDA) ayuda a separar clases visualmente.
    ■ Enunciado del Reto: Visualizar datos en 4 dimensiones (Iris) es complejo. 
        • Utiliza LDA para reducir el dataset a 2 componentes principales que maximicen la separabilidad de las clases.
        • genera un 'gráfico de dispersión' (scatter plot) para observar cómo se agrupan las especies. """

    import matplotlib.pyplot as plt
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn import datasets
    from colorama import Fore, Style

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    
    # Carga de datos
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # ■ Nombres de las categorias (setosa, verdicolor, virginica)
    cat_names = iris.target_names
    for name in cat_names:
        print(name)

    # ■ Reducción a 2 dimensiones usando LDA
    # ■ LDA busca maximizar la distancia entre medias de clases y minimizar la varianza interna
    lda = LinearDiscriminantAnalysis(n_components=2)
    X_lda = lda.fit(X, y).transform(X)

    # Visualización de los resultados
    plt.figure(figsize=(8, 6))
    colors = ['navy', 'turquoise', 'darkorange']

    # Dibuja 3 Graficos. Uno encima de otro
    for i, color, name in zip([0, 1, 2], colors, iris.target_names):
        col_0 = X_lda[y == i, 0]    # de las filas encontradas(y==i, selecciona la columna 0)
        col_1 = X_lda[y == i, 1]    # de las filas encontradas(y==i, selecciona la columna 1)
        plt.scatter( x = X_lda[y == i, 0], y = X_lda[y == i, 1], color=color, alpha=.8, label=name)

    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('LDA: Proyección del dataset Iris en 2D')
    plt.show()

    print(""" Justificación: El alumno analiza la capacidad de LDA para proyectar datos preservando la información de
    clase, diferenciándolo de un simple análisis estadístico. """)

def ejercicio_05():
    TEXTO = """ Ejercicio 5 - Sensibilidad al Escalamiento en SVM  🦀🦀🦀🦀 (EDA)
    ■ Objetivo: Analizar la importancia del PRE-PROCESAMIENTO de datos en algoritmos basados en distancias.
    ■ Enunciado del Reto: Los modelos SVM son extremadamente sensibles a la escala de las variables. Demuestra
    este impacto comparando el rendimiento de un modelo SVM entrenado con los datos de Cáncer de Mama
    "crudos" frente a uno entrenado con los datos normalizados usando StandardScaler. 
    ■ Este conjunto de datos se utiliza para clasificación binaria (predecir si un tumor es maligno o benigno) 
    y contiene información sobre características de núcleos celulares extraídas de imágenes
    """

    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    from colorama import Fore, Style

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    # Datos
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,random_state=1)

    # 1. Modelo sin escalado
    svm_raw = SVC().fit(X_train, y_train)
    score_raw = svm_raw.score(X_test, y_test)

    # 2. Modelo con escalado
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    svm_scaled = SVC().fit(X_train_scaled, y_train)
    print(f'PARAMETROS DEL MODELO: {svm_scaled.get_params(deep=True)}')

    score_scaled = svm_scaled.score(X_test_scaled, y_test)

    # ■ Resultado
    print(f"Rendimiento sin escalado: {score_raw:.4f}")
    print(f"Rendimiento con escalado: {score_scaled:.4f}")

    print(""" Justificación: Analiza la importancia del preprocesamiento, comprendiendo que la arquitectura del algoritmo
    (márgenes) depende de la magnitud de los vectores. """)

def ejercicio_06():
    TEXTO = """ Ejercicio 6 - Selección de Kernel en SVM 🦀🦀🦀🦀 (HIPERPARAMETROS + VALIDACION CRUZADA DE ALGORITMOS)
    ■ Objetivo: Evaluar la eficacia de diferentes fronteras de decisión (lineales vs no lineales).
    ■ Enunciado del Reto: En el dataset de cáncer de mama, las relaciones entre variables pueden no ser lineales.
    Evalúa el rendimiento de un SVM con kernel 'linear' frente a uno 'rbf' utilizando validación cruzada (Cross-
    Validation) para determinar cuál generaliza mejor. """

    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score
    from colorama import Fore, Style

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    cancer = load_breast_cancer()
    # Definimos los modelos a comparar
    modelos = {
    "SVM Lineal": SVC(kernel='linear'),
    "SVM RBF (No lineal)": SVC(kernel='rbf')
    }
    print("Resultados de Validación Cruzada (CV=5):")
    for nombre, modelo in modelos.items():
        puntuaciones = cross_val_score(modelo, cancer.data, cancer.target, cv=5)
        print(f"- {nombre}: {puntuaciones.mean():.4f} (+/- {puntuaciones.std() * 2:.4f})")

    print(""" Justificación: Al evaluar resultados estadísticos, el alumno decide críticamente qué configuración matemática
    es superior para un conjunto de datos específico. """)

def ejercicio_07():
    TEXTO = """  Ejercicio 7 - Análisis de Errores con Matriz de Confusión 🦀🦀🦀🦀
    ■ Objetivo: Evaluar el coste de los errores en un modelo de clasificación.
    ■ Enunciado del Reto: No todos los errores pesan igual. En el diagnóstico de cáncer, un Falso Negativo es
    mucho más grave que un Falso Positivo. Genera una Matriz de Confusión para el clasificador de cáncer de
    mama e identifica cuántos casos malignos fueron erróneamente clasificados como benignos. """

    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    import matplotlib.pyplot as plt
    from colorama import Fore, Style
    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    data = load_breast_cancer()

    # Split de datos
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
    test_size=0.3, random_state=0)

    # Entrenar modelo (usamos kernel lineal por su estabilidad en este dataset)
    clf = SVC(kernel='linear').fit(X_train, y_train)
    print(f'PARAMETROS DEL MODELO: {clf.get_params(deep=True)}')

    y_pred = clf.predict(X_test)

    # Generar la matriz de confusion
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
    disp.plot(cmap='Reds')
    plt.title("Matriz de Confusión: Diagnóstico Oncológico")
    plt.show()

    print(""" Justificación: El alumno evalúa la utilidad real del modelo mediante el análisis detallado de la matriz,
    reconociendo la diferencia entre precisión y seguridad. """)

def ejercicio_08():
    TEXTO = """ Ejercicio 8 - Clasificación Discriminante vs Probabilística 🌷🌷🌷🌷
    ■ Objetivo: Evaluar las diferencias entre LDA y Naive Bayes en condiciones reales.
    ■ Enunciado del Reto: 
    • Entrena un clasificador LDA y uno Naive Bayes sobre el dataset Iris. 
    • Determina cuál de los dos comete menos errores en el conjunto de prueba y
    • reflexiona sobre si la suposición de independencia de variables de Naive Bayes afecta los resultados. """

    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn import datasets
    from colorama import Fore, Style
    from sklearn.metrics import classification_report
    from sklearn.model_selection import train_test_split

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    iris = datasets.load_iris()

    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
    test_size=0.4, random_state=42)
    # ■ Entrenamiento
    lda = LinearDiscriminantAnalysis().fit(X_train, y_train)
    print(f'\nPARAMETROS DEL MODELO Linea (LDA): {lda.get_params(deep=True)}')
    print("•••••••••••• Entrenamiento/fit [ lda ] Cargado OK")

    gnb = GaussianNB().fit(X_train, y_train)
    print(f'\nPARAMETROS DEL MODELO GaussianNB: {gnb.get_params(deep=True)}')
    print("•••••••••••• Entrenamiento/fit [ gnb ] Cargado OK")

    # ■ Reporte de resultados
    print("\n████ Rendimiento LDA ---")
    print(classification_report(y_test, lda.predict(X_test), target_names=iris.target_names))

    print("\n████ Rendimiento Naive Bayes ---")
    print(classification_report(y_test, gnb.predict(X_test), target_names=iris.target_names))

    print(""" Justificación: El alumno evalúa supuestos teóricos comparando métricas de precisión: 
    recall y F1-score para dos paradigmas distintos de clasificación. """)
def ejercicio_09():
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

def ejercicio_10():
    TEXTO = """ Ejercicio 10 - Pipeline Integral de Machine Learning    🌷🌷🌷🌷
    ■ Objetivo: Crear una solución de extremo a extremo (End-to-End) robusta y profesional.
    ■ Enunciado del Reto: Como consultor experto, debes crear un "Pipeline" 
    que automatice todo el flujo de trabajo para nuevos datos de investigación floral: 
    1. Escale los datos, 
    2. Reduzca la dimensionalidad con LDA a 1 componente ,
    3. Clasifique mediante SVM. Este pipeline debe ser capaz de entrenarse y predecir de forma atómica. """

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.svm import SVC
    from sklearn import datasets
    from colorama import Fore, Style

    print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

    # ■■■■■■■■■■■ Cargar datos
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # ■■■■■■■■■■■ Construcción del Pipeline Profesional
    # ■■■■■■■■■■■ El Pipeline asegura que el escalado y la reducción se apliquen consistentemente
    pipeline_floral = Pipeline([
        ('escalador', StandardScaler()),
        ('reductor_lda', LinearDiscriminantAnalysis(n_components=2)),
        ('clasificador_svm', SVC(kernel='poly', degree=3, C=1.0))
    ])

    # ■■■■■■■■■■■ Entrenamiento completo del flujo
    pipeline_floral.fit(X, y)
    print(f'PARAMETROS DEL MODELO: {pipeline_floral.get_params(deep=True)}')

    # ■■■■■■■■■■■ Simulación de llegada de nuevos datos
    nuevos_datos = [[5.0, 3.6, 1.4, 0.2], [6.5, 3.0, 5.2, 2.0]]
    predicciones = pipeline_floral.predict(nuevos_datos)
    print("Predicciones del Pipeline para nuevas muestras:")

    for i, pred in enumerate(predicciones):
        print(f" Muestra {i+1}: {iris.target_names[pred].upper()}")

    print(""" Justificación: Demuestra la capacidad de creación al ensamblar múltiples componentes técnicos en una
    solución arquitectónica coherente, escalable y reproducible. """)


def mis_pruebas():
    # from modulos.info_data import ver_data____ as vd
    import modulos.eda as eda
    from sklearn.datasets import load_breast_cancer
    from sklearn.datasets import load_iris
    
    pass
    # cancer = load_breast_cancer()
    # print('■'*30)
    # I.ver_data(cancer)
    # print('■'*30)
    # I.ver_data__(cancer)
    # print('■'*30)
    # I.ver_data____(cancer)
    # print('■'*30)
    # I.descripcion_dataset(cancer)
    
    pass
    iris = load_iris()
    print('■'*30)
    eda.ver_data(iris)
    print('■'*30)
    eda.ver_data__(iris)
    print('■'*30)
    eda.ver_data____(iris)    
    print('■'*30)
    eda.descripcion_dataset(iris)

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ej_01. 🌷🌷 SVC ■ Ciclo Basico con algoritmo SVM(Categoriás) ■ GRAF: pairplot | displot:": ejercicio_01, 
        "Ej_02. 🌷🌷 Algoritmo Naive Bayes ■ Probabilidad": ejercicio_02 , 
        "Ej_03. 🦀🦀 SVC ■ Porcentaje de Aciertos ": ejercicio_03,
        "Ej_04. 🌷🌷 EDA ■ Análisis Discriminante Lineal( LDA ) ■ GRAF: scatter": ejercicio_04,
        "Ej_05. 🦀🦀 EDA ■ Escalado de los Datos ": ejercicio_05,
        "Ej_06. 🦀🦀 SVC ■ Hiper-Parametros ■ Validación Cruzada": ejercicio_06,
        "Ej_07. 🦀🦀 SVC ■ METRICAS ■ GRAF: Matriz de Confusión": ejercicio_07,
        "Ej_08. 🌷🌷 Compara  LDA && Naive Bayes ■ METRICAS": ejercicio_08,
        "Ej_09. 🦀🦀 SVC ■ Hiperparámetros C y gamma ■ GridSearchCV (MultiParametros)": ejercicio_09,
        "Ej_10. 🌷🌷 PipeLine (all in one)": ejercicio_10,
        "Ej_11. PRUEBAS": mis_pruebas,
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
    print("Ejercicios de Clase Modulo 3 Parte 1")
    main()
