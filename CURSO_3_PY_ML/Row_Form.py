import tkinter as tk

class RowForm:
    def __init__(self, root, title="Formulario", ancho=300, alto=450, 
                 num_filas=None, cols_by_fila=1, padx=5, pady=5):
        """
        Clase para generalizar la creación de formularios por filas.
        
        :param root: Ventana principal (tk.Tk() o Toplevel).
        :param title: Título de la ventana.
        :param ancho: Ancho de la ventana.
        :param alto: Alto de la ventana.
        :param num_filas: Entero. Si es None, se deduce del máximo índice en cols_by_fila.
        :param cols_by_fila: Int (columnas fijas) o Dict {fila: num_columnas}.
        :param padx: Padding horizontal global.
        :param pady: Padding vertical global.
        """
        self.root = root
        self.root.title(title)
        self.root.geometry(f"{ancho}x{alto}")
        self.padx = padx
        self.pady = pady
        
        # Determinar el número total de filas a generar
        if num_filas is None:
            if isinstance(cols_by_fila, dict):
                self.max_rows = max(cols_by_fila.keys()) + 1
            else:
                self.max_rows = 1 # Por defecto al menos una
        else:
            self.max_rows = num_filas

        # Diccionario para guardar los frames de cada fila (Nivel 2)
        self.rows = {}

        # --- NIVEL 1: Contenedor General ---
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        # Configuración de expansión del contenedor
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self._build_structure(cols_by_fila)

    def _build_structure(self, cols_config):
        """Genera internamente los frames de Nivel 2 y configura sus columnas."""
        for i in range(self.max_rows):
            # 1. Determinar si es una fila activa o un espacio vacío
            is_active = False
            num_cols = 0

            if isinstance(cols_config, int):
                is_active = True
                num_cols = cols_config
            elif isinstance(cols_config, dict):
                if i in cols_config:
                    is_active = True
                    num_cols = cols_config[i]
            
            # 2. Crear el Frame de la fila
            if is_active:
                # Fila con contenido: padding normal
                frame = tk.Frame(self.container)
                frame.pack(fill="x", padx=self.padx, pady=self.pady)
                
                # Configurar las columnas (grid_columnconfigure)
                for col in range(num_cols):
                    frame.grid_columnconfigure(col, weight=1)
                
                self.rows[i] = frame
            else:
                # Fila vacía: Solo un Frame vacío con doble pady para hacer de separador
                spacer = tk.Frame(self.container)
                spacer.pack(fill="x", pady=self.pady * 2)
                self.rows[i] = spacer

    def to_row(self, index):
        """Devuelve el frame correspondiente a la fila solicitada."""
        if index in self.rows:
            return self.rows[index]
        else:
            raise IndexError(f"La fila {index} no ha sido inicializada en RowForm.")

# ==========================================
# EJEMPLO DE USO (Transformación de tu código)
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    
    config_columnas = {0: 5, 1: 5, 2: 1, 4: 5, 5: 5, 6: 5, 7: 5 }
    """ >>> Definimos la configuración de columnas según tu ejemplo:
    • Fila 0: 5 cols (Check y Botón)
    • Fila 1: 5 cols (Label ruta)
    • Fila 2: 1 col  (Listbox - se usa pack expand)
    • Fila 3: Espacio vacío (No la incluimos en el dict)
    • Fila 4: 5 cols (Botones CRUD)
    • Fila 5: 5 cols (Titulo)
    • Fila 6: 5 cols (Autor)
    • Fila 7: 5 cols (Num Pag)     """

    # Instanciamos la abstracción
    formulario = RowForm(root, title="Mi Biblioteca Ninja", cols_by_fila=config_columnas)

    # --- Ahora creamos los widgets directamente en las filas ---
    
    # Fila 0: Checkbutton
    chk = tk.Checkbutton(formulario.to_row(0), text="Cargar Babel")
    chk.grid(row=0, column=0, sticky="ew")

    # Fila 2: Listbox (como tiene 1 sola columna, podemos usar pack)
    lbx = tk.Listbox(formulario.to_row(2))
    lbx.pack(fill="both", expand=True)

    # Fila 4: Botones CRUD
    btn_add = tk.Button(formulario.to_row(4), text="Add")
    btn_add.grid(row=0, column=0, columnspan=2, sticky="ew")
    
    btn_updt = tk.Button(formulario.to_row(4), text="Updt")
    btn_updt.grid(row=0, column=2, columnspan=2, sticky="ew")

    # Fila 5: Entry de Título
    lbl_t = tk.Label(formulario.to_row(5), text="Título:")
    lbl_t.grid(row=0, column=0, columnspan=2, sticky="we")
    
    txt_t = tk.Entry(formulario.to_row(5))
    txt_t.grid(row=0, column=2, columnspan=3, sticky="we")

    root.mainloop()