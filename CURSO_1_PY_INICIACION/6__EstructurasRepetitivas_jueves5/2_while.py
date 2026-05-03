"""
 1. Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta.        
"""
def ejer1():
    P="pass"
    while (True):
        valp=input("Intro passw...")
        if valp==P:
            print(" ;) ")
            break
        else:
            print(" :( ")


"""
2. Calcular el factorial de un número
"""
def ejer2():

    uno=int(input("Intro num..."))
    r = 1
    while(uno>=1):
        r = uno * r
        print(uno, end="x")
        uno-=1
    else:
        print("\n",r)


"""
3. Sucesión de Fibonacci en Python.
▻ En matemáticas, la sucesión de Fibonacci es una sucesión
infinita de números naturales, donde el siguiente numero se
consigue sumando los dos anteriores.
"""
INI=12
def fibonacci(hasta):         
    a = 0
    b = 1
    print("\n",a, end =",")
    print(b, end=",")

    i = 0
    while i < hasta :
        c = a + b    
        print(a + b, end =", " if i!=hasta-1 else "")
        a=b 
        b=c    
        i+= 1    
    print ("\n")
# --------------------------------------
ejer1()
# ejer2()
# fibonacci(11)