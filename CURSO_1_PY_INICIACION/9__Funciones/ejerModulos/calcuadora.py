import math
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return math.pow(a,b)

def factorial(a):
    return math.factorial(a)
    
def tantoX100(a,b):
    if b>0 and b<=1: 
        b=math.prod(b*100)
    return math.prod(a, b) / 100

while True:
    print("Elija una opcion:")
    print("Opcion 1: Sumar")
    print("Opcion 2: Resta")
    print("Opcion 3: Multiplicacion")
    print("Opcion 4: Division")
    print("Opcion 5: Salir")
    opcion = int(input())
    if opcion == 5:
        print("Adios :(")
        break
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce un numero: "))
    if opcion == 1:    
        print(suma(num1,num2))
    elif opcion == 2:
        resultado = resta(num1,num2)
        print(resultado)
    elif opcion == 3:
        resultado = multiplicacion(num1,num2)
        print(resultado)
    elif opcion == 4: 
        if num2 == 0:
            print("Este no vale")
        else:
            resultado = division(num1,num2)
            print(resultado)
    else:
        continue
    
    