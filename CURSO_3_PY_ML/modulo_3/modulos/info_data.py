import pandas as pd

# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
# VISUALIZAR dataset Según Viene
# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
def ver_data(data_to_view):
    # 1. Convertir a DataFrame
    df = pd.DataFrame(data_to_view.data, columns=data_to_view.feature_names)

    # 2. (Opcional) Añadir la columna de diagnóstico (el 'target')
    df['target'] = data_to_view.target

    # 3. Mostrar las primeras 5 filas
    print(f"\n■ Visualización del Head del Dataset ")
    print(df.head())

def ver_data__(data_to_view):
    # Imprime el nombre de la característica y su valor para la primera fila
    for nombre, valor in zip(data_to_view.feature_names, data_to_view.data[0]):
        print(f"{nombre}: {valor}")

def ver_data____(data_to_view):
    # Imprimimos los nombres de las columnas (cabecera)
    print(f"{' | '.join(data_to_view.feature_names[:4])} ")
    
    # Recorremos las primeras 7 filas
    for fila in data_to_view.data[:7]:
        # Mostramos solo los primeros 4 valores de cada fila para no saturar la pantalla
        print(fila[:4])


# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■  
# DESCRIPCION - INFORMACION
# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■  
def descripcion_dataset(data_view):
    if isinstance(data_view, pd.DataFrame): 
        print('Es dataset')
    # describe e info son de pandas
    df = pd.DataFrame(data_view.data, columns=data_view.feature_names)

    print('■'*30 + ' DIMENSIONES DATASET')
    print(f'\n••••• Dim: {df.shape}')
    print(f'\n••••• Len: {len(df)}' )
    
    print('■'*30 + ' INDICE DATASET')
    print(df.index)

    print('■'*30 + ' DESCRIPCION DATASET')
    print(df.describe())
    
    print('■'*30 + ' INFORMACIÓN DATASET')
    df.info()

    # print('■'*30 + ' COLUMNAS')
    # print(df.columns)

    print('■'*30 + ' VALORES NaN')
    print(f'\n••••• count (no nulos por columna)\n {df.count()}')
    print(f'\n••••• count x Columnas (axis = 0 )\n {df.count(axis=0)}')
    print(f'\n••••• count x Filas (axis = 1 )\n {df.count(axis=1)}')

# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
# ESCALADO DE DATOS
# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
def escalado(modelo_fit):
    from sklearn.preprocessing import StandardScaler
    
    # 1. Modelo sin escalado
    score_raw = modelo_fit.score(X_test, y_test)
    # 2. Modelo con escalado

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
def splitter(X, y):
    from sklearn.model_selection import train_test_split

    # 70% train - 30% resto
    X_train, X_R, y_train, y_R = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # del 30% ,  50% test - 50% pruebas
    X_test, X_pruebas, y_test, y_pruebas = train_test_split(X_R, y_R, test_size=0.5, random_state=4)

    # Retorno 
    return X_train, X_test, X_pruebas, y_train, y_test, y_pruebas
# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 