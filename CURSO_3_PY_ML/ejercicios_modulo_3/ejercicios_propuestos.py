from sklearn.model_selection import train_test_split
from sklearn.svm import SVC



import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from  colorama import Fore, Style
import os           # Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     # Funcion que crea un menu y devuelve un int(opcion)

def get_d_datos(dataset_name='iris', test_porciento=None):
    """ Cacho los datos del dataset que vayamos a usar y devuelvo un diccionario con todos los datos 
    y el split hecho.
    test_porciento puede ser entre 0 y 1 para el test y asume pocentaje o 30% por ejemplo.
    si test_porciento = None, devuelve el dataset.
    """
    from sklearn import datasets
    # ■■■■■■■■■ Cargo el dataset
    dataset_name = dataset_name.strip().lower()    
    if dataset_name == 'iris':
        data_load = datasets.load_iris()   
    elif dataset_name == 'cancer':
        data_load = datasets.load_breast_cancer()
    else:
        return None
    # ■■■■■■■■■ Si no me das la proporción de test, te doy el dataset.
    if test_porciento == None and dataset_name:
        return data_load
    
    # ■■■■■■■■■ Me vale lo que quieras: 0.7 o 70%
    if test_porciento > 0 and test_porciento <= 1:
        pass
    else:
        test_porciento = test_porciento / 100   
    pass

    datos_x = data_load.data
    datos_y = data_load.target

    # ■■■■■■■■■ 
    x_train, x_test, y_train, y_test = train_test_split(data_load.data, data_load.target, test_size = test_porciento, random_state = 42)
    
    # Creo un pandas con los nombres de las columnas
    df = pd.DataFrame(data = datos_x, columns = data_load.feature_names)
    # Y le añado una columna mas con los resultados (0, 1, 2), así preparo el pandas para lo que venga.
    df['resultado'] = data_load.target
    
    # ■ Cargo el diccionario de retorno
    datos_retorno = {
        'X': datos_x, 
        'y': datos_y, 
        'X_train': x_train, 
        'y_train': y_train, 
        'X_test': x_test, 
        'y_test': y_test,
        'df': df, 
        'target_names': data_load.target_names,
        'feature_names': data_load.feature_names,
    }
    # ■  imprimo el head del dataset para echar un primer vistazo a los datos en el ejercicio
    print(f"\n■■■■■■■■■ DATOS INICIALES\n{df.head()}")
    # ■ Retorno
    return datos_retorno
    # return X, y, X_train, X_test, y_train, y_test, df, target_names, feature_names
    

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
    print('En cuanto a la distribución de los datos se puede ver en el grafico que setosa(0) está bien diferenciada de las otras dos que mantienen un conjunto bien claro pero comparten un subconjunto de medidas confusas')

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
    vecinos = KNN(n_neighbors=2)
    modelos_K = {'x_original': dd['X'], 'x_modificado': X_lda}
    for key, X in modelos_K.items():
        modelo_fit = vecinos.fit(X=X, y=dd['y'])
        precision = modelo_fit.score(X=X, y=dd['y'])
        print(f'Precision modelo {key} = {precision:.2f}')

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

    st_scaler = StandardScaler()
    X_train_st = st_scaler.fit_transform( X = dd['X_train'] )
    X_test_st = st_scaler.transform( X = dd['X_test'] )

    mm_scaler = MinMaxScaler()
    X_train_mm = mm_scaler.fit_transform(dd['X_train'])
    X_test_mm = mm_scaler.transform(dd['X_test'])

    modelo_fit_st = SVC().fit(X_test_st, dd['y_train'])
    modelo_fit_mm = SVC().fit(X_test_mm, dd['y_train'])

    score_st = modelo_fit_st.score(X_test_st, dd['y_test'])
    score_mm = modelo_fit_st.score(X_test_mm, dd['y_test'])

    print(f'Precision Escalado Standar = {score_st}')
    print(f'Precision Escalado Min-Max = {score_mm}')


def ejercicio_06():
    ENUNCIADO = """ 6. Validación Cruzada Estratificada: 
    Modifica el Ejercicio 6 para implementar StratifiedKFold con 10 carpetas (folds). 
    - Compara la desviación estándar de los resultados frente a la validación cruzada simple y
    - Argumenta por qué esta técnica es más robusta en datasets de salud. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    from sklearn.model_selection import StratifiedKFold, KFold

    dd = get_d_datos('cancer', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")

    # Configuramos 3 Folds
    skf = StratifiedKFold(n_splits=10)


def ejercicio_07():
    ENUNCIADO = """ 7. Ajuste del Umbral de Decisión: En el Ejercicio 7, habilita la opción probability=True en el modelo
    SVC. Utiliza predict_proba para obtener las probabilidades de cáncer. Define un umbral
    personalizado: si la probabilidad de "maligno" es mayor a 0.25, clasifícalo como positivo. Observa cómo
    cambia el Recall y el número de Falsos Negativos. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('cancer', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")

def ejercicio_08():
    ENUNCIADO = """ 8. Naive Bayes y Supuestos de Independencia: Investiga el impacto de la correlación entre variables en
    Naive Bayes. Crea un nuevo dataset sintético basado en Iris donde dos variables sean copias exactas
    una de la otra. Compara el rendimiento de Naive Bayes frente a LDA en este dataset "redundante". """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")

def ejercicio_09():
    ENUNCIADO = """ 9. Optimización por Búsqueda Aleatoria (RandomizedSearch): Sustituye GridSearchCV del Ejercicio 9
    por RandomizedSearchCV. Define una distribución continua para el parámetro C (por ejemplo, usando
    scipy.stats.expon) y realiza 20 iteraciones. Compara la eficiencia temporal frente a la búsqueda por
    rejilla. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('cancer', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")

def ejercicio_10():
    ENUNCIADO = """ 10. Persistencia y Despliegue del Pipeline: Completa el Ejercicio 10 utilizando la librería joblib para
    guardar el pipeline entrenado en un archivo llamado modelo_iris_final.pkl. Escribe un pequeño
    script independiente que cargue este archivo y realice predicciones sobre 5 nuevas muestras
    inventadas por ti, simulando un entorno de producción. """
    print (f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")    

    dd = get_d_datos('iris', 30)    
    if not dd: return
    print("\n■■■■■■■■■ ")


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
    print("Ejercicios de Analisis de Datos - Modulo 2")
    main()
