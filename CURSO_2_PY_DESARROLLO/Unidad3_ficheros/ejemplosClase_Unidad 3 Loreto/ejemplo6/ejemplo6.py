import csv
        
#Escritura
datos = ["Kike",40,"Murcia",666190181]

datos1 = [["Kike",40,"Murcia",666190181],
          ["Paco",40,"Beniajan",666190181]]

with open("ejemplo6\personas.csv","a",newline='') as fichero:
    escribir = csv.writer(fichero,delimiter=";")
    escribir.writerow(datos)
    
#Lectura
with open("ejemplo6\personas.csv","r",newline="") as fichero:
    lineas = csv.reader(fichero)
    #Saltar la cabecera
    #next(lineas)
    for linea in lineas:
        print(linea)