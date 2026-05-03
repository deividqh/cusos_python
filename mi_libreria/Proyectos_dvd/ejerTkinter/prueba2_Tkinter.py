# Modulo de widgets(Formularios y controles)
import tkinter as tk

# Para manejar los eventos
from tkinter import ttk     

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter")

# Utilizando el método pack()
tk.Label(root, text="Etiqueta con pack()", background='#FDFE89', foreground='#777777').pack()
tk.Entry(root, background='#FDFE89', foreground='#777777').pack()

# Crear un Frame para utilizar el método grid()
frame_grid = tk.Frame(root, background='#F5E5D3')
frame_grid.pack()

tk.Label(frame_grid, text="Etiqueta con grid()", background='#F5E5D3', foreground='#777777').grid(row=0, column=0)
tk.Entry(frame_grid, background='#F5E5D3').grid(row=0, column=1)

# Utilizando el método place()
def on_click():
    print("Botón con place() presionado")

button = tk.Button(root, text="Botón con place()", command=on_click)
button.place(x=100, y=100)

# Checkbutton y Radiobutton
tk.Checkbutton(root, text="Checkbutton").pack()

ttk.Label(root, text="Seleccione una opción", background='#FDFE89').pack()

variable = tk.StringVar()
variable.set("Opción 1")
ttk.Radiobutton(root, text="Opción 1", variable=variable, value="Opción 1").pack()
ttk.Radiobutton(root, text="Opción 2", variable=variable, value="Opción 2").pack()

root.mainloop()
