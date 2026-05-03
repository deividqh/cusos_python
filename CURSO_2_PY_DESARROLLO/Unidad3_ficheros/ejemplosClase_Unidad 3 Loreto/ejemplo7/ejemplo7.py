import csv
ruta = r"C:\Users\Usuario\Desktop\PythonII\Unidad 3\ejemplo7\perros.csv"

#Lectura sola
def leer():
    try:
        #Leer
        with open("ejemplo7\perros.csv","r",encoding="utf-8") as a_csv:
            lector_csv = csv.reader(a_csv)
            for fila in lector_csv:
                print(fila)
    except FileNotFoundError:
        print("Error: No se ha encontrado el archivo")
    except Exception as e:
        print(f"Error: {e}")


#Lectura formateada  
def leer_formateado():
    try:
        #Leer
        with open("ejemplo7\perros.csv","r",encoding="utf-8") as a_csv:
            lector_csv = csv.reader(a_csv)
            #Almaceno los encabezados en una lista
            encabezados = next(lector_csv)
            for fila in lector_csv:
                print(f"{encabezados[0]}:{fila[0]},{encabezados[1]}:{fila[1]},{encabezados[2]}:{fila[2]}")
    except FileNotFoundError:
        print("Error: No se ha encontrado el archivo")
    except Exception as e:
        print(f"Error: {e}")
    
#Añadir una fila
def anadir_fila():
    try:
        #Leer
        with open("ejemplo7\perros.csv","a",encoding="utf-8",newline="") as a_csv:
            escribir_csv = csv.writer(a_csv)
            nueva_fila = ["Ellie",1,"Border Collie",18.8,"Mediano","Blanco y negro","No","Si"]
            escribir_csv.writerow(nueva_fila)
    except FileNotFoundError:
        print("Error: No se ha encontrado el archivo")
    except Exception as e:
        print(f"Error: {e}")
    
#Modificación
def modificar():
    try:
        #Leer
        with open("ejemplo7\perros.csv","r",encoding="utf-8") as a_csv:
            lector_csv = csv.reader(a_csv)
            filas = list(lector_csv)
               
        nuevo_peso = 23.7
        filas[6][3]= nuevo_peso
        
        #Escribir
        with open("ejemplo7\perros.csv","w",encoding="utf-8",newline="") as a_csv:
            escribir_csv = csv.writer(a_csv)
            escribir_csv.writerows(filas)
        
    except FileNotFoundError:
        print("No se encuentra el directorio o el archivo")
        
modificar()
leer()