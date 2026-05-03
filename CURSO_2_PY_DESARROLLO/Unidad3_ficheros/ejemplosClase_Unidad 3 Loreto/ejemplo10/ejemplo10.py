import json

datos = '{"Nombre":"Galletas","Precio":2.45}'
print(datos)

articulos = json.loads(datos)

print(articulos)

with open("ejemplo10\datos.json","w") as a_json:
    json.dump(articulos,a_json,indent=4)