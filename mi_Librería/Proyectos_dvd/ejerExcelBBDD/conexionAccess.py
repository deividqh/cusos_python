import pyodbc 
[x for x in pyodbc.drivers() if x.startswith('Microsoft')]
""" ----- INSTALAR UN MODULO QUE NO ESTÁ INTEGRADO -------- """
# pip install --upgrade pip
# pip install pyodbc
# python -c "import pyodbc; print(pyodbc.version)"

""" 
- conectar con una base de datos access 
"""

# Conectar a una base de datos Access
path=r"C:\Users\pc\Desktop\Personal\ExcelDVD\CONTROL-PADEL\RRH_PaddelREAL.accdb"
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=file:\C:\Users\pc\Desktop\Personal\ExcelDVD\CONTROL-PADEL\RRH_PaddelREAL.accdb' 
    r'DFLT_BIGINT_BIND_STR=1'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Leer datos de una tabla
cursor.execute('SELECT * FROM Clases')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Insertar datos en una tabla
# cursor.execute("INSERT INTO tabla (columna1, columna2) VALUES (?, ?)", ('valor1', 'valor2'))
# conn.commit()

# Cerrar la conexión
conn.close()
