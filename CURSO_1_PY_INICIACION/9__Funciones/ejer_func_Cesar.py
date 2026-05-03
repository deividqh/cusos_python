# Ejercicios Funciones II ............... Cesar

import re       #Para usar expresiones Regulares
import os
os.system('cls')
# ejercicio1 
""" 1. Crea un programa que introduciendo una lista como argumento de una función.
Realice: a. Suma de todos los elementos de la lista, b. La media , c. El número mayor y menor de la lista
 """
def ejer01(laLista):
    suma=sum(laLista)   ;    media=suma/len(laLista)  ;  maximo=max(laLista) ; minimo=min(laLista)
    return(suma, media, maximo, minimo)
print(ejer01([1,2,3]))
print("===>Fin Ejercicio 1 \n")

# ejercicio     C e s a r 
"""
2. Crea un programa de cifrado y descifrado, utilizando el Método Cesar. 
Que consiste en desplazar la letra original x puestos hacia la derecha.

a.  Por ejemplo, utilizando la frase: El perro y haciendo 2 desplazamientos a la
    derecha quedaría Gn rgttq.

Recordar que Python es Case Sensitive (distingue entre mayúsculas y minúsculas)
Se puede elegir el desplazamiento que se quiera 
"""

import string
# --------------------------------------------Variables Globales
# --------------------------------------------Variables Globales
abc=string.ascii_lowercase  # 'abcdefg....'
ABC=string.ascii_uppercase  # 'ABCDEFG....'
listResultado=[]            # lista que genera el resultado que luego se convierte a str con join().

D=2                 # Desplazamiento del Cifrado
S1=45               # El numero de caracteres que se repite "=". Lo uso para los finales
NWORDS=50          

# ------------------------------------------- M o t o r   H e a d  (Index) >
# ------------------------------------------- M o t o r   H e a d  (Index) >
# os.system('cls')
def esValido(texto):
    """     
    Def:    Valida la Entrada segun expresion la Regular: r'^[da-zA-Z]+$' 
            Si [texto] no se ajusta al patron => ha introducido un char no valido($ pej)

            ^          => Inicio de la cadena
            [da-zA-Z]  => [char] | d=>un digito | a-z => From a To z | A-Z => from A to Z
            + =>  cualquier numero de veces. Si no se pone sólo valdría para un sólo char
            $          => Fin de la cadena
    Args:   [texto] = str() no Validado.
    
    Return: (True/False)
    """
    if not isinstance(texto, str):  return False
    patron=r'^[da-zA-Z]+$'
    if re.search(patron, texto)==None:
        return True
    else:
        return False

# --------------------- Index Motor Head
# --------------------- Index Motor Head
print("EJERCICIO DE ENCRIPTACION CESAR:")
while(True):
    desp=input(f"Actual Desplazamiendo( {D} )\n\tIntroduce nuevo Desplazamiento o cualquier tecla Xa {D}.... ")    
    if str(desp).isdigit() or (str(desp[1:]).isdigit() and desp[0]=='-'): 
        D=int(desp)
    introFrase=input(f"Actual Desplazamiendo( {D} )\nEsperando Frase Para Cifrado.... ")
    if esValido(introFrase.strip())==True:
        print()
        break
    print(f'< {introFrase} >\nFrase con caracteres no Válidos')
# ------------------------------------------- M o t o r   H e a d  (Index) ]
# ------------------------------------------- M o t o r   H e a d  (Index) ]

# ------------------------------------------Solucion 1 >

def Cesar_01(frase):        
    for i,n in enumerate(frase):
        if n!=" ":
            if n in abc:                
                pos=abc.find(n)
                loadListResultado(abc, pos)
            elif n in ABC:
                pos=ABC.find(n)
                loadListResultado(ABC, pos)            
            elif str(n).isdigit:       # Los numeros los pongo tal cual
                listResultado.append(n) 
            else:
                return None
        else:
            listResultado.append(" ")
    return listResultado

# ----------------- 
def loadListResultado(abc, pos):
    """ 
    CASOS LIMITE
    limit=len(abc)-D (D=desplazamiento) =>    limit = 26-3    =>  limit = 23
    D-(len(abc)-pos  =  long del Abcdario(=26) - posicion de la letra (pej=24) = [2]\n
                        Como [2] es mas pequeño que el limit (pos < limit) : Desplazamiento(pej=3) - [2] = Nueva Posicion(=1)

    Args:   abc = String abcdario, puede ser mayusculas o minusculas.
            pos = Posicion que ocupa el caracter en abc
    Return: No Retorna nada porque la listResultado es variable global del módulo.
    """    
    limit=len(abc)-D    
    if pos < limit:
        newPos= pos + D
        listResultado.append(abc[newPos])
    else:        
        # newPos=D-(len(abc)-pos)
        listResultado.append(abc[D-(len(abc)-pos)])

# ----------------- index
# ----------------- index
listResultado = Cesar_01(introFrase.strip())
if listResultado != []:   cifrado=''.join(listResultado)
else:                       cifrado = ":("
print(f"{'Solucion 1 .... (con limit del abcdario): ':<55} {cifrado:<50}")
# ------------------------------------------ Solucion 1 ]



# ---por char() ord()----------------------- Solucion 2 >
# ---por char() ord()----------------------- Solucion 2 >

# He mirado estas opciones[ char() ord() ] y son geniales para el desplazamiento tb 
# pero tengo que comprobar el limite igualmente, así que busco otra opcion para solucion 2

# -----------------------------
# Se me acaba de ocurrir que si encadeno dos cadenas iguales pero una es inicial y la otra la duplicada
# con comprobar si el desplazamiento es positivo o negativo no necesito el limite.
def Cesar_02(frase):
    # Validacion Inicial
    if abs(D)>=len(abc): 
        print(f"el Desplazamiento {D}, no puede ser mayor que la long del abcdario({len(abcdario)}):")
        return None

    strMatch = ''   #Cadena con la que voy a cruzar cada caracter. generada dinamicamente
    cursor=0        #start en find() de strMatch. Depende del desplazamiento positivo o negativo(setStrCursor).

    # listResultado=[]      #Si lo declaro aqui lo estoy declarando local
    for n in frase:
        if n!=" ":
            if n in abc:                
                strMatch, cursor = setStrCursor(abc)
            elif n in ABC:
                strMatch, cursor = setStrCursor(ABC)                
            else:       # Los numeros los pongo tal cual
                listResultado.append(n) 

            # Controla que no solo se introducen números            
            if strMatch != '':     # ....pero listResultado ya lo tiene append
                # Añado a la listaResultado el caracter en la nueva Posicion            
                pos=strMatch.find(n, cursor)
                if pos != -1:           # si va por el else no va a encontrar pos                
                    listResultado.append(strMatch[pos+D])
                    # listResultado.append(strMatch[pos:(pos+D)+1])
        else:
            listResultado.append(' ')
    # ------ Salida
    return listResultado

# -----------------------------
def setStrCursor(abcdario):    
    """ 
    Def:    Establece la cadena y el cursor para desplazamiento
            positivo o negativo.
    Args:   [abcdaario] = 'abcd.....vwxy'  ó  'ABCD.....WXYZ'
    Return: ('abcd.....vwxy'*2 , 0)   ==> D>=0     
            ('abcd.....vwxy'*2 , 26)  ==> D<0
            ('ABCD.....WXYZ'*2 , 0)   ==> D>=0
            ('ABCD.....WXYZ'*2 , 26)  ==> D<0           
    """
    if int(D)>=0:
        return (abcdario + abcdario) , 0
    else:
        return (abcdario + abcdario) , len(abcdario)
        # return abcdario[::-1] + abcdario    

# ---------- Index Solucion 2
# ---------- Index Solucion 2
listResultado=[]
listResultado = Cesar_02(introFrase.strip())
if listResultado != None:   cifrado=''.join(listResultado)
else:                       cifrado = ":("

print(f"{'Solucion 2 .... (Solucion Alternativa): ':<55} {cifrado:<50}")
# ------------------------------------------ Solucion 2 ]




#------------------------------------------- Solucion 3 >
#------------------------------------------- Solucion 3 >
# Utilizo:  1-setStrCursor() de la Solucion 2
#           2-funcDesplaza()... import re


# funcDesplaza la defino como una funcion de re, por lo que recibe un solo argumento(match)
def funcDesplaza(match):
    char = match.group()
    if char in abc:                
        strMatch, cursor = setStrCursor(abc)
    elif char in ABC:
        strMatch, cursor = setStrCursor(ABC)
    else:       
        return char                         # Si es otra cosa lo dejo tal cual Sp o _ incluido.
    pos=strMatch.find(char, cursor)        # calculo la posicion en el texto de strMatch    
    return strMatch[pos+D]                 # Devuelvo el nuevo caracter
    
# -------------------------------------------
# \w                # Cualquier  cualquier carácter alfanumérico (letras, dígitos y _).
# patron=r'\w+'     # Me vale cualquier caracter porque ya he validado en el esValido() que la entrada sea valida
                        # Pero no incluye el espacio blanco
# patron=r'(\w+)'   # Crea un grupo que se recupera con group() | 
                    # en este caso cacha cada palabras pq no incluye Sp
                    # porque \w no incluye sp
# patron=r'[\w+]'   # letra-digit-guionBajo ; (+)cualquier numero de veces. (Todo el texto)
patron=r'[\w\s]'    # letra-digit-guionBajo o(inclusivo) Sp
# -------------------------------------------

# ---------- Index Solucion 3
# ---------- Index Solucion 3
    # Esto se tendría que leer:
        # ...Por cada char de entrada(IntroFrase) devuelveme un caracter sustituido
        # ...y lo metes en la lista.
listResultado=[]
for i,n in enumerate(introFrase):
    listResultado.append(re.sub(patron, funcDesplaza, n))    

cifrado=''.join(listResultado)
print(f"{'Solucion 3 .... (con Expresiones Regulares): ':<55} {cifrado:<50}")
#----------------------------------------- Solucion 3 ]




#----------------------------------------- Solucion 4 >
#----------------------------------------- Solucion 4 >
    # Utilizo:  1-setStrCursor() de la Solucion 2
    #           2-funcDesplaza()... import re

    # Esto se tendría que leer:
            # ...Por cada char de entrada(IntroFrase) devuelveme un caracter sustituido
            # ...y lo metes en la lista.

# ---------- Index Solucion 4       ..... y esto es la versión X Comprension!!!! medalla!!! ;)
# ---------- Index Solucion 4       ..... y esto es la versión X Comprension!!!! medalla!!! ;)
listResultado=[ re.sub(patron, funcDesplaza, n) for n in introFrase ]

cifrado = ''.join(listResultado)
print(f"{'Solucion 4 .... (Reg Expr) +':<30}" + f"{'Listas de Comprension:':<25} {cifrado:<50}")
#----------------------------------------- Solucion 4 ]