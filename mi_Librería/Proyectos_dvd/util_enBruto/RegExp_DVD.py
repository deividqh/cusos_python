import re           #re (regex)
# Función: Este módulo se utiliza para trabajar con expresiones regulares (regex). 

# Las expresiones regulares SON secuencias de caracteres que definen 
# PATRONES DE BUSQUEDA en cadenas de texto. 



# ---------------------------------------------------------
# SE USA el módulo re para buscar, extraer y reemplazar subcadenas 
# que coincidan con un patrón determinado.
# ---------------------------------------------------------
# .      # Cualquier carácter, excepto una nueva línea. 
# \d      # Coincide con cualquier dígito decimal.
# \D      # Cualquier carácter que no sea un dígito decimal.
# \w      # Cualquier  cualquier carácter alfanumérico (letras, dígitos y _).
# \W      # Cualquier  cualquier carácter que no sea alfanumérico.
# \b      #Esta es una frontera de palabra. Marca el límite entre un carácter de palabra (letras, números o guion bajo) y 
                    # un carácter que no sea de palabra (como un espacio, puntuación, etc.). 
                    # En otras palabras, asegura que lo que viene después esté al comienzo de una palabra o 
                    # que lo que viene antes esté al final de una palabra.

# PALABRAS CONCRETAS
# [aeiou]   #Coincide con cualquier carácter entre corchetes, en este caso, las vocales.
# [^aeiou]  #Coincide con cualquier carácter que no esté entre corchetes, en este caso, todo excepto las vocales.

# \s        #Coincide con cualquier espacio en blanco.
# \S        #Coincide con cualquier carácter que no sea un espacio en blanco.

# _________________________
# Modificadores de cantidad que indican la cantidad de coincidencias posibles # DEL CARACTER ANTERIOR
# ?       #opcional
# *       #0 o más
# +       #1 o más
# {3}     #{} definen la cantidad exacta de veces que debe repetirse el carácter anterior. 
                #\d{3}  representa tres dígitos.
# {n,}    #Coincide con n o más repeticiones.
# {n,m}   #Coincide con al menos n y hasta m repeticiones

# ^       #Indica el comienzo de la cadena. Y la negacion en caso de [palabras-Concretas]
# $       #Indica el final de la cadena.

# |       #Representa una alternativa (OR)

# ________________
# ()      #Grupos: Se usan para agrupar expresiones y capturar texto.
                    # Puedes acceder al texto capturado usando group() en el objeto del resultado.
                    # Ejemplo:  Para una cadena "abc123", la expresión (\w+)(\d+) 
                    #           captura las letras y los números en dos grupos distintos.

# ---------------------------------------------------------
# Los FLAGS son opciones que alteran el comportamiento de las expresiones regulares:
# re.IGNORECASE (re.I)    #Ignora las mayúsculas/minúsculas en la búsqueda.
# re.MULTILINE (re.M)     #Permite que los metacaracteres ^ y $ coincidan al principio y al final de cada línea, no solo de la cadena.

# ---------------------------------------------------------
# Ejemplos:

# ^\d{3}-\d{3}-\d{4}$       :Coincide con un número de teléfono de EE. UU. en el formato ###-###-####.

# \b[a-zA-Z]+\b              :Coincide con cualquier palabra que contenga solo letras.

# [\w\.-]+                   (Patron Conjunto de caracteres = \w(numeros, letras , guionBajo) , "." , "-")

# ^[\w\.-]+@[\w\.-]+\.\w+$   (Patron correo electrónico).

# \+?\d{1,3}                    :(código de país opcional), con un signo + opcional seguido de 1 a 3 dígitos

# [-.\s]?                       :Permite un separador opcional (guion, punto o espacio)

# \(?\d{3}\)?                   :Coincide con un área de 3 dígitos opcionalmente entre paréntesis.

# ^\d{4}/\d{2}/\d{2}$        (Patrón para validar una fecha en formato "AAAA/MM/DD")

# ^\w{3,16}$                 (Patrón para validar nombres de usuario)

# ^[\w.]+-[\w.]+$               palabra1-palabra2 -> (letras, numeros, guiones bajos y puntos)(guion obligatorio)(letras, numeros, guiones bajos y puntos)
                                # usuario-nombre (SI) ; usuario.nombre (NO, no hay guion) ; nombre-de.usuario (SI)

# ^[\w]+[-.][\w]+$              palabra1[guion o punto oblig]palabra2 -> (letras, numeros y guion bajo)[guion o punto obligatorio](letras, numeros y guion bajo)
                                # usuario-nombre (SI) ; usuario.nombre(SI) ; nombreusuario(NO)

# Forzar que haya al menos uno de cada tipo, sin importar el orden (punto o guion)
# ^(?=.*[.-])[\w.-]+$           name.usu-dominio(SI) ; usu-name (SI); usu.name(SI) ; nombreusuario (NO)

#   (?=.*[.-]):   Este es un lookahead. Indica que, en cualquier parte de la cadena, debe haber al menos un punto o un guion. 
#                 No consume caracteres, solo verifica la condición.

# ---------------------------------------------------------
# -------- FUNCIONES CON EXPRESIONES REGULARES ------------
# re.match() o re.search()    #Buscar coincidencias
# re.findall()                #Extraer múltiples coincidencias
# re.sub()                    #Reemplazar texto usando .
# re.split()                  #Dividir cadenas usando.


# ---------------------------------------------------------

def buscar1_ExpReg(text):
    print ("\n", "INI \t", text)

    pattern = "texto"
    print(text, "\nPatron a Buscar :\'", pattern,"\'")
    result = re.search(pattern, text)
    if result:
        print("Encontrado")
    else:
        print("No encontrado")
    
    print ("\n..........This is The End\n")

# ---------------------------------------------------------
def Extraer1_ExpReg(text):
    print ("\n", "INI \t", text)
    
    pattern = r"\w+"
    print(text, "\nPatron a Buscar :\'", pattern,"\'")
    result = re.findall(pattern, text)
    print(f"Entrada: {text}\nTipo de result: ", type(result), "\nDato de result: ",result)
    
    print ("..........This is The End\n")
# ---------------------------------------------------------

def Reemplazar1_ExpReg(text):
    print ("\n", "INI \t", text)
    
    pattern = "palabras"
    sustituirX="words"
    result = re.sub(pattern, sustituirX, text)
    print(result)
    
    print ("..........This is The End\n")
def sustitute():
    return "words"
# ---------------------------------------------------------

# Funcion que Recube un DNI(8num(?)letra) y devuelve el dni en una tupla(numero, letra). 
    # Puedes meter guion, barraInvertida, espacio....entre el número y la letra.
def extract_dni_values(dni):      
    pattern = r"^(\d{8})[-.\s]?([A-Z])$"
    # (\d{8})       8 digitos (0 a 9)
    # [-.\s]?       (guion o punto o espacio en blanco opcionales)
    # ([A-Z])       :Letra Mayuscula de la A a la Z.
    # [A-Za-z]      :Letra del alfabeto en mayúscula o minúscula.  
       
    match = re.match(pattern, dni)
    guion = r"^-?"
    letra = r"[a-z$]"
    if match:
        # Devolver una tupla con el número y la letra
        number = match.group(1)
        letter = match.group(2)
        return (number, letter)
    else:
        return None

# ------Uso:
text = "Este es un texto de prueba para BUSCAR una palabra en una cadena"
buscar1_ExpReg(text)
# ------Uso:
text = "Este es un texto de prueba con una serie de palabras para EXTRAER palabras de una cadena"
Extraer1_ExpReg(text)
# ------Uso:
text = "Este es un texto de prueba con una serie de palabras para REEMPLAZAR palabras."
Reemplazar1_ExpReg(text)

# ------Uso:
dni = "12345678A"
result = extract_dni_values(dni)
print("DNI: ",dni," \tResultado en Tupla: ", result)  # Devuelve ('12345678', 'A', '1')

print ("..........This is The End\n")

# ------Uso:
dni = "00000000 Y"
result = extract_dni_values(dni)
print("DNI: ",dni," \tResultado en Tupla: ", result)  # Devuelve ('00000000', 'Y', '9')

print ("..........This is The End\n")
# ---------------------------------------------------------



