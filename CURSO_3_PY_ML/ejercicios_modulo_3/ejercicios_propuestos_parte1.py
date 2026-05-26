from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from  colorama import Fore, Style
import os           # Para Limpiar la terminal con  os.system('cls') 
# import  menuDvd     # Funcion que crea un menu y devuelve un int(opcion)
from XindeX import menuDvd          # Menu con diccionario de datos para mostrar en cada item

from sklearn import datasets
# from modulos.datos import get_d_datos

from ejercicios_modulo_3.modulos.datos import get_d_datos

# def get_d_datos(dataset_name='iris', test_porciento=None, b_split=False):
#     """ Cacho los datos del dataset que vayamos a usar y devuelvo un diccionario con todos los datos 
#     y el split hecho.
#     test_porciento puede ser entre 0 y 1 para el test y asume pocentaje o 30% por ejemplo.
#     si test_porciento = None, devuelve el dataset.
#     """
#     # ■■■■■■■■■ Cargo el dataset
#     dataset_name = dataset_name.strip().lower()    
#     if dataset_name == 'iris':
#         data_load = datasets.load_iris()   
#     elif dataset_name == 'cancer':
#         data_load = datasets.load_breast_cancer()
#     else:
#         return None
#     # ■■■■■■■■■ Si no me das la proporción de test, te doy el dataset.
#     if test_porciento == None and dataset_name:
#         return data_load
    
#     # ■■■■■■■■■ Me vale lo que quieras: 0.7 o 70%
#     if test_porciento > 0 and test_porciento <= 1:
#         pass
#     else:
#         test_porciento = test_porciento / 100   
#     pass

#     X = data_load.data
#     y = data_load.target

#     # ■■■■■■■■■ 
#     x_train, x_test, y_train, y_test = train_test_split(data_load.data, data_load.target, test_size = test_porciento, random_state = 42)
    
#     # Creo un pandas con los nombres de las columnas
#     df = pd.DataFrame(data = X, columns = data_load.feature_names)
#     # Y le añado una columna mas con los resultados (0, 1, 2), así preparo el pandas para lo que venga.
#     df['resultado'] = data_load.target
    
#     # ■ Cargo el diccionario de retorno
#     datos_retorno = {
#         'X': X, 
#         'y': y, 
#         'X_train': x_train, 
#         'y_train': y_train, 
#         'X_test': x_test, 
#         'y_test': y_test,
#         'df': df, 
#         'target_names': data_load.target_names,
#         'feature_names': data_load.feature_names,
#     }
#     # ■  imprimo el head del dataset para echar un primer vistazo a los datos en el ejercicio
#     print(f"\n■■■■■■■■■ DATOS INICIALES\n{df.head()}")
#     # ■ Retorno
#     if b_split == False:
#         return datos_retorno
#     else:
#         return X, y, x_train, x_test, y_train, y_test, df, target_names, feature_names
    

def ejercicio_01():
    ENUNCIADO = """ 1. Exploración de Kernels en SVM: Utilizando el código del Ejercicio 1, 
    modifica el kernel de 'linear' a 'poly' (grado 3) y 'rbf'. 
        • Genera un informe breve comparando la precisión obtenida en cada caso y 
        • explica por qué crees que un kernel funciona mejor que otro para el dataset Iris basándote en la distribución de los datos. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    
    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    kernel_s = ['linear', 'poly', 'rbf']
    for kernel in kernel_s:
        modelo = SVC(kernel = kernel, probability = True)        
        fit = modelo.fit(X=dd['X_train'] , y=dd['y_train'])
        # print(f'• Log de Parametos del Modelo: {modelo.get_params(deep=True)}')
        
        # Score/Precisión devuelve un float
        new_score   = modelo.score(X=dd['X_test'], y = dd['y_test'])                

        # Probabilidad/predict_proba devuelve un array de  lista de n floats(columnas), 
        # donde n es el número de categorias(setosa/verdinosequé/virginica)
        # y las filas coinciden con len(y_test) ...
        new_proba_s = modelo.predict_proba( X = dd['X_test'] )        
        print (f'■■ Kernel {kernel}: Precisión del entrenamiento: {new_score:.2f} ' )

    
    print('En cuanto al kernel no podemos sacar ningún dato concluyente con respecto a la precisión')
    sns.pairplot(data=dd['df'], hue='resultado')
    plt.show()
    print(f'{Fore.YELLOW}En cuanto a la distribución de los datos se puede ver en el grafico que setosa(0) está bien diferenciada de las otras dos que mantienen un conjunto bien claro pero comparten un subconjunto de medidas confusas{Style.RESET_ALL}')

def ejercicio_02():
    ENUNCIADO = """ 2. Análisis Probabilístico Comparativo: 
    Retoma el Ejercicio 2. 
    ■ Ejercicio 2: En un estudio genético, se requiere no solo clasificar la especie, sino conocer el nivel de confianza de la predicción. 
        Implementa el algoritmo Gaussian Naive Bayes sobre el dataset Iris y muestra las
        probabilidades exactas de que una flor con medidas [6.7, 3.1, 4.4, 1.4] pertenezca a cada una de las tres categorías. 

    • Selecciona tres muestras del conjunto de prueba que el modelo clasifique correctamente 
      pero con una probabilidad de certeza inferior al 70%.

    • Investiga qué medidas físicas (longitud/anchura) hacen que esas muestras sean "ambiguas" 
      para el modelo Gaussian Naive Bayes. """

    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    
    from sklearn.naive_bayes import GaussianNB
    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    algoritmo = GaussianNB()
    modelo = algoritmo.fit(X = dd['X_train'], y = dd['y_train'])
    
    probabilidade_s = modelo.predict_proba( X = dd['X_test'] )
    
    prediccione_s = modelo.predict( X = dd['X_test'] )

    menos_70 = [ i for i, prob in enumerate(probabilidade_s) 
                    if prediccione_s[i] == dd['y_test'][i] and max(prob) < 0.7 ]

    # print(menos_70)    

    indices = menos_70[:3] if len(menos_70) >=3 else menos_70[:]
    tres_muestras = dd['X_test'][indices]
    print(f'■ las 3 Muestras: \n{tres_muestras}')

    proba_muestras = modelo.predict_proba(X=tres_muestras)
    print(f'Probabilidad de las muestras\n{proba_muestras.round(4)*100}')

    print(f'{Fore.YELLOW}Me cuesta la Interpretación de los gráficos aun, mas allá de sacar datos, para interpretarlos hay que saber abordarlos, estudiarlos{Style.RESET_ALL}')

def ejercicio_03():
    ENUNCIADO = """ 3. Simulación de Desbalanceo de Clases: En el dataset de Cáncer de Mama (Ejercicio 3), 
    modifica el conjunto de datos para eliminar el 80% de las muestras de la clase 'malignant'. 
    Entrena el modelo SVM y calcula la matriz de confusión. 
    Explica por qué la métrica Accuracy puede ser engañosa en este nuevo escenario. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

    cancer = get_d_datos('cancer')    
    if not cancer: return
    print("\n■■■■■■■■■ ")
    # ■ Modifica el conjunto de datos para eliminar el 80% de las muestras de la clase 'malignant (0)
    # Esto significa que de la y_test tengo que identificar cuales son malignant (= 0)
    # y de todos los malignant elimnar el 80% y montar el train y test a partir de ahí....mola
    df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
    df['resultado'] = cancer.target
        
    # Filtro
    df_malignos = df[df['resultado'] == 0] # Malignant es 0
    df_benignos = df[df['resultado'] == 1] # Benign es 1

    df_reducidos = df_malignos.sample(frac=0.2, random_state=42)
    df_resultados = pd.concat([df_benignos, df_reducidos])
    
    # Se quita la columna 'resultado' porque no se puede pasar el resultado a train_test_split
    X = df_resultados.drop('resultado', axis=1)
    y = df_resultados['resultado']
    X_train, X_test, y_train, y_test = train_test_split(X,  y, test_size = 0.3, random_state = 88)

    # ■ Entrena el modelo SVM y calcula la matriz de confusión. 
    algoritmo = SVC()
    modelo = algoritmo.fit(X = X_train , y = y_train)
    prediccione_s = modelo.predict(X = X_test)

    matriz_c = confusion_matrix( y_true = y_test, y_pred = prediccione_s )
    disp = ConfusionMatrixDisplay(confusion_matrix = matriz_c, display_labels = cancer.target_names)
    disp.plot(cmap='Reds')
    plt.title("Matriz de Confusión: Diagnóstico Oncológico")
    plt.show()

    print(f'{Fore.YELLOW}Me cuesta la Interpretación de los gráficos aun, mas allá de sacar datos, para interpretarlos hay que saber abordarlos, estudiarlos{Style.RESET_ALL}')
    print(f"""• Puedo decir que TP/FP/TN/FN:  
     T y P =  +
     F y N =  - 
     • Si los multiplico, habla de la 'Realidad' por ejemplo: TP(+*+) = Realidad Benigno  , FP(-*+) = Realidad Maligno
     • La 'Prediccion' es la P y la N, luego:{Fore.CYAN}     
     TP = Realidad: benigno (+,+) ■  Prediccion: (P) benigno
     FP = Realidad: maligno (-,+) ■  Prediccion: (P) benigno
     TN = Realidad: maligno (+,-) ■  Prediccion: (N) maligno
     FN = Realidad: benigno (-,-) ■  Prediccion: (N) maligno     
    {Style.RESET_ALL}""")


def ejercicio_04():
    ENUNCIADO = """ 4. LDA como Preprocesamiento para otros Modelos: En lugar de usar LDA solo para visualizar
    (Ejercicio 4), utilízalo como un paso de reducción de dimensiones a 2 componentes. 
    Posteriormente, entrena un modelo de K-Nearest Neighbors (KNN) sobre esas componentes y compara su precisión
    con un modelo KNN entrenado con las variables originales. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.neighbors import KNeighborsClassifier as KNN

    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    # ■ Reducción a 2 dimensiones usando LDA
    lda = LinearDiscriminantAnalysis(n_components=2)
    X_lda = lda.fit( X = dd['X'], y = dd['y'] ).transform(X = dd['X'])
    algoritmo = KNN(n_neighbors=2)
    modelos_K = {'x_original': dd['X'], 'x_modificado': X_lda}
    for key, X in modelos_K.items():
        modelo = algoritmo.fit(X=X, y=dd['y'])
        precision = modelo.score(X=X, y=dd['y'])
        print(f'Precision modelo {key} = {precision:.2f}')
    
    print(f'{Fore.YELLOW}Me cuesta la Interpretación  aún, mas allá de sacar datos, para interpretarlos hay que saber abordarlos, estudiarlos{Style.RESET_ALL}')

def ejercicio_05():
    ENUNCIADO = """ 5. Impacto del MinMaxScaler vs StandardScaler: 
    El Ejercicio 5 demuestra el impacto del escalado.
    Repite el experimento utilizando MinMaxScaler (que escala los datos al rango [0, 1]) en lugar de
    StandardScaler. ¿Existe una diferencia notable en el rendimiento de la SVM? Justifica tu respuesta. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import MinMaxScaler

    dd = get_d_datos('cancer', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    df=dd['df']
    
    d_escalado = {'StandardScaller':StandardScaler(), 'MinMaxScaler':MinMaxScaler()}
    for key, value in d_escalado.items():
        escalado = value
        X_train = escalado.fit_transform(X = dd['X_train'])
        X_test  = escalado.transform(X = dd['X_test'])
        # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
        algoritmo = SVC()
        modelo = algoritmo.fit(X = X_train, y = dd['y_train'])
        # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
        precision = modelo.score( X = X_test ,  y = dd['y_test'] )
        print(f'• Escalado {key} \t• Precision = {precision:.2f}')    

    print(f'{Fore.YELLOW}No hay una diferencia notable si ambas precisiones son similares. {Style.RESET_ALL}')
    

def ejercicio_06():
    ENUNCIADO = """ 6. Validación Cruzada Estratificada: 
    Modifica el Ejercicio 6 para implementar StratifiedKFold con 10 carpetas (folds). 
    - Compara la desviación estándar de los resultados frente a la validación cruzada simple y
    - Argumenta por qué esta técnica es más robusta en datasets de salud. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    from sklearn.model_selection import StratifiedKFold, KFold
    from sklearn.model_selection import cross_val_score    

    dd = get_d_datos('cancer')    
    if not dd: return
    print("\n■■■■■■■■■ ")
    data = dd.data
    target = dd.target
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■ IA
    # Definimos los dos métodos de validación 
    cv_simple = KFold(n_splits=10, shuffle=True, random_state=42)
    cv_estratificado = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■
    modelos = { "SVM Lineal": SVC(kernel='linear'), "SVM RBF (No lineal)": SVC(kernel='rbf') }

    print(f"\n{'MODELO':<20} | {'CV SIMPLE (std)':<20} | {'CV ESTRATIF. (std)':<20}")
    print("-" * 70)
    for nombre, modelo in modelos.items():
        simple = cross_val_score(estimator=modelo, X=data, y=target, cv = cv_simple)
        estrat = cross_val_score(estimator=modelo, X=data, y=target, cv = cv_estratificado)

        # Imprimimos comparando la desviación estándar (std)
        print(f"{nombre:<20} | {simple.mean():.3f} (+/- {simple.std():.4f}) | {estrat.mean():.3f} (+/- {estrat.std():.4f})")
    pass
    print(f'{Fore.YELLOW}La estratificada me parece mejor porque tiene menos varianza, a pesar de la media.  {Style.RESET_ALL}')


def ejercicio_07():
    ENUNCIADO = """ 7. Ajuste del Umbral de Decisión: 
    En el Ejercicio 7, habilita la opción probability=True en el modelo SVC. 
    • Utiliza predict_proba para obtener las probabilidades de cáncer. 
    • Define un umbral personalizado: 
        • if la probabilidad de "maligno" es mayor a 0.25, clasifícalo como positivo. 
        • Observa cómo cambia el Recall y el número de Falsos Negativos. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    from modulo_3_clase_parte1 import ejercicio_07 as ejerciciosiete

    dd = get_d_datos('cancer', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    algoritmo = SVC(kernel='linear', probability=True)
    modelo = algoritmo.fit(dd['X_train'], dd['y_train'])
    
    predict = modelo.predict(dd['X_test'])
    proba   = modelo.predict_proba(dd['X_test'])
    
    # Todas las filas , la columna de maligno (pandas)
    probabilidad_maligno = proba[ : , 1 ]
    # Y el por qué python me gusta
    filtrado_25 = [1 if p > 0.25 else 0 for p in probabilidad_maligno]
    pass
    kung_fu = confusion_matrix(y_true = dd['y_test'], y_pred = filtrado_25)
    matrix_UI = ConfusionMatrixDisplay(confusion_matrix = kung_fu, display_labels = dd['target_names'])
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ MENU PARA PODER COMPARAR LOS DOS RESULTADOS
    sub_menu = {"Matriz de Confusión ejercicio 7": None, "Matriz de Confusión Con Umbral al 25%":None}
    while (True):
        i = menuDvd.MenuDiccionario(sub_menu, tituloMenu = "ELIGE GRAFICO PARA COMPARAR" ,
                                    num_char=60, char_1='', char_2='', char_3='_',
                                    texto_exit= '◀️  Atrás | - clear' )
        if i == 0: 
            break  # ❌ PRIMERO LA DE SALIDA                
        elif i == 1:
            ejerciciosiete()
        elif i == 2:
            matrix_UI.plot(cmap='Reds')
            plt.show()
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

def ejercicio_08():
    ENUNCIADO = """ 8. Naive Bayes y Supuestos de Independencia: 
    • Investiga el impacto de la correlación entre variables en Naive Bayes. 
    • Crea un nuevo dataset sintético basado en Iris donde dos variables sean copias exactas una de la otra. 
    • Compara el rendimiento de Naive Bayes frente a LDA en este dataset "redundante". """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    print(f'{Fore.YELLOW}NO ENTIENDO EL ENUNCIADO DEL EJERCICIO  {Style.RESET_ALL}')

def ejercicio_09():
    ENUNCIADO = """ 9. Optimización por Búsqueda Aleatoria (RandomizedSearch): 
    Sustituye GridSearchCV del Ejercicio 9 por RandomizedSearchCV. 
    Define una distribución continua para el parámetro C (por ejemplo, usando scipy.stats.expon) y 
    realiza 20 iteraciones. 
    Compara la eficiencia temporal frente a la búsqueda por rejilla. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    
    
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.preprocessing import StandardScaler

    cancer = get_d_datos('cancer')    
    if not cancer: return
    print("\n■■■■■■■■■ ")

    X_escalado = StandardScaler().fit_transform(cancer.data)    
    parametros = {
        'C': [0.1, 1, 10, 100],
        'gamma': [1, 0.1, 0.01, 0.001],
        'kernel': ['rbf']
    }
    # Crear y ejecutar la búsqueda
    algoritmo = RandomizedSearchCV(
        estimator = SVC(),    # el Modelo.
        param_distributions = parametros, # ¡Cambiado de param_grid!
        n_iter = 20,         # Muy importante: ¿cuántas combinaciones probar?
        refit = True,        # Re-entrena el mejor modelo al final
        verbose = 0,         # Silencioso (puedes subirlo a 2 para ver progreso)
        cv = 5,              # Validación cruzada
        n_jobs = -1,         # (Opcional) Usa toda la CPU para ir más rápido
        random_state = 42    # (Opcional) Para que el azar sea reproducible
    )
    algoritmo.fit(X=X_escalado, y=cancer.target)

    print(f"Mejores parámetros encontrados: {algoritmo.best_params_}")
    print(f"Mejor precisión obtenida: {algoritmo.best_score_:.4f}")


def ejercicio_10():
    ENUNCIADO = """ 10. Persistencia y Despliegue del Pipeline: 
    • Completa el Ejercicio 10 utilizando la librería joblib para guardar el pipeline entrenado 
    en un archivo llamado modelo_iris_final.pkl. 
    • Escribe un pequeño script independiente que cargue este archivo y realice predicciones sobre 5 
    nuevas muestras inventadas por ti, simulando un entorno de producción. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")
    
    print(f'{Fore.YELLOW}NO ENTIENDO EL ENUNCIADO DEL EJERCICIO  {Style.RESET_ALL}')

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ejercicio_01. 🌷🌷 SVC ■ Cambio de Kernell ■ ": ejercicio_01, 
        "Ejercicio_02. 🌷🌷 Naive Bayes ■ Probabilidad certeza": ejercicio_02 , 
        "Ejercicio_03. 🦀🦀 SVC ■ Matriz confusion ■ Accuracy ": ejercicio_03,
        "Ejercicio_04. 🌷🌷 EDA ■ Kneighbors(KNN) ■ Reducir Dimensiones ( LDA ) ■ GRAF: scatter": ejercicio_04,
        "Ejercicio_05. 🦀🦀 EDA ■ Escalado de los Datos, MinScaler vs StandarScaler ": ejercicio_05,
        "Ejercicio_06. 🦀🦀 SVC ■ Validación Cruzada Estratificada(StratifiedKFold) && Desviación standar": ejercicio_06,
        "Ejercicio_07. 🦀🦀 SVC ■ METRICAS ■ GRAF: Matriz de Confusión": ejercicio_07,
        "Ejercicio_08. 🌷🌷 Compara  LDA && Naive Bayes ■ METRICAS": ejercicio_08,
        "Ejercicio_09. 🦀🦀 SVC ■ Hiperparámetros C y gamma ■ GridSearchCV (MultiParametros)": ejercicio_09,
        "Ejercicio_10. 🌷🌷 PipeLine (all in one)": ejercicio_10,
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
    print("Ejercicios de  Modulo 3 - Algoritmos - Metricas Parte 1")
    main()
