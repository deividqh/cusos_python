import tkinter as tk

class Nivel_2:
    def __init__(self, root, title="Formulario", ancho=300, alto=450, 
                 num_filas=None, cols_by_fila=1, padx=5, pady=5):
        # ... (Atributos de inicialización previos) ...
        self.root = root
        self.root.title(title)
        # self.root.geometry(f"{ancho}x{alto}")
        self.padx = padx
        self.pady = pady
        # self.max_rows = num_filas if num_filas else 0
        self.max_rows = len(cols_by_fila) if len(cols_by_fila) > 0 else 0

        # Estructuras de datos
        self.level_2 = {}      # Diccionario de filas: '0': 
        self.d_family = {}  # Diccionario de familias: { 'nombre': [ widget1, widget2, ... ] }
        
        self.level_1 = tk.Frame(self.root)
        self.level_1.pack(fill="both", expand=True)
        
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
                new_fila = tk.Frame(self.level_1)
                new_fila.pack(fill="x", padx=self.padx, pady=self.pady)
                
                # Configurar las columnas automáticamente
                for col in range(num_cols):
                    new_fila.grid_columnconfigure(col, weight=1)
                
                self.level_2[i] = new_fila
            else:
                # Si es 0 o None, creamos el separador (espacio vacío) (pady up-down)
                spacer = tk.Frame(self.level_1)
                spacer.pack(fill="x", pady=self.pady * 2)
                self.level_2[i] = spacer

    def to_row(self, index):
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

    

# ==========================================
# EJEMPLO DE USO (Transformación de tu código)
# ==========================================
if __name__ == "__main__":
    
    root = tk.Tk()

    # ■ Creamos la estructura
    alt_config = [0, 0,  5 , 5,  2, 1]
    L2 = Nivel_2(root, cols_by_fila=alt_config)

    # ■ Creamos widgets
    lbl_nom = tk.Label(L2.to_row(2), text='Nombre: ')
    txt_nom = tk.Entry(L2.to_row(2))
    lbl_ape = tk.Label(L2.to_row(2), text='Apellido: ')
    txt_ape = tk.Entry(L2.to_row(2))
    
    btn_add = tk.Button(L2.to_row(3), text="Añadir")
    btn_del = tk.Button(L2.to_row(3), text="Borrar")
    btn_upt = tk.Button(L2.to_row(3), text="Actualiza")
    
    # L2.order([])
    # ■ Posicionamos
    L2.add(lbl_ape, 0)
    L2.add(txt_ape, 1)
    L2.add(lbl_nom, 3)
    L2.add(txt_nom, 4)
    
    L2.add(btn_add, 0)
    L2.add(btn_del, 1)
    L2.add(btn_upt, 4)
    
    root.mainloop()