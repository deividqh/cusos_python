import tkinter as tk

def agregar_registro():
    # Obtener el contenido de las entradas
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    profesion = entry_profesion.get()

    # Formatear el registro con los 4 campos
    if nombre and edad and ciudad and profesion:
        registro = f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, Profesión: {profesion}"
        listbox_registros.insert(tk.END, registro)

    # Limpiar las entradas
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Registros")
root.geometry("400x300")

# Crear el Listbox para mostrar los registros
listbox_registros = tk.Listbox(root, width=50, height=10)
listbox_registros.pack(pady=20)

# Crear las etiquetas y campos de entrada
frame_entradas = tk.Frame(root)
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_entradas)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_entradas, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(frame_entradas)
entry_edad.grid(row=1, column=1)

tk.Label(frame_entradas, text="Ciudad:").grid(row=2, column=0)
entry_ciudad = tk.Entry(frame_entradas)
entry_ciudad.grid(row=2, column=1)

tk.Label(frame_entradas, text="Profesión:").grid(row=3, column=0)
entry_profesion = tk.Entry(frame_entradas)
entry_profesion.grid(row=3, column=1)

# Botón para agregar registros
boton_agregar = tk.Button(root, text="Agregar Registro", command=agregar_registro)
boton_agregar.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
