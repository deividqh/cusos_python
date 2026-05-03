
import os
os.system('cls')

""" C S V  
w: Sobrescribe el fichero desde el seek(0) (inicial) , si no existe el archivo, lo crea

"""
import csv

# =========================
# Abre y Lee.
nameFile="desarrolloConPython/Unidad3_ficheros/ejemplo6/personas.csv"
with open(file=nameFile, 
            mode="r", 
            encoding="utf-8") as fichero:    

    lineas = csv.reader(fichero)
    # Saltar la cabecera
    next(lineas)

    for linea in lineas:
        print(linea)

    print(f'estoy en la posicion: {fichero.tell()}') #en que posicion está


"""
Escritura """
datos=['Kike', 40, "Murcia", 609361573]
datos1=['Paco', 50, "Beniajan", 611555445]

with open(file=nameFile, 
            mode="a", 
            newline='',         
            encoding="utf-8"
            ) as fichero:
    
    escribir=csv.writer(fichero, delimiter=",")
    escribir.writerow(datos1)