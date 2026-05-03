import sqlite3

lista_libros = [
    (None, 'El señor de los Anilllos', '', 2000),
    (None, 'El señor de los Anilllos 2', '', 2002),
    (None, 'El señor de los Anilllos 3', '', 2003),
    (None, 'Psicosis', '', 1975)
]

def crear_conexion():
    conexion = sqlite3.connect(r'biblio.db')
    cursor = conexion.cursor()
    return cursor, conexion

def crear_tabl_libros(conexion, cursor):
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS T_libros(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        titulo TEXT, 
        autor TEXT, 
        publicacion INT
    )
    """)
    conexion.commit()

def add_libro(conexion, cursor, id, titulo, autor, publicacion):
    cursor.execute(''' INSERT INTO T_libros VALUES (?, ?, ?, ?);''', (id, titulo, autor, publicacion) )
    conexion.commit()

def add_lista_libro(conexion, cursor, lista):
    cursor.executemany(''' INSERT INTO T_libros VALUES (?, ?, ?, ?);''', lista )
    conexion.commit()

def cerrar_conexion(conexion):
    conexion.close()

def mostrar_datos(cursor):
    cursor.execute(""" SELECT * FROM T_libros """)
    lst_filas = cursor.fetchall()
    for fila in lst_filas:
        print(fila)

def busca_autor_argumento(cursor, autor):
    cursor.execute(""" SELECT * FROM T_libros WHERE autor = ?; """, (autor,))
    
    lst_filas = cursor.fetchall()
    for fila in lst_filas:
        print(fila)

def busca_autor(cursor):
    cursor.execute(""" 
        SELECT * FROM T_libros WHERE autor='Prejuicio'
    """)
    
    lst_filas = cursor.fetchall()
    for fila in lst_filas:
        print(fila)

def actualizar_datos(cursor, conexion):
    cursor.execute(""" UPDATE T_libros SET Autor='Prejuiciososo' WHERE autor='Prejuicio' """)
    conexion.commit()

def borrar_datos(cursor, conexion):
    cursor.execute(""" DELETE T_libros FROM T_libros WHERE autor='Prejuicio' """)
    conexion.commit()

# _________________________________________________
cursor, conexion = crear_conexion()
crear_tabl_libros(conexion=conexion, cursor=cursor)
conexion.commit()
add_libro(conexion=conexion, cursor=cursor, id=None, titulo='Orgulloso', autor='Prejuicio', publicacion=1813)
add_libro(conexion=conexion, cursor=cursor, id=None, titulo='La Edad del', autor='Missing', publicacion=2024)
mostrar_datos(cursor)
busca_autor(cursor=cursor)
busca_autor_argumento(cursor=cursor, autor='Prejuicio')
add_lista_libro(conexion=conexion, cursor=cursor, lista=lista_libros)
actualizar_datos(cursor=cursor,conexion=conexion)

cerrar_conexion(conexion)