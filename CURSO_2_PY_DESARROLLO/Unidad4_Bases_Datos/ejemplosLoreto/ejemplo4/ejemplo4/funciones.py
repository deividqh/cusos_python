import sqlite3

def crear_conexion():
    conexion = sqlite3.connect(r"ejemplo4\curso.db")
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
        (None,'Dell','Inspirion'),
        (None,'Dell','Inspirion'),
        (None,'Dell','Inspirion'),
        (None,'MSI','Katana'),
        (None,'MSI','Katana'),
        (None,'HP','Pavilion'),
        (None,'HP','Pavilion'),
        (None,'HP','Pavilion')
        ])
    conexion.commit()
    
def anadir_alumno(cursor,conexion):
    cursor.executemany('''
        INSERT INTO T_Alumno(Id,Nombre,Apellidos,DNI,Id_Ordenador)
        VALUES(?,?,?,?,?);
    ''',[
        (None,'Loreto','Pelegrin Castillo','48660787D',2),
        (None,'Fran','Navarro Cayuela','31492099Q',1),
        (None,'Fernanda','De Sousa Finassi','12521011H',3),
        (None,'Kaloyan','Evgeniev Georgiev','74216952T',4),
        (None,'Jose Vicente','Florenciano Jara','77911422A',6),
        (None,'David','Garcia Marcos','28138523R',5),
        (None,'Teodoro','Gomariz Ferrero','39367511K',7)
        ])
    conexion.commit()
    
#SELECT - FROM
def mostrar_ordenadores(cursor):
    
    cursor.execute('''
        SELECT Id,Marca,Modelo
        FROM T_Ordenador;
    ''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def contar_ordenadores_totales(cursor):
    
    cursor.execute('''
        SELECT COUNT(Id) As Num_Ordenadores
        FROM T_Ordenador;
    ''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

#WHERE
#Marca = MSI
def modelo_msi(cursor):
    cursor.execute('''
    SELECT Marca, COUNT(Id) As MSI
    FROM T_Ordenador
    WHERE Marca = 'MSI';
    ''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

#ORDER BY
def ordenar_alumnos_apellido(cursor):
    cursor.execute('''
    SELECT Apellidos,Nombre,DNI
    FROM T_Alumno
    ORDER BY Apellidos
    LIMIT 5;
    ''')
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

#INNER JOIN
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

#Consulta Anidada
#Consulta ordenadores que estan libres.
def ordenadores_libres(cursor):
    cursor.execute("""
        SELECT *
        FROM T_Ordenador
        WHERE Id NOT IN(SELECT Id_Ordenador 
                        FROM T_Alumno);
    """)

    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


def cerrar_conexion(conexion):
    conexion.close()


cursor,conexion = crear_conexion()
# crear_tabla_ordenador(cursor,conexion)
# crear_tabla_alumno(cursor,conexion)
# anadir_ordenador(cursor,conexion)
# anadir_alumno(cursor,conexion)
# mostrar_alumno_ordenador(cursor)
# ordenadores_libres(cursor)
# ordenar_alumnos_apellido(cursor)
# modelo_polular(cursor)
contar_ordenadores_totales(cursor)
modelo_msi(cursor)
cerrar_conexion(conexion)