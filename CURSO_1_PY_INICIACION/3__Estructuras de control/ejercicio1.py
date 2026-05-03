"""
Ejercicio 1: Escribir un programa que almacene la cadena de caracteres
password en una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con la guardada en
la variable.
"""

p="password"
valp=input("Intro passw")
if valp==p:
    print(" ;) ")
else:
    print(" :( ")