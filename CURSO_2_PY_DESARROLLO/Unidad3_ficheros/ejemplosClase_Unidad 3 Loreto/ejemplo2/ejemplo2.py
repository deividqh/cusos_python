#read(): Lee todo el contenido del archivo y lo devuelve como una cadena
with open("ejemplo2/texto.txt","r",encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
    
#readline(): Lee una linea de un archivo cada vez
with open("ejemplo2/texto.txt","r",encoding="utf-8") as fichero:
    linea = fichero.readline()
    while linea:
        print(linea)
        linea = fichero.readline()
        
#readlines(): Lee todas las lineas del archivo y devuelve una lista
with open("ejemplo2/texto.txt","r",encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas)
    for linea in lineas:
        print(linea)
    