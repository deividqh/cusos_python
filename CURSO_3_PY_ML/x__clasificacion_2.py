from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os
import multiprocessing
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ARCHIVOS DE LOS EJERCICIOS.
from ejercicios_modulo_3 import clase_clasificacion_2 as clase_clasif_2
from ejercicios_modulo_3 import prop_clasificacion_2 as prop_clasif_2

# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■    MENU PRINCIPAL   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    # ■ CREAR ■
    The_X_Men = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    # ■ CONFIGURAR MENUS ■
    TIT_PPAL = "Algoritmos de Clasificacion"
    SUB1 = "De Clase (Copy/Paste)"
    SUB2 = "Ejercicios Propuestos:"

    The_X_Men.addX( titulo=TIT_PPAL, padre=None, ipadre=None, 
                    lst_items=[ (SUB1, None), 
                                (SUB2, None), ])
    
    The_X_Men.addX( titulo='Ejercicios de Clase', padre=TIT_PPAL, ipadre=SUB1, 
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
    
    The_X_Men.addX( titulo='Ejercicios Propuestos Para el Alumno', padre=TIT_PPAL, ipadre=SUB2, 
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
    
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo=TIT_PPAL, head_datapush="ALGORITMOS CLASIFICACION - SUPERVISADO 2ª PARTE", pad_x=3 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()