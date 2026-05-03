from classMenuDvdX import GestorHilosXindiceX
import tkinter as tk

# Funciones de ejemplo
def tarea_terminal():
    print("Tarea ejecutándose en terminal.")

def formulario_tkinter():
    root = tk.Tk()
    root.title("Formulario Ejemplo")
    tk.Label(root, text="Formulario en ejecución").pack()
    tk.Button(root, text="Cerrar", command=root.destroy).pack()
    return root


# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorHilosXindiceX()
    gestor.add(
        "Menu Principal",
        ["Ejecutar tarea", "Abrir formulario"],
        [tarea_terminal, formulario_tkinter],
    )

    gestor.start("Menu Principal", withConfig=False)
