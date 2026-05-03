""""

Ejercicio 1: Una panadería vende trozos de tarta a 3.49€ cada una.
El trozo que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de trozos vendidos de hoy como que los no son del día.
Después el programa debe mostrar el precio habitual de un trozo, el descuento que se le hace por no ser fresco, 
el coste de lo ganado en los trozos del día y los que no, y el coste final total.

"""
P=3.49
D=0.6
uno=int(input("Intro hoy...."))
dos=int(input("Intro no hoy...."))
# import string library function 

print("PrecioFilnal....", float(round(P*uno,2)) + float(round(P*dos*D,2)))