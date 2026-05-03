try: 
    with open("ejemplo5/datos7.txt","w",encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se ha encontrado")
except PermissionError:
    print("No tienes permiso de acceso al archivo")
except IOError as e:
    print(f"Error: {e}")

    