
#Version 1
fichero = open("ejemplo1/hola.txt","r")
fichero.seek(0)
print(fichero.tell())
print(fichero.read())
print(fichero.tell())
fichero.close()

#Version 2
with open("ejemplo1/adios.txt","r") as archivo:
    archivo.seek(5)
    print(archivo.tell())
    print(archivo.read())
    print(archivo.tell())
    
