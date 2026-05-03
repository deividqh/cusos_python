# Tipos de lecturas que existen ficheros python

# Version 2(No hay que cerrar el fichero)
with open("desarrolloConPython/Unidad3_ficheros/ejemplo2/texto.txt", "r", encoding="utf-8") as file:
    file.seek(5)
    print(f'estoy en la posicion: {file.tell()}') #en que posicion está
    contenido = file.read()
    print(contenido)
    print(f'estoy en la posicion: {file.tell()}') #en que posicion está

with open("desarrolloConPython/Unidad3_ficheros/ejemplo2/texto.txt", "r", encoding="utf-8") as file:
    linea=file.readline()
    while linea:
        print(linea)
        linea = file.readline()
print("\nnuevo")
with open("desarrolloConPython/Unidad3_ficheros/ejemplo2/texto.txt", "r", encoding="utf-8") as file:
    lineas=file.readlines()
    for liena in lineas:
        print (linea)
    
    
