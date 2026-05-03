import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Treeview con Datos Simulados")

        # Crear el Treeview
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Edad", "Ciudad", "Fecha"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar las columnas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Ciudad", text="Ciudad")
        self.tree.heading("Fecha", text="Fecha")

        # Ajustar el ancho de las columnas
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Nombre", width=150, anchor=tk.W)
        self.tree.column("Edad", width=50, anchor=tk.CENTER)
        self.tree.column("Ciudad", width=100, anchor=tk.W)
        self.tree.column("Fecha", width=100, anchor=tk.CENTER)

        # Insertar datos simulados
        datos = [
            (1, "Juan Pérez", 30, "Madrid", "2024-11-01"),
            (2, "María Gómez", 25, "Barcelona", "2024-11-02"),
            (3, "Carlos Ruiz", 35, "Valencia", "2024-11-03"),
            (4, "Ana López", 28, "Sevilla", "2024-11-04"),
            (5, "Luis Torres", 40, "Bilbao", "2024-11-05")
        ]

        for dato in datos:
            self.tree.insert("", tk.END, values=dato)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
