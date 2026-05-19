import tkinter as tk

class Nivel_2:
    def __init__(self, root, title="Formulario", ancho=300, alto=450, 
                 num_filas=None, cols_by_fila=1, padx=5, pady=5):
        # ■■■■
        # ... (Atributos de inicialización previos) ...
        self.root = root
        self.root.title(title)                      # le pone titulo a la ventana principal ❌ error
        # self.root.geometry(f"{ancho}x{alto}")     # le pone ANCHO ventana principal ❌ error
        # ■■■■
        self.padx = padx                            # ❌
        self.pady = pady                            # ✔️ Determina el espacio entre filas
        # ■■■■
        # self.max_rows = num_filas if num_filas else 0     
        self.max_rows = len(cols_by_fila) if len(cols_by_fila) > 0 else 0
        # ■■■■
        # Estructuras de datos
        self.level_2 = {}      # Diccionario de filas: '0': 
        self.d_family = {}  # Diccionario de familias: { 'nombre': [ widget1, widget2, ... ] }
        # ■■■■
        self.level_1 = tk.Frame(self.root)
        self.level_1.pack(fill="both", expand=True)
        # ■■■■
        if num_filas or isinstance(cols_by_fila, list):
            self._build_structure(cols_by_fila)

    def _build_structure(self, cols_config):
        """
        Recorre la lista. El índice 'i' es el número de fila.
        El valor 'num_cols' es la cantidad de columnas.
        """
        for i, num_cols in enumerate(cols_config):
            # Si el valor es mayor que 0, creamos fila activa
            if num_cols and num_cols > 0:
                frame_fila = tk.Frame(self.level_1)
                frame_fila.pack(fill="x", padx=self.padx, pady=self.pady)
                
                # Configurar las columnas automáticamente
                for col in range(num_cols):
                    frame_fila.grid_columnconfigure(col, weight=1)
                
                self.level_2[i] = frame_fila
            else:
                # Si es 0 o None, creamos el separador (espacio vacío) (pady up-down)
                spacer = tk.Frame(self.level_1)
                spacer.pack(fill="x", pady=self.pady * 2)
                self.level_2[i] = spacer

    def row(self, index):
        return self.level_2.get(index)

    # Añade el widget al nivel_2 de tKinter(hace grid por ti)
    def add(self, widget, column, **kwargs):
        """
        Posiciona el widget en la columna indicada.
        La 'row' siempre será 0 porque cada nivel_2 es un Frame de una sola fila.
        """
        # Configuramos un sticky por defecto si el usuario no pasa uno
        if 'sticky' not in kwargs:
            kwargs['sticky'] = "we"
            
        widget.grid(row=0, column=column, **kwargs)
        return widget # Lo devolvemos por si quieres asignarlo en la misma línea

    def set_row(self, row, *items, **kwargs):
        """
        Coloca varios widgets en una fila respetando el orden recibido.

        Cada elemento ocupa su posición dentro de la fila. Si se pasa "_"
        o None, esa posición queda vacía y se mantiene el espacio.
        """
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
        """Indica si una posición de la fila debe quedar vacía."""
        return item is None or item == "_" or item == '-' or item == 'x'
    
    def frame(self):
        return self.level_1 if self.level_1 else None

    

# ==========================================
# EJEMPLO DE USO (Transformación de tu código)
# ==========================================
# if __name__ == "__main__":
    
#     root = tk.Tk()

#     # ■ Creamos la estructura
#     alt_config = [6, 6,  6 , 6,  6, 6]
#     L2 = Nivel_2(root, cols_by_fila=alt_config, padx=15, pady=7)

#     # ■ Creamos widgets y los asigno a una fila del frame L2
#     lbl_nom = tk.Label(L2.row(1), text='Nombre: ')
#     txt_nom = tk.Entry(L2.row(1))    
#     lbl_ape = tk.Label(L2.row(2), text='Apellido: ')
#     txt_ape = tk.Entry(L2.row(2))    
#     btn_add = tk.Button(L2.row(3), text="Añadir")
#     btn_del = tk.Button(L2.row(3), text="Borrar")
#     btn_upt = tk.Button(L2.row(3), text="Actualiza")
    
#     # L2.order([])
#     # ■ Posicionamos
#     # L2.add(lbl_ape, column= 0)
#     # L2.add(txt_ape, column= 1)
#     # L2.add(lbl_nom, column= 4)
#     # L2.add(txt_nom, column= 5)

#     # L2.add(btn_add, column= 0)
#     # L2.add(btn_del, column= 1)
#     # L2.add(btn_upt, column= 5)
    
#     L2.set_row(1, lbl_nom, txt_nom)
#     L2.set_row(2, lbl_ape, txt_ape)
#     L2.set_row(3, btn_add, btn_upt , "_", "_", "_",btn_del)
    
#     L2.frame().config(bg="lightgray")
    
#     root.mainloop()

# [
# [lbl_nom, "+" , "_" , txt_nom], 
# [lbl_ape, "_", txt_ape],
# None,
# [],
# [btn_add, btn_upt , "+", "+", "_", "_" btn_del],
# ]