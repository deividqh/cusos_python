import tkinter as tk
from ui_tk.Familia import Familia

class Nivel_2:
    def __init__(self, contenedor, shape=None, padx=5, pady=5 ):
        # ■■■■
        self.contenedor = contenedor
        # ■■■■
        self.padx = padx
        self.pady = pady
        # ■■■■
        self.filas = None       # Numero de filas del shape
        self.columnas = None    # Guarda el número de columnas (para shape)
        # ■■■■
        self.level_1 = None     # Frame que hereda de contenedor
        self.level_2 = {}       # Diccionario key = num_fila (0, 1, 2)  valor = Frame hijo de level_1
        # ■■■■
        self.family = Familia() # Objeto familia para tener los widget unidos por grupos custom.
        
        self.level_1 = tk.Frame(self.contenedor)
        self.level_1.pack(fill="both", expand=True)
        # ■ Procesar shape 
        if shape is not None:
            # Parsear formato "filasxcolumnas" (ej: "4x6")
            try:
                filas_str, cols_str = shape.lower().split('x')
                self.filas    = int(filas_str.strip())
                self.columnas = int(cols_str.strip())
                # Crear lista de columnas para cada fila
                columns_x_fila = [self.columnas] * self.filas
            except ValueError:
                raise ValueError(f"Formato de shape inválido: '{shape}'. Use formato 'filasxcolumnas' (ej: '4x6')")
        # ■ ■ ■ ■ ■ ■ ■ ■ ■ 
        
        if self.filas or (isinstance(columns_x_fila, list) and len(columns_x_fila) > 0):
            self._build_structure(columns_x_fila)

    def _build_structure(self, cols_config):
        for i, num_cols in enumerate(cols_config):
            if num_cols and num_cols > 0:
                frame_fila = tk.Frame(self.level_1)
                frame_fila.pack(fill="x", padx=self.padx, pady=self.pady)
                for col in range(num_cols):
                    frame_fila.grid_columnconfigure(col, weight=1)
                self.level_2[i] = frame_fila
            else:
                spacer = tk.Frame(self.level_1)
                spacer.pack(fill="x", pady=self.pady * 2)
                self.level_2[i] = spacer

    def row(self, index):
        return self.level_2.get(index)

    def add(self, widget, column, **kwargs):
        if 'sticky' not in kwargs:
            kwargs['sticky'] = "we"
        widget.grid(row=0, column=column, **kwargs)
        return widget

    def set_row(self, row, *items, **kwargs):
        if row not in self.level_2:
            raise ValueError(f"La fila {row} no existe.")
        added_widgets = []
        for column, item in enumerate(items):
            if self._is_empty_cell(item):
                continue
            new_widget = self.add(item, column, **kwargs)
            added_widgets.append(new_widget)
        return added_widgets
    
    def _is_empty_cell(self, item):
        return item is None or item == "_" or item == '-' or item == 'x'
    
    def frame(self):
        return self.level_1 if self.level_1 else None


# ==========================================
# EJEMPLO DE USO CON LA NUEVA FORMA
# ==========================================
if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("600x200")

    # ■ Nueva forma de crear la estructura: 4 filas x 6 columnas
    F1 = Nivel_2(root, shape="6x6", padx=15, pady=7)
    
    print(f"Número de filas creadas: {F1.filas}")
    print(f"Número de columnas guardadas: {F1.columnas}")

    # ■ Creamos widgets y los asignamos a filas del frame F1
    lbl_nom = tk.Label(F1.row(0), text='Nombre: ')
    txt_nom = tk.Entry(F1.row(0))    
    lbl_ape_1 = tk.Label(F1.row(1), text='Apellido1: ')
    txt_ape_1 = tk.Entry(F1.row(1))    
    lbl_ape_2 = tk.Label(F1.row(2), text='Apellido2: ')
    txt_ape_2 = tk.Entry(F1.row(2))    
    btn_add = tk.Button(F1.row(3), text="Añadir")
    btn_del = tk.Button(F1.row(3), text="Borrar")
    btn_upt = tk.Button(F1.row(3), text="Actualiza")

    scrollbar = tk.Scrollbar(F1.row(0), orient=tk.VERTICAL)
    listbox = tk.Listbox(F1.row(4), yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    
    # ■ Posicionamos con set_row
    F1.set_row(0, lbl_nom, txt_nom)
    F1.set_row(1, lbl_ape_1, txt_ape_1 )
    F1.set_row(2, lbl_ape_2, txt_ape_2 )
    F1.set_row(3, btn_add, btn_upt, "_", "_", "_", btn_del)
    F1.set_row(4, listbox)
    
    F1.frame().config(bg="lightgray")



    
    root.mainloop()