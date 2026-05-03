texto = "ser O No Ser.... That's the cuestion"
print ("\n", "Ejercicios de Cadenas")
print(texto.upper())        # SER O NO SER.... THAT'S THE CUESTION
print(texto.lower())        # ser o no ser.... that's the cuestion
print(texto.capitalize())   # Ser o no ser.... that's the cuestion
print(texto.title())        # Ser O No Ser.... That'S The Cuestion
# ---------------------------------------------------------

texto = " ser O No Ser.... That's the cuestion  "
print("(i)"+texto.strip()+"(f)")        # ser O No Ser.... That's the cuestion
# ---------------------------------------------------------

texto = "  ser O No Ser.... That's the cuestion  "
print("(i)"+texto.lstrip()+ "(f)")       # ser O No Ser.... That's the cuestion
# ---------------------------------------------------------

texto = " ser O No Ser.... That's the cuestion  "
print("(i)"+texto.rstrip()+"(f)")       # ser O No Ser.... That's the cuestion
# ---------------------------------------------------------

nuevo_texto = texto.replace("Ser", "estar")
print(nuevo_texto)  
# ---------------------------------------------------------

lista = texto.split(",")
print(lista)
# ---------------------------------------------------------

lista = texto.split(" ")
print(lista)
# ---------------------------------------------------------

lista = texto.strip().split(" ")
print(lista)
# ---------------------------------------------------------

lista = ['Hola', 'Mundo', 'Python']
texto = " ".join(lista)
print(texto)  # Hola Mundo Python
# ---------------------------------------------------------

texto = "Hola Mundo"
print(texto.find("Mundo"))  # 5
print(texto.index("Mundo"))  # 5

# Si no encuentra el texto:
print(texto.find("Python"))  # -1
# print(texto.index("Python"))  # Generaría un error
# ---------------------------------------------------------
texto = "Hola Mundo"
print(texto.startswith("Hola"))  # True
print(texto.endswith("Mundo"))   # True
# ---------------------------------------------------------
texto = "Hola Hola Hola"
print(texto.count("Hola"))  # 3
# ---------------------------------------------------------
texto = "Hola"
numero = "12345"
alphanum = "Hola123"

print(texto.isalpha())  # True (solo letras)
print(numero.isdigit())  # True (solo números)
print(alphanum.isalnum())  # True (letras y números)
# ---------------------------------------------------------

texto = "Hola Mundo"
print(len(texto))  # 10
# ---------------------------------------------------------
nombre = "Juan"
edad = 30
texto = "Me llamo {} y tengo {} años".format(nombre, edad)
print(texto)  # Me llamo Juan y tengo 30 años
print(f"Me llamo {nombre} y tengo {edad} años")  # Me llamo Juan y tengo 30 años
