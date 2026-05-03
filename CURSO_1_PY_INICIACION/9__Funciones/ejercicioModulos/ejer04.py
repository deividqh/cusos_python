textEjer=""" 
4. Crear un programa que genere un boleto de lotería ganador. 
    a. Generar 5 números de una tabla de 54 (números del 1 al 54) 
        y uno más (número clave) de una tabla de 10 (del 0 al 9). 
        Los números no pueden ser repetidos.  
    b. Imprimir la fecha del día de hoy. (Modulo datetime) 
"""
import random
def boleto():
    lstNumeros=[]

    cont=0
    while True:
        numBoleto=random.randint(1, 55)
        if not numBoleto in lstNumeros:
            cont+=1
            lstNumeros.append(random.randint(1, 55))
            if cont==5:break

    numPlus=random.randint(0,9)
    return lstNumeros, numPlus
    