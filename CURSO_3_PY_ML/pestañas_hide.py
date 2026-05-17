import tkinter as tk
from tkinter import ttk

def verificar_pestana1(*args):
    # Activa el botón solo si el texto es exactamente 'hola'
    if var_entry1.get() == "hola":
        btn_pestana1.config(state="normal")
    else:
        btn_pestana1.config(state="disabled")

def ir_a_pestana2():
    # Actualiza el label de la pestaña 2 con el texto de la pestaña 1
    lbl_ref_pestana2.config(text=f"Texto anterior: {var_entry1.get()}")
    # Muestra y selecciona la pestaña 2
    notebook.add(pestana2)
    notebook.select(pestana2)

def verificar_pestana2(*args):
    # Activa la pestaña 3 si se escribe 'hola'
    if var_entry2.get() == "hola":
        notebook.add(pestana3)
        # Se vincula el evento de selección para actualizar los datos al cambiar
        notebook.select(pestana3)

def verificar_pestana3(*args):
    # Activa la pestaña 4 si se escribe 'hola'
    if var_entry3.get() == "hola":
        notebook.add(pestana4)
        notebook.select(pestana4)

# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Flujo de Pestañas Secuenciales")
ventana.geometry("450x300")

# 2. Creación del Notebook
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# 3. Creación de los 4 Marcos (Frames)
pestana1 = ttk.Frame(notebook)
pestana2 = ttk.Frame(notebook)
pestana3 = ttk.Frame(notebook)
pestana4 = ttk.Frame(notebook)

# Añadimos inicialmente solo la pestaña 1
notebook.add(pestana1, text="Pestaña 1")

# ==================== CONFIGURACIÓN PESTAÑA 1 ====================
lbl1 = ttk.Label(pestana1, text="Escribe 'hola' para activar el botón:")
lbl1.pack(pady=10)

var_entry1 = tk.StringVar()
var_entry1.trace_add("write", verificar_pestana1) # Detecta la escritura

entry1 = ttk.Entry(pestana1, textvariable=var_entry1)
entry1.pack(pady=5)

btn_pestana1 = ttk.Button(pestana1, text="Usar datos", state="disabled", command=ir_a_pestana2)
btn_pestana1.pack(pady=10)

# ==================== CONFIGURACIÓN PESTAÑA 2 ====================
lbl_ref_pestana2 = ttk.Label(pestana2, text="Texto anterior: ")
lbl_ref_pestana2.pack(pady=10)

lbl2_instruccion = ttk.Label(pestana2, text="Escribe 'hola' para avanzar a la Pestaña 3:")
lbl2_instruccion.pack(pady=5)

var_entry2 = tk.StringVar()
var_entry2.trace_add("write", verificar_pestana2)

entry2 = ttk.Entry(pestana2, textvariable=var_entry2)
entry2.pack(pady=5)

# ==================== CONFIGURACIÓN PESTAÑA 3 ====================
# Mostramos los dos textos introducidos previamente
lbl_ref1_pestana3 = ttk.Label(pestana3, text="Texto 1: hola")
lbl_ref1_pestana3.pack(pady=5)
lbl_ref2_pestana3 = ttk.Label(pestana3, text="Texto 2: hola")
lbl_ref2_pestana3.pack(pady=5)

lbl3_instruccion = ttk.Label(pestana3, text="Escribe 'hola' para terminar:")
lbl3_instruccion.pack(pady=5)

var_entry3 = tk.StringVar()
var_entry3.trace_add("write", verificar_pestana3)

entry3 = ttk.Entry(pestana3, textvariable=var_entry3)
entry3.pack(pady=5)

# ==================== CONFIGURACIÓN PESTAÑA 4 ====================
# Al ser la última pestaña, muestra el historial completo mediante 3 Labels
notebook.add(pestana2, text="Pestaña 2")
notebook.add(pestana3, text="Pestaña 3")
notebook.add(pestana4, text="Pestaña 4")

# Las ocultamos inmediatamente para cumplir la regla del flujo secuencial
notebook.hide(pestana2)
notebook.hide(pestana3)
notebook.hide(pestana4)

# Contenido estático final de la pestaña 4 (ya que todos los campos requirieron 'hola')
ttk.Label(pestana4, text="Resumen de datos recolectados:", font=("Arial", 10, "bold")).pack(pady=10)
ttk.Label(pestana4, text="Contenido Pestaña 1: hola").pack(pady=2)
ttk.Label(pestana4, text="Contenido Pestaña 2: hola").pack(pady=2)
ttk.Label(pestana4, text="Contenido Pestaña 3: hola").pack(pady=2)

ventana.mainloop()
