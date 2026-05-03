import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    # Abrir cuadro de diálogo para seleccionar un archivo
    archivo_seleccionado = filedialog.askopenfilename(
        title="Seleccionar un archivo", 
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    
    # Mostrar la ruta del archivo seleccionado en la etiqueta
    if archivo_seleccionado:
        etiqueta_archivo.config(text=f"Archivo seleccionado: {archivo_seleccionado}")

# Crear la ventana principal
root = tk.Tk()
root.title("Selector de Archivos")
root.geometry("400x200")

# Botón para abrir el cuadro de diálogo y seleccionar un archivo
boton_seleccionar = tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=20)

# Etiqueta para mostrar la ruta del archivo seleccionado
etiqueta_archivo = tk.Label(root, text="Ningún archivo seleccionado")
etiqueta_archivo.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
