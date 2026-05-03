# Ejercicios Listas

import os           #Para Limpiar la terminal con  os.system('cls') 

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
print("Rutas en sys.path:")
for ruta in sys.path:
    print(ruta)



""" Ejercicio 1.
"""
# Genero la lista  en la ejecución (abajo)....
def listas_01A(lista):    
    os.system('cls')
    print ("\nINI..........Ejercicio1 - LISTAS","\n"+
""" 
A. Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla. """)
    print("\nResultado A):\t", lista)
    print ("\n..........This is The End","\n") 

# Yo estudio....
def listas_01B(lista):
    os.system('cls')
    print ("\nINI..........Ejercicio1 - LISTAS","\n",
""" 
B. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las
asignaturas de la lista.""")

    print("\nResultado B):\t", lista)
    for idx in lista:
        print("Yo estudio ",idx)
    print ("\n..........This is The End","\n") 

# ----------------------------------------------------------

def listas_01C(lista):    
    os.system('cls')
    txtEjer=""" 
C. Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física, Química, Historia y Lengua) en una lista:
    1- pregunte al usuario la nota que ha sacado en cada asignatura, 
    2- Las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
       asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""
    
    print ("\nINI..........Ejercicio1 - LISTAS\n",txtEjer)

    print("\nResultado C):\t", lista)
    
    # for asig in range(len(lista)):
    #     num=abs(float(input(f"Intro Nota de {lista[asig]} ........")))
    #     lista[asig]=[lista[asig], num]

    lista=setAsignaturasNotas(lista)        #Me devuelve una lista de [Asignatura, nota]+
    print("\nResultado")
    for n in lista:
        print(f" En {n[0]} has sacado un  {n[1]} ", ":(" if int(n[1])<5 else " ;) ")

    print ("\n..........This is The End","\n") 

def listas_01D(lista):
    os.system('cls')    
    txtEjer="""
D. Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    1-Pregunte al usuario la nota que ha sacado en cada asignatura y 
    2-Elimine de la lista las asignaturas aprobadas.
    3-Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""
    print ("\nINI..........Ejercicio1 - LISTAS\n",txtEjer)
    
    print("D)\t", lista)
    nLista=[]    
    lista=setAsignaturasNotas(lista)     #Me devuelve una lista de [Asignatura, nota]+    
    if len(lista)!=0:
        for n in lista:
            if float(n[1]) < 5.0:
                nLista.append(n)
        print("\nResultado", end=": ")
        print(nLista)
    print ("\n..........This is The End","\n") 


# @lista,  list() con las asignaturas ["Fisica", "Quimica",...]
# @return,  Me devuelve la lista de entrada pero modificada -> [Asignatura, nota]+  (Debe de pasar xReferencia)
def setAsignaturasNotas(lista):
    for asig in range(len(lista)):
        num=abs(float(input(f"Intro Nota de {lista[asig]} ........")))
        lista[asig]=[lista[asig], num]
    return lista
# --------------------------------------------------------------------------


# --------- E J E C U C I O N      A B A J O ------------------------

"""  
Ejercicio 2. 
"""
def ejer02():
    os.system('cls')
    txtEjer=""" 
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva:
    1-los almacene en una lista y 
    2-los muestre por pantalla ordenados de menor a mayor. """
    print ("\nINI..........Ejercicio2 - LISTAS","\n"+txtEjer)
    
    nGANADORES=6
    lista=[]
    #----- W O R K I N G  P R O C E D U R E
    for n in range(nGANADORES):
        num=abs(int(input("Intro Num Ganador Bolita Loteria ........")))
        lista.append(num)
    lista.sort()                # .sort() ordena la lista y devuelve None, ergo NO se puede hacer print(lista.sort()) 
    # print(lista)
    print(f"\nResultado: {lista}")
    #-----
    print ("..........This is The End","\n")
# --------- E J E C U C I O N      A B A J O ------------------------


""" 
Ejercicio 3. 
"""
def ejer03():
    os.system('cls')
    txtEjer="""
Escribir un programa que almacene en una lista con 10 números y los ordene de mayor a menor."""
    print ("\nINI..........Ejercicio3 - LISTAS","\n"+txtEjer)
    
    lista=[0,1,8,3,4,5,6,7,2,9]
    print(f"\nBefore sort: {lista}")    
    #----- 
    lista.sort(reverse=True)    # .sort() ordena la lista y devuelve None, ergo NO se puede print(lista.sort()) 
    print(f"\nAfter sort: {lista}" )
    #-----
    print ("..........This is The End","\n")
# --------- E J E C U C I O N      A B A J O ------------------------

""" 
Ejercicio 4.  
"""
def ejer04():
    os.system('cls')
    
    txtEjer=""" 
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8 
    1- Muestre por pantalla el menor y el mayor de los precios. """    
    print ("\nINI..........Ejercicio4 - LISTAS","\n", txtEjer)

    lista=[50, 75, 46, 22, 80, 65, 8]
    #----- W O R K I N G  P R O C E D U R E
    print(f"\nLista: {lista}")
    print("\nMenor: ",min(lista))
    print("Mayor: ",max(lista))
    #-----
    print ("\n..........This is The End","\n")

# --------- E J E C U C I O N      A B A J O ------------------------


#---------------------------------------------------- Listas anidadas 
# Ejercicio 5.  
def ejer05():
    os.system('cls')

    txtEjer=""" 
A. Crear una matriz de 3x3 utilizando listas anidadas y mostrarlo por pantalla.
B. Acceder al elemento 1,2 de la matriz y mostrarlo por pantalla. 
C. Imprimir todos los elementos de una lista anidada.     """
    print ("\nINI..........Ejercicio5 - LISTAS","\n", txtEjer)
    
    #----- W O R K I N G  P R O C E D U R E
    fila1=[5, 7, 4]
    fila2=[50, 70, 40]
    fila3=[500, 700, 400]
    
    tabla=[fila1,fila2,fila3]
    print(tabla)

    print(f"Elemento(1,2)={tabla[1][2]}")
    #-----
    print ("..........This is The End","\n")

# --------- E J E C U C I O N      A B A J O ------------------------

# Ejercicio 6. 
def ejer06():
    os.system('cls')
    txtEjer=""" 
Dada esta lista: calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]. 
    1-Calcula la nota media de cada alumno y muéstrala por pantalla."""
    print ("\nINI..........Ejercicio6 - LISTAS","\n",txtEjer)

    calificaciones = [[8, 7, 9], [6, 5, 8], [10, 9, 10]]
    #----- W O R K I N G  P R O C E D U R E
    # for notasAsig in calificaciones:
    #     print(f"Media Alumno {round(sum(notasAsig)/len(notasAsig),1)}")
    """ 
    Alternativa con el indice
    """
    for i, notasAsig in enumerate(calificaciones):
        media = round(sum(notasAsig) / len(notasAsig), 1)
        print(f"Media Alumno {i}: {media}")

    #-----
    print ("\n..........This is The End","\n")

# --------- E J E C U C I O N      A B A J O ------------------------

# ------------------------------------------Listas de comprensión 
# Ejercicio 7. 
def ejer07():
    os.system('cls')
    txtEjer=""" 
Crear una lista con los primeros 10 números pares.
"""
    print ("\nINI..........Ejercicio7 - LISTAS","\n",txtEjer)
    lista=[]        
    #----- W O R K I N G  P R O C E D U R E
    for i in range(1,10+1):
        lista.append(i*2)
    
    print(lista)
    
    """ Alternativa """
    for i, num in enumerate(lista):
        print(f"item {i} = {num} ", sep=")")        #   ;) sep NO funciona con f''

    #-----
    print ("..........This is The End","\n")

# --------- E J E C U C I O N    A B A J O ------------------------

#  Ejercicio 8. 
def ejer08():
    os.system('cls')
    txtEjer=""" 
Crear una lista con las primeras letras de una está lista: palabras = ["manzana", "banana", "cereza"] """

    print ("\nINI..........Ejercicio8 - LISTAS","\n",txtEjer)
    palabras = ["manzana", "banana", "cereza"]
    lista=[]    
    #----- W O R K I N G
    for p in palabras:
        lista.append(p[:1])
    
    print(f"Lista de Palabras: {palabras}")
    print(f"Lista de Primeras Letras: {lista}")
    #-----
    print ("..........This is The End","\n")


# --------- E J E C U C I O N  ------------------------

# Ctrl + ñ -> ir a la Terminal.


# listas_01A(lista)         # Crear/Imprimir Lista 
# listas_01B(lista)         # Recorrer Lista 
# listas_01C(lista)         # Reasignacion/Modificacion de Listas 
# listas_01D(lista)           # Crear a partir de otras y Modificar Listas.
# ejer02()
# ejer03()
# ejer04()
# ejer05()
# ejer06()
# ejer07()
# ejer08()

#------- 
# os.system('cls') => cls de la terminal. 
# Ctrl+ñ = ir a Terminal
#------- 

os.system('cls')
from dvd.menuDvd import *
# import dvd.menuDvd        #También vale.

menu=["Ejercicio1 A", "Ejercicio1 B", "Ejercicio1 C", "Ejercicio1 D", "Ejercicio_2","Ejercicio_3", "Ejercicio_4","Ejercicio_5","Ejercicio_6","Ejercicio_7","Ejercicio_8"] 

while (True):
    """ 
        # Imprime Menu:
        print ('-'*18,'\nMenu')
        for index,opc in enumerate(menu):
            print (f'{index}....{opc}')
        print ('-'*18)

        # Selecciona Opcion:
        i=abs(int(input("Intro opcion....... ")))
    """    
    # Alternativa al codigo anterior con Importacion enn el mismo directorio.
    # En caso de ser en distintos directorios ( from ..menuDvd import MenuLista )
    # Comentar swap para alternar.
    i=MenuLista(menu)

    if i==0: break  #PRIMERO LA DE SALIDA
    
    if i==1:
        lista=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
        listas_01A(lista)
    elif i==2:
        lista=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
        listas_01B(lista)
    elif i==3:
        lista=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
        listas_01C(lista)
    elif i==4:
        lista=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
        listas_01D(lista)
    elif i==5:
        ejer02()
    elif i==6:
        ejer03
    elif i==7:
        ejer04()
    elif i==8:
        ejer05()
    elif i==9:
        ejer06()
    elif i==10:
        ejer07()
    elif i==11:
        ejer08()    
    else:
        continue
# --------------------------
