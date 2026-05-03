import sqlite3

#Crear la conexion y si no existe la base de datos se crea
conexion = sqlite3.connect(r"ejemplo1\biblioteca.db")

#Crear cursor - ejecuta las sentencias SQL
cursor = conexion.cursor()

#Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Libros(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Autor TEXT,
        Publicacion INT
        );
    ''')

#Añadir elementos
cursor.execute('''
        INSERT INTO T_Libros VALUES (
            NULL,
            'Orgullo y Prejuicio',
            'Jane Austen',
            1813
        );
    ''')

#Guardar en base de datos
conexion.commit()

cursor.execute('SELECT * FROM T_Libros;')
print(cursor.fetchall())

cursor.execute("SELECT * FROM T_Libros")
print(cursor.fetchall())

conexion.close()