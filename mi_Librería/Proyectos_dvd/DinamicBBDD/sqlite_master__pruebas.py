import sqlite3

def explorar_sqlite_master(nombre_bd):
    # Conectar a la base de datos
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()
    
    # Consultar sqlite_master
    cursor.execute("SELECT type, name, tbl_name, sql FROM sqlite_master ORDER BY name;")
    resultados = cursor.fetchall()
    
    # Imprimir resultados
    for tipo, nombre, tabla, sql in resultados:
        print(f"Tipo: {tipo}")
        print(f"Nombre: {nombre}")
        print(f"Tabla asociada: {tabla}")
        print(f"SQL de creación: {sql}\n")
    
    # Cerrar conexión
    conexion.close()

# Llamar a la función
explorar_sqlite_master("mi_base_de_datos.db")
