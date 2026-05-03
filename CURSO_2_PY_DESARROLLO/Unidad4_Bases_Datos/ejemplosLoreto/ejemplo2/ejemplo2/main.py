import ejemplo2 as ej

cursor, conexion = ej.crear_conexion()

ej.crear_tabla_libros(cursor,conexion)

ej.anadir_libro(cursor,conexion,None,'Orgullo y Prejuicio','Jane Austen',1813)
ej.anadir_libro(cursor,conexion,None,'Persuasión','Jane Austen',1821)
ej.anadir_libro(cursor,conexion,None,'La edad del aire','Sergio',2024)

# ej.mostrar_datos(cursor)
# ej.busca_autor(cursor)
ej.busca_autor_argumento(cursor,"Jane Austen")


lista_libros = [
    (None,"El señor de los anillos 1", "Tolkien", 1945),
    (None,"El señor de los anillos 2", "Tolkien", 1947),
    (None,"El señor de los anillos 3", "Tolkien", 1949)
]
ej.anadir_lista_libros(cursor,conexion,lista_libros)

ej.cerrar_conexion(conexion)