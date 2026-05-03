import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Columnas de Tabla")

        # Variable para almacenar el path de la base de datos
        self.db_path = None

        # ComboBox para seleccionar la tabla
        self.combo_tablas = ttk.Combobox(root, state="readonly")
        self.combo_tablas.pack(pady=10)
        self.combo_tablas.bind("<<ComboboxSelected>>", self.mostrar_columnas)

        # Botón para abrir base de datos
        btn_cargar_db = tk.Button(root, text="Cargar Base de Datos", command=self.cargar_base_datos)
        btn_cargar_db.pack(pady=5)

        # Text para mostrar columnas
        self.text_columnas = tk.Text(root, width=50, height=10, state="disabled")
        self.text_columnas.pack(pady=10)

    def cargar_base_datos(self):
        # Seleccionar base de datos
        self.db_path = filedialog.askopenfilename(
            title="Seleccionar Base de Datos",
            filetypes=(("Archivos SQLite", "*.sqlite;*.db"), ("Todos los archivos", "*.*"))
        )
        if not self.db_path:
            return  # Si el usuario cancela, no hacemos nada

        try:
            # Conectar y obtener tablas
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            """ 
            -VER LA ESTRUCTURA DE UNA TABLA ESPECIFICA:
                SELECT sql FROM sqlite_master WHERE type='table' AND name='usuarios'; 
            
            -LISTAR TODAS LAS TABLAS:
                SELECT name FROM sqlite_master WHERE type='table';
            """

            tablas = [tabla[0] for tabla in cursor.fetchall()]
            conn.close()

            if tablas:
                self.combo_tablas["values"] = tablas
                self.combo_tablas.set(tablas[0])  # Seleccionar la primera por defecto
                messagebox.showinfo("Éxito", f"Base de datos cargada con {len(tablas)} tablas.")
            else:
                messagebox.showwarning("Sin tablas", "La base de datos no tiene tablas.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la base de datos.\n{e}")

    def mostrar_columnas(self, event=None):
        tabla_seleccionada = self.combo_tablas.get()
        if not tabla_seleccionada or not self.db_path:
            return

        try:
            # Conectar y obtener columnas de la tabla seleccionada
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({tabla_seleccionada});")
            lst_columns = [col[1] for col in cursor.fetchall()]  # El nombre de columna está en la posición 1
            conn.close()


            # Mostrar columnas en el Text
            self.text_columnas.configure(state="normal")
            self.text_columnas.delete("1.0", tk.END)
            self.text_columnas.insert(tk.END, f"Columnas de la tabla '{tabla_seleccionada}':\n")
            self.text_columnas.insert(tk.END, "\n".join(lst_columns))
            self.text_columnas.configure(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener las columnas.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
