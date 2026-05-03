# SQLite es una biblioteca de C que provee una base de datos ligera basada en disco que no requiere 
# un proceso de servidor separado y permite acceder a la base de datos usando una variación 
# no estándar del lenguaje de consulta SQL. Algunas aplicaciones pueden usar SQLite para
#  almacenamiento interno. 
# También es posible prototipar una aplicación usando SQLite y luego transferir el código
#  a una base de datos más grande como PostgreSQL u Oracle.

# También se puede agregar el nombre especial :memory: para crear una base de datos en memoria RAM.


# ---------------------------------------------------------
# INSTALAR BBDD SQLITE y CREAR UNA BBDD DESDE PYTHON
# 1- ==> https://sqlitebrowser.org/dl/ y descargar la version   x64 (mi pc)

# 2-Instalar sqlite3 y ejecutar.
# 3-ya viene, no hay que instalarlo:
import sqlite3
# 4- el archivo que se genera(mibase1), se crea en la raiz del proyecto(en este caso python-Dvd)
conexion = sqlite3.connect("mibase1")

cur = conexion.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conexion.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conexion.close()

# Los datos guardados son persistidos y están disponibles en sesiones posteriores:

# Usualmente, las operaciones SQL necesitarán usar valores de variables de Python
# se usan los parámetros de sustitución DB-API. Colocar ? como un marcador de posición en el lugar donde se usara un valor, y luego se provee una tupla de valores como segundo argumento del método del cursor execute() (otros módulos de bases de datos pueden usar un marcado de posición diferente, como %s o :1). Por ejemplo:

# Never do this -- insecure!
symbol = 'RHAT'
cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)










# ---------------------------------------------------------
# INSTALAR [sqlite odbc] y PARA MIGRAR Y VINCULAR DATOS CON BBDD ODBC (Access, SQL Server, mysql)
        # Descargar e instalar el [sqlite odbc]  ==> http://www.ch-werner.de/sqliteodbc/
        # (Hay que descargar el adecuado, en mi caso [sqliteodbc_w64.exe])









# MIGRAR BBDD ACCESS A SQLITE (Herramientas para la conversion)
# https://code.google.com/archive/p/mdb-sqlite/
# https://code.google.com/archive/p/access2sqlite/



