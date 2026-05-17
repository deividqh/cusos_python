from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split


def get_d_datos(dataset_name='iris', test_porciento=None, b_split=False):
    """ Cacho los datos del dataset que vayamos a usar y devuelvo un diccionario con todos los datos 
    y el split hecho.
    test_porciento puede ser entre 0 y 1 para el test y asume pocentaje o 30% por ejemplo.
    si test_porciento = None, devuelve el dataset cargadao data_load.
    si b_split = True devuelve los datos uno a uno parametrizados en el orden del return.
    """
    # ■■■■■■■■■ Cargo el dataset
    dataset_name = dataset_name.strip().lower()    
    if dataset_name == 'iris':
        data_load = datasets.load_iris()   
    elif dataset_name == 'cancer':
        data_load = datasets.load_breast_cancer()
    elif dataset_name == 'digits':                      # digits
        data_load = datasets.load_digits()
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

    X = data_load.data
    y = data_load.target

    # ■■■■■■■■■ 
    X_train, X_test, y_train, y_test = train_test_split(data_load.data, data_load.target, test_size = test_porciento, random_state = 42)
    
    # Creo un pandas con los nombres de las columnas
    df = pd.DataFrame(data = X, columns = data_load.feature_names)
    # Y le añado una columna mas con los resultados (0, 1, 2), así preparo el pandas para lo que venga.
    df['resultado'] = data_load.target
    
    # ■ Cargo el diccionario de retorno
    datos_retorno = {
        'X': X, 
        'y': y, 
        'X_train': X_train, 
        'y_train': y_train, 
        'X_test': X_test, 
        'y_test': y_test,
        'df': df, 
        'target_names': data_load.target_names,
        'feature_names': data_load.feature_names,
    }
    # ■  imprimo el head del dataset para echar un primer vistazo a los datos en el ejercicio
    print(f"\n■■■■■■■■■ DATOS INICIALES\n{df.head()}")
    # ■ Retorno
    if b_split == False:
        return datos_retorno
    else:
        return X, y, X_train, X_test, y_train, y_test, df, data_load.target_names, data_load.feature_names



