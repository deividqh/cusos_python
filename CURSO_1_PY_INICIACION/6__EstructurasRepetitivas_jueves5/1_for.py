"""
 1. Escribir un programa que pida al usuario una palabra y la muestre
10 veces por pantalla.
"""
def ejer1():
    uno=input("Intro word.....")
    for i in range(10):
        print(i,")",uno) 
        

"""
2. Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares desde 1
hasta ese número separados por comas.
"""

def ejer2():
    uno=abs(int(input("Intro num....")))
    for i in range(1,uno+1,2):
        print(i) 

"""
3. Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla la cuenta atrás desde ese número
hasta cero separados por comas.
"""

def ejer3():
    uno=abs(int(input("Intro num.... ")))
    for i in range(uno, -1 , -1):
        t="," if i>0  else ""
        print(i,end= t )

# -----------------------------------------------------
ejer1()
# ejer2()
# ejer3()