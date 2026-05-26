from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os
import multiprocessing
import tkinter as tk
from tkinter import ttk
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from ui_tk.pestanas_dicc import StepByStab      # Pestañas con diccionario de datos para mostrar en cada pestaña
from Pruebas_Forms.Row_Form import Nivel_2      # Dibujar formularios Tkinter
import comandos_ui_tk as cmd                    # (Opt) Acciones de los widgets y separar el menú de la lógica.
from XindeX import menuDvd          # Menu con diccionario de datos para mostrar en cada item

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from ejercicios_modulo_1.tarea5 import calcula_pendiente as tarea5
from ejercicios_modulo_1.conversorHTML import convertir_html
from ejercicios_modulo_1.tarea6 import tarea6
from ejercicios_modulo_1.tarea7 import tarea7
def m1():
    xm1 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm1.addX( titulo='M1', padre=None, ipadre=None, 
                    lst_items=[ ('Tarea 5: Calcula la pendiente de una curva', tarea5), 
                                ('convertir ipynb a html', convertir_html), 
                                ('tarea6', tarea6), 
                    ])
                        
    xm1.mystyca( titulo='M1', head_datapush="Ejercicios del Módulo 1: Introducción al Curso", pad_x=30)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from ejercicios_modulo_2 import main as m2_main
def m2():
    xm2 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm2.addX( titulo='M2', padre=None, ipadre=None, 
            lst_items=[ 
                ('Ej_1. Analisis de Canales de Marketing ■ GRAF: histplot ■ estilos desde archivo', m2_main.ejercicio_01) ,
                ('Ej_2. Tráfico Web Semanal ■ GRAF: plot ■ estilo context ', m2_main.ejercicio_02) , 
                ('Ej_3. Calidad en Manufactura ■ GRAF: boxplot (outliers)', m2_main.ejercicio_03) , 
                ('Ej_4. Optimización de Dataset ■ astype ', m2_main.ejercicio_04) ,
                ('Ej_5. Educación vs Salario ■ GRAF: scatterplot ■ Compara Categorias', m2_main.ejercicio_05) ,
                ('Ej_6. Control de Calidad Alimentaria ■ IQR ■ outliers', m2_main.ejercicio_06),
                ('Ej_7. Rendimiento de Exámenes. ■ GRAF: Kde (comparacion notas)', m2_main.ejercicio_07),
                ('Ej_8. Variables Meteorológicas ■ GRAF: heatmap ■', m2_main.ejercicio_08),
                ('Ej_9. Precios Inmobiliarios Sesgados ■ GRAF: boxplot ■ outliers', m2_main.ejercicio_09),
                ('Ej_10. Dashboard de Ventas Regional: GRAF: barplot(Barras) - histplot(HIstograma)', m2_main.ejercicio_10),
        ])
    xm2.mystyca( titulo='M2', head_datapush="Ejercicios del Módulo 2: Exploración del Conjunto de Datos(EDA)", pad_x=10 )
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# LIBRERÍAS DONDE ESTAN LOS EJERCICIOS - IMPORTO LAS FUNCIONES DE LOS EJERCICIOS PARA ASOCIARLAS A LOS ITEMS DEL MENU
from ejercicios_modulo_3 import ejercicios_propuestos_parte1 as prop1
from ejercicios_modulo_3 import ejercicios_propuestos_parte2 as prop2
from ejercicios_modulo_3 import modulo_3_clase_parte1 as clp1
from ejercicios_modulo_3 import modulo_3_clase_regresion as clr
from ejercicios_modulo_3 import modulo_3_clase_parte2 as clp2

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def m3():
    xm3 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm3.addX( titulo='M3', padre=None, ipadre=None, 
            lst_items=[ 
                ('CLASE - Clasificación - Supervisado - parte1', None), 
                ('CLASE - Clasificación - Supervisado - parte2', None), 
                ('CLASE - Regresión', None), 
                ('PROPUESTO - Clasificación - Supervisado - parte1', None), 
                ('PROPUESTO - Clasificación - Supervisado - parte2', None), 
                ('PROPUESTO - REGRESION', None), 
            ])

    xm3.addX( titulo='CLASIFICACION (CLASE) - 1:', padre='M3', ipadre='CLASE - Clasificación - Supervisado - parte1', 
            lst_items=[ 
                ('EJ_01. SVC ■ Ciclo Basico con algoritmo SVM(Categoriás) ■ GRAF: pairplot | displot:', clp1.ejercicio_01),  
                ('EJ_02. (iris) ■ Algoritmo Naive Bayes ■ Probabilidad', clp1.ejercicio_02), 
                ('Ej_03. (cancer) ■ SVC ■ Porcentaje de Aciertos', clp1.ejercicio_03), 
                ('Ej_04. (iris) ■ EDA ■ Análisis Discriminante Lineal( LDA ) ■ GRAF: scatter', clp1.ejercicio_04),
                ('Ej_05. (cancer) ■ EDA ■ Escalado de los Datos', clp1.ejercicio_05),
                ('Ej_06. (cancer) ■ SVC ■ Hiper-Parametros ■ Validación Cruzada', clp1.ejercicio_06),
                ('Ej_07. (cancer) ■ SVC ■ METRICAS ■ GRAF: Matriz de Confusión', clp1.ejercicio_07),
                ('Ej_08. (iris) ■ Compara  LDA && Naive Bayes ■ METRICAS', clp1.ejercicio_08),
                ('Ej_09. (cancer) ■ SVC ■ Hiperparámetros C y gamma ■ GridSearchCV (MultiParametros)', clp1.ejercicio_09),
                ('Ej_10. (iris) ■ PipeLine (all in one)', clp1.ejercicio_10),                                
            ])
                        
    xm3.addX( titulo='CLASIFICACION (CLASE) - 2:', padre='M3', ipadre='CLASE - Clasificación - Supervisado - parte2', 
            lst_items=[ 
                # ('Ej_01. PCA: Reducción de Dimensionalidad', m3_cl_p2_ej1), 
                ('Ej_01. PCA: Reducción de Dimensionalidad', clp2.ejercicio_01), 
                ("Ej_02. K-Nearest Neighbors (KNN): Clasificación Espacial ", clp2.ejercicio_02), 
                ("Ej_03. Árboles de Decisión: Interpretación de Reglas", clp2.ejercicio_03), 
                ("Ej_04. Bosque Aleatorio (Random Forest): Ensambles", clp2.ejercicio_04),
                ("Ej_05. Redes Neuronales: Perceptrón Multicapa (MLP)", clp2.ejercicio_05),
                ("Ej_06. PCA + KNN: Impacto de la Reducción", clp2.ejercicio_06),
                ("Ej_07. Importancia de Características (Feature Importance)", clp2.ejercicio_07),
                ("Ej_08. Ejercicio 8 - Optimización de Hiperparámetros en Árboles", clp2.ejercicio_08),
                ("Ej_09. Comparativa Maestra de Modelos", clp2.ejercicio_09),
                ("Ej_10. Creación de un Clasificador Inteligente (Ensemble)", clp2.ejercicio_10),                                
            ])
    xm3.addX( titulo='REGRESION (CLASE):', padre='M3', ipadre='CLASE - Regresión', 
            lst_items=[ 
                ('Ejercicio 1 - Regresión Lineal Simple (Scikit-Learn)', clr.ejer_1), 
                ('Ejercicio 2 - Regresión Lineal con Statsmodels', clr.ejer_2), 
                ('Ejercicio 3 - Ajuste de Mínimos Cuadrados (Fundamentos)', clr.ejer_3), 
                ('Ejercicio 4 - Regresión Lineal Múltiple', clr.ejer_4),
                ('Ejercicio 5 - Tratamiento de Variables Categóricas en Regresión', clr.ejer_5),
                ('Ejercicio 6 - Regresión Polinomial', clr.ejer_6),
                ('Ejercicio 7 - Análisis de Complejidad y Sobreajuste (Overfitting)', clr.ejer_7),
                ('Ejercicio 8 - Regresión Logística (Introducción)', clr.ejer_8),
                ('Ejercicio 9 - Evaluación de Regresión Logística', clr.ejer_9),
                ('Ejercicio 10 - Creación de un Pipeline de Regresión Completo', clr.ejer_10),                                
            ])

    xm3.addX( titulo='CLASIFICACION - PROPUESTO - 1:', padre='M3', ipadre='PROPUESTO - Clasificación - Supervisado - parte1', 
            lst_items=[ 
                ('Ej_01. (iris) ■ SVC ■ Cambio de Kernell ', prop1.ejercicio_01), 
                ('Ej_02. (iris) ■  Naive Bayes ■ Probabilidad certeza', prop1.ejercicio_02), 
                ('Ej_03. (cancer) ■ SVC ■ Matriz confusion ■ Accuracy', prop1.ejercicio_03), 
                ('Ej_04. (iris) ■ EDA ■ Kneighbors(KNN) ■ Reducir Dimensiones ( LDA ) ■ GRAF: scatter', prop1.ejercicio_04),
                ('Ej_05. (cancer) ■ EDA ■ Escalado de los Datos, MinScaler vs StandarScaler', prop1.ejercicio_05),
                ('Ej_06. (cancer) ■ SVC ■ Validación Cruzada Estratificada(StratifiedKFold) && Desviación standar', prop1.ejercicio_06),
                ('Ej_07. (cancer) ■ SVC ■ METRICAS ■ GRAF: Matriz de Confusión', prop1.ejercicio_07),
                ('Ej_08. (iris) ■ Compara  LDA && Naive Bayes ■ METRICAS', prop1.ejercicio_08),
                ('Ej_09. (cancer) ■ SVC ■ Hiperparámetros C y gamma ■ GridSearchCV (MultiParametros)', prop1.ejercicio_09),
                ('Ej_10. (iris) ■  PipeLine (all in one)', prop1.ejercicio_10),                                
            ])

    xm3.addX( titulo='CLASIFICACION - PROPUESTO - 2:', padre='M3', ipadre='PROPUESTO - Clasificación - Supervisado - parte2', 
            lst_items=[ 
                ('Ejercicio_01. (circles) ■ El Misterio de los Kernels', prop2.ejercicio_01), 
                ('Ejercicio_02. (custom) ■ Clasificador de Spam (Naive Bayes)', prop2.ejercicio_02), 
                ('Ejercicio_03. (digits) ■ Reducción de Ruido con PCA', prop2.ejercicio_03), 
                ('Ejercicio_04. (iris) ■  Búsqueda del Vecino Óptimo', prop2.ejercicio_04),
                ('Ejercicio_05. (cancer) ■ Poda de Árboles (Pruning)', prop2.ejercicio_05),
                ('Ejercicio_06. (cancer) ■ Estabilidad del Bosque', prop2.ejercicio_06),
                ('Ejercicio_07. (custom) Visualización Comparativa (LDA vs PCA)', prop2.ejercicio_07),
                ('Ejercicio_08. Arquitectura de Neuronas  "', prop2.ejercicio_08),
                ('Ejercicio_09. (custom) ■ Análisis de Falsos Alarmas', prop2.ejercicio_09),
                ('Ejercicio_10. Proyecto Integrador: Scoring Bancario', prop2.ejercicio_10),                                
            ])


    xm3.addX( titulo='PROPUESTO - REGRESION:', padre='M3', ipadre='PROPUESTO - REGRESION', 
            lst_items=[ 
                ('Ejercicio_01. ', None), 
                ('Ejercicio_02. ', None), 
                ('Ejercicio_03. ', None), 
                ('Ejercicio_04. ', None),
                ('Ejercicio_05. ', None),
                ('Ejercicio_06. ', None),
                ('Ejercicio_07. ', None),
                ('Ejercicio_08. ', None),
                ('Ejercicio_09. ', None),
                ('Ejercicio_10. ', None),                                
            ])


    # ■■ ■■ ■■ ■■ ■■ ■■  
    xm3.mystyca( titulo='M3', head_datapush="Ejercicios del Módulo 3: Algoritmos de Machine Learning", pad_x=10 )

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■    MENU PRINCIPAL   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    # ■ CREAR ■
    The_X_Men = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True)
    # ■ CONFIGURAR MENUS ■
    The_X_Men.addX( titulo='Menu_Principal', padre=None, ipadre=None, 
                    lst_items=[ 
                        ('Modulo 1. Introducción al Curso', m1), 
                        ('Modulo 2. Exploración del Conjunto de Datos(EDA)', m2), 
                        ('Modulo 3. Algoritmos de Machine Learning', m3), 
                        ('Modulo 4. Redes Neuronales', None), 
                    ])
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="CURSO MACHINE LEARNING - PYTHON", pad_x=5 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()