from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os
import multiprocessing
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ARCHIVOS DE LOS EJERCICIOS.
from ejercicios_modulo_3 import clase_no_supervisado as clase_no_sup
from ejercicios_modulo_3 import prop_no_supervisado as prop_no_sup

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
    
    The_X_Men.addX( titulo='Ejercicios Clase', padre="Menu_Principal", ipadre="De Clase (Copy/Paste) ", 
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
    
    The_X_Men.addX( titulo='Ejercicios Propuestos', padre="Menu_Principal", ipadre="Ejercicios Propuestos: ", 
                    lst_items=[ 
                ('Ej. 01. Segmentación por Edad y Gasto ■ KMeans', prop_no_sup.ejercicio_01), 
                ('Ej. 02. Optimización de K ■ KMeans', prop_no_sup.ejercicio_02), 
                ('Ej. 03. LabelPropagation para predecir etiquetas', prop_no_sup.ejercicio_03), 
                ('Ej. 04. Q-Learning', prop_no_sup.ejercicio_04),
                ('Ej. 05. Actualizacion del Modelo ■ partial_fit', prop_no_sup.ejercicio_05),
                ('Ej. 06. [Iris] ■ Torneo de Clasificadores ■ LazyPredict', prop_no_sup.ejercicio_06),
                ('Ej. 07. Auditoría de Calidad con PyCaret(NO)', prop_no_sup.ejercicio_07),
                ('Ej. 08. El Experimento del Daltónico ■ K-Means', prop_no_sup.ejercicio_08),
                ('Ej. 09. Mantenimiento Predictivo ■ Isolation Forest', prop_no_sup.ejercicio_09),
                ('Ej. 10. Mini-AutoML ■ RegresionL, Árbol de Decisión, SVR', None),                                
                    ])                        
    
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="EJERCICOS ALGORITMOS NO SUPERVISADOS", pad_x=3 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()