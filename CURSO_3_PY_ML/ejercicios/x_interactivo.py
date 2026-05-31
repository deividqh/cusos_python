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
# LIBRERÍAS DONDE ESTAN LOS EJERCICIOS - IMPORTO LAS FUNCIONES DE LOS EJERCICIOS PARA ASOCIARLAS A LOS ITEMS DEL MENU
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
    # ■■ ■■ ■■ ■■ ■■ ■■                          
    xm1.mystyca( titulo='M1', head_datapush="Ejercicios del Módulo 1: Introducción al Curso", pad_x=3)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# LIBRERÍAS DONDE ESTAN LOS EJERCICIOS - IMPORTO LAS FUNCIONES DE LOS EJERCICIOS PARA ASOCIARLAS A LOS ITEMS DEL MENU
from ejercicios_modulo_2 import main as m2_main
def m2():
    xm2 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm2.addX( titulo='M2', padre=None, ipadre=None, 
            lst_items=[ 
                ('Ej_1. Analisis de Canales Marketing ■ histplot ■ estilos d archivo', m2_main.ejercicio_01) ,
                ('Ej_2. Tráfico Web Semanal ■ GRAF: plot ■ estilo context ', m2_main.ejercicio_02) , 
                ('Ej_3. Calidad en Manufactura ■ GRAF: boxplot (outliers)', m2_main.ejercicio_03) , 
                ('Ej_4. Optimización de Dataset ■ astype ', m2_main.ejercicio_04) ,
                ('Ej_5. Educación vs Salario ■ GRAF: scatterplot ■ Compara Categorias', m2_main.ejercicio_05) ,
                ('Ej_6. Control de Calidad Alimentaria ■ IQR ■ outliers', m2_main.ejercicio_06),
                ('Ej_7. Rendimiento de Exámenes. ■ GRAF: Kde (comparacion notas)', m2_main.ejercicio_07),
                ('Ej_8. Variables Meteorológicas ■ GRAF: heatmap ■', m2_main.ejercicio_08),
                ('Ej_9. Precios Inmobiliarios Sesgados ■ GRAF: boxplot ■ outliers', m2_main.ejercicio_09),
                ('Ej_10. Dashboard de Ventas Regional: ■ barplot-histplot', m2_main.ejercicio_10),
        ])
    # ■■ ■■ ■■ ■■ ■■ ■■  
    xm2.mystyca( titulo='M2', head_datapush="Ejercicios del Módulo 2: Exploración del Conjunto de Datos(EDA)", pad_x=3 )
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# LIBRERÍAS DONDE ESTAN LOS EJERCICIOS - IMPORTO LAS FUNCIONES DE LOS EJERCICIOS PARA ASOCIARLAS A LOS ITEMS DEL MENU
from ejercicios_modulo_3 import clase_clasificacion_1 as clase_clasif_1
from ejercicios_modulo_3 import prop_clasificacion_1 as prop_clasif_1

from ejercicios_modulo_3 import clase_clasificacion_2 as clase_clasif_2
from ejercicios_modulo_3 import prop_clasificacion_2 as prop_clasif_2

from ejercicios_modulo_3 import clase_regresion as clase_reg
from ejercicios_modulo_3 import prop_regresion as prop_reg

from ejercicios_modulo_3 import clase_no_supervisado as clase_no_sup
from ejercicios_modulo_3 import prop_no_supervisado as prop_no_sup


def m3():
    xm3 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm3.addX( titulo='M3', padre=None, ipadre=None, 
            lst_items=[ 
                ('• CLASE - Clasificación - Supervisado - parte1', None), 
                ('• PROPUESTO - Clasificación - Supervisado - parte1', None), 
                ('• CLASE - Clasificación - Supervisado - parte2', None), 
                ('• PROPUESTO - Clasificación - Supervisado - parte2', None), 
                ('• CLASE - Supervisado - Regresión', None), 
                ('• PROPUESTO - Supervisado - REGRESION', None), 
                ('• CLASE - NO SUPERVISADO', None), 
                ('• PROPUESTO - NO SUPERVISADO', None), 
            ])

    xm3.addX( titulo='CLASIFICACION (CLASE) - 1:', padre='M3', ipadre='• CLASE - Clasificación - Supervisado - parte1', 
            lst_items=[ 
                ('EJ_01. SVC ■ Ciclo Basico  SVM(Categoriás) ■ pairplot | displot:', clase_clasif_1.ejercicio_01),  
                ('EJ_02. (iris) ■ Algoritmo Naive Bayes ■ Probabilidad', clase_clasif_1.ejercicio_02), 
                ('Ej_03. (cancer) ■ SVC ■ Porcentaje de Aciertos', clase_clasif_1.ejercicio_03), 
                ('Ej_04. (iris) ■ EDA ■ Análisis Discriminante Lineal( LDA ) ■ scatterplot', clase_clasif_1.ejercicio_04),
                ('Ej_05. (cancer) ■ EDA ■ Escalado de los Datos', clase_clasif_1.ejercicio_05),
                ('Ej_06. (cancer) ■ SVC ■ Hiper-Parametros ■ Validación Cruzada', clase_clasif_1.ejercicio_06),
                ('Ej_07. (cancer) ■ SVC ■ METRICAS ■ GRAF: Matriz de Confusión', clase_clasif_1.ejercicio_07),
                ('Ej_08. (iris) ■ Compara  LDA && Naive Bayes ■ METRICAS', clase_clasif_1.ejercicio_08),
                ('Ej_09. (cancer) ■ SVC ■ Hiperparám C y gamma ■ GridSearchCV (MultiParam)', clase_clasif_1.ejercicio_09),
                ('Ej_10. (iris) ■ PipeLine (all in one)', clase_clasif_1.ejercicio_10),                                
            ])
                        
    xm3.addX( titulo='CLASIFICACION (CLASE) - 2:', padre='M3', ipadre='• CLASE - Clasificación - Supervisado - parte2', 
            lst_items=[ 
                ('Ej_01. PCA: Reducción de Dimensionalidad', clase_clasif_2.ejercicio_01), 
                ("Ej_02. K-Nearest Neighbors (KNN): Clasificación Espacial ", clase_clasif_2.ejercicio_02), 
                ("Ej_03. Árboles de Decisión: Interpretación de Reglas", clase_clasif_2.ejercicio_03), 
                ("Ej_04. Bosque Aleatorio (Random Forest): Ensambles", clase_clasif_2.ejercicio_04),
                ("Ej_05. Redes Neuronales: Perceptrón Multicapa (MLP)", clase_clasif_2.ejercicio_05),
                ("Ej_06. PCA + KNN: Impacto de la Reducción", clase_clasif_2.ejercicio_06),
                ("Ej_07. Importancia de Características (Feature Importance)", clase_clasif_2.ejercicio_07),
                ("Ej_08. Ejercicio 8 - Optimización Hiperparámetros en Árboles", clase_clasif_2.ejercicio_08),
                ("Ej_09. Comparativa Maestra de Modelos", clase_clasif_2.ejercicio_09),
                ("Ej_10. Creación de un Clasificador Inteligente (Ensemble)", clase_clasif_2.ejercicio_10),                                
            ])
    xm3.addX( titulo='REGRESION (CLASE):', padre='M3', ipadre='• CLASE - Supervisado - Regresión', 
            lst_items=[ 
                ('Ej 1 - Regresión Lineal Simple (Scikit-Learn)', clase_reg.ejer_1), 
                ('Ej 2 - Regresión Lineal con Statsmodels', clase_reg.ejer_2), 
                ('Ej 3 - Ajuste de Mínimos Cuadrados (Fundamentos)', clase_reg.ejer_3), 
                ('Ej 4 - Regresión Lineal Múltiple', clase_reg.ejer_4),
                ('Ej 5 - Tratamiento de Variables Categóricas en Regresión', clase_reg.ejer_5),
                ('Ej 6 - Regresión Polinomial', clase_reg.ejer_6),
                ('Ej 7 - Análisis de Complejidad y Sobreajuste (Overfitting)', clase_reg.ejer_7),
                ('Ej 8 - Regresión Logística (Introducción)', clase_reg.ejer_8),
                ('Ej 9 - Evaluación de Regresión Logística', clase_reg.ejer_9),
                ('Ej 10 - Creación de un Pipeline de Regresión Completo', clase_reg.ejer_10),                                
            ])

    xm3.addX( titulo='CLASIFICACION - PROPUESTO - 1:', padre='M3', ipadre='• PROPUESTO - Clasificación - Supervisado - parte1', 
            lst_items=[ 
                ('Ej_01. (iris) ■ SVC ■ Cambio de Kernell ', prop_clasif_1.ejercicio_01), 
                ('Ej_02. (iris) ■  Naive Bayes ■ Probabilidad certeza', prop_clasif_1.ejercicio_02), 
                ('Ej_03. (cancer) ■ SVC ■ Matriz confusion ■ Accuracy', prop_clasif_1.ejercicio_03), 
                ('Ej_04. (iris) ■ EDA ■ Kneighbors(KNN) ■ Reducir Dimension(LDA) ■ scatter', prop_clasif_1.ejercicio_04),
                ('Ej_05. (cancer) ■ EDA ■ Escalado Datos, MinScaler vs StandarScaler', prop_clasif_1.ejercicio_05),
                ('Ej_06. (cancer) ■ SVC ■ Cross Valid Estratified(StratifiedKFold)', prop_clasif_1.ejercicio_06),
                ('Ej_07. (cancer) ■ SVC ■ METRICAS ■ GRAF: Matriz de Confusión', prop_clasif_1.ejercicio_07),
                ('Ej_08. (iris) ■ Compara  LDA && Naive Bayes ■ METRICAS', prop_clasif_1.ejercicio_08),
                ('Ej_09. (cancer) ■ SVC ■ Hiperparámetros C y gamma ■ GridSearchCV ', prop_clasif_1.ejercicio_09),
                ('Ej_10. (iris) ■  PipeLine (all in one)', prop_clasif_1.ejercicio_10),                                
            ])

    xm3.addX( titulo='CLASIFICACION - PROPUESTO - 2:', padre='M3', ipadre='• PROPUESTO - Clasificación - Supervisado - parte2', 
            lst_items=[ 
                ('Ej. (circles) ■ El Misterio de los Kernels', prop_clasif_2.ejercicio_01), 
                ('Ej. (custom) ■ Clasificador de Spam (Naive Bayes)', prop_clasif_2.ejercicio_02), 
                ('Ej. (digits) ■ Reducción de Ruido con PCA', prop_clasif_2.ejercicio_03), 
                ('Ej. (iris) ■  Búsqueda del Vecino Óptimo', prop_clasif_2.ejercicio_04),
                ('Ej. (cancer) ■ Poda de Árboles (Pruning)', prop_clasif_2.ejercicio_05),
                ('Ej. (cancer) ■ Estabilidad del Bosque', prop_clasif_2.ejercicio_06),
                ('Ej. (custom) Visualización Comparativa (LDA vs PCA)', prop_clasif_2.ejercicio_07),
                ('Ej. (custom) Arquitectura de Neuronas  "', prop_clasif_2.ejercicio_08),
                ('Ej. (custom) ■ Análisis de Falsos Alarmas', prop_clasif_2.ejercicio_09),
                ('Ej. (custom) Proyecto Integrador: Scoring Bancario', prop_clasif_2.ejercicio_10),                                
            ])

    xm3.addX( titulo='PROPUESTO - REGRESION:', padre='M3', ipadre='• PROPUESTO - Supervisado - REGRESION', 
            lst_items=[ 
                ('Ej.01. Rendimiento Académico - Regresión Lineal Simple ', None), 
                ('Ej.02. Satisfacción Laboral ■ Statsmodels ■ p-valor ', None), 
                ('Ej.03. El Algoritmo desde Cero ', None), 
                ('Ej.04. Tasación de Vehículos ■  Regresión Múltiple ', None),
                ('Ej.05. Eficiencia Energética con Categorías ■ One-Hot Encoding ', None),
                ('Ej.06. Trayectoria de Mercado ■ Regresión Polinomial ', None),
                ('Ej.07. Prevención del Overfitting ■ Regresión Polinomial ', None),
                ('Ej.08. Diagnóstico Médico ■ Regresión Logística ', None),
                ('Ej.09. Auditoría Fraude ■ Matriz de Confusión ■ reporte declasificación ', None),
                ('Ej.10. (PROYECTO FINAL) Desarrolla un Pipeline Completo', None),                                
            ])
    
    xm3.addX( titulo='CALSE - NO SUPERVISADO:', padre='M3', ipadre='• CLASE - NO SUPERVISADO', 
            lst_items=[ 
                ('Ej. 01. - Agrupamiento con K-Means', clase_no_sup.ejercicio_01), 
                ('Ej. 02. - El Método del Codo (Elbow Method)', clase_no_sup.ejercicio_02), 
                ('Ej. 03. - Aprendizaje Semisupervisado (Label Propagation)', clase_no_sup.ejercicio_03), 
                ('Ej. 04. - Aprendizaje por Refuerzo (Q-Learning básico)', clase_no_sup.ejercicio_04),
                ('Ej. 05. - Aprendizaje en Continuo (Incremental Learning)', clase_no_sup.ejercicio_05),
                ('Ej. 06. - Comparativa Instantánea con LazyPredict', clase_no_sup.ejercicio_06),
                ('Ej. 07. - Low-Code ML con PyCaret', clase_no_sup.ejercicio_07),
                ('Ej. 08. - Comparación: Supervisado vs No Supervisado', clase_no_sup.ejercicio_08),
                ('Ej. 09. - Detección de Anomalías (Isolation Forest)', clase_no_sup.ejercicio_09),
                ('Ej. 10. - Creación de un Pipeline de AutoML Integral', clase_no_sup.ejercicio_10),                                
            ])
    xm3.addX( titulo='PROPUESTO - NO SUPERVISADO:', padre='M3', ipadre='• PROPUESTO - NO SUPERVISADO', 
            lst_items=[ 
                ('Ej. 01. Segmentación por Edad y Gasto ■ KMeans', prop_no_sup.ejercicio_01), 
                ('Ej. 02. Optimización de K ■ KMeans', prop_no_sup.ejercicio_02), 
                ('Ej. 03. LabelPropagation para predecir etiquetas', prop_no_sup.ejercicio_03), 
                ('Ej. 04. Q-Learning', prop_no_sup.ejercicio_04),
                ('Ej. 05. Actualizacion del Modelo ■ partial_fit', None),
                ('Ej. 06. [Iris] ■ Torneo de Clasificadores ■ LazyPredict', None),
                ('Ej. 07. Auditoría de Calidad con PyCaret(NO)', None),
                ('Ej. 08. El Experimento del Daltónico ■ K-Means', None),
                ('Ej. 09. Mantenimiento Predictivo ■ Isolation Forest', None),
                ('Ej. 10. Mini-AutoML ■ RegresionL, Árbol de Decisión, SVR', None),                                
            ])

    # ■■ ■■ ■■ ■■ ■■ ■■  
    xm3.mystyca( titulo='M3', head_datapush="Ejercicios del Módulo 3: Algoritmos de Machine Learning", pad_x=3 )

def m4():
    xm4 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm4.addX( titulo='M4', padre=None, ipadre=None, 
            lst_items=[ 
                ('ejemplo 1 para reemplazar', None), 
                ('ejemplo 2 para reemplazar', None), 
            ])
    xm4.mystyca( titulo='M4', head_datapush="Ejercicios del Módulo 4: Redes Neuronales", pad_x=3 )


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
                        ('Modulo 4. Redes Neuronales', m4), 
                    ])
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="CURSO MACHINE-LEARNING & DEEP-LEARNING - PYTHON", pad_x=3 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()