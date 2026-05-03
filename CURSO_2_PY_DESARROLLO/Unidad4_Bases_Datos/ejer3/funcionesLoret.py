import sqlite3

def crear_conexion():
    conexion = sqlite3.connect(r"eje3\curso.db")
    cursor = conexion.cursor()
    return cursor,conexion

def crear_tabla_ordenador(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Ordenador(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Marca TEXT,
        Modelo TEXT
        );
    ''')
    conexion.commit()
    
def crear_tabla_alumno(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Alumno(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        Apellidos TEXT,
        DNI TEXT,
        Id_Ordenador INT,
        Foreign Key (Id_Ordenador) REFERENCES T_Ordenador(Id)
        );
    ''')
    conexion.commit()
    
    
def anadir_ordenador(cursor,conexion):
    cursor.executemany('''
        INSERT INTO T_Ordenador(Id,Marca,Modelo)
        VALUES(?,?,?);
    ''',[
        (None,'Dell','Inspirion'),
        (None,'MSI','Katana'),
        (None,'HP','Pavilion')
        ])
    conexion.commit()
    
def anadir_alumno(cursor,conexion):
    cursor.executemany('''
        INSERT INTO T_Alumno(Id,Nombre,Apellidos,DNI,Id_Ordenador)
        VALUES(?,?,?,?,?);
    ''',[
        (None,'Loreto','Pelegrin Castillo','48660787D',2),
        (None,'Fran','Navarro Cayuela','11111111H',1)
        ])
    conexion.commit()
    
def mostrar_ordenadores(cursor):
    
    cursor.execute('''
    SELECT Marca,Modelo
    FROM T_Ordenador;
    ''')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


def mostrar_alumno_ordenador(cursor):
    cursor.execute('''
    SELECT 
        A.Nombre,
        A.Apellidos,
        A.DNI,
        O.Marca,
        O.Modelo
    FROM T_Alumno A
    INNER JOIN
        T_Ordenador O ON A.Id_Ordenador = O.Id;
''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


    
def cerrar_conexion(conexion):
    conexion.close()
    

cursor,conexion = crear_conexion()
crear_tabla_ordenador(cursor,conexion)
crear_tabla_alumno(cursor,conexion)
anadir_ordenador(cursor,conexion)
anadir_alumno(cursor,conexion)
mostrar_alumno_ordenador(cursor)
cerrar_conexion(conexion)