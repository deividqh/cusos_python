import sqlite3

class Sqlite3_InOut:
    def __init__(self, path_bbdd):
        self.path_bbdd = path_bbdd
        self.conexion_inout = None
        self.cursor_inout = None

    def __enter__(self):
        """Abre la conexión a la base de datos y devuelve el cursor."""
        self.conexion_inout = sqlite3.connect(self.path_bbdd)
        self.cursor_inout = self.conexion_inout.cursor()
        return self.cursor_inout  

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Cierra la conexión y maneja posibles excepciones."""
        if exc_type is not None:
            self.conexion_inout.rollback()
        else:            
            self.conexion_inout.commit()        

        self.conexion_inout.close()

# Ejemplo de uso

db_name = r'dvd_contextoBD/example.db'

# Crear una tabla, insertar datos y realizar una consulta dentro del contexto
with Sqlite3_InOut(db_name) as cursor:
    cursor.execute( """ CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT) """ )
    cursor.execute("INSERT INTO users (name) VALUES (?)", ('Alice',))    
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

for fila in rows:
    print(fila)
