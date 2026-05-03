import tkinter as tk
from tkinter import messagebox

def abrir_ventana_emergente():
    
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.title("Ventana Emergente")
    
    # Configurar el tamaño de la ventana emergente
    ventana_emergente.geometry("300x200")
    
    # Crear un Frame dentro de la ventana emergente para añadir márgenes
    frame_contenido = tk.Frame(ventana_emergente, padx=20, pady=20)
    frame_contenido.pack(fill="both", expand=True)

    # Obtener el contenido del cuadro de texto
    texto_ingresado = text_box.get("1.0", tk.END).strip()
    # Mostrar el contenido del cuadro de texto en la ventana emergente
    etiqueta = tk.Label(frame_contenido, text=f"\nTexto ingresado:\n\n{texto_ingresado}")
    etiqueta.pack(pady=20, padx=10)
    
    # Botón para cerrar la ventana emergente
    boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
    boton_cerrar.pack(pady=5)

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("400x300")

# Etiqueta y cuadro de texto en la ventana principal
etiqueta_principal = tk.Label(root, text="Ingresa texto:")
etiqueta_principal.pack(pady=5)

text_box = tk.Text(root, height=2, width=40)
text_box.pack(pady=5)

# Botón en la ventana principal para abrir la ventana emergente
boton_abrir = tk.Button(root, text="Abrir Ventana Emergente", command=abrir_ventana_emergente)
boton_abrir.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
