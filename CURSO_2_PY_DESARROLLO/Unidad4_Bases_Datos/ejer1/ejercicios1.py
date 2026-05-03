import sqlite3
"""     I N S T A L A R   L A S    E X T E N S I O N E S
1-SQLITE VIEWER = visualizador de datos sqlite
2-better-python-string-sql

Instalada por mi en mi Pc
SQLite3 Editor

 """

# Crear la conexion y si no existe la base de datos, se crea.
conexion=sqlite3.connect(r"ejer1\biblioteca.db")

# Crear cursor - Ejecuta las sentencias de sql
cursor=conexion.cursor()
#Crear tabla 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS T_libros(
        Id INTEGER PRIMARY KEY AUTOINCREMENT ,
        Titulo TEXT, 
        Autor TEXT, 
        Publicacion INT
    );
 """)

# Añadir elementos
cursor.execute(""" 
    INSERT INTO T_libros VALUES (NULL, 'Orgullo', 'Prejuicio', 1813)
 """)

# Guardar en la base de datos
conexion.commit()
# Seleccion basica
cursor.execute(""" SELECT * FROM T_libros """)

# Muestra todos los valores
print(cursor.fetchall())


conexion.close


