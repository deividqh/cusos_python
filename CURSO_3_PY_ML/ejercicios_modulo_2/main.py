import os           #Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)
from colorama import Fore, Back, Style, init

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_01():
    txtEjer="""Ejercicio 1. Analisis de Canales de Marketing:
    • Crea un gráfico que compare el número de leads generados a través de 4 canales distintos: 'SEO', 'PPC', 'Social Media' y 'Email'."""
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")    
    
    print("\n■■■■■■■■■ DATOS INICIALES")
    canales = ['SEO','PPC','Social Media','Email']
    # Ahora hay que generar los datos para estas categorias
    data_canales = np.random.choice(canales, size=50, p=[0.2,0.2,0.1,0.5])
    # Creo el dataframe
    df_leads = pd.DataFrame({'leads':data_canales})
    
    # ■ Para un vistazo inicial de los datos, 'numpy' es mas rapido y directo. 
    # ■ Sobre 'pandas' hay df.head(), df.tail(), df.info(), df.describe() y df.value_counts() para categorias.
    print(data_canales)

    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(f'\n{df_leads.info()}')

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")

    # ■ Se ejecuta despues de cerrar el grafico.
    print(Fore.GREEN + """
    ■ DataFrame.describe() ► muestra un resumen estadístico. Solo información en consola. 
    ■ El gráfico de barras muestra la cantidad de leads generados por cada canal de marketing, lo que permite identificar cuál es el canal más efectivo para generar leads.
    ■ Otors graficos que podrían ser útiles para analizar la distribución de los leads por canal incluyen:
        • Gráfico de pastel (pie chart) para mostrar la proporción de leads generados por cada canal.
        • Gráfico de líneas para visualizar la tendencia de leads a lo largo del tiempo si se tienen datos temporales.
        • Gráfico de dispersión (scatter plot) para analizar la relación entre el número de leads y otras variables, como el presupuesto de marketing o la tasa de conversión.
        • Gráfico de caja (boxplot) para identificar la variabilidad y posibles outliers en el número de leads generados por cada canal.
        • Gráfico de barras apiladas (stacked bar chart) para comparar la contribución de cada canal a lo largo del tiempo o entre diferentes segmentos de clientes.
        • Gráfico de violín (violin plot) para mostrar la distribución de los leads generados por cada canal, incluyendo la densidad y los outliers.
    """ + Style.RESET_ALL) 
    
    # ■ Asignacion del estilo del grafico a través de un archivo .mplstyle
    with plt.style.context('./dark.mplstyle'):
        # Creo el Grafico
        a = sns.histplot(data = df_leads,  x='leads')
        # print(type(a)) # <class 'matplotlib.axes._subplots.AxesSubplot'> ► Es un objeto de tipo 'AxesSubplot' que representa el área donde se dibuja el gráfico.
        
        # ■ Textos
        plt.title('context with ./dark.mplstyle', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Nombre Leads (Categoría)', fontsize=12)
        plt.ylabel('Grafico usado: histograma(histplot)', fontsize=10)

        plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_02():
    txtEjer="""Ejercicio 2. Tráfico Web Semanal:
1 • Visualiza la tendencia de visitas diarias a un sitio web durante una semana completa.
2 • ¿Qué día se observa el mayor pico?"""

    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")    

    print("\n■■■■■■■■■ DATOS INICIALES")
    np.random.seed(42)  # Para reproducibilidad
        
    dias_semana  = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    data_visitas = np.random.randint(low=0, high=100000, size = 7)
    data_frame = pd.DataFrame({'dias':dias_semana, 'visitas':data_visitas})
    print(data_frame)
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(data_frame.describe().round(2))


    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")

    print("🛠️...El mayor pico de visitas se observa el día:", data_frame.loc[data_frame['visitas'].idxmax(), 'dias'])
    print(Fore.GREEN + """
    ■ El gráfico de líneas muestra la tendencia de visitas a lo largo de la semana, permitiendo identificar patrones y picos en el tráfico web.
    ■ El día con el mayor pico de visitas se determina utilizando 'idxmax()' para encontrar el índice del valor máximo en la columna 'visitas' y luego se accede al día correspondiente en la columna 'dias'.
        •  data_frame.loc[data_frame['visitas'].idxmax(), 'dias'] ► devuelve el día de la semana con el mayor número de visitas.
    """ + Style.RESET_ALL)
    print(Fore.GREEN + """■ uso de plt.plot() para graficar una serie temporal, donde el eje x representa los días de la semana y el eje y representa el número de visitas.
    Opcion A: por posicion      ► plt.plot(data_frame['dias'], data_frame['visitas'], marker='o')
    Opcion B: Usando 'data'     ► plt.plot('dias', 'visitas', data=data_frame, marker='o')
    Opcion C: Usando 'x' e 'y'  ► plt.plot(x1, y1, x2, y2, x3, y3)
    """ + Style.RESET_ALL)
    
    # ■ Asignacion del estilo del grafico [ dark_background , bmh , ggplot , fivethirtyeight , seaborn-darkgrid , seaborn-whitegrid , seaborn-poster , seaborn-talk , seaborn-ticks ]
    ESTILO = 'fivethirtyeight'
    with plt.style.context(ESTILO):
        plt.figure(figsize=(9.5, 7))
        plt.plot(data_frame['dias'], data_frame['visitas'], marker='o')
        # ■ Textos
        plt.title('\n■ Estilo Usado: ' + ESTILO + '\n■ Tipo de Grafico:: "plot" \n■ Usado para "Series Temporales" ', fontsize=10,  pad=15)
        plt.xlabel('Dias Semana', fontsize=10, labelpad=10)
        plt.ylabel('Visitas Diarias', fontsize=10, labelpad=10)

        plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_03():
    txtEjer="""\nEjercicio 3. Calidad en Manufactura:
En una línea de producción de piezas metálicas, se mide el grosor de 150 unidades.
    1 • Utiliza un boxplot para determinar si hay piezas defectuosas (outliers)."""
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    grosor_optimo = 4
    mas_menos = 0.005
    grosor_piezas = np.random.uniform(low=4-mas_menos, high=4+mas_menos, size=150)
    total_piezas = np.concatenate([grosor_piezas, [4.5, 5 , 3.5 , 5.15, 4.25]])
    print(total_piezas)
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(f'Piezas totales: {len(total_piezas)}')
    print(f'Grosor medio: {total_piezas.mean():.4f}')
    print(f'Grosor minimo: {total_piezas.min():.4f}')
    print(f'Grosor maximo: {total_piezas.max():.4f}')
    print(f'Grosor desviacion estandar: {total_piezas.std():.4f}')

    # print("\n■ ■ ■ ■ ■ ■ ■  📈 ")

    print(Fore.GREEN + """
    ■ El 'boxplot' muestra la distribución de las piezas y permite identificar los outliers.
    ■ Quiero diferenciar el uso de 'numpy' y 'pandas' para describir los datos, y 'matplotlib' y 'seaborn' para visualizarlos
    ■ Uso 'numpy' para calcular la 'media', el 'minimo', el 'maximo' y la 'desviacion estandar' del grosor de las piezas.
    ■ Uso 'pandas' para crear un DataFrame y obtener una descripción estadística más completa con df.describe().
    ■ El 'boxplot' revela que hay piezas con grosor significativamente diferente al óptimo(outliers).
    ■ otros graficos como el 'histograma' o el 'scatter plot' podrían ser útiles para analizar la distribución de los grosores y detectar patrones adicionales en los datos.
    """ + Style.RESET_ALL) 

    sub_menu={  
        "Sin DataFrame (sobre objeto 'matplotlib' trabajado con 'numpy')": None, 
        "Con DataFrame (sobre objeto 'seaborn' trabajado con 'pandas')": None , 
    }
    
    while (True):
        i = menuDvd.MenuDiccionario(sub_menu, tituloMenu = TITULO_SUB_MENU ,
                                    num_char=60, char_1='', char_2='', char_3='_',
                                    texto_exit= '◀️  Atrás | - clear')
        if i == 0: 
            break  # ❌ PRIMERO LA DE SALIDA                
        if i == 1:
            with plt.style.context('Solarize_Light2'):
                plt.boxplot(total_piezas)
                plt.show()  
        elif i == 2:
            with plt.style.context('fivethirtyeight'):
                df = pd.DataFrame({'piezas':total_piezas})
                sns.boxplot(data=df)
                plt.show()  
        pass

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_04():
    txtEjer="""Ejercicio 4. Optimización de Dataset
Tienes un dataset con 500,000 registros de temperatura (float64) y estado del sensor (bool).
    1 • Analiza el ahorro de memoria al convertir la temperatura a float32.
"""
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    temperatura = np.random.uniform(low=10, high=40, size=500000)
    estado = np.random.choice(['True', 'False'], size=500000)
    df = pd.DataFrame({'temperatura':temperatura, 'estado':estado})
    print(df.head(n=10))

    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(f'Información Inicial{df.describe()}')
    df.info(verbose=True, memory_usage='deep')

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    # Cambio el tipo de dato de la columna 'temperatura' a float32 para reducir el uso de memoria.
    new_df = df['temperatura'].astype('float32')
    print()
    new_df.info()
    
    print(Fore.GREEN + """
    ■ El uso de memoria se ha reducido al convertir la columna 'temperatura' a float32.
    ■ tambien podria haber usado 'estado' como tipo booleano en lugar de string, lo que también reduciría el uso de memoria.
    ■ otra alternativa para ver el uso de memoria es usar el método 'memory_usage()' de pandas, que muestra el uso de memoria por columna y el total del DataFrame.
    """ + Style.RESET_ALL)

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_05():
    txtEjer="""Ejercicio 5. Educación vs Salario
1• Investiga la relación entre los "Años de Estudio" y el "Salario Mensual".
2• Representa la correlación mediante un scatter plot con línea de tendencia.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    annos_estudio = np.random.randint(low=1, high=10, size=50)
    salario_mensual = np.random.randint(low=1000, high=5500, size=50)
    df = pd.DataFrame({'annos':annos_estudio, 'salario':salario_mensual})
    print(df)
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(df.describe().round(2))
    
    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    
    print(Fore.GREEN + """ 
    ■ El scatter plot muestra la relación entre los años de estudio y el salario mensual, donde cada punto representa a un individuo.
    ■ La línea de tendencia ( regresión ) indica si existe una correlación positiva, negativa o nula entre las variables. En este caso, podríamos observar una tendencia positiva, lo que sugiere que a medida que aumentan los años de estudio, también tiende a aumentar el salario mensual.
    """+ Style.RESET_ALL ) 

    # sns.regplot(x='annos', y='salario', data=df)
    
    with plt.style.context('./test.mplstyle'):
        sns.scatterplot(data=df, x='annos', y='salario', hue='salario')
        plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_06():
    txtEjer="""Ejercicio 6. Control de Calidad Alimentaria:
Un lote de leche tiene mediciones de pH.
1. Implementa el método IQR para filtrar mediciones erróneas que podrían indicar fallos en los sensores.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    
    print("\n■■■■■■■■■ DATOS INICIALES")
    np.random.seed(42)
    outliers = np.array([8.0, -1.05, 9.2, -3.0, 5.0])
    ph = np.random.normal(loc=3.5, scale=1, size = 50)
    ph = np.concatenate([ph,outliers])
    df_ph = pd.DataFrame({'ph':ph})

    print(ph)
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    # print(df_ph)
    print(df_ph.describe())

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    # ■ Cálculo de IQR
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

    print(Fore.GREEN + """
    ■ El método IQR es una técnica estadística que se utiliza para identificar y filtrar valores atípicos en un conjunto de datos.
    ■ El IQR se calcula como la diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1) de los datos.
    ■ Los límites para identificar outliers se establecen utilizando la fórmula:
        • Limite inferior = Q1 - 1.5 * IQR
        • Limite superior = Q3 + 1.5 * IQR  
    ■ Cualquier valor que caiga por debajo del límite inferior o por encima del límite superior se considera un outlier.
    ■ En este caso, los valores de pH que se encuentran fuera de estos límites podrían indicar fallos en los sensores.
    """ + Style.RESET_ALL)

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_07():
    txtEjer="""Ejercicio 7. Rendimiento de Exámenes:
1• Compara la distribución de notas de dos grupos de alumnos (Grupo A y Grupo B) utilizando gráficos KDE superpuestos.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    np.random.seed(42)

    # loc = promedio, scale = desviación estándar, size = cantidad de alumnos
    notas_a = np.random.normal(loc=6, scale=1.5, size=15)
    notas_b = np.random.normal(loc=6, scale=1.5, size=15)
    print(notas_a)
    print(notas_b)
    # Aseguramos que las notas estén en el rango de 0 a 10
    notas_a = np.clip(notas_a, 0, 10).round(2)
    notas_b = np.clip(notas_b, 0, 10).round(2)
    # print(notas_a, notas_b)
    df = pd.DataFrame({'grupo_a':notas_a, 'grupo_b':notas_b})
    # print(df)
    
    #  He tenido que ir cambiando loc y scale para que me quede una distribución de notas creible  
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(df['grupo_a'].describe())
    print(df['grupo_b'].describe().round(2))

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")

    print(Fore.GREEN + """
■ distribución normal(Campana Gaus) ► np.random.normal( loc = 6, scale = 1.5 , size = 15 )
    • loc = promedio  ■ scale = desviación estándar  ■ size = cantidad de alumnos/muestras
■ Sigue la regla de 68-95-99.7:
    • Aproximadamente el 68% de los datos cae dentro de 1 desviación estándar del promedio ► 6 + 1.5 * 1 = 7.5
    • el 95% de los datos cae dentro de 2 desviaciones estándar del promedio ► 6 + 1.5 * 2 = 9
    • el 99.7% de los datos cae dentro de 3 desviaciones estándar del promedio ► 6 + 1.5 * 3 = 10.5 
■ clip acota entre 0 y 10 las notas ► np.clip(notas_a, 0, 10)
    """ + Style.RESET_ALL)

    # ■ Estilo definido en un diccionario.
    tema_negocios = {
        "axes.facecolor": "#ffffff",
        "axes.prop_cycle": plt.cycler(color=["#003f5c", "#bc5090", "#ffa600"]),
        "font.family": "serif"
    }
    plt.rcParams.update(tema_negocios)

    # sns.kdeplot(data=df, fill=True, common_norm=False)
    sns.kdeplot(data=df, fill=True, common_norm=True)
    plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_08():
    txtEjer="""Ejercicio 8. Variables Meteorológicas:
• Crea un mapa de calor que muestre la correlación entre: 
    Temperatura, 
    Humedad, 
    Velocidad del Viento, 
    Presión Atmosférica 
    Radiación Solar.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    
    np.random.seed(42)
    print("\n■■■■■■■■■ DATOS INICIALES")
    """ RELACIONES ENTRE LAS VARIABLES: MIRADO POR INTERNET """
    n_muestras = 100
    # ■ Radiación: El motor de todo (0 a 1000 W/m2)
    radiacion = np.random.uniform(low=0, high=1000, size=n_muestras)
    
    # ■ Temperatura: Relacionada con la radiación + un poco de ruido
    # A más sol, más calor.
    temperatura = 15 + (radiacion / 50) + np.random.normal(loc=0, scale=2, size=n_muestras)

    # ■ Humedad: Inversamente proporcional a la temperatura
    # Si hace calor, el aire se seca (humedad relativa baja).
    humedad = 100 - (temperatura * 1.5) + np.random.normal(loc=0, scale=5, size=n_muestras)
    humedad = np.clip(a=humedad, a_min=10, a_max=95) # Limitamos para que no salga del rango 0-100
    
    # ■ Presión: Oscilando cerca de los 1013 hPa
    pAh = np.random.normal(loc=1013, scale=10, size=n_muestras)

    # ■ Viento: Un poco más fuerte si la presión es baja (simplificado)
    viento = np.random.uniform(low= 0, high=25, size=n_muestras) + (1030 - pAh) * 0.5
    viento = np.clip(viento, 0, 60)

    df = pd.DataFrame({'temperatura' : temperatura, 
                    'humedad' : humedad, 
                    'viento': viento , 
                    'pAh' : pAh , 
                    'radiacion' : radiacion
                    })
    print(df.head(n=10) )
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(df.describe().round(2))
    print()
    df.info()

    # print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")

    print(Fore.GREEN + """
    ■ El mapa de calor muestra la fuerza y dirección de las relaciones entre las variables.
    ■ Utilizo un 'head-map' para visualizar la correlación entre las variables.
    ■ En sns.heatmap(data=df.corr(), annot=True, cmap='coolwarm')
        • df.corr()  ► crea una correlación de los datos con la dimensión 5x5 
        • annot=True ► muestra los valores de correlación en cada celda del mapa de calor
        • cmap='coolwarm' ► elige una paleta de colores que va de azul (correlación negativa) a rojo (correlación positiva) pasando por blanco (sin correlación)
    """ + Style.RESET_ALL)

    sub_menu={  
        "Opt. sin equivalencia data_frame.corr():": None, 
        "Opt. con data_frame.corr()": None , 
    }
    while (True):
        i = menuDvd.MenuDiccionario(sub_menu, tituloMenu = TITULO_SUB_MENU ,
                                    num_char=60, char_1='', char_2='', char_3='_',
                                    texto_exit= '◀️  Atrás | - clear' )
        if i == 0: 
            break  # ❌ PRIMERO LA DE SALIDA                
        if i == 1:
            sns.heatmap(data=df, cmap='coolwarm')
        elif i == 2:
            # Esto genera una tabla de 5x5 en lugar de 100x5
            sns.heatmap(data=df.corr(), annot=True, cmap='coolwarm')
        
        plt.show()  

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_09():
    txtEjer="""# Ejrcicio 9. Precios Inmobiliarios Sesgados:
1. Calcula **media** y **mediana** de los precios de una calle donde 5 casas valen 200k y una mansión vale 5M.
2. Justifica cuál usarías para una tasación justa.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    precios = [200000, 200000, 200000, 200000, 200000, 5000000]
    print(precios)
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(f"Media: {np.mean(precios)}")
    print(f"Mediana: {np.median(precios)}")
    
    df = pd.DataFrame({'precios':precios})
    print(df.describe().round(2))
    
    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")    

    print(Fore.GREEN + """
    ■ La 'media' se ve fuertemente influenciada por el valor extremo de la mansión, resultando en un precio promedio de aproximadamente 1.2 millones, lo cual no refleja adecuadamente el valor típico de las casas en esa calle.
    ■ La 'mediana', por otro lado, es 200k, lo que representa el valor central de los precios y proporciona una tasación más justa para la mayoría de las casas, ya que no se ve afectada por el precio extremadamente alto de la mansión.    
    ■ Si quiero extraer el valor de la media, tengo que usar numpy.mean(precios) y Si quiero solo información estadística de los precios, puedo usar pandas.describe() con un DataFrame.
    ■ Para 'visualizar la distribución' de los precios, un 'boxplot' es útil para mostrar la presencia de valores atípicos (outliers) como la mansión de 5M, que se destacará claramente en el gráfico.
    """ + Style.RESET_ALL)

    sns.boxplot(data=df, x='precios')
    plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ejercicio_10():
    txtEjer="""Ejrcicio 10. Dashboard de Ventas Regional:
Diseña un dashboard con dos paneles:
    1• Gráfico de barras de ventas por región.
    2• Histograma de la cantidad de artículos comprados por cliente.
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    print("\n■■■■■■■■■ DATOS INICIALES")
    np.random.seed(42)
    regiones = ['Norte', 'Sur', 'Este', 'Oeste']
    ventas = np.random.randint(low=1000, high=5000, size=4)
    cantidad_articulos = np.random.randint(low=1, high=20, size=100)
    df_ventas = pd.DataFrame({'regiones':regiones, 'ventas':ventas})
    df_articulos = pd.DataFrame({'cantidad_articulos':cantidad_articulos})
    print(df_ventas)
    print(df_articulos.head(n=10))
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(df_ventas.describe().round(2))
    print(df_articulos.describe().round(2))

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")

    print(Fore.GREEN + """
    ■ fig, axes = plt.subplots(1, 2, figsize=(12, 5)) ► crea una figura con 1 fila y 2 columnas para colocar dos gráficos.
        • axes[0] se refiere al primer gráfico (barras) y axes[1] al segundo gráfico (histograma).
        • el objeto axes permite personalizar cada gráfico individualmente, como establecer títulos, etiquetas y estilos.
        • 'subplot' es una forma de acceder a 'matplotlib' y acceder a la herencia madre, donde 'figura' es el contenedor general y 'axes' es un arreglo de objetos para cada gráfico que contiene a axis, ticks, labels, ...
        • figsize=(12, 5) establece el tamaño de la figura en pulgadas. No necesario como dato.
        • sns.barplot() se utiliza para crear un gráfico de barras que muestra las ventas por región, mientras que sns.histplot() se emplea para visualizar la distribución de la cantidad de artículos comprados por cliente.
    
    ■ El gráfico de barras muestra claramente las diferencias en las ventas entre las regiones, mientras que el histograma revela la distribución de la cantidad de artículos comprados por cliente, lo que puede ayudar a identificar patrones de compra y segmentar a los clientes según su comportamiento.
    """ + Style.RESET_ALL)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfico de barras de ventas por región
    sns.barplot(data=df_ventas, x='regiones', y='ventas', ax=axes[0])
    axes[0].set_title('Ventas por Región')
    
    # Histograma de la cantidad de artículos comprados por cliente
    sns.histplot(data=df_articulos, x='cantidad_articulos', bins=10, ax=axes[1])
    plt.show()
    
def estilos():
    print(Fore.YELLOW + "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ■ ■ ■ ■ ■ ■ ■ " + Style.RESET_ALL)
    print(Fore.CYAN + """ 
■ El 'Ambito' Para Aplicar un Estilo:
    • 'GLOBAL'                          ► plt.style.use('nombre_estilo') 
    • 'contexto específico'             ► with plt.style.context('nombre_estilo'): """ + Style.RESET_ALL ) 
    print( Fore.GREEN + """
a) plt.style.use('ggplot')              ► Aplica el estilo 'ggplot' a todos los gráficos posteriores(GLOBAL).
b) with plt.style.context('bmh'):       ► Aplica el estilo 'bmh' solo dentro del bloque de código indentado, 
        plt.plot(x, y)                  ► Tiene que implementarse el grafico dentro del bloque para que se aplique el estilo.
        plt.show() 
""" + Style.RESET_ALL ) 
    print(Fore.CYAN + """
■ 'ggplot' ► inspirado en el estilo de gráficos de R, con un fondo gris claro y líneas de cuadrícula.
■ 'bmh' ► estilo de gráficos utilizado en el libro "Bayesian Methods for Hackers", con un fondo blanco y líneas de cuadrícula sutiles.)
■ 'dark_background' ► fondo oscuro con líneas de cuadrícula claras, ideal para presentaciones.
■ 'fivethirtyeight' ► inspirado en el estilo de gráficos del sitio web FiveThirtyEight, con un fondo gris claro y líneas de cuadrícula.
■ 'seaborn-darkgrid' ► estilo de gráficos de Seaborn con un fondo oscuro y líneas de cuadrícula, ideal para resaltar los datos.
""" + Style.RESET_ALL)    
    print (Fore.GREEN + """
    with plt.style.context('bmh'):
        sns.histplot(data=df_leads, x='leads')
        plt.show() 
""" + Style.RESET_ALL )
    print( Fore.CYAN + """
* También es posible crear 'Estilos Personalizados' guardando las configuraciones en un archivo [ .mplstyle ] 
y luego aplicándolo con plt.style.use('./nombre_estilo.mplstyle') o plt.style.context('./nombre_estilo.mplstyle') para un contexto específico.: 
""" + Style.RESET_ALL)
    print(Fore.GREEN + """        
    with plt.style.context('./mi_estilo.mplstyle'):
        sns.histplot(data=df_leads, x='leads')
        plt.show()
""" + Style.RESET_ALL ) 
    print( Fore.CYAN + """
* Otra forma de aplicar estilos personalizados es definiendo un diccionario con las configuraciones y 
luego actualizando los parámetros de Matplotlib con plt.rcParams.update(mi_estilo).
""" + Style.RESET_ALL)    
    print( Fore.GREEN + """
    tema_negocios = {
        "axes.facecolor": "#ffffff",
        "axes.prop_cycle": plt.cycler(color=["#003f5c", "#bc5090", "#ffa600"]),
        "font.family": "serif"
    }
    plt.rcParams.update(tema_negocios) 
""" + Style.RESET_ALL)
    print(Fore.YELLOW + "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ■ ■ ■ ■ ■ ■ ■ " + Style.RESET_ALL)


# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def extras():
    from PIL import Image
    sub_menu={  
        "Numpy": None, 
        "Pandas": None , 
        "Matplotlib": None , 
        "Seaborn": None ,
        "Seaborn_2": None, 
        "APLICACION DE ESTILOS": None, 
    }
    while (True):
        i = menuDvd.MenuDiccionario(sub_menu, tituloMenu = TITULO_SUB_MENU ,
                                    num_char=60, char_1='', char_2='', char_3='_',
                                    texto_exit= '◀️  Atrás | - clear'
                                    )
        if i == 0: 
            break  # ❌ PRIMERO LA DE SALIDA                
        if i == 1:
            # Abre la imagen
            imagen = Image.open("numpy_arbol_gen.png")
            imagen.show()
        elif i == 2:
            imagen = Image.open("pandas_arbol_gen.png")
            imagen.show()
        elif i == 3:
            imagen = Image.open("matplotlib_arbol_gen.png")
            imagen.show()
        elif i == 4:
            imagen = Image.open("seaborn_arbol_gen.png")
            imagen.show()
        elif i == 5:
            imagen = Image.open("seaborn_arbol_gen_2.png")
            imagen.show()
        elif i == 6:
            # estilos = ['ggplot', 'bmh', 'dark_background', 'fivethirtyeight', 'seaborn-darkgrid']
            estilos()
        else:
            pass

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ (Nulos y Relleno)
# Contexto: Tienes un dataset de sensores industriales donde algunos datos se perdieron por fallos
# de conexión. No podemos simplemente borrar las filas porque perderíamos información valiosa 
# de otras columnas.
def ejercicio_11():
    print(Fore.YELLOW + "  Ejercicio 11: Tratamiento de Valores Nulos  " + Style.RESET_ALL)
    txtEjer=""" Contexto: Tienes un dataset de sensores industriales donde algunos datos se perdieron por fallos
de conexión. No podemos simplemente borrar las filas porque perderíamos información valiosa de otras columnas.
    1. Crea un DataFrame con valores nulos (NaN) en algunas columnas.
    2. Identifica dónde están los nulos utilizando df.isnull().
    3. Rellena los nulos usando df.fillna() con diferentes estrategias (media, mediana, valor constante).
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")
    
    # 1. Creamos datos con "agujeros" (NaN)
    data = {
        'sensor_id': [1, 2, 3, 4, 5],
        'temperatura': [25.5, np.nan, 26.2, np.nan, 24.8],
        'presion': [1012, 1013, np.nan, 1010, 1015]
    }
    df = pd.DataFrame(data)
    print("\n■■■■■■■■■ DATOS INICIALES (Con Nulos):")
    print(df)
    
    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(df.describe().round(2))

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    # 2. Identificar nulos: df.isnull() devuelve una máscara booleana
    print("\n¿Dónde hay nulos? (Suma por columna):")
    print(df.isnull().sum()) 

    # 3. Estrategia de Relleno: df.fillna()
    # Rellenamos temperatura con la MEDIA y presión con un valor CONSTANTE
    df['temperatura'] = df['temperatura'].fillna(df['temperatura'].mean())
    df['presion'] = df['presion'].fillna(1000) # Asumimos 1000 por protocolo
    
    print("\n■ Dataset Limpio (Post-fillna):")
    print(df)
    
    print(f"\n{Fore.GREEN}INFO: 'isnull()' es tu detector de mentiras. "
          f"'fillna()' permite que el modelo no colapse por falta de datos.{Style.RESET_ALL}")
    pass

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ (Encoding y Scaling)
def ejercicio_12():
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    
    print(Fore.CYAN + "  Ejercicio 12: Encoding y Escalado  " + Style.RESET_ALL)
    txtEjer=""" Contexto: Los modelos no entienden qué es "Marketing" o "Ventas", solo entienden números. 
    Además, si comparas "Años de Estudio" (1-20) con "Salario" (1000-5000), el salario dominará 
    la matemática por pura magnitud. """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")    

    df = pd.DataFrame({
        'departamento': ['Ventas', 'IT', 'IT', 'Ventas', 'RRHH'],
        'experiencia_años': [2, 10, 8, 1, 5],
        'salario_mensual': [1500, 4500, 3800, 1200, 2500] 
        })
    
    print("\n■■■■■■■■■ DATOS INICIALES")
    print(df)
    
    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    # --- CODIFICACIÓN (Encoding) ---
    # Convertimos categorías de texto a números (0, 1, 2...)
    le = LabelEncoder()
    df['dep_encoded'] = le.fit_transform(df['departamento'])
    
    # --- ESCALADO (Scaling) ---
    # Llevamos los números a una escala común (Media 0, Desviación 1)
    scaler = StandardScaler()
    # Escalamos solo las columnas numéricas
    df[['exp_scaled', 'sal_scaled']] = scaler.fit_transform(df[['experiencia_años', 'salario_mensual']])
    
    print("\n■ Dataset Transformado:")
    print(df[['departamento', 'dep_encoded', 'exp_scaled', 'sal_scaled']])
    
    print(f"\n{Fore.GREEN}INFO: StandardScaler evita que las variables con números grandes "
          f"tengan más peso injustificado en el modelo.{Style.RESET_ALL}")

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ (Balance de Clases)
from sklearn.utils import resample
def ejercicio_13():
    print(Fore.YELLOW + " Ejercicio 13: Balance de Clases (Resampling) " + Style.RESET_ALL)
    txtEjer = """
Ejercicio 13: El Problema de la Aguja en el Pajar (Balance de Clases)
Contexto: Imagina que intentas detectar fraudes bancarios. 
El 99.9% de las transacciones son legales. Si el modelo dice "Todas son legales", 
tendrá un 99.9% de precisión, ¡pero fallará en su único objetivo!
    """
    print (f"\n{Fore.LIGHTYELLOW_EX}{txtEjer}{Style.RESET_ALL}")    

    # Creamos un dataset muy desbalanceado
    n_legales = 100
    n_fraudes = 5
    
    df_clase_A = pd.DataFrame({'tipo': ['Legal'] * n_legales, 'monto': np.random.randint(10, 100, n_legales)})
    df_clase_B = pd.DataFrame({'tipo': ['Fraude'] * n_fraudes, 'monto': np.random.randint(500, 1000, n_fraudes)})
    df_total = pd.concat([df_clase_A, df_clase_B])

    print("\n■■■■■■■■■ DESCRIPCION DE LOS DATOS")
    print(f"Antes del balanceo:\n{df_total['tipo'].value_counts()}")
    print(df_total)

    print("\n■ ■ ■ ■ ■ ■ ■  PROCESO ✔️")
    # ESTRATEGIA: Oversampling (Aumentar la clase minoritaria)
    df_minority_upsampled = resample(df_clase_B, 
                                     replace=True,     # Duplicar filas
                                     n_samples=100,    # Igualar a la clase mayoritaria
                                     random_state=42)
    
    df_balanceado = pd.concat([df_clase_A, df_minority_upsampled])
    
    print(f"\nDespués del balanceo (Oversampling):\n{df_balanceado['tipo'].value_counts()}")
    
    print(f"\n{Fore.GREEN}INFO: Al balancear, obligamos al modelo a prestar "
          f"tanta atención al 'Fraude' como a lo 'Legal'.{Style.RESET_ALL}")

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline  # <-- Importante añadir esto

def ejercicio_14():
    tabla = """ 
    A[Datos Brutos de Entrada] --> B[1. Limpieza de Datos: Detección de Duplicados e IQR]
    B -► C[2. Imputación: Tratamiento de Valores Nulos]
    C -► D[3. Codificación de Categorías: One-Hot Encoding]
    D -► E[4. Escalado: Estandarización de Variables Numéricas]
    E -► F[Datos Listos para alimentar el Modelo de IA]
    """
    enunciado = """ 
    procesaremos un dataset médico que contiene información sobre pacientes. El
    dataset incluye variables numéricas (como la Presion_Arterial), variables categóricas (como el Genero) y
    tiene problemas de valores nulos y outliers que debemos resolver de forma robusta antes de entrenar un
    modelo que prediga patologías.
    """
    print(f'FLUJO DE DATOS: \n{Fore.BLUE}{tabla}{Style.RESET_ALL}')
    print(f'ENUNCIADO DEL EJERCICIO:\n{Fore.CYAN}{enunciado}{Style.RESET_ALL}')
    
    # 1. Creación de un dataset médico bruto con problemas
    np.random.seed(10)
    datos_medicos = {
        'Paciente_ID': [101, 102, 103, 104, 105, 106],
        'Edad': [45, np.nan, 29, 65, 52, 38], 
        'Presion_Arterial': [120, 130, 240, 115, np.nan, 125], 
        'Genero': ['Masculino', 'Femenino', 'Femenino', 'Masculino', np.nan, 'Femenino'] 
    }
    df_medico = pd.DataFrame(datos_medicos)
    print("\n ■ ■ DATASET ORIGINAL BRUTO ■ ■ ")
    print(df_medico)
    
    # 2. Tratamiento de Outliers de Presión Arterial
    df_medico.loc[df_medico['Presion_Arterial'] > 200, 'Presion_Arterial'] = np.nan
    print(f'■ OUTLIERS:\n{df_medico}')
    
    # 3. Separación de Variables
    variables_numericas = ['Edad', 'Presion_Arterial']
    variables_categoricas = ['Genero']
    
    # 4. Configuración del Pipeline Automatizado
    # Creamos sub-pipelines independientes para ejecutar los pasos de forma secuencial
    pipeline_numerico = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    pipeline_categorico = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Unimos todo en el transformador por columnas utilizando los sub-pipelines
    preprocesador = ColumnTransformer(transformers=[
        ('num_trans', pipeline_numerico, variables_numericas),
        ('cat_trans', pipeline_categorico, variables_categoricas)
    ], remainder="drop")
    
    # 5. Aplicación práctica del Pipeline sobre los datos
    datos_procesados = preprocesador.fit_transform(df_medico)
    
    # Reconstruimos el DataFrame resultante para visualización
    columnas_numericas_salida = variables_numericas
    
    # Accedemos de forma segura al objeto 'onehot' que vive dentro del sub-pipeline 'cat_trans'
    obj_onehot = preprocesador.named_transformers_['cat_trans'].named_steps['onehot']
    columnas_categoricas_salida = obj_onehot.get_feature_names_out(variables_categoricas)
    
    todas_las_columnas = list(columnas_numericas_salida) + list(columnas_categoricas_salida)
    df_procesado_final = pd.DataFrame(datos_procesados, columns=todas_las_columnas)
    
    print("\n--- DATASET FINAL LIMPIO Y PREPROCESADO ---")
    print(df_procesado_final)

    conclusion="""
• Imputación de Nulos: El valor nulo de Edad en el registro 2 se rellenó de forma autónoma con la
  mediana del resto de pacientes (45.0). El valor erróneo/outlier de Presion_Arterial (240.0) fue
  filtrado y rellenado estadísticamente con 122.5 (mediana libre de outliers).
• Codificación One-Hot: La columna de texto Genero desapareció por completo y se transformó en dos
  columnas binarias: Genero_Femenino y Genero_Masculino.
• Estandarización y Escalado: Las variables de Edad y Presion_Arterial ahora se encuentran
  expresadas en una escala centrada en 0 con desviación estándar 1. Ya no hay peligro de que una
  variable domine erróneamente sobre la otra debido a diferencias de magnitud física.
 """
    print(f'CONCLUSION FINAL\n{Fore.MAGENTA}{conclusion}{Style.RESET_ALL}')

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    global TITULO_SUB_MENU 
    TITULO_SUB_MENU = Fore.LIGHTBLUE_EX + '■■■■■■■■■■' + Fore.YELLOW + ' Sub Menu ' + Style.RESET_ALL +  Fore.LIGHTBLUE_EX + '■■■■■■■■■■' + Style.RESET_ALL
    # ■ Si quiero aplicar un estilo a todos los gráficos, puedo usar plt.style.use('nombre_estilo') 
    # ■ al inicio del programa para establecer un estilo global.
    # plt.style.use('./test.mplstyle')
    menu={  
        "Ej_1. Analisis de Canales de Marketing ■ GRAF: histplot ■ estilos desde archivo": ejercicio_01, 
        "Ej_2. Tráfico Web Semanal ■ GRAF: plot ■ estilo 'context' ": ejercicio_02 , 
        "Ej_3. Calidad en Manufactura ■ GRAF: boxplot (outliers)": ejercicio_03,
        "Ej_4. Optimización de Dataset ■ astype ": ejercicio_04,
        "Ej_5. Educación vs Salario ■ GRAF: scatterplot ■ Compara Categorias": ejercicio_05,
        "Ej_6. Control de Calidad Alimentaria ■ IQR ■ outliers": ejercicio_06,
        "Ej_7. Rendimiento de Exámenes. ■ GRAF: Kde (comparacion notas)": ejercicio_07,
        "Ej_8. Variables Meteorológicas ■ GRAF: heatmap ■ ": ejercicio_08,
        "Ej_9. Precios Inmobiliarios Sesgados ■ GRAF: boxplot ■ outliers": ejercicio_09,
        "Ej_10. Dashboard de Ventas Regional: GRAF: barplot(Barras) - histplot(HIstograma)": ejercicio_10,
        "Ej_11. Tratamiento de Valores Nulos": ejercicio_11,
        "Ej_12. Encoding y Escalado": ejercicio_12,
        "Ej_13. Balance de Clases": ejercicio_13,
        "Ej_14. Pipeline de Pre-Procesamiento": ejercicio_14,
        "◘ EXTRAS": extras,
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
