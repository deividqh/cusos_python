import tkinter as tk
from tkinter import ttk

# ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def verificar_pestana1(*args):
    # Si borra 'hola' en la 1, se desactiva TODO lo posterior
    if var_entry1.get() != "hola":
        btn_pestana1.config(state="disabled")
        
        # Limpiar los campos siguientes para romper la cadena
        var_entry2.set("")
        var_entry3.set("")
        
        # Desactivar en cascada
        notebook.tab(pestana2, state="disabled")
        notebook.tab(pestana3, state="disabled")
        notebook.tab(pestana4, state="disabled")
    else:
        # Solo activa el botón; el usuario debe pulsarlo para avanzar a la 2
        btn_pestana1.config(state="normal")

# ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def ir_a_pestana2():
    lbl_ref_pestana2.config(text=f"Texto anterior: {var_entry1.get()}")
    notebook.tab(pestana2, state="normal")
    notebook.select(pestana2)

# ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def verificar_pestana2(*args):
    if var_entry2.get() == "hola":
        notebook.tab(pestana3, state="normal")
        notebook.select(pestana3)
    else:
        # Si borra 'hola' en la 2, limpia la 3 y apaga la 3 y la 4
        var_entry3.set("")
        notebook.tab(pestana3, state="disabled")
        notebook.tab(pestana4, state="disabled")

# ■ ■ ■ ■ ■ ■ ■ ■ ■ 
def verificar_pestana3(*args):
    if var_entry3.get() == "hola":
        notebook.tab(pestana4, state="normal")
        notebook.select(pestana4)
    else:
        # Si borra 'hola' en la 3, apaga la pestaña 4
        notebook.tab(pestana4, state="disabled")

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Pestañas Dinámicas Bidireccionales")
ventana.geometry("450x300")

# 2. Creación del Notebook
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# 3. Creación de los Marcos
pestana1 = ttk.Frame(notebook)
pestana2 = ttk.Frame(notebook)
pestana3 = ttk.Frame(notebook)
pestana4 = ttk.Frame(notebook)

notebook.add(pestana1, text="Datos")
notebook.add(pestana2, text="Split")
notebook.add(pestana3, text="Algoritmo/Modelo")
notebook.add(pestana4, text="Metricas")

# Bloqueo inicial
notebook.tab(pestana2, state="disabled")
notebook.tab(pestana3, state="disabled")
notebook.tab(pestana4, state="disabled")

# ==================== PESTAÑA 1 ====================
lbl1 = ttk.Label(pestana1, text="Escribe 'hola' para activar el botón:")
lbl1.pack(pady=10)

var_entry1 = tk.StringVar()
var_entry1.trace_add("write", verificar_pestana1)
entry1 = ttk.Entry(pestana1, textvariable=var_entry1)
entry1.pack(pady=5)

btn_pestana1 = ttk.Button(pestana1, text="Usar datos", state="disabled", command=ir_a_pestana2)
btn_pestana1.pack(pady=10)

# ==================== PESTAÑA 2 ====================
lbl_ref_pestana2 = ttk.Label(pestana2, text="Texto anterior: ")
lbl_ref_pestana2.pack(pady=10)

lbl2_instruccion = ttk.Label(pestana2, text="Escribe 'hola' para avanzar a la Pestaña 3:")
lbl2_instruccion.pack(pady=5)

var_entry2 = tk.StringVar()
var_entry2.trace_add("write", verificar_pestana2)
entry2 = ttk.Entry(pestana2, textvariable=var_entry2)
entry2.pack(pady=5)

# ==================== PESTAÑA 3 ====================
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

# ==================== PESTAÑA 4 ====================
ttk.Label(pestana4, text="Resumen de datos recolectados:", font=("Arial", 10, "bold")).pack(pady=10)
ttk.Label(pestana4, text="Contenido Pestaña 1: hola").pack(pady=2)
ttk.Label(pestana4, text="Contenido Pestaña 2: hola").pack(pady=2)
ttk.Label(pestana4, text="Contenido Pestaña 3: hola").pack(pady=2)

ventana.mainloop()
