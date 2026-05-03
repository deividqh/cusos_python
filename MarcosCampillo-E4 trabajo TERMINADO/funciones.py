import sqlite3
from clases import Propietario, Mascota

def crear_conexion():
    conexion = sqlite3.connect(("veterinario.db"))
    cursor = conexion.cursor()
    return cursor,conexion

def cerrar_conexion(conexion):
    conexion.close()

def crear_tabla_propietario(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Propietarios(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE TEXT,
        DNI TEXT,
        FECHA_NACIMIENTO TEXT,
        DIRECCION TEXT,
        EMAIL TEXT,
        FOREIGN KEY(ID) REFERENCES T_Mascotas(IDPROPIETARIO)
        );
    ''')
    conexion.commit()

def crear_tabla_mascotas(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Mascotas(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        IDPROPIETARIO INT,
        NOMBRE TEXT,
        TIPO TEXT,
        RAZA TEXT,
        FECHA_NACIMIENTO TEXT,
        PESO TEXT,
        COLOR TEXT,
        FOREIGN KEY(ID) REFERENCES T_Visitas(IDMASCOTAS)
        );
    ''')
    conexion.commit()

def crear_tabla_visitas(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Visitas(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        IDMASCOTAS INT,
        FECHA_VISITA TEXT,
        DESCRIPCION TEXT,
        TRATAMIENTO TEXT,
        FOREIGN KEY(IDMASCOTAS) REFERENCES T_Facturas(IDMASCOTAS) 
        );
    ''')
    conexion.commit()

# He cambiado las columnas y adaptado las foreign porque me era imposible obtener el id autogenerado
def crear_tabla_facturas(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Facturas(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        IDMASCOTAS INT,
        PRECIO INT
        );
    ''')
    conexion.commit()

def menu_propietarios():
    """ GENERA UN OBJETO EN LA CLASE PROPIETARIOS. LO INSERTA EN LA TABLA. SE PUEDEN MODIFICAR Y CONTAR SEGÚN LA OPCIÓN  """
    ast = "*"
    gui = "_"
    x = int(input(f"{ast*30}\n¿Qué quieres hacer?\n{gui*20}\n1. Crear Propietario\n2. Modificar Propietario\n3. Mostrar todas las mascotas de un propietario\n{ast*30}\nOpción: "))
    if x == 1:
        nombre = input("Introduce el nombre: ")
        dni = input("Introduce el DNI: ")
        fecha = input("Introduce la fecha de nacimiento: ")
        direccion = input("Introduce la dirección: ")
        email = input("Introduce el email: ")
        propietario = Propietario(" ",nombre,dni,fecha,direccion,email)
        cursor, conexion = crear_conexion()
        crear_tabla_propietario(cursor,conexion)
        cursor.execute('''
            INSERT INTO T_Propietarios(ID,NOMBRE,DNI,FECHA_NACIMIENTO,DIRECCION,EMAIL)
            VALUES(?,?,?,?,?,?);
            ''',(None,
                 propietario.get__nombre(),
                 propietario.get__dni(),
                 propietario.get__fechanacimiento(),
                 propietario.get__direccion(),
                 propietario.get__email()))
        conexion.commit()
        cerrar_conexion(conexion)
    if x == 2:
        cursor, conexion = crear_conexion()
        # Obtiene el ID de la mascota a actualizar desde el usuario
        id_propietario = input("Introduce el ID del propietario que quieres modificar: ")

        # Obtiene las nuevas propiedades de la mascota desde el usuario
        propiedades_actualizadas = {
            "NOMBRE": input("Introduce el nombre: "),
            "DNI": input("Introduce el DNI: "),
            "FECHA": input("Introduce la fecha de nacimiento: "),
            "DIRECCION": input("Introduce la dirección: "),
            "EMAIL": input("Introduce el correo electrónico: ")
        }
        cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
        # Crea una consulta SQL para actualizar la entrada especificada
        cursor.execute("""
            UPDATE T_Propietarios
            SET NOMBRE = ?, DNI = ?, FECHA_NACIMIENTO = ?, DIRECCION = ?, EMAIL = ?
            WHERE ID = ?
        """, (propiedades_actualizadas["NOMBRE"], propiedades_actualizadas["DNI"], propiedades_actualizadas["FECHA"], propiedades_actualizadas["DIRECCION"], propiedades_actualizadas["EMAIL"], id_propietario,))
        conexion.commit()

        cursor.close()  # Cierra el cursor
        cerrar_conexion(conexion) 

    if x == 3: 
        cursor, conexion = crear_conexion()
        v = input("Introduce el ID del propietario: ")   # Ejecuta la consulta SQL
        cursor.execute("""
            SELECT COUNT(idpropietario) AS NumMascotas
            FROM T_Mascotas
            WHERE idpropietario = ?
        """, (v))
        resultado = cursor.fetchone()     # Obtiene el resultado de la consulta
        num_mascotas = resultado[0]
        print(f"El propietario {v} tiene {num_mascotas} mascota(s).")
        cerrar_conexion(conexion)

def menu_mascotas():
    """ GENERA UN OBJETO EN LA CLASE MASCOTAS, LO INSERTA EN LA TABLA. SE PUEDEN MODIFICAR Y CONTAR SEGÚN LA OPCIÓN """
    ast = "*"
    gui = "_"
    y = int(input(f"{ast*30}\n¿Qué quieres hacer?\n{gui*20}\n1. Crear mascota\n2. Modificar mascota\n3. Mostrar todas las mascotas de un tipo\n{ast*30}\nOpción: "))
    if y == 1:
        nombre = input("Introduce el nombre: ")
        id_pro = input("Introduce el id del propietario: ")
        fecha = input("Introduce la fecha de nacimiento: ")
        tipo = input("Introduce la tipo: ")
        raza = input("Introduce la raza: ")
        peso = input("Introduce el peso: ")
        color = input("Introduce el color: ")
        mascota = Mascota(" ",id_pro,nombre,tipo,raza,fecha,peso,color)
        cursor, conexion = crear_conexion()
        crear_tabla_mascotas(cursor,conexion)
        cursor.execute('''
            INSERT INTO T_Mascotas(ID,IDPROPIETARIO,NOMBRE,TIPO,RAZA,FECHA_NACIMIENTO,PESO,COLOR)
            VALUES(?,?,?,?,?,?,?,?);
            ''',(None,
                 mascota.get__idpropietario(),
                 mascota.get__nombre(),
                 mascota.get__tipo(),
                 mascota.get__raza(),
                 mascota.get__fechanacimiento(),
                 mascota.get__peso(),
                 mascota.get__color()))
        conexion.commit()
        cerrar_conexion(conexion)
    if y == 2:
        cursor, conexion = crear_conexion()
        # Obtiene el ID de la mascota a actualizar desde el usuario
        id_mascota = input("Introduce el ID de la mascota que quieres modificar: ")

        # Obtiene las nuevas propiedades de la mascota desde el usuario
        propiedades_actualizadas = {
            "IDPROPIETARIO": input("Introduce el ID del propietario: "),
            "NOMBRE": input("Introduce el nombre de la mascota: "),
            "TIPO": input("Introduce el tipo de la mascota: "),
            "RAZA": input("Introduce la raza de la mascota: "),
            "FECHA_NACIMIENTO": input("Introduce la fecha de nacimiento de la mascota: "),
            "PESO": input("Introduce el peso de la mascota: "),
            "COLOR": input("Introduce el color de la mascota: ")
        }
        cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
        # Crea una consulta SQL para actualizar la entrada especificada
        cursor.execute("""
            UPDATE T_Mascotas
            SET IDPROPIETARIO = ?, NOMBRE = ?, TIPO = ?, RAZA = ?, FECHA_NACIMIENTO = ?, PESO = ?, COLOR = ?
            WHERE ID = ?
        """, (propiedades_actualizadas["IDPROPIETARIO"], propiedades_actualizadas["NOMBRE"], propiedades_actualizadas["TIPO"], propiedades_actualizadas["RAZA"], propiedades_actualizadas["FECHA_NACIMIENTO"], propiedades_actualizadas["PESO"], propiedades_actualizadas["COLOR"], id_mascota,))
        conexion.commit()

        cursor.close()  # Cierra el cursor
        cerrar_conexion(conexion)


    if y == 3:
        cursor, conexion = crear_conexion()
        t = input("Introduce el TIPO de la mascota: ")   # Ejecuta la consulta SQL
        cursor.execute("""
            SELECT COUNT(TIPO) AS NumMascotas
            FROM T_Mascotas
            WHERE TIPO = ?
        """, (t,))
        resultado = cursor.fetchone()     # Obtiene el resultado de la consulta
        num_mascotas = resultado[0]
        print(f"Hay {num_mascotas} mascota(s) del tipo {t}.")
        cerrar_conexion(conexion)

def menu_visitas():
    """ GENERA UNA VISITA, LA INSERTA EN LA TABLA. SE PUEDEN MODIFICAR Y VISUALIZAR SEGÚN LA OPCIÓN """
    ast = "*"
    gui = "_"
    z = int(input(f"{ast*30}\n¿Qué quieres hacer?\n{gui*20}\n1. Crear visita\n2. Modificar visita\n3. Borrar visita\n4. Mostrar todas las visitas de una mascota.\n{ast*30}\nOpción: "))
    if z == 1:
        visitas = []
        idmascotas = input("Introduce el id de la mascota: ")
        fecha_visita = input("Introduce la fecha de la visita: ")
        descripcion = input("Introduce la descripción de la visita: ")
        tratamiento = input("Introduce el tipo de tratamiento: ")
        visitas.append(idmascotas)
        visitas.append(fecha_visita)
        visitas.append(descripcion)
        visitas.append(tratamiento)
        cursor, conexion = crear_conexion()
        crear_tabla_visitas(cursor,conexion)
        cursor.execute('''
            INSERT INTO T_Visitas(ID, IDMASCOTAS, FECHA_VISITA, DESCRIPCION, TRATAMIENTO)
            VALUES(?,?,?,?,?);
            ''',(None,
                visitas[0],
                visitas[1],
                visitas[2],
                visitas[3]))
        conexion.commit()
        facturas = []  # Se gengera la factura conforme genera la visita, así comparten el id. Por eso la función de borrar factura 
        precio = input("Introduce el precio de la consulta: ")
        facturas.append(idmascotas)
        facturas.append(precio)
        crear_tabla_facturas(cursor,conexion)
        cursor.execute('''
            INSERT INTO T_Facturas(ID, IDMASCOTAS, PRECIO)
            VALUES(?,?,?);
            ''',(None,
                facturas[0],
                facturas[1]))
        conexion.commit()
        cursor.close()  # Cierra el cursor
        cerrar_conexion(conexion)

    if z == 2:

        cursor, conexion = crear_conexion()
        # Obtiene el ID de la mascota a actualizar desde el usuario
        id = input("Introduce el ID de la visita que quieres modificar: ")

        # Obtiene las nuevas propiedades de la mascota desde el usuario
        propiedades_actualizadas = {
            "IDMASCOTAS": input("Introduce el id de las mascota: "),
            "FECHA_VISITA": input("Introduce la Fecha de la Visita: "),
            "DESCRIPCION": input("Introduce la Descripcion de la Visita: "),
            "TRATAMIENTO": input("Introduce el Tratamiento a aplicar: ")
        }
        cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
        # Crea una consulta SQL para actualizar la entrada especificada
        cursor.execute("""
            UPDATE T_Visitas
            SET IDMASCOTAS = ?, FECHA_VISITA = ?, DESCRIPCION = ?, TRATAMIENTO = ?
            WHERE ID = ?
        """, (  propiedades_actualizadas["IDMASCOTAS"],
                propiedades_actualizadas["FECHA_VISITA"], 
                propiedades_actualizadas["DESCRIPCION"],
                propiedades_actualizadas["TRATAMIENTO"],id,))                
        conexion.commit()

        cursor.close()  # Cierra el cursor
        cerrar_conexion(conexion)
    
    if z == 3:
        cursor, conexion = crear_conexion()
        b = input("Introduce el id de la visita que quieres borrar: ")
        cursor = conexion.cursor()

        # Crea una consulta SQL para borrar la entrada especificada
        cursor.execute(f"DELETE FROM T_Visitas WHERE ID = {b}")

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Cierra la conexión a la base de datos
        cursor.close()
        cerrar_conexion(conexion)

    
    if z == 4:
        cursor, conexion = crear_conexion()
        n = input("Introduce el ID de la mascota: ")   # Ejecuta la consulta SQL
        cursor.execute("""
            SELECT COUNT(IDMASCOTAS) AS NumMascotas
            FROM T_Visitas
            WHERE IDMASCOTAS = ?
        """, (n,))
        resultado = cursor.fetchone()     # Obtiene el resultado de la consulta
        num_visitas = resultado[0]
        print(f"Hay {num_visitas} visita(s) de la mascota con ID {n}.")
        cerrar_conexion(conexion)

def menu_faturacion():
    ast = "*"
    gui = "_"
    s = int(input(f"{ast*30}\n¿Qué quieres hacer?\n{gui*20}\n1. Borrar factura\n2. Mostrar todas las facturas\n{ast*30}\nOpción: "))
    if s == 1:

        cursor, conexion = crear_conexion()
        fac = input("Introduce el id de la visita que quieres borrar: ")
        cursor = conexion.cursor()

        # Crea una consulta SQL para borrar la entrada especificada
        cursor.execute(f"DELETE FROM T_Facturas WHERE ID = {fac}")

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Cierra la conexión a la base de datos
        cursor.close()
        cerrar_conexion(conexion)

    if s == 2:

        cursor, conexion = crear_conexion()
        cursor.execute("""
            SELECT *
            FROM T_Facturas
        """)
        resultado = cursor.fetchall()     # Obtiene el resultado de la consulta
        print(resultado)
        cerrar_conexion(conexion)