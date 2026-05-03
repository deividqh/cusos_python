"""
Ejercicio 2: Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar un error.

"""

uno=input("Intro num 1")
dos=input("Intro num 2")

if dos==0:
    print   (" :( ")
else:
    print(" division :  ", int(uno)/int(dos))