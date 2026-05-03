import funciones

if __name__ == "__main__":
    ruta = r'ejemplo3\empresa.csv'
    cursor,conexion = funciones.crear_conexion()
    funciones.crear_tabla_cliente(cursor,conexion)
    lista_clientes = funciones.leer_csv_cliente(ruta)
    funciones.guardar_en_db(lista_clientes,cursor,conexion)
    funciones.leer_csv_cliente_guardar(ruta,cursor,conexion)
    funciones.cerrar_conexion(conexion)