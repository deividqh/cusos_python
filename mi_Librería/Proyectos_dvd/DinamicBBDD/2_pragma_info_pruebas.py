import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Columnas y Tipos de Tabla")

        # Variable para almacenar el path de la base de datos
        self.bbdd_fdlg_select = None

        # ComboBox para seleccionar la tabla
        self.combo_tablas = ttk.Combobox(root, state="readonly")
        self.combo_tablas.pack(pady=10)
        self.combo_tablas.bind("<<ComboboxSelected>>", self.mostrar_columnas)

        # Botón para abrir base de datos
        btn_cargar_db = tk.Button(root, text="Cargar Base de Datos", command=self.cargar_base_datos)
        btn_cargar_db.pack(pady=5)

        # Text para mostrar columnas
        self.text_columnas = tk.Text(root, width=60, height=15, state="disabled")
        self.text_columnas.pack(pady=10)

    def cargar_base_datos(self):
        # Seleccionar base de datos
        self.bbdd_fdlg_select = filedialog.askopenfilename(
            title="Seleccionar Base de Datos",
            filetypes=(("Archivos SQLite", "*.sqlite;*.db"), ("Todos los archivos", "*.*"))
        )
        if not self.bbdd_fdlg_select:
            return  # Si el usuario cancela, no hacemos nada

        try:
            # Conectar y obtener tablas
            conn = sqlite3.connect(self.bbdd_fdlg_select)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
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
        # Obtener la tabla seleccionada
        tabla_seleccionada = self.combo_tablas.get()
        if not tabla_seleccionada or not self.bbdd_fdlg_select:
            return

        try:
            # Conectar y obtener columnas de la tabla seleccionada
            conn = sqlite3.connect(self.bbdd_fdlg_select)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({tabla_seleccionada});")
            info_columnas = cursor.fetchall()  # [cid, name, type, notnull, dflt_value, pk]
            conn.close()

            # Mostrar información en el Text
            self.text_columnas.configure(state="normal")
            self.text_columnas.delete("1.0", tk.END)
            self.text_columnas.insert(tk.END, f"Columnas de la tabla '{tabla_seleccionada}':\n")
            self.text_columnas.insert(tk.END, f"{'Nombre':<20} {'Tipo':<15} {'Primary Key':<10}\n")
            self.text_columnas.insert(tk.END, "-" * 50 + "\n")
            for col in info_columnas:
                nombre = col[1]
                tipo = col[2]
                pk = "Sí" if col[5] == 1 else "No"
                self.text_columnas.insert(tk.END, f"{nombre:<20} {tipo:<15} {pk:<10}\n")
            self.text_columnas.configure(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener las columnas.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
