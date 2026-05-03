"""Ejercicio 1. Se desea diseñar una base de datos para almacenar y gestionar la
información empleada por una empresa dedicada a la venta de automóviles,
teniendo en cuenta los siguientes aspectos. La empresa dispone de una serie de
coches para su venta.
▰ Se necesita conocer la matrícula, marca y modelo, el color y el precio de venta de
cada coche.
▰ Los datos que interesa conocer de cada cliente son el NIF, nombre, dirección,
ciudad y número de teléfono: además, los clientes se diferencian por un código
interno de la empresa que se incrementa automáticamente cuando un cliente se da
de alta en ella. Un cliente puede comprar tantos coches como desee a la empresa.
Un coche determinado solo puede ser comprado por un único cliente.
El concesionario también se encarga de llevar a cabo las revisiones que se realizan
a cada coche. Cada revisión tiene asociado un código que se incrementa
automáticamente por cada revisión que se haga. De cada revisión se desea saber
si se ha hecho cambio de filtro, si se ha hecho cambio de aceite, si se ha hecho
cambio de frenos u otros. Los coches pueden pasar varias revisiones en el
concesionario”."""

import sqlite3 

conexion = sqlite3.connect("Concesionario.db")       # Doble barra porque si no entiende que es un comando. (r de rutas)

cursor = conexion.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS CLIENTES(
               NIF TEXT NOT NULL PRIMARY KEY,
               NOMBRE TEXT,
               DIRECCION TEXT,
               CIUDAD TEXT,
               TELEFONO TEXT,
               MATRICULA TEXT,
               Cod_Interno INT,
               ID_MANTENIMIENTO INT,
               FOREIGN KEY(Cod_Interno) REFERENCES MANTENIMIENTO(ID),
               FOREIGN KEY(MATRICULA) REFERENCES COCHES(MATRICULA));
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS COCHES(
               MATRICULA TEXT NOT NULL PRIMARY KEY,
               MARCA TEXT,
               MODELO TEXT,
               COLOR TEXT, 
               PRECIO TEXT
               );
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS MANTENIMIENTO(
               ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               FILTROS TEXT,
               ACEITE TEXT,
               FRENOS TEXT,
               OTROS TEXT
               );
""")