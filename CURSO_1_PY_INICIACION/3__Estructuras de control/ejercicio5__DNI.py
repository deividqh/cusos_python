"""
Ejercicio 5: Crear un programa que pida al usuario su DNI sin letra, y la letra.
Calcular si el DNI es correcto. Para calcular la letra del DNI, el número entero del
DNI modulo 23 y el resto es la letra.
"""

uno=int(input("Intro numDNI...."))
dos=input("Intro letra....")

import string    
result = string.ascii_lowercase

letra=int(uno%23)
val=int(result.find(dos))
if val==-1:
    print(" :( ")
elif val==letra:
    print (" ;) ")
else:
    print(" :( ")
