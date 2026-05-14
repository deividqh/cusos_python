# ■■■■■■■■■■■■■■■■■■■■ ANALISIS EXPLORATORIO DE DATOS ( EDA ) ■■■■■■■■■■■■■■■■■■■■ 
# ■■■■■■■■■■■■■■■■■■■■ DATOS ESTRUCTURADOS ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# █ A █ Pregunta a Responder  ... Cual es el objeto del estudio?
# █ B █ Generalidades Dataset ... Idea General
# █ C █ Tipos de datos 
# █ D █ Estadistica descriptiva 
# █ E █ Visualización de los datos
# █ F █ Interaciones entre los componentes del dataset
# █ G █ Conclusiones y sumarización
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

import pandas as pd
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ESTADISTICA DESCRIPTIVA 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def estadisticas(np):
    print("\n■■■■■■■■■ Estadisticas Sobre objeto Numpy")
    print(f'Piezas totales: {len(np)}')
    print(f'Grosor medio: {np.mean():.4f}')
    print(f'Grosor minimo: {np.min():.4f}')
    print(f'Grosor maximo: {np.max():.4f}')
    print(f'Grosor desviacion estandar: {np.std():.4f}')


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Cálculo de IQR - RANGO DE CUANTILES
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Q1 y Q2 son datos numéricos que representan el valor de los primeros 25% de los datos.
# O sea: Si tengo 100 valores, Q1 representa el valor del dato de la posicion 25.
# ■■■■■■■■ ■ ■ ■ ■ ■ FORMULA █■
def outliers_iqr(data_frame, nombre_columna):
    Q1 = data_frame[nombre_columna].quantile(0.25)
    Q3 = data_frame[nombre_columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    # ■■■■■■■■ ■ ■ ■ ■ ■ FORMULA ■█
    # 
    print(f"{'■'*50}")
    print(f"q1: {Q1} \t q2:{Q3}")
    print(f"iqr: {IQR}")
    print(f"{'■'*50}")

    print(limite_inferior, "-" , limite_superior)

    # ■ Identificación de outliers: Los que estan entre los limites.
    outliers = ((data_frame[nombre_columna] < limite_inferior)  |
                (data_frame[nombre_columna] > limite_superior)
                )
    print(f"{'■'*50}")
    print(f"Valores atípicos detectados:")

    # Esto le dice a Pandas: "Muéstrame las filas donde outliers sea True"
    print(data_frame[outliers])

    return data_frame[outliers]
    """
    ■ El método IQR es una técnica estadística que se utiliza para identificar y filtrar valores atípicos en un conjunto de datos.
    ■ El IQR se calcula como la diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1) de los datos.
    ■ Los límites para identificar outliers se establecen utilizando la fórmula:
        • Limite inferior = Q1 - 1.5 * IQR
        • Limite superior = Q3 + 1.5 * IQR  
    ■ Cualquier valor que caiga por debajo del límite inferior o por encima del límite superior se considera un outlier.
    ■ En este caso, los valores de pH que se encuentran fuera de estos límites podrían indicar fallos en los sensores.
    """


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



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
def escalado_standar_scaler(X_train, X_test):
    from sklearn.preprocessing import StandardScaler

    algoritmo = SVC()
    modelo = algoritmo.fit(X_train, y_train)

    escalado = StandardScaler()
    X_train_scaled = escalado.fit_transform(X_train)
    X_test_scaled = escalado.transform(X_test)

# ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
