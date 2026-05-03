import string
txtejer=""" 
3. Crear un programa para crear contraseñas seguras.
    a. El usuario debe introducir la longitud que desea de la contraseña.
"""
import random as ran
def funRe(match):
    char = match.group()

    # Iba a dejar este, pero incluye caracteres en blanco y tabulacion \t 
    # strPrintables = string.printable
    # print(string.ascii_letters)
    # print(string.digits)
    # print(string.punctuation)
    strPrintables = string.ascii_letters + string.digits + string.punctuation 

    if not char in strPrintables: return ''
    longPrint=len(strPrintables)
    aleatorio=ran.randint(0, longPrint-1)
    return strPrintables[aleatorio]