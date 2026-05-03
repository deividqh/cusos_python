import tkinter as tk
from tkcalendar import DateEntry

def mostrar_fecha():
    print(f"Fecha seleccionada: {date_entry.get()}")

# Configuración de la ventana
root = tk.Tk()
root.title("Selector de Fecha")

# Creación del DateEntry
date_entry = DateEntry(root, width=12, background='darkblue', 
                       foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
date_entry.pack(pady=10)

# Botón para mostrar la fecha seleccionada
btn = tk.Button(root, text="Mostrar Fecha", command=mostrar_fecha)
btn.pack(pady=5)

root.mainloop()
