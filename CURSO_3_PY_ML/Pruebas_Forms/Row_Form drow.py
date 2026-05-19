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
        self.level_2 = {}      # Diccionario de filas: '0': FRAME
        self.d_family = {}  # Diccionario de familias: { 'nombre': [ widget1, widget2, ... ] }
        # ■■■■
        self.level_1 = tk.Frame(self.root)
        self.level_1.pack(fill="both", expand=True)
        # ■■■■
        if num_filas or isinstance(cols_by_fila, list):
            self._build_structure(cols_by_fila)
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def row(self, index):
        """ Devuelve el Frame Fila indicado o  """
        return self.level_2.get(index)

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def _is_empty_cell(self, item):
        """Indica si una posición de la fila debe quedar vacía."""
        return item is None or item == "_" or item == '-' or item == 'x'
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def frame(self):
        return self.level_1 if self.level_1 else None

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def drow(self, rows_data):
        """
        ■ Recibe una lista donde cada elemento representa una fila del layout.
        • Cada elemento puede ser:
          - list / tuple : Se colocan los widgets en la fila usando set_row().
                         Las celdas con "x", "_", "-" o None se saltan.
          - None, "x", "_", '-', [] : Se crea/usará un separador (spacer) 
                                       en esa posición de fila.
        • Las filas se numeran automáticamente según el índice de la lista.
        • Si una fila no existe, se crea dinámicamente respetando el tipo.
        """
        for i, row_data in enumerate(rows_data):
            # ¿Es una fila con widgets o un separador?
            is_widget_row = isinstance(row_data, (list, tuple)) and len(row_data) > 0
            
            # ── Crear la fila si aún no existe ──
            if i not in self.level_2:
                if is_widget_row:
                    num_cols = len(row_data)
                    frame_fila = tk.Frame(self.level_1)
                    frame_fila.pack(fill="x", padx=self.padx, pady=self.pady)
                    for col in range(num_cols):
                        frame_fila.grid_columnconfigure(col, weight=1)
                    self.level_2[i] = frame_fila
                else:
                    spacer = tk.Frame(self.level_1)
                    spacer.pack(fill="x", pady=self.pady * 2)
                    self.level_2[i] = spacer
                
                # Actualizar contador de filas máximas si es necesario
                if i >= self.max_rows:
                    self.max_rows = i + 1
            
            # ── Posicionar widgets si corresponde ──
            if is_widget_row:
                self.set_row(i, *row_data)


# ==========================================
# EJEMPLO DE USO con drow()
# ==========================================
if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("600x180")

    # ■ Creamos la estructura (6 filas, todas activas con 6 columnas)
    alt_config = [2, 6, 6, 6, 6, 6]
    L2 = Nivel_2(root, cols_by_fila=alt_config, padx=15, pady=7)

    # ■ Creamos widgets donde master es el frame fila. 
    # De esta manera puedo aglutinar todos los contreles y ver la fila donde caen.
    lbl_nom = tk.Label(L2.row(0), text='Nombre: ')
    txt_nom = tk.Entry(L2.row(0))    
    lbl_ape1 = tk.Label(L2.row(1), text='Apellido 1: ')
    txt_ape1 = tk.Entry(L2.row(1))    
    lbl_ape2 = tk.Label(L2.row(1), text='Apellido 2: ')
    txt_ape2 = tk.Entry(L2.row(1))    
    btn_add = tk.Button(L2.row(5), text="Añadir")
    btn_del = tk.Button(L2.row(5), text="Borrar")
    btn_upt = tk.Button(L2.row(5), text="Actualiza")

    # ■ Introducimos todo de golpe con drow()
    L2.drow([
        [lbl_nom    , txt_nom                                           ],   
        [lbl_ape1   , txt_ape1  , "x", lbl_ape2 , txt_ape2              ],                
        [],
        None,                                      
        [btn_add    , btn_upt   , "x", "x"      , "x"       , btn_del   ]    
    ])
    
    # L2.frame().config(bg="lightgray")
    
    root.mainloop()