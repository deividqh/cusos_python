# Modulo de widgets(Formularios y controles)
import tkinter as tk

# Para manejar los eventos
from tkinter import ttk     

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter")
# Cambiar tamaño del formulario (ancho x alto)
root.geometry("600x400")

# Utilizando el método pack()
tk.Label(root, text="Etiqueta con pack()", background='#FDFE89', foreground='#777777').pack()
tk.Entry(root, background='#FDFE89', foreground='#777777').pack()

# Crear un Frame para utilizar el método grid()
frame_grid = tk.Frame(root, background='#F5E5D3')
# frame_grid.pack()

# Fila 0
tk.Label(frame_grid, text="Etiqueta con grid()", background='#F5E5D3', foreground='#777777').grid(row=0, column=0)
tk.Entry(frame_grid, background='#F5E5D3').grid(row=0, column=1)

# Utilizando el método place()
def on_click():
    print("Botón con place() presionado")

# Fila 2
# Checkbutton y Radiobutton
tk.Checkbutton(frame_grid, text="Checkbutton").grid(row=2, column=0)

# Fila 3
tk.Label(frame_grid, text="Seleccione una opción", background='#FDFE89').grid(row=3, column=0)

variable = tk.StringVar()
variable.set("Opción 1")
ttk.Radiobutton(frame_grid, text="Opción 1", variable=variable, value="Opción 1").grid(row=3, column=1)
ttk.Radiobutton(frame_grid, text="Opción 2", variable=variable, value="Opción 2").grid(row=3, column=2)

# Fila 4
button = tk.Button(frame_grid, text="Botón con place()", command=on_click)
button.grid(row=4, column=0)

frame_grid.pack()
root.mainloop()
