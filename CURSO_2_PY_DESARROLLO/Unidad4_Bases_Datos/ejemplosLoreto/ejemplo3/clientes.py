import sqlite3

class Cliente:
    def __init__(self,id,nombre,apellidos,telefono,email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email


    def guardar(self,cursor,conexion):
        cursor.execute('''
        INSERT INTO T_Clientes(id,nombre,apellidos,telefono,email)
        VALUES(?,?,?,?,?);
        ''',(self.id,self.nombre,self.apellidos,self.telefono,self.email))
        
        conexion.commit()


    
    