import sqlite3
import csv
from clientes import Cliente

def crear_conexion():
    conexion = sqlite3.connect(r"ejemplo3\empresa.db")
    cursor = conexion.cursor()
    return cursor,conexion

def crear_tabla_cliente(cursor,conexion):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS T_Clientes(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        Apellidos TEXT,
        Telefono INT,
        Email TEXT
        );
    ''')
    conexion.commit()
    
def cerrar_conexion(conexion):
    conexion.close()
    
def leer_csv_cliente(nombre_ruta):
    clientes = []
    with open(nombre_ruta,'r',encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)
        
        for fila in lector:
            cliente = Cliente(None,fila[0],fila[1],fila[2],fila[3])
            clientes.append(cliente)
            
    return clientes

def leer_csv_cliente_guardar(nombre_ruta,cursor,conexion):
    with open(nombre_ruta,'r',encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)
        
        for fila in lector:
            cliente = Cliente(None,fila[0],fila[1],fila[2],fila[3])
            cliente.guardar(cursor,conexion)





def guardar_en_db(clientes,cursor,conexion):
    for cliente in clientes:
        cursor.execute('''
            INSERT INTO T_Clientes(id,nombre,apellidos,telefono,email)
            VALUES(?,?,?,?,?);
            ''',(cliente.id,cliente.nombre,cliente.apellidos,cliente.telefono,cliente.email))
    
    conexion.commit()
    
    
# cursor,conexion = crear_conexion()
# lista_clientes = leer_csv_cliente('ejemplo3\empresa.csv')
# crear_tabla_cliente(cursor,conexion)
# guardar_en_db(lista_clientes,cursor,conexion)