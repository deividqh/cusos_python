import sqlite3

def crear_conexion():
    conexion = sqlite3.connect(r"ejemplo2\biblioteca.db")
    cursor = conexion.cursor()
    return cursor,conexion

def crear_tabla_libros(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Libros(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Autor TEXT,
        Publicacion INT
        );
    ''')
    conexion.commit()

def anadir_libro(cursor,conexion,id,titulo,autor,publicacion):
    cursor.execute("INSERT INTO T_Libros VALUES (?,?,?,?)",(id,titulo,autor,publicacion))
    conexion.commit()

def anadir_lista_libros(cursor,conexion,lista):
    cursor.executemany("INSERT INTO T_Libros VALUES(?,?, ?, ?)", lista)
    conexion.commit()

def mostrar_datos(cursor):
    cursor.execute("SELECT * FROM T_Libros")
    print(cursor.fetchall())
    

def busca_autor(cursor):
    cursor.execute('''
    SELECT * 
    FROM T_Libros
    WHERE Autor = "Jane Austen"''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
        
def busca_autor_argumento(cursor,autor):
    cursor.execute('''
    SELECT * 
    FROM T_Libros
    WHERE Autor = ?;
    ''',(autor,))
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    
    


def cerrar_conexion(conexion):
    conexion.close()



