# Modulo de widgets(Formularios y controles)
import tkinter as tk

# Para manejar los eventos
from tkinter import ttk     

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter")
root.geometry("600x400")

# Crear un Frame para utilizar el método grid()
frame_01 = tk.Frame(root, background='#F5E5D3')
frame_01.pack()

lbl01=tk.Label(frame_01, text="Etiqueta con grid()", background='#F5E5D3', foreground='#777777')
lbl01.place(x=10, y=10)
txt01=tk.Entry(frame_01, background='#F5E5D3').place(x=100, y=10)

# Utilizando el método place()
def on_click():
    print("Botón con place() presionado")

button01 = tk.Button(frame_01, text="Botón con place()", command=on_click)
button01.place(x=10, y=30)

# Checkbutton y Radiobutton
tk.Checkbutton(frame_01, text="Checkbutton").place(x=10, y=50)
ttk.Label(frame_01, text="Seleccione una opción", background='#FDFE89').place(x=100, y=50)

variable = tk.StringVar()
variable.set("Opción 1")
ttk.Radiobutton(frame_01, text="Opción 1", variable=variable, value="Opción 1").place(x=10, y=70)
ttk.Radiobutton(frame_01, text="Opción 2", variable=variable, value="Opción 2").place(x=100, y=70)

root.mainloop()
