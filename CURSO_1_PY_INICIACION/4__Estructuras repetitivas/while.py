"""
While
Ejercicio 1: Crea un programa utilizando el bucle while en que hay que mostrar
por pantalla números del 1 al 10.
"""
i=1
while i<11:
    print(i)
    i+=1

"""
Ejercicio 2: Creo un programa para calcular la suma de números que introduzca
el usuario por pantalla hasta que ingrese 0.
"""
while (True):
    uno=int(input("Intro num"))
    if uno == 0:
        break

"""
Ejercicio 3: Pedir al usuario 5 números y decir si son par o impar.
"""
i=1
while i<5-1:
    if i%2==0 : print("par")
    else: print("impar")
    i+=1

"""
Ejercicio 4: Crear un programa, que pida al usuario un número, y muestre por
pantalla, los números en orden inverso hasta 0.
"""

i=int(input("Intro num....."))
while (i>=0):    
    print (i)
    i-=1

"""
Ejercicio 5: Tenemos la pantalla del móvil bloqueada. Partiendo de un
PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3
intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario
'login correcto'. Sino, 'llamando al policía'.
"""
PIN="1234"
i=1
while (True):
    uno=int(input("Intro pin...."))
    if uno == PIN:
        print(";)")
        break
    if i>=3: print("Policia")
    i+=1
