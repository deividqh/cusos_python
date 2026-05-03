import csv

try:
    # Leer
    with open("ejemplo7\perros.csv", 'r', encoding="utf-8") as a_csv:
        lector_csv=csv.reader(a_csv)
        filas = list(lector_csv)

    nuevo_peso=23.7
    filas[3][6]=nuevo_peso

    # Escribir:
    with open("ejemplo7\perros.csv", 'a', encoding="utf-8", newline='') as a_csv:
        escribir_csv = csv.writer(a_csv)
        escribir_csv.writerows(filas)    

except:
    pass