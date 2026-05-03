# Tipos de lecturas que existen ficheros python
class Galleta():
    def __init__(self, marca, sabor):
        self.marca=marca
        self.sabor= sabor
        pass
    
    def __str__(self):
        return f'Galleta de marca {self.marca} y sabor {self.sabor}'

def crear_galleta(nombre_archivo, lista_galetas):
    # lista_galletas=[]
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            marca,sabor = linea.split(",")
            galleta=Galleta(marca=marca, sabor=sabor)
            lista_galetas.append(galleta)

    return lista_galletas

lista_galletas=[]
newGalleta=crear_galleta(nombre_archivo="desarrolloConPython/Unidad3_ficheros/ejemplo3/texto.txt", 
                         lista_galetas=lista_galletas)
for galleta in lista_galletas:
    print(galleta.marca)