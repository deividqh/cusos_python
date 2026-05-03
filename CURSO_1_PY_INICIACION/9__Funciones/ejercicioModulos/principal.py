""" 
                                Modulo Principal
"""
if __name__=="__main__":
    pass

# Para usar el paquete dvd
# import os, sys
# proyecto_ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' ,'..'))
# # oyecto_ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
# print(f'proyecto file: {proyecto_ruta}')
# sys.path.append(proyecto_ruta)
# # Impresion de los path metidos en el sys de python y comprobar que está metido el proyecto.
# print("Rutas en sys.path:")
# for ruta in sys.path:
#     print(ruta)

# from dvd import menuDvd as men
# import dvd.menuDvd as men
# from dvd.menuDvd import *
import ejer02 as ej2

print(ej2.txtejer)
menu=["Intro Numero"]
while(True):
    numero = input('Intro numero.....')
    if not numero.isdigit():
        break
    if int(ej2.elegido)==int(numero):
        print("*"*20+"\nEnhoraBuena!!!\n"+"*"*20)
    elif int(ej2.elegido)>int(numero):
        print("el numero Intro es menor que el que tengo en mente")
    else:
        print("el numero Intro es mayor que el que tengo en mente")
print("*"*20+"\nSaliste del ejercicio")

def esValidInt(strNum):
    """ 
    Def: Valida si el codeDigit pasado como argumento es un número entero.
            No incluye _ , . (decimal)
            si entra en el patron True / si no entra, False 
    """
    # .... Se lee: en toda la cadena [ From Ini(^); to Fin ($) ]
    #              Buscamos:  guion(-) opcional(?) y/o  0-9(\d)   ,  n veces(+)(solo el digito) 
    patronInt=r'^-?\d+$'
    num=re.match(patronInt, str(strNum))        
    return (True if num else False)

import ejer03 as ej3
import random as ran
import re
import string

# def funRe(match):
#     char = match.group()

#     # Iba a dejar este, pero incluye caracteres en blanco y tabulacion \t 
#     # strPrintables = string.printable
#     # print(string.ascii_letters)
#     # print(string.digits)
#     # print(string.punctuation)
#     strPrintables = string.ascii_letters + string.digits + string.punctuation 

#     if not char in strPrintables: return ''
#     longPrint=len(strPrintables)
#     aleatorio=ran.randint(0, longPrint-1)
#     return strPrintables[aleatorio]

print(ej3.txtejer)
long = input('Intro longitud de contraseña.....')
if esValidInt(long): long = int(long)
passw=''
for i in range(long):
    passw+="X"

otroPatron=r'.'    # letra-digit-guionBajo o(inclusivo) Sp

# listResultado=[re.sub(patron, funRe, passw) for i in range(long)]
listResultado=[ re.sub(otroPatron, ej3.funRe, n) for n in passw ]
print(f'Password Recomendada de {long} char\'s ==> '+''.join(listResultado),"\n")

    
import ejer04 as ej4
print(ej4.textEjer)


from ....dvd import menuDvd as men
men.MenuDvd()

# men.MenuDvd()
