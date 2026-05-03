import sqlite3
def crear_conexion():
    conexion = sqlite3.connect(r"ejer3/curso.db")
    cursor = conexion.cursor()
    return cursor, conexion

def crear_tabla_ordenador(cursor, conexion):
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS T_ordenador( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT,
                modelo TEXT
        );
    ''')
    
    conexion.commit()
def crear_tabla_alumno(cursor, conexion):
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS T_alumno( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                dni TEXT,
                id_ordenador INTEGER, 
                Foreign Key(id_ordenador) References T_ordenador(id)                                
                );
        """)
    conexion.commit()


def anadir_ordenador(cursor, conexion):
    cursor.executemany(""" INSERT INTO T_ordenador(id, marca, modelo) VALUES(?,?,?) """ , 
        [ (None, 'del', 'inspiron'),
        (None, 'del2', 'inspiron2'),
        (None, 'del3', 'inspiron3'),
        (None, 'del4', 'inspiron4'),
        (None, 'del5', 'inspiron5'),
        (None, 'del6', 'inspiron6')
        ]
    )
    conexion.commit()

def anadir_alumno(cursor, conexion):
    cursor.executemany(""" INSERT INTO T_alumno(id, nombre, apellido, dni, id_ordenador) VALUES(?,?,?,?,?) """, 
        [ (None, 'ana', 'aana', 'dana', 11),
        (None, 'ana2', 'aana2', 'dana2', 22),
        (None, 'ana3', 'aana3', 'dana3', 33),
        (None, 'ana4', 'aana4', 'dana4', 44),
        (None, 'ana5', 'aana5', 'dana5', 55),
         
        ]
    )
    conexion.commit()

def mostrar_alumno_ordenador(cursor):
    cursor.execute(""" 
        SELECT 
            A.nombre, A.apellido, A.dni, O.marca, O.modelo
        FROM T_alumno A
        INNER JOIn T_ordenador O ON A.id_ordenador=O.id;            
     """
  )
    filas = cursor.fetchall()
    print( [fila  for fila in filas] , end = '\n' )



cursor, conexion = crear_conexion()

# crear_tabla_ordenador(cursor=cursor, conexion=conexion)
# crear_tabla_alumno(cursor=cursor, conexion=conexion)
# anadir_alumno(cursor=cursor, conexion=conexion)
# anadir_ordenador(cursor=cursor, conexion=conexion)

mostrar_alumno_ordenador(cursor=cursor)
conexion.close()
