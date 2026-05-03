# Ejercicios Listas

#Para Limpiar la terminal con  os.system('cls') 
import os           
from enum import Enum
from sobreForms.form_biblioteca import form_biblioteca as TheBibliot
import tkinter as tk


def main():
    os.system('cls')
    root = tk.Tk()
    ninja_babel = TheBibliot(root=root, title="Biblioteca Loretix-Plus")
    root.mainloop()


if __name__=='__main__':
    main()



