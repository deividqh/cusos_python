class Galleta:
    def __init__(self,marca,sabor):
        self.marca = marca
        self.sabor = sabor
        
    def __str__(self):
        return f"Galleta de marca {self.marca} y su sabor {self.sabor}"

def crear_galletas(nombre_archivo,lista_galletas):  
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            marca, sabor = linea.split(",")
            galleta = Galleta(marca,sabor)
            lista_galletas.append(galleta)
    return lista_galletas

def mas_galletas(nombre_archivo):
    with open(nombre_archivo,"a") as archivo:       
        archivo.write("\nLidl,Saladitas")
  
def more_galletas(nombre_archivo):
    with open(nombre_archivo,"a") as archivo:
        marca,sabor = input("Introduce sabor y marca separado por espacio").split()
        archivo.write(f"\n{marca},{sabor}")      
        

#Main
lista_galletitas = []
ruta = "ejemplo3-Galleta/datos.txt"
lista_galletitas = crear_galletas(ruta,lista_galletitas)

mas_galletas(ruta)
   
for galletita in lista_galletitas:
    print(galletita)      
    
