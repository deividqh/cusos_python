import json

#Crear un diccionario
persona = {"nombre":"Loreto Peleñin",
           "ciudad":"Murcia",
           "hobbies":["Padel","Leer","programar en Python :D"],
           "contacto":{
               "email":"profesor3@avanzaformacion.org",
               "telefono":"666190181"
           }}

#Escribir el diccionario en el archivo JSON
try:
    with open("datos2.json","w",encoding="utf-8") as a_json:
        #Indent = tabulacion, mejora legibilidad
        json.dump(persona,a_json, indent=4)
except Exception as e:
    print(f"Error: {e}")
    
#Leer json
try:
    with open("datos2.json","r",encoding="utf-8") as a_json:
        datos = json.load(a_json)
        print(datos)
except Exception as e:
    print(f"Error: {e}")

#Modificacion
try:
    with open("datos2.json","r",encoding="utf-8") as a_json:
        datos = json.load(a_json)
        
    #Modifico el valor
    datos["nombre"]="Loreto Pelegrín"
    
    
    with open("datos2.json","w",encoding="utf-8") as a_json:
        #Vuelvo a escribir datos en el fichero
        json.dump(datos,a_json,indent=4)
except Exception as e:
    print(f"Error: {e}")