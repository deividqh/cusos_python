""" 
Archivo donde quiero que estén los comands de los widgets creados 
Tengo que importar las bibliotecas que necesite.
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json

def limpiar_textos(textos):
    for i, t in enumerate(textos):
        t.delete(0, tk.END)
        # t.insert(0, f"Hello Texto {i}")


def mostrar_alerta(texto_alerta):
    # El primer parámetro es el título de la ventana y el segundo es el texto
    messagebox.showinfo("Titulo", texto_alerta)

# A B R E V I A   LA RUTA       Para ver en  self.lbl_archivo
def ruta_abrevd(ruta, numpartes=2):
    """ Def: Divide la ruta en partes new_ruta=self.ruta_abrevd(ruta)"""
    partes = str(ruta).split('/')

    # Toma solo las dos últimas carpetas y añade '...'
    if len(partes) > numpartes:            
        return os.path.join("...", partes[-2], partes[-1])
    else:
        # Si hay menos de dos carpetas, muestra la ruta tal cual
        return ruta

# F I L E D I A L O G . Retorna self.archivo
def selectFile(self):
    """ 
    Def: Selecciona un Archivo con fileDialog y devuelve el resultado.
    """
    # Obtiene el directorio del archivo de Python actual
    carpeta_inicial = os.path.dirname(os.path.abspath(__file__))
    archivo = filedialog.askopenfilename(title="Seleccionar Archivo", 
                                        initialdir=carpeta_inicial ,
                                        filetypes=[ ("Archivos JSON", "*.json"), 
                                                    ("Archivos CSV", "*.csv"), 
                                                    ("Archivos de texto", "*.txt")])
    
    return archivo if archivo else None

# L E E  F I C H E R O    AL INICIAR SOLAMENTE.(NO USADA)
def lectura_inicial(self, archivo_json=''):
    """ 
    Def: si existe el archivo lo lee y devuelve en formato json
    """
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []  # Crear una lista nueva si el archivo no existe
    return datos

# M E N S A J E S   DE LA APP
def informarApp(self, txt_info='', txt_subinfo=''):
    print('informar app')

# ____________________
# B O T O N  Para FILEDIALOG       Del Fichero seleccionado  a lbl_archivo y self.archivo
def bttn_loadfile_click():      
    """     
    >>> Def: Load Fichero  """
    archivo = selectFile()
    if archivo:
        # messagebox.showinfo(title="Load File:", message=f"Fichero cargado {archivo} ")
        # Nombre y path
        nombre_archivo = os.path.basename(p=archivo)
        ruta_archivo = os.path.dirname(p=archivo)
        ruta_abrevd = ruta_abrevd(ruta_archivo)
        # print(ruta_abrevd)
        informarApp('Load File', 'OK ;)')
        
    else:
        messagebox.showinfo(title="Load File:", message=f"No se ha cargado ningún archivo ")
        informarApp('Load File', 'Failed :(')
        # Salir y no hacer nada
    