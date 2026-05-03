""" 
    Cómo se puede utilizar un diccionario para almacenar empleados agrupados por departamento.
"""
def ejercicioDiccionario01():
    empleados_por_depto = {
        "Recursos Humanos": ["Ana", "Carlos", "Luis"],
        "Desarrollo": ["Juan", "María", "Pedro"],
        "Ventas": ["Lucía", "Javier", "Sofía"]
    }

    for departamento, empleados in empleados_por_depto.items():
        print(f"Departamento: {departamento}")
        print(f"Empleados: {', '.join(empleados)}")

# ----------Uso:
# ejercicioDiccionario01()


""" 
Este ejemplo muestra cómo gestionar un inventario de productos con sus cantidades utilizando un diccionario. 
"""
def ejercicioDiccionario02():
    inventario = {
        "Laptops": 50,
        "Teléfonos": 120,
        "Tabletas": 75
    }

    inventario["Laptops"] -= 10  # Se vendieron 10 laptops
    inventario["Teléfonos"] += 20  # Se recibieron 20 teléfonos nuevos

    for producto, cantidad in inventario.items():
        print(f"Producto: {producto}, Cantidad: {cantidad}")

# ----------Uso:
# ejercicioDiccionario01()


""" 
Este ejemplo maneja un diccionario donde se almacenan los salarios de los empleados y se calcula el salario promedio.
"""
def ejercicioDiccionario03():
    salarios = {
        "Ana": 3000,
        "Carlos": 3500,
        "María": 4000,
        "Pedro": 4500
    }

    total_salarios = sum(salarios.values())
    promedio = total_salarios / len(salarios)
    print(f"El salario promedio es: {promedio}")

# ------Uso:
ejercicioDiccionario03() 
 
     
"""
 Este ejemplo ilustra cómo usar tuplas para almacenar las coordenadas de distintas oficinas de la empresa. 
"""
def ejercicioTupla01():
    oficinas = {
        "Madrid": (40.416775, -3.703790),
        "Nueva York": (40.712776, -74.005974),
        "Tokio": (35.676192, 139.650311)
    }

    for ciudad, coordenadas in oficinas.items():
        print(f"Ciudad: {ciudad}, Coordenadas: {coordenadas}")

# ------Uso:
ejercicioTupla01()

"""
 Usamos tuplas para almacenar detalles inmutables de pedidos como número de pedido y fecha. 
"""
def ejercicioTupla02():
    pedidos = [
        (1001, "2024-01-01"),
        (1002, "2024-01-03"),
        (1003, "2024-01-05")
    ]

    for pedido in pedidos:
        print(f"Número de pedido: {pedido[0]}, Fecha: {pedido[1]}")
# ------Uso:
ejercicioTupla02()

"""
 Un ejemplo donde las tuplas almacenan los horarios de reuniones para evitar modificaciones. 
"""
def ejercicioTupla03():
    reuniones = [
        ("Lunes", "10:00 AM"),
        ("Martes", "11:00 AM"),
        ("Viernes", "03:00 PM")
    ]

    for dia, hora in reuniones:
        print(f"Reunión el {dia} a las {hora}")
# ------Uso:
ejercicioTupla03()


"""
 Este ejemplo ilustra cómo manejar una lista de tareas pendientes y cómo marcar tareas como completadas. 
"""
def ejercicioLista01():
    tareas = ["Preparar informe", "Llamar a cliente", "Actualizar inventario"]

    tareas_completadas = tareas.pop(0)  # Completa la primera tarea

    print(f"Tarea completada: {tareas_completadas}")
    print(f"Tareas restantes: {tareas}")
# ------Uso:
ejercicioLista01()


"""
 Se utiliza una lista para manejar los nombres de los miembros de un equipo y asignar nuevos integrantes. 
"""
def ejercicioLista02():
    equipo = ["Ana", "Carlos", "María"]
    
    equipo.append("Pedro")  # Se añade un nuevo miembro al equipo
    equipo.remove("Carlos")  # Carlos deja el equipo
    
    print(f"Equipo actualizado: {equipo}")
# ------Uso:
ejercicioLista02()

""" 
Se usa una lista para registrar las calificaciones de rendimiento de
empleados y calcular la calificación promedio.   
"""
def ejercicioLista03():
    calificaciones = [8.5, 9.0, 7.5, 8.0, 9.5]
    
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Calificación promedio: {promedio}")

# ------Uso:
ejercicioLista03()
