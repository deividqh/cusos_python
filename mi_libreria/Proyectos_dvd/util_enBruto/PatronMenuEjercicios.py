# ************************************************************************************

#------------------------------ EJECUTAR DIRECTAMENTE --------------------------------

#-------------------------- Para ver el menu de ejercicios ---------------------------

#       (Tiene que tener el modulo menuDvd.py en la misma raiz para que funcione.)

# ************************************************************************************

import os           #Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)

""" 
Ejercicio 1. 
"""
def ejer01():
    # os.system('cls')
    txtEjer="""Loren Ipsum - Texto del Ejercicio"""

    print ("\nINI..........Ejercicio1 - Diccionarios","\n"+txtEjer)    
    #----- W O R K I N G  P
    #-----
    print ("..........This is The End","\n")

""" 
Ejercicio 2. 
"""
def ejer02():
    # os.system('cls')
    txtEjer="""Loren Ipsum - Texto del Ejercicio"""

    print ("\nINI..........Ejercicio2 - Dicc","\n"+txtEjer)    
    #----- W O R K I N G  P
    #-----
    print ("..........This is The End","\n")


# -----------------------------------------------------------------------------------------------------
# Para añadir ejercicios al menu:   1d2) añadir elemento al diccionario [k]=str(nombreEjer) ; [v]=func sin parentesis '()' 
# -----------------------------------------------------------------------------------------------------
menu={"Ejercicio_1": ejer01, "Ejercicio_2":ejer02 }
while (True):
    i=menuDvd.MenuDiccionario(menu, tituloMenu='Menu de Ejercicios')
    if i==0: break  #PRIMERO LA DE SALIDA
    
    for idx ,ejer in enumerate(menu):
        if i==idx+1:
            os.system('cls')
            menu[ejer]()
