import tkinter as tk
from tkinter import ttk

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Pestañas")
ventana.geometry("400x300")

# 2. Crear el contenedor de pestañas (Notebook)
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# 3. Crear los marcos (Frames) que actuarán como el contenido de cada pestaña
pestana1 = ttk.Frame(notebook)
pestana2 = ttk.Frame(notebook)

# 4. Añadir los marcos al Notebook asignándoles un título
notebook.add(pestana1, text="Inicio")
notebook.add(pestana2, text="Configuración")

# 5. Agregar elementos dentro de la primera pestaña
label1 = ttk.Label(pestana1, text="¡Bienvenido a la pestaña de Inicio!")
label1.pack(padx=20, pady=20)

# 6. Agregar elementos dentro de la segunda pestaña
label2 = ttk.Label(pestana2, text="Aquí puedes cambiar tus opciones.")
label2.pack(padx=20, pady=20)

# Iniciar la aplicación
ventana.mainloop()
