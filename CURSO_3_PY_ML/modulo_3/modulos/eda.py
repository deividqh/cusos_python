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

# ■ C
#   Variables Numericas
#       discretas
#       continuas
#   Categoricas 
#       nominales 
#       ordinales (numerica)
#       binarios(Si/No, soltero/casado)
# ■ D
#   Media                   El promedio central.
#   Mediana                 Divide los datos en dos mitades
#   Desviación estandar     que tanto se alejan los datos de la media
#   Rango Quantiles         diferencia entre percentil 75 y 25

# ■ E
#   histograma
#   boxplot

# ■ F
#   Analisis uni-variado          Analizar una sola variable, por ejemplo precio 
#   Analisis bi-variado           Compara pares de variables (grafica de dispersión , indice de correlacion)
#   Analisis multivariado         Relaziones entre 2 o mas variables 
#       histograma, 
#       displot, 
#       pairplot
#       heatmap




# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ESTADISTICA DESCRIPTIVA 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
print(f'Piezas totales: {len(np_total_piezas)}')
print(f'Grosor medio: {np_total_piezas.mean():.4f}')
print(f'Grosor minimo: {np_total_piezas.min():.4f}')
print(f'Grosor maximo: {np_total_piezas.max():.4f}')
print(f'Grosor desviacion estandar: {np_total_piezas.std():.4f}')


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Cálculo de IQR - RANGO DE CUANTILES
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Q1 y Q2 son datos numéricos que representan el valor de los primeros 25% de los datos.
# O sea: Si tengo 100 valores, Q1 representa el valor del dato de la posicion 25.
# ■■■■■■■■ ■ ■ ■ ■ ■ FORMULA █■
Q1 = df_ph['ph'].quantile(0.25)
Q3 = df_ph['ph'].quantile(0.75)
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
outliers = ((df_ph['ph'] < limite_inferior)  |
            (df_ph['ph'] > limite_superior)
            )
print(f"{'■'*50}")
print(f"Valores atípicos detectados:")

# Esto le dice a Pandas: "Muéstrame las filas donde outliers sea True"
print(df_ph[outliers])
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