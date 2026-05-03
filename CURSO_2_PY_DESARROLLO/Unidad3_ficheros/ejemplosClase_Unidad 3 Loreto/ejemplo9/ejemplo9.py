import json

#Lista de diccionarios
productos=[{"nombre":"Galletas","precio":2.99},
           {"nombre":"Arroz","precio":1.25},
           {"nombre":"Pan","precio":0.50},
           {"nombre":"Huevos","precio":3},
           {"nombre":"Leche","precio":1.50},
           {"nombre":"Harina","precio":2.99},
           {"nombre":"Cereales","precio":3.99}]

#Escribir
try:
    with open("compra.json","w") as a_json:
        json.dump(productos,a_json,indent=4)
except Exception as e:
    print(f"Error: {e}")
    
#Imprimir json formateado
try:
    with open("compra.json","r") as a_json:
        datos = json.load(a_json)
        
        #Imprimir datos
        for producto in datos:
            print(f"Nombre: {producto["nombre"]}  Precio: {producto["precio"]}")
            print("-"*30)
except Exception as e:
    print(f"Error: {e}")

