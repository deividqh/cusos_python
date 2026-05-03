#Ejercicio 1: Crear un programa para contar las palabras de un fichero.

def contar_palabras(nombre_archivo):

    contador_palabras = 0
    try:
        with open(n_archivo, 'r') as archivo:
            for linea in archivo:
                palabras = linea.split()
                contador_palabras += len(palabras)
        return contador_palabras
    except FileNotFoundError:
        print("No se encontro el fichero")
        
n_archivo = "ejercicioclase1\ejercicio1.py"
total_palabras = contar_palabras(n_archivo)
print("El archivo contiene", total_palabras, "palabras.")