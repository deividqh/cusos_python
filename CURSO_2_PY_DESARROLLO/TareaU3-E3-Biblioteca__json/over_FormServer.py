import tkinter as tk
from sobreForms.form_biblioteca import form_biblioteca as FB

rootS = tk.Tk()
FormServidor=FB(root=rootS, title="Formulario Pruebas", ancho=250, alto=300)
rootS.mainloop()

