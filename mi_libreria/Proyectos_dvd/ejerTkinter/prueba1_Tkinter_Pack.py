# Modulo de widgets(Formularios y controles)
import tkinter as tk

""" 
1- Tkinter - Vemtanas - Formularios
"""


def on_click():
    # label.config(text="Button clicked!")
    label.config(text="Button clicked222!")

root = tk.Tk()                                  #Instncia TkInter. aun no se ve. 
root.title("Sample Tkinter App")
root.geometry("600x400")

label = tk.Label(root, text="Hello, World!")    
label.pack()

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

label2 = tk.Label(root, text="Hello2, World!")
label2.pack()

button2 = tk.Button(root, text="Click", command=on_click)
button2.pack()
root.mainloop()


