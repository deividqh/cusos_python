# ************************************************************************************

#------------------------------ EJECUTAR DIRECTAMENTE --------------------------------

#-------------------------- Para ver el menu de ejercicios ---------------------------

#       (Tiene que tener el modulo menuDvd.py en la misma raiz para que funcione.)

# ************************************************************************************

import os           #Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)

# ============================================================================
# =============== PARA LA IMPORTACION DE PAQUETES ==============================
# sirver para ver y añadir un paquete a la lista del sistema. 
# daba fallo pq el directorio raiz de vsc es uno y el directorio creado en vsc es otro, por lo que 
# hay que añadir el directorio raiz del proyecto abierto a la lista del sistema y asi usar las rutas relativas de los paquetes.
# Normalmente esto lo incluye python por defecto, pero si no ocurre de esta forma se puede arreglar.
# Las rutas no se incluyen para siempre, hay que ejecutar este codigo cada vez.
import sys
# Ruta absoluta a la carpeta del proyecto (python-Dvd)
proyecto_ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Añadir la ruta al sys.path
sys.path.append(proyecto_ruta)

# Imprime las rutas del syspath.
# print("Rutas en sys.path:")
# for ruta in sys.path:
#     print(ruta)


from dvd.menuDvd import MenuDvd


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
    # i=MenuDiccionario(menu)
    i=MenuDvd(menu)
    if i==0: break  #PRIMERO LA DE SALIDA
    
    for idx ,ejer in enumerate(menu):
        if i==idx+1:
            os.system('cls')
            menu[ejer]()
