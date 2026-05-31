from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os
import multiprocessing
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ARCHIVOS DE LOS EJERCICIOS.
from ejercicios_modulo_3 import clase_regresion as clase_reg
from ejercicios_modulo_3 import prop_regresion as prop_reg

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
                        ('Ejercicios Propuestos: ', prop_reg.regresion_all), ])
    
    The_X_Men.addX( titulo='Ejercicios Resueltos', padre="Menu_Principal", ipadre="De Clase (Copy/Paste) ", 
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
    
    The_X_Men.addX( titulo='Ejercicios Propuestos', padre="Menu_Principal", ipadre="Ejercicios Propuestos: ", 
                    lst_items=[ 
                        ('Ej.01. Rendimiento Académico - Regresión Lineal Simple ', prop_reg.ejercicio_01), 
                        ('Ej.02. Satisfacción Laboral ■ Statsmodels ■ p-valor ', prop_reg.ejercicio_02), 
                        ('Ej.03. El Algoritmo desde Cero ', prop_reg.ejercicio_03), 
                        ('Ej.04. Tasación de Vehículos ■  Regresión Múltiple ', prop_reg.ejercicio_04),
                        ('Ej.05. Eficiencia Energética con Categorías ■ One-Hot Encoding ', prop_reg.ejercicio_05),
                        ('Ej.06. Trayectoria de Mercado ■ Regresión Polinomial ', prop_reg.ejercicio_06),
                        ('Ej.07. Prevención del Overfitting ■ Regresión Polinomial ', prop_reg.ejercicio_07),
                        ('Ej.08. Diagnóstico Médico ■ Regresión Logística ', prop_reg.ejercicio_08),
                        ('Ej.09. Auditoría Fraude ■ Matriz de Confusión ■ reporte declasificación ', prop_reg.ejercicio_09),
                        ('Ej.10. (PROYECTO FINAL) Desarrolla un Pipeline Completo', prop_reg.ejercicio_10),
                    ])                        
    
    # ■ LANZAR ■
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="EJERCICOS ALGORITMOS DE REGRESIÓN", pad_x=3 )
    # ■ DESPEDIDA ■
    print('Bye Bye')

# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
# ██████■■■■██████████████████ █ █ █ █ █ █ ██████████████████■■■■██████
if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()