# Ejercicios Diccionarios

""" Ejercicio 1:
A. Crear un diccionario para representar un inventario de una frutería.
Ej.: Manzanas = 3, Peras=4, Naranjas = 8
B. Acceder a un valor específico de Peras.
C. Agregar un nuevo elemento.
D. Modificar un valor existente.
E. Mostrar las claves del inventario. (Nombres de la fruta)
F. Mostrar los valores del inventario. (Cantidad de fruta)
G. Mostrar el inventario completo, nombres y cantidad.
H. Verificar la existencia de uvas en el inventario.
 """
# A-Crear un diccionario para representar un inventario de una frutería.
print("ejercicio 1 A")
dictFruteria={"Manzanas":3,"Peras":4,"Naranjas":8}
print("-"*20)

# B-Acceder a un valor específico de Peras.
print("ejercicio 1 B")
print(f'B- {dictFruteria["Peras"]}')
print("-"*20)

# C. Agregar un nuevo elemento-
print("ejercicio 1 C")
dictFruteria["platano"]=7
print("-"*20)

# D-. Modificar un valor existente.
print("ejercicio 1 D")
dictFruteria["Peras"]=6
print("-"*20)

# E. Mostrar las claves del inventario. (Nombres de la fruta)
print("ejercicio 1 E")
print(dictFruteria.keys())
print("-"*20)

# F. Mostrar los valores del inventario. (Cantidad de fruta)
print("ejercicio 1 F")
print(dictFruteria.values())
print("-"*20)

# G. Mostrar el inventario completo, nombres y cantidad.
print("ejercicio 1 G")
for f,c in dictFruteria.items():
    print(f'Fruta: {f}, Cantidad:{c}')
print("-"*20)

# H. Verificar la existencia de uvas en el inventario.
print("ejercicio 1 H")
bmatch=False
for f in dictFruteria.keys():
    if f=="uvas":      
        bmatch=True
        break
print(f'Fruta: {f}, Encontrada!!') if bmatch==True else print("No encontrada")
print("-"*20)
# print (dictFruteria)

""" Ejercicio 2:
"""
# A. Crear un diccionario de estudiantes con sus calificaciones.
# Ej. Juan = Matemáticas: 9, Historia: 8, Lengua: 7
# alumnos={nombre:{asignatura:nota}}
print("ejercicio 2 A")
dictAlumnos={}
dictAlumnos["Juan"]=[{"matematicas":9},{"Historia":8},{"Lengua":7}]
dictAlumnos["Ana"]=[{"matematicas":8},{"Historia":9},{"Lengua":9}]
dictAlumnos["Loreto"]=[{"matematicas":5},{"Historia":10},{"Lengua":9}]

print(dictAlumnos)
print("-"*20)
# B. Acceder a una calificación específica. 
# pej acceder a Ana/Historia
print("ejercicio 2 B")
listNotas = dictAlumnos["Ana"]
for d in listNotas:
    for a,n in d.items():
        if a=="Historia":
            print(a, n)
            break
print("-"*20)
# C. Mostrar el contenido del diccionario para que quede de la siguiente manera: 
# Las notas de juan son:
# matematicas:9
# historia:8
# lengua:7
# la nota media es 8.0
# las notas de ana son:
# matematicas:8
# historia:9
# lengua:9
# la nota media es 8.0
# las notas de Loreto son:
# matematicas:5
# historia:10
# lengua:9
# la nota media es 8.0
print("ejercicio 2 C")
for alumno in dictAlumnos:
    nota = 0
    print(f"las notas de {alumno} son:")
    for d in dictAlumnos[alumno]:
        
        for a,n in d.items():
            print(f"{a}: {n}")
            nota+=n
    print(f'la media de {alumno} es:{round(nota/len(dictAlumnos[alumno]),2)}')
print("-"*20)

