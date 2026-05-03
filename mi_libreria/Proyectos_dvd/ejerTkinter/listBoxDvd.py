import tkinter as tk

root = tk.Tk()
# listbox = tk.Listbox(root)

# LISTBOX C/ SELECCION MULTIPLE:
# listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

# listbox.pack()

# _____________________________________
# LISTBOX C/ DESPLAZAMIENTO:>>>>>>>>
scrollbar = tk.Scrollbar(root)
# Ajustado a la derecha y en el vertice Y
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)
# LISTBOX C/ DESPLAZAMIENTO:<<<<<<<<
# LISTBOX C/ DESPLAZAMIENTO:<<<<<<<<

# _____________________________________
listbox.insert(tk.END, "Elemento 1")
listbox.insert(tk.END, "Elemento 2")
listbox.insert(tk.END, "Elemento 3")
listbox.insert(tk.END, "Elemento 4")
listbox.insert(tk.END, "Elemento 5")

# CREACION DE UN BOTON Y EVENTO CLICK DONDE SACA EL INDICE DEL ELEMENTO SELECCIONADO
def get_selection():
    selected_item = listbox.get(listbox.curselection())
    print("Selected item:", selected_item)

button = tk.Button(root, text="Obtener selección", command=get_selection)
button.pack()

# _____________________________________
# ---- SELECCION EN LISTBOX >>>>>>>>>>>>
def on_select(event):
    print("Selected item:", listbox.get(listbox.curselection()))

listbox.bind("<<ListboxSelect>>", on_select)
# ---- SELECCION EN LISTBOX <<<<<<<<<<<


# ________________________________
# Insertar elementos en el Listbox en una ubicación específica:
# listbox.insert(1, "Elemento 8")

# ________________________________
# Eliminar elementos del Listbox:
# listbox.delete(0, tk.END)  # Elimina todos los elementos
# listbox.delete(1)  # Elimina el elemento con el índice 1

# ________________________________
# Obtener el índice de un elemento específico:
try:
    index = listbox.index("Elemento 3")
    print(index)  # Salida: 1
except Exception as e:
    print(f"\nError index {e}")

def buscar_click():
    index = listbox.index("Elemento 3")
    print(index)  # Salida: 1

button = tk.Button(root, text="Buscar Elemento 3", command=buscar_click)
button.pack()

# ------EVENTOS-----------------------------------------------
# Evento de selección de elemento:
# listbox.bind("<<ListboxSelect>>", funcion_de_callback)

# Evento de doble clic en un elemento:
# listbox.bind("<Double-1>", funcion_de_callback)

# Evento de desplazamiento del Listbox:
# listbox.bind("<Configure>", funcion_de_callback)

# Evento de arrastrar y soltar un elemento:
# listbox.bind("<<ListboxSelect>>", funcion_de_callback_arrastrar)
# listbox.bind("<ButtonRelease-1>", funcion_de_callback_soltar)
# -----------------------------------------------------------

root.mainloop()
