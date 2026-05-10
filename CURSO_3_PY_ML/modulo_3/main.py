import os           #Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)
from colorama import Fore, Back, Style, init

# █_____________________________________________________█
# █■ ■ ■ ■ ■ ■ ■ ■   FUNCIONES
# █_____________________________________________________█
def ejercicio_01():
    import ejer01
def ejercicio_02():
    import ejer02
def ejercicio_03():
    import ejer03
def ejercicio_04():
    import ejer04
def ejercicio_05():
    import ejer05
def ejercicio_06():
    import ejer06
def ejercicio_07():
    import ejer07
def ejercicio_08():
    import ejer08
def ejercicio_09():
    import ejer09
def ejercicio_10():
    import ejer10

def mis_pruebas():
    # from modulos.info_data import ver_data____ as vd
    import modulos.info_data as I
    from sklearn.datasets import load_breast_cancer
    from sklearn.datasets import load_iris
    
    pass
    # cancer = load_breast_cancer()
    # print('■'*30)
    # I.ver_data(cancer)
    # print('■'*30)
    # I.ver_data__(cancer)
    # print('■'*30)
    # I.ver_data____(cancer)
    # print('■'*30)
    # I.descripcion_dataset(cancer)
    
    pass
    iris = load_iris()
    print('■'*30)
    I.ver_data(iris)
    print('■'*30)
    I.ver_data__(iris)
    print('■'*30)
    I.ver_data____(iris)    
    print('■'*30)
    I.descripcion_dataset(iris)




# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■   MENU PRINCIPAL    ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■█
# █■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■█
def main():
    menu={  
        "Ej_01. 🌷🌷 SVC ■ Ciclo Basico con algoritmo SVM(Categoriás) ■ GRAF: pairplot | displot:": ejercicio_01, 
        "Ej_02. 🌷🌷 Algoritmo Naive Bayes ■ Probabilidad": ejercicio_02 , 
        "Ej_03. 🦀🦀 SVC ■ 'Porcentaje de Aciertos ": ejercicio_03,
        "Ej_04. 🌷🌷 EDA ■ Análisis Discriminante Lineal( LDA ) ■ GRAF: scatter": ejercicio_04,
        "Ej_05. 🦀🦀 EDA ■ Escalado de los Datos ": ejercicio_05,
        "Ej_06. 🦀🦀 SVC ■ Hiper-Parametros ■ Validación Cruzada": ejercicio_06,
        "Ej_07. 🦀🦀 SVC ■ METRICAS ■ GRAF: Matriz de Confusión": ejercicio_07,
        "Ej_08. 🌷🌷 Compara  LDA && Naive Bayes ■ METRICAS": ejercicio_08,
        "Ej_09. 🦀🦀 SVC ■ Hiperparámetros C y gamma ■ GridSearchCV (MultiParametros)": ejercicio_09,
        "Ej_10. 🌷🌷 PipeLine (all in one)": ejercicio_10,
        "Ej_11. PRUEBAS": mis_pruebas,
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
