"""

Ejercicio 3: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu
índice de masa corporal es imc donde imc es el índice de masa corporal calculado redondeado con dos decimales.
Imc = peso/estatura**2
Redondear con 2 decimales => round(variable,2)

"""

P=112
M=75
uno=int(input("Intro kg...."))
dos=int(input("Intro mtr...."))


print("Tu índice de masa corporal es  = " , float(round(uno*dos**2,2)))

