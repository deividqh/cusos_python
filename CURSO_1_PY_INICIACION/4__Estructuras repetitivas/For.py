"""
While
Ejercicio 1: Crea un programa utilizando el bucle for en que hay que mostrar
por pantalla números del 1 al 10.
"""
def ejer1():
    for i in range(1, 10+1):
        print(i)
    
"""
Ejercicio 2: Pedir al usuario 5 números y decir si son par o impar.
"""
def ejer2():
    for i in range(1, 5):
        uno=int(input("Intro num....."))
        if uno%2==0 : print("par")
        else: print("impar")


"""
Ejercicio 3. Crea un programa que imprima una tabla de multiplicar del número
que introduzca el usuario.
"""

def ejer3():
    uno=int(input("Intro num....."))
    for i in range(1, 10+1):
        print (uno,"x",i,"=",i*uno)
    
"""
Ejercicio 4. Crear un programa, que pida al usuario un número, y muestre por
pantalla, los números en orden inverso hasta 0.
"""
def ejer4():
    uno=int(input("Intro num....."))
    for i in range(uno, 0):
        print(i)

"""
Ejercicio 5. Tenemos la pantalla del móvil bloqueada. Partiendo de un
PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3
intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario
'login correcto'. Sino, 'llamando al policía'.
"""
PIN="1234"
def ejer5():
    bmatch=False
    for i in range(1, 3):
        uno=int(input("Intro pin....."))
        if uno==PIN:
            bmatch=True
            exit 
    if bmatch == True: print(";)")
    else:  print(":(") 

# -------------------------------

ejer1()
# ejer2()
# ejer3()
# ejer4()
# ejer5()