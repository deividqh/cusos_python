import os
os.system('cls')
""" ESCRITURA EN FICHEROS 
w: Sobrescribe el fichero desde el seek(0) (inicial) , si no existe el archivo, lo crea

"""

# =========================
# Abre y escribe.
with open(file="desarrolloConPython/Unidad3_ficheros/ejemplo4/datos.txt", 
            mode="w", 
            encoding="utf-8") as archivo:    

    archivo.write("0123456789")
    print(f'estoy en la posicion: {archivo.tell()}') #en que posicion está

# =========================
# Abre el archivo en modo añadir
# el nuevo contenido se añade al final
with open(file="desarrolloConPython/Unidad3_ficheros/ejemplo4/datos.txt", 
            mode="a", 
            newline='',
            encoding="utf-8") as archivo:

    archivo.write("x2x")
    print(f'estoy en la posicion: {archivo.tell()}') #en que posicion está

# =========================
# OPCION DE APERTURA 'a'
# =========================
with open(file="desarrolloConPython/Unidad3_ficheros/ejemplo4/texto.txt", 
            mode="a", 
            newline='',
            encoding="utf-8") as archivo:    
    archivo.write("Loreto Pelegrin Castillo, Teo Gomariz Ferrero, Pablo Ortiz Hernaiz")
    print(f'estoy en la posicion: {archivo.tell()}') #en que posicion está

with open(file="desarrolloConPython/Unidad3_ficheros/ejemplo4/texto.txt", 
            mode="a", 
            newline='',
            encoding="utf-8") as archivo:
    
    lista_nombres=[]
    for linea in archivo:
        nombre, apellido1, apellido2 = linea.split()
        lista_nombres.append(nombre)

for name in lista_nombres:
    print(name)
    

    
