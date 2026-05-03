""" 1. Escribir un programa que pregunte el nombre del usuario en la consola y
un número entero e imprima por pantalla en líneas distintas el nombre del
usuario tantas veces como el número introducido. """
def cadenas1():
    print ("\n")
    nombre=input("Intro Nombre........")
    num=abs(int(input("Intro num........")))
    for i in range(0, num):
        print(i,")",nombre)
    print ("..........This is The End","\n")

""" 2.Escribir un programa que pregunte el nombre completo del usuario en la
consola y después muestre por pantalla el nombre completo del usuario
tres veces, una con todas las letras minúsculas, otra con todas las letras
mayúsculas y otra solo con la primera letra del nombre y de los apellidos en
mayúscula. El usuario puede introducir su nombre combinando mayúsculas
y minúsculas como quiera """
def cadenas2():
    print ("\n")
    nombre=input("Intro Nombre........")
    print(nombre.lower() ,"\n", nombre.upper(),"\n",nombre.title())
    print ("..........This is The End","\n")


""" 3. Crea un programa que pida al usuario una frase y luego:
▻ Convierta toda la frase a minúsculas.
▻ Cuente cuántas veces aparece la letra "a" en la frase.
▻ Imprima la frase sin las vocales. """
def cadenas3():
    print ("\n")
    nombre=input("Intro Frase........")
    print(nombre.lower())
    print("hay ",nombre.count("o"), " oes en la frase")
    
    print("sin vocales= ",nombre.replace("aeiou", ""))


    print ("..........This is The End","\n")

""" 4. Introducir una cadena de caracteres e indicar si es un palíndromo. Una
palabra palíndroma es aquella que se lee igual adelante que atrás.
 """
def cadenas4():
    nombre=input("Intro Frase........")
    long = len(nombre.strip())
    
    
    if (long%2) == 0:
        mitad=nombre[:int((long/2)+1)]
        otraMitad=nombre[long/2+2:-1]

        if mitad==otraMitad: print("palindroma")        
    else:
        mitad=nombre[:long//2]
        otraMitad=nombre[long/2+2:-1]

        if mitad==otraMitad:
            print("palindroma")

    print(mitad, "\n", otraMitad)


    print ("..........This is The End","\n")

# -----------------------------------------------------



""" 
Ejercicio 1: Los teléfonos de una empresa tienen el siguiente formato prefijo-númeroextensión 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por
ejemplo 

+34-913724710-56 

Escribir un programa que pregunte por un número de teléfono con este formato en la consola y
muestre por pantalla el número de teléfono sin el prefijo y la extensión.
 """
def cadenas5():
    print ("\nINI..........ejercicio1 - Ejercicios de Cadenas","\n")

    tlf=input("Intro Tlf........")
    long = len(tlf.strip())
    listaTlf=tlf.split("-")
    print (listaTlf[1])

    print ("..........This is The End","\n")



""" Ejercicio 2: Escribir un programa que pida al usuario que introduzca una frase en la
consola y muestre por pantalla la frase invertida.
 """
def cadenas6():
    print ("\nINI..........ejercicio2 - Ejercicios de Cadenas","\n")

    tlf=input("Intro Frase........")
    print(tlf[::-1])
    
    print ("..........This is The End","\n")


""" Ejercicio 3: Escribir un programa que pida al usuario que introduzca una frase en la
consola y una vocal en minúscula, y después muestre por pantalla la misma frase, pero
con la vocal introducida en mayúscula
 """
def cadenas7():
    print ("\nINI..........ejercicio3 - Ejercicios de Cadenas","\n")
    #-----
    tlf=input("Intro Frase........")
    vocal=input("Intro Vocal Min........")    
    result=tlf.replace(vocal, vocal.upper())

    print(result)
    #-----
    print ("..........This is The End","\n")


""" Ejercicio 4: Escribir un programa que pregunte el correo electrónico del usuario en la
consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte
delante de la arroba @) pero con dominio avanza.es.

From deividqh@gmail.com
To   deividqh@avanza.es
 """
def cadenas8():
    print ("\nINI..........ejercicio4 - Ejercicios de Cadenas","\n")
    #-----
    
    correo=input("Intro correo........")
    listaCorreo=correo.split("@")
    domininoAvanza="avanza.es"

    print(listaCorreo[0]+"@"+domininoAvanza)
    
    #-----
    print ("..........This is The End","\n")

""" Ejercicio 5: Escribir un programa que pregunte por consola  los productos de una
cesta de la compra, separados por comas, y muestre por pantalla cada uno de los
productos en una línea distinta. """
def cadenas9():
    print ("\nINI..........ejercicio5 - Ejercicios de Cadenas","\n")
    #-----
    prod=input("Intro productosSeparadosPorComas........")
    
    result = prod.strip().replace(" ","").split(",")
    for  ab in result: 
        print(ab)
    #-----
    print ("..........This is The End","\n")

"Pruebas Dvd con delimitadores de Cadena:"
def cadenas10():
    txt="aeiou"

    print(txt[:1])
    print(txt[0:1])

    print(txt[:1:-1])
    print(txt[-3:-1])

    print(txt[-3:-1:1])
    print(txt[-3:-1:-1])

""" Ejercicio Extra 1. Hemos comenzado a trabajar en una empresa del sector farmacéutico
llamada BioNTech. Nos vamos a ocupar de ciertos análisis bioinformáticos. La primera
ocupación que tenemos a nuestra llegada es trabajar sobre la siguiente cadena de ARN:
“AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUG
GUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGG
UCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUG
GTOAUGGOTGACUGG”
Cada carácter de la cadena representa un nucleótido que forma parte del ARN. Sabemos
que ARN esta formado por 4 nucleótidos: Adenina(A), Guanina(G), Citosina(C) y Uracilo
(U).
La empresa está interesada en saber cuántas tripletas de nucleótidos presentes en la
cadena van a codificar en aminoácido triptófano (UGG). Aparte de eso ha habido ciertos
errores en la secuencia y han aparecido signos extraños (T y O) que no pertenecen al
ARN.
Escribe un programa que primero limpie la cadena de caracteres extraños y a
continuación cuente el numero de tripletas UGG presentes.
"""
def cadenas11():
    print ("\nINI..........ejercicio1 Extra - Ejercicios de Cadenas","\n")
    #-----
    cad="AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUG"
    print(cad.replace("O", ""))
    print(cad.replace("T", ""))
    print(cad.count("UGG"))

    #-----
    print ("..........This is The End","\n")
""" 
Ejercicio Extra  2. Ingresar un mail por teclado. Verificar si el texto ingresado contiene solo un
carácter "@".
"""
def cadenas12():
    print ("\nINI..........ejercicio2 Extra - Ejercicios de Cadenas","\n")
    #-----
    tlf=input("Intro Frase........")
    if tlf.count("@") > 1:
        print(":(")
    #-----
    print ("..........This is The End","\n")

""" 
 Ejercicio Extra  3. Crear un programa que cuente las palabras que tiene una oración.
"""
def cadenas13():
    print ("\nINI..........ejercicio 3 Extra - Ejercicios de Cadenas")
    #-----
    tlf=input("Intro Frase........")
    print("num palabras: ",tlf.strip().count(" ") + 1)
    # print("num palabras: ",tlf.strip().replace(" ", ""))
    # print("num palabras: ",tlf.strip().replace(" ", ","))
    # print("num palabras: ",tlf.strip().replace(" ", ","))
    #-----
    print ("..........This is The End","\n")

# ---------------E J E R C I C I O S----------------
# cadenas1()
# cadenas2()
# cadenas3()
# cadenas4()
# cadenas5()
# cadenas6()
# cadenas7()
# cadenas8()
# cadenas9()
# cadenas10()
# cadenas11()
# cadenas12()
# cadenas13()