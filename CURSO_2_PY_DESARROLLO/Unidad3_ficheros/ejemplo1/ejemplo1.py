# Version 1
fichero = open("desarrolloConPython/Unidad3_ficheros/ejemplo1/hola.txt", "r")
print(fichero.read())

#posicionate en el caracter 5 (empezando de zero)
#Es un puntero de posicion
fichero.seek(5) 
print(f'estoy en la posicion: {fichero.tell()}') #en que posicion está

print(fichero.read())                            # lee desde la posicion hasta el final
print(f'estoy en la posicion: {fichero.tell()}') #en que posicion está

fichero.close()

# Version 2(No hay que cerrar el fichero)
with open("desarrolloConPython/Unidad3_ficheros/ejemplo1/hola.txt", "r") as archivo:
    archivo.seek(5)
    print(f'estoy en la posicion: {archivo.tell()}') #en que posicion está
    print(archivo.read())    
    print(f'estoy en la posicion: {archivo.tell()}') #en que posicion está

    



