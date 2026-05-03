#write:
# w: Archivo en modo escritura. Sobreescribe el texto que hay en el fichero

with open("ejemplo4/datos.txt","w",encoding="utf-8",newline='') as archivo:
    archivo.write("Árbol, camión y ñandú\n")
    
#a: Abre el archivo en modo añadir. El nuevo contenido se añade al final
with open("ejemplo4/datos.txt","a",encoding="utf-8",newline='') as archivo:
    archivo.write("Pelota, tenis, agua y ratón")
    
#writelines: Escribir multiples lineas a la vez. 
# La lista debe contener las linas de cadenas de texto
with open("ejemplo4/datos1.txt","a",encoding="utf-8") as archivo:
    lista = ["Loreto Pelegrín Castillo\n","Teo Gomariz Ferrero\n", "Pablo Ortiz Hernaiz\n"]
    archivo.writelines(lista)

#Leer datos1.txt
with open("ejemplo4/datos1.txt","r",encoding="utf-8") as archivo:
    lista_nombres = []
    for linea in archivo:
        nombre,apellido1,apellido2 = linea.split()
        lista_nombres.append(nombre)
    
for name in lista_nombres:
    print(name)
    
#Datos formateados
nombre = "Alex"
apellido1 ="Martinez"
apellido2 = "López"

with open("ejemplo4/datos2.txt","a",encoding="utf-8") as archivo:
    archivo.write(f"Nombre: {nombre} Apellido: {apellido1} Apellido: {apellido2}")    






