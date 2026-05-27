from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os
import multiprocessing
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ARCHIVOS DE LOS EJERCICIOS.
from ejercicios_modulo_3 import clase_clasificacion_1 as clase_clasif_1
from ejercicios_modulo_3 import prop_clasificacion_1 as prop_clasif_1


# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■    MENU PRINCIPAL   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    # ■ CREAR ■
    The_X_Men = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    # ■ CONFIGURAR MENUS ■
    The_X_Men.addX( titulo='Menu_Principal', padre=None, ipadre=None, 
                    lst_items=[ ('De Clase (Copy/Paste) ', None), 
                        ('Ejercicios Propuestos: ', None), ])
    
    The_X_Men.addX( titulo='Ejercicios de Clase', padre="Menu_Principal", ipadre="De Clase (Copy/Paste) ", 
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
    
    The_X_Men.addX( titulo='Ejercicios Propuestos Para el Alumno', padre="Menu_Principal", ipadre="Ejercicios Propuestos: ", 
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
    
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="CURSO MACHINE LEARNING - PYTHON", pad_x=3 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()