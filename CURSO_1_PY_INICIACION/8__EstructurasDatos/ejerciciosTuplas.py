# Ejercicios Listas

import os           #Para Limpiar la terminal con  os.system('cls') 

""" Ejercicio 1.
"""
# 
def ejer01  (tupla):    
    os.system('cls')
    print ("\nINI..........Ejercicio1 - TUPLAS","\n"+
""" 
A. Crea una tupla con los nombres de los días de la semana.
B. Imprime el tercer día de la semana.
C. Imprime los días de la semana en orden inverso
 """)
    print("\nA):\t", tupla)

    print("\nB):\t", tupla[2])

    print("\nC):\t", tupla[::-1])
    
    print ("\n..........This is The End","\n") 


"""  
Ejercicio 2. 
"""
def ejer02():
    os.system('cls')
    txtEjer=""" 
A. Crea una tupla con tus datos personales (nombre, apellido, edad).
B. Imprime una frase que incluya tus datos. """
    print ("\nINI..........Ejercicio2 - TUPLAS","\n"+txtEjer)
    
    mitupla=["David", "Quesada", 50]
    #----- W O R K I N G  P R O C E D U R E

    # print(lista)
    print(f"\nResultado: hola {mitupla[0]} {mitupla[1]} tienes {mitupla[2]}")
    #-----
    print ("..........This is The End","\n")
# --------- E J E C U C I O N      A B A J O ------------------------


""" 
Ejercicio 3. 
"""
def ejer03():
    os.system('cls')
    txtEjer="""
A. Crea una tupla con los números del 1 al 10.
B. Calcula la suma de todos los números."""
    print ("\nINI..........Ejercicio3 - TUPLAS","\n"+txtEjer)
    
    tupla=tuple(range(1,11))
    #-----
    print(f"A-tupla: {tupla} ")
    print(f"B-suma: {sum(tupla)} ")
    #-----
    print ("..........This is The End","\n")
# --------- E J E C U C I O N      A B A J O ------------------------

""" 
Ejercicio 4.  
"""
def ejer04():
    os.system('cls')
    
    txtEjer=""" 
A. Crea una tupla de tuplas para representar una matriz de 3x3.
B. Imprime el elemento en la segunda fila y tercera columna. """    
    tupla=(1, 2, 3), (4, 5, 6), (7,8,9)
    #----- W O R K I N G  P R O C E D U R E
    for a in tupla:
        print(a)
    print(f"\nLista: {tupla}")
    print("\nf(2), c(3): ",tupla[1][2])
    #-----

# --------- E J E C U C I O N      A B A J O ------------------------


# Ejercicio 5.  
def ejer05():
    os.system('cls')

    txtEjer=""" 
A. Crea una lista de números.
B. Convierte la lista en una tupla.
C. Multiplica cada elemento de la tupla por 2 y guarda el resultado en una nueva tupla.    """
    
    #----- W O R K I N G 
    # A-
    lista=[5, 7, 4]
    print(f"A-lista: {lista}, tipo {type(lista)}")
    # B-
    tupla=tuple(lista)
    print(f'B-tipo de la lista convertida: {type(tupla)}')
    # C
    lista2=[]
    for n in tupla:
        lista2.append(n*2) 
    tupla2=tuple(lista2)

    print(f'\n5-tupla nueva = {tupla2}, tipo:{type(tupla2)}')

# --------- E J E C U C I O N      A B A J O ------------------------


from enum import Enum

# Definicion de una Enumeracion(para no tener que usar index). 
    # 1-Hay que importar:  from enum import Enum 
    # 2-Se define una clase. no hay tipo Enum. 
    # 3-Uso: dP.PELI
class dP(Enum):
    PELI = 0
    AUTOR = 1
    ANNO = 2

# Ejercicio 6. 
def ejer06():
    os.system('cls')

    
    
    txtEjer=""" 
A. Crea una tupla anidada para representar una pequeña biblioteca.
Cada elemento de la tupla será un libro con título, autor y año de
publicación.
• Cien años de soledad, Gabriel García Márquez, 1967
• El señor de los anillos, J.R.R. Tolkien, 1954
• La sombra del viento, Carlos Ruiz Zafón, 2001
• Orgullo y prejuicio, Jane Austen, 1813
• 1984, George Orwell, 1949
• Harry Potter y las Reliquias de la Muerte, J.K. Rowling, 2007
• Ángeles y demonios, Dan Brown, 2000

B. Imprime todos los libros publicados después de 2000"""
    print ("\nINI..........Ejercicio6 - TUPLAS","\n",txtEjer)

    pelicula = (("Cien años de soledad", "Gabriel García Márquez", 1967), 
    ("El señor de los anillos", "J.R.R. Tolkien", 1954),
    ("La sombra del viento", "Carlos Ruiz Zafón", 2001),
    ("Orgullo y prejuicio"," Jane Austen", 1813),
    ("1984", "George Orwell", 1949),
    ("Harry Potter y las Reliquias de la Muerte", "J.K. Rowling", 2007),
    ("Ángeles y demonios","Dan Brown", 2000))
    
    print("-"*10+" "+ str(dP.PELI))
    for p in pelicula:
        if p[2]>2000:
            # Solucion:
            # print (f'Pelicula: {p[0]} \nAutor: {p[1]}, \nAño: {p[2]}\n')

            # Alternativa con Enum:
            # Las tuplas no admiten Enum(Vaya!!), hay que ponerles .value (la verdad que ya no mola tanto)
            print (f'Pelicula: {p[dP.PELI.value]} \nAutor: {p[dP.AUTOR.value]}, \nAño: {p[dP.ANNO.value]}\n')
    #-----




# He creado un paquete "dvd" y lo añado al sys.path
import sys
proyecto_ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# cacho la ruta del proyecto para luego poder posicionarme desde ahí (dvd.Modulo)
# print(f'proyecto file: {proyecto_ruta}')

sys.path.append(proyecto_ruta)
# Validacion de las rutas:
# print(f"\nRutas en sys.path:\n{sys.path}", sep="\n")

# os.system('cls')

menu=["Tuplas 1",  "Tuplas 2","Tuplas 3", "Tuplas 4","Tuplas 5","Tuplas 6"] 

from dvd.menuDvd import *
while (True):
   
    # Alternativa al codigo anterior con Importacion enn el mismo directorio.
    # En caso de ser en distintos directorios ( from ..menuDvd import MenuLista )
    # Comentar swap para alternar.
    i=int(MenuLista(menu))

    if i==0: break  #PRIMERO LA DE SALIDA
    
    if i==1:        
        tupla=("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
        ejer01(tupla=tupla)
    elif i==2:
        ejer02()
    elif i==3:
        ejer03()
    elif i==4:
        ejer04()
    elif i==5:
        ejer05()
    elif i==6:
        ejer06()
    else:
        continue
# --------------------------
