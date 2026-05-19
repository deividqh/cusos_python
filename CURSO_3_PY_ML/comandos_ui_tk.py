""" 
Archivo donde quiero que estén los comands de los widgets creados 
Tengo que importar las bibliotecas que necesite.
"""
import tkinter as tk
from tkinter import messagebox


def limpiar_textos(textos):
    for i, t in enumerate(textos):
        t.delete(0, tk.END)
        # t.insert(0, f"Hello Texto {i}")


def mostrar_alerta(texto_alerta):
    # El primer parámetro es el título de la ventana y el segundo es el texto
    messagebox.showinfo("Titulo", texto_alerta)