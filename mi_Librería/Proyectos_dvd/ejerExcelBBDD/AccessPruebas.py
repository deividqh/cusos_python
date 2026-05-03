# pip install pyodbc
import pyodbc

print("Drivers ODBC")
print(pyodbc.drivers())
print("\n"*2)

import struct
# Si el resultado es 32, estás usando Python de 32 bits; si es 64, estás usando Python de 64 bits.
print(struct.calcsize("P") * 8)


pathArchivoAccess=r"C:\Users\pc\Desktop\Personal\ExcelDVD\CONTROL-PADEL\RRH_PaddelREAL.accdb"

import platform
print(f"num bits en el sistema: {platform.architecture()[0]}")

def conectar_access():
    # Ruta a la base de datos Access
    # database_path = pathArchivoAccess
    # database_path =r'C:\Users\pc\Desktop\Personal\ExcelDVD\CONTROL-PADEL\RRH_PaddelREAL.accdb'
    database_path =pathArchivoAccess

    # Conectar usando el controlador ODBC de Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={pathArchivoAccess};'
    )

    try:
        # Establecer la conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Ejecutar una consulta SQL (ejemplo: leer una tabla)
        cursor.execute('SELECT * FROM Clases')

        # Obtener los resultados de la consulta
        filas = cursor.fetchall()

        # Imprimir los resultados
        for fila in filas:
            print(fila)

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

# ------ Llamar la función para conectar a la base de datos
conectar_access()



def insertar_datos_access():
    # Ruta a la base de datos Access
    database_path = pathArchivoAccess

    # Conectar usando el controlador ODBC de Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={database_path};'
    )

    try:
        # Establecer la conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Consulta para insertar datos (ajusta los nombres de columna y valores)
        cursor.execute('''
            INSERT INTO nombre_de_la_tabla (columna1, columna2)
            VALUES (?, ?)
        ''', (valor1, valor2))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al insertar datos: {e}")

# ------ Llamar la función para insertar datos
# insertar_datos_access()


def actualizar_datos_access():
    # Ruta a la base de datos Access
    # database_path = r'C:\ruta\hacia\tu_base_de_datos.accdb'
    database_path = pathArchivoAccess


    # Conectar usando el controlador ODBC de Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={database_path};'
    )

    try:
        # Establecer la conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Consulta para actualizar datos (ajusta los nombres de columna y condiciones)
        cursor.execute('''
            UPDATE nombre_de_la_tabla
            SET columna1 = ?
            WHERE columna2 = ?
        ''', (nuevo_valor, valor_existente))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al actualizar datos: {e}")

# ------ Llamar la función para actualizar datos
# actualizar_datos_access()



def eliminar_datos_access():
    # Ruta a la base de datos Access
    # database_path = r'C:\ruta\hacia\tu_base_de_datos.accdb'
    database_path = pathArchivoAccess

    # Conectar usando el controlador ODBC de Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={database_path};'
    )

    try:
        # Establecer la conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Consulta para eliminar datos (ajusta las condiciones)
        cursor.execute('''
            DELETE FROM nombre_de_la_tabla
            WHERE columna1 = ?
        ''', (valor,))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al eliminar datos: {e}")

# ------ Llamar la función para eliminar datos
# eliminar_datos_access()


from openpyxl import Workbook

def exportar_access_a_excel():
    # Conectar a la base de datos Access
    database_path = r'C:\ruta\hacia\tu_base_de_datos.accdb'
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={database_path};'
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Ejecutar una consulta para obtener los datos
        cursor.execute('SELECT * FROM nombre_de_la_tabla')
        filas = cursor.fetchall()

        # Crear un archivo Excel
        wb = Workbook()
        hoja = wb.active
        hoja.title = "Datos Access"

        # Escribir los encabezados de las columnas
        encabezados = [i[0] for i in cursor.description]
        hoja.append(encabezados)

        # Escribir los datos en la hoja de Excel
        for fila in filas:
            hoja.append(fila)

        # Guardar el archivo Excel
        wb.save("datos_exportados_access.xlsx")

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al exportar datos: {e}")

# ------ Llamar la función para exportar los datos
# exportar_access_a_excel()
