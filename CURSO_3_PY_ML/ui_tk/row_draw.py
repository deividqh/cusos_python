import tkinter as tk
from tkinter import ttk             # Importa los componentes modernos
from tkinter import filedialog
import os

class FDialoger:
    """
    Widget compuesto: Entry + Button que lanza un FileDialog.
    Hereda de ttk.Frame para poder insertarse directamente en matrices de draw().
    """
    def __init__(self, parent, texto_boton, title="Seleccionar Archivo",
                 initialdir=None, filetypes=None, entry_width=40):
        
        # Variable de control
        self.var_ruta = tk.StringVar(value="")

        # ■ Widgets sueltos (hijos de 'parent')
        self.entry = ttk.Entry(parent, textvariable=self.var_ruta, width=entry_width)
        self.btn = ttk.Button(parent, text=texto_boton, command=self._abrir_dialogo)

        # ■ Configuración del diálogo
        self._titulo = title
        self._dir_inicial = initialdir if initialdir else os.path.dirname(os.path.abspath(__file__))
        self._tipos = filetypes if filetypes else [
            ("Todos los archivos", "*.*"),
            ("Archivos JSON", "*.json"),
            ("Archivos CSV", "*.csv"),
            ("Archivos de texto", "*.txt")
        ]

        # ■ Callback opcional tras seleccionar archivo
        self._on_select = None

    def _abrir_dialogo(self):
        archivo = filedialog.askopenfilename(
            parent=self.entry.winfo_toplevel(),   # ← CORREGIDO
            title=self._titulo,
            initialdir=self._dir_inicial,
            filetypes=self._tipos
        )
        if archivo:
            self.var_ruta.set(archivo)
            self.entry.xview_moveto(1.0)
        pass
    def get_ruta(self):
        """Devuelve la ruta completa seleccionada."""
        return self.var_ruta.get()

    def set_ruta(self, ruta):
        """Establece manualmente la ruta en el Entry."""
        self.var_ruta.set(ruta)

    def get_ruta_abreviada(self, numpartes=2):
        """Devuelve la ruta acortada: .../ultima_carpeta/archivo."""
        ruta = self.var_ruta.get()
        if not ruta:
            return ""
        partes = ruta.replace("\\", "/").split("/")
        if len(partes) <= numpartes:
            return ruta
        ultimas = partes[-numpartes:]
        ruta_corta = os.path.join("...", *ultimas)
        return ruta_corta

    

class Familia:
    def __init__(self):
        self.d_family = {}  # { 'nombre': [widgets] }

    def __call__(self, nombre_familia: str = None):
        """ 
        Permite usar la instancia como una función: F() o F('nombre')
        Llama internamente a la visualización.
        """
        self.view(nombre_familia)

    def view(self, nombre_familia: str = None):
        """
        Lógica de impresión en consola.
        """
        if nombre_familia:
            if nombre_familia in self.d_family:
                print(f"\n[ DETALLE FAMILIA: '{nombre_familia}' ]")
                print(f"{'Índice':<8} | {'Tipo':<15} | {'Nombre ID':<15} | {'Texto/Valor'}")
                print("-" * 65)
                for i, w in enumerate(self.d_family[nombre_familia]):
                    tipo = type(w).__name__
                    nombre_id = w.winfo_name()
                    
                    info = ""
                    try:
                        if isinstance(w, (tk.Button, tk.Label, tk.Checkbutton)):
                            info = w.cget("text")
                        elif isinstance(w, tk.Entry):
                            info = w.get()
                    except:
                        info = "n/a"
                    
                    info = str(w)

                    print(f"{i:<8} | {tipo:<15} | {nombre_id:<15} | {info}")
            else:
                print(f"⚠️ La familia '{nombre_familia}' no existe.")
        else:
            print("\n[ RESUMEN DE TODAS LAS FAMILIAS ]")
            print(f"{'Nombre Familia':<20} | {'Nº Widgets'}")
            print("-" * 45)
            for fam, lista in self.d_family.items():
                print(f"{fam:<20} | {len(lista)}")

    # ■■■■ Crea / Elimina lista de widgets en una 'nombre_familia'
    def formar(self, nombre_familia: str, widgets: list = [], b_del: bool = False):
        if nombre_familia not in self.d_family and not b_del:
            self.d_family[nombre_familia] = []
        
        if b_del:
            """ Borrar """
            if nombre_familia in self.d_family:
                for w in widgets:
                    if w in self.d_family[nombre_familia]:
                        self.d_family[nombre_familia].remove(w)
        else:
            """ Crear """
            for w in widgets:
                if w not in self.d_family[nombre_familia]:
                    self.d_family[nombre_familia].append(w)
            pass
        pass
        self.view(nombre_familia)
    
    # ■■■■ Devuelve los widget de la familia  
    def familiares(self, nombre_familia: str) -> list:
        return self.d_family.get(nombre_familia, [])

    # ■■■■ Pone estilo comun a todos los widget de la familia.
    def style_family(self, nombre_familia: str, **kwargs):
        for w in self.familiares(nombre_familia):
            try:
                w.config(**kwargs)
            except tk.TclError:
                pass

    # ■■■■ Activa / Des-activa los widget de 'nombre_familia'
    def active_family(self, nombre_familia: str, activa: bool = True):
        estado = "normal" if activa else "disabled"
        for w in self.familiares(nombre_familia):
            try:
                w.config(state=estado)
            except tk.TclError:
                pass 

    def clean_family(self, nombre_familia: str):
        for w in self.familiares(nombre_familia):
            if isinstance(w, tk.Entry):
                w.delete(0, tk.END)
            elif isinstance(w, tk.Text):
                w.delete("1.0", tk.END)
            elif isinstance(w, tk.Listbox):
                w.delete(0, tk.END)

# ==========================================
# TEST OPERATIVO FAMILIA
# ==========================================
# if __name__ == "__main__":
#     root = tk.Tk()
#     F = Familia()
#     Frame1 = tk.Frame(root, background='#111111')
#     Frame1.pack()
#     btn_add = tk.Button(Frame1, text="Añadir")
#     btn_add.pack()
#     btn_del = tk.Button(Frame1, text="Borrar")
#     btn_del.pack()
#     txt_nom = tk.Entry(root)
#     txt_nom.pack(padx=10, pady=10)
#     txt_nom.insert(0, "Juan")
#     # Registro
#     F.formar('botones_control', [ btn_add , btn_del ])
#     F.formar('entradas', [txt_nom])
#     F.familiares('botones_control')[0].config(bg="lightgray")
#     # --- PRUEBAS DE LLAMADA DIRECTA ---
#     F('botones_control')        # Esto funciona gracias a __call__
#     F()                         # Muestra el resumen

#     root.mainloop() # Cerramos la ventana de test

class Nivel_2:
    """ 
    • Crea un Frame Formulario e inserta los widgets con un dibujo ( draw() )
    • Mete los elementoes en level_1 por lo que NO tienes que definir la fila en el momento de la creación.
    • De esta forma al definir el objeto puedo pasarle simplemente frame (level_1)
      dibujas el formulario con draw y ahí se define la posición definitiva de los widgets. 
    • Es mas cuadrado que row_fix porque define cada espacio.
    """
    def __init__(self,  contenedor, 
                        shape=None,
                        title="Formulario", 
                        ancho=300, alto=450, 
                        padx=5, pady=5 ):
        self.contenedor = contenedor
        """ contenedor del Frame que vamos a crear. """
        self.padx = padx
        self.pady = pady
        """ Distancia horizontal y vertical entre widgets, y filas vacías y columnas vacías. """
        self.level_1 = tk.Frame(self.contenedor)
        """ frame contenedor principal. se obtiene con frame()  """
        self.level_1.pack(fill="both", expand=True, padx=self.padx, pady=pady)
        self.level_2 = {}      # Diccionario de filas existentes (metadatos)
        """ diccionario de frames fila contenidos en level_1  """
        self.filas = None
        """ Numero de filas del frame """        
        self.columnas = None   
        """ Numero de columnas del frame """        
        self._draw_map = []    
        """ Mapa de posiciones tras draw() """        
        self.family = Familia()
        """ Clase familia para hacer agrupaciones de widgets custom """        
        
        # ■ ■  Procesar shape "filasxcolumnas" 
        if shape is not None:
            try:
                filas_str, cols_str = shape.lower().split('x')
                self.filas = int(filas_str.strip())
                self.columnas = int(cols_str.strip())
                #  [6] * 5 = [6,6,6,6,6] ... lo uso como validación: 
                cols_by_fila = [self.columnas] * self.filas
            except ValueError:
                raise ValueError(f"Formato de shape inválido: '{shape}'. Use formato 'filasxcolumnas' (ej: '4x6')")
        pass        
        # Construye level_1 y level_2
        if self.filas or (isinstance(cols_by_fila, list) and len(cols_by_fila) > 0):
            self._construye_estructura_levels(cols_by_fila)

    def _construye_estructura_levels(self, cols_config):
        """
        Configura level_1 como grid maestro.
        level_2[i] registra metadatos de cada fila.
        """
        for i, num_cols in enumerate(cols_config):
            if num_cols and num_cols > 0:
                self.level_1.grid_rowconfigure(i, weight=0, minsize=self.pady)
                self.level_2[i] = {'row': i, 'cols': num_cols, 'type': 'active'}
            else:
                # Fila vacía: dejamos espacio reservado
                self.level_1.grid_rowconfigure(i, weight=0, minsize=self.pady * 2)
                self.level_2[i] = {'row': i, 'cols': 0, 'type': 'spacer'}
        
        # Configurar columnas en level_1
        max_cols = max((c for c in cols_config if isinstance(c, int)), default=0)
        for col in range(max_cols):
            self.level_1.grid_columnconfigure(col, weight=1)
    
    @property
    def frame(self):
        return self.level_1 if self.level_1 else None

    def row(self, index):
        """
        ■ Siempre devuelve level_1.
        Todos los widgets se crean como hijos del mismo contenedor.
        El posicionamiento real lo hace draw().
        """
        return self.level_2.get(index)

    def _add(self, widget, column, row=0, **kwargs):
        """
        ■ posiciona en level_1.
        """
        if 'sticky' not in kwargs:
            kwargs['sticky'] = "we"
        widget.grid(in_=self.level_1, row=row, column=column, **kwargs)
        return widget

    def _set_row(self, row, *items, **kwargs):
        """
        ■ posiciona widgets en una fila específica de level_1.
        """
        if row not in self.level_2:
            raise ValueError(f"La fila {row} no existe.")
        added_widgets = []
        for column, item in enumerate(items):
            if self._is_empty_cell(item):
                continue
            widget = item
            widget.grid_forget()
            widget.grid(in_=self.level_1, row=row, column=column, sticky="we", **kwargs)
            added_widgets.append(widget)
        return added_widgets
    
    def _is_empty_cell(self, item):
        return item is None or item == "_" or item == '-' 
    
    def draw(self, matrix):
        """
        • Recibe una matriz de widgets (todos hijos de level_1).
        • La posición en la matriz PREVALECE sobre cualquier grid anterior.
        • Guarda un mapa interno self._draw_map con la situación final.
        """
        self._draw_map = []

        for row_idx, row_data in enumerate(matrix):
            if self._skip_row(row_data, row_idx):
                continue

            col_idx = 0
            placed = []     # Tracking interno para colspan

            for item in row_data:
                if self._is_empty_cell(item):
                    placed.append(self._celda_vacia(row_idx, col_idx))
                elif item == "+":
                    self._colspan(placed)
                else:
                    placed.append(self._widget_real(item, row_idx, col_idx))
                col_idx += 1

        return self


    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
    # ■ MÉTODOS MODULARES (KISS)
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 

    def _skip_row(self, row_data, row_idx):
        """ ■ Decide si una fila del matrix debe saltarse."""
        if row_data is None or (isinstance(row_data, (list, tuple)) and len(row_data) == 0):
            return True
        if not isinstance(row_data, (list, tuple)):
            return True
        if row_idx not in self.level_2:
            raise IndexError(
                f"La fila {row_idx} no existe en la estructura. "
                f"Filas disponibles: 0..{self.filas-1}."
            )
        if self.level_2[row_idx]['type'] == 'spacer':
            return True
        return False

    def _celda_vacia(self, row_idx, col_idx):
        """ ■ Crea un frame vacío, lo posiciona y registra el tracking."""
        empty_frame = tk.Frame(self.level_1, width=self.padx)
        empty_frame.grid(in_=self.level_1, row=row_idx, column=col_idx, sticky="we")

        self._draw_map.append({
            'fila': row_idx, 'columna': col_idx,
            'widget': empty_frame, 'tipo': 'empty', 'span': 1
        })
        return {'type': 'empty', 'widget': empty_frame, 'col': col_idx, 'span': 1}

    def _colspan(self, placed):
        """ ■ Extiende el span del último widget real a la izquierda."""
        target = None
        target_pos = None

        for k in range(len(placed) - 1, -1, -1):
            p = placed[k]
            if p['type'] == 'widget':
                target = p['widget']
                target_pos = k
                break
            elif p['type'] == 'empty':
                break

        if target is not None:
            new_span = placed[target_pos].get('span', 1) + 1
            placed[target_pos]['span'] = new_span
            target.grid_configure(columnspan=new_span)

            for m in self._draw_map:
                if m['widget'] is target:
                    m['span'] = new_span
                    break

    def _widget_real(self, item, row_idx, col_idx):
        """ ■ Posiciona un widget real en el grid y registra el tracking."""
        item.grid_forget()
        item.grid(in_=self.level_1, row=row_idx, column=col_idx, sticky="we")

        self._draw_map.append({
            'fila': row_idx, 'columna': col_idx,
            'widget': item, 'tipo': 'widget', 'span': 1
        })
        return {'type': 'widget', 'widget': item, 'col': col_idx, 'span': 1}


    def fdlg(self,  texto_boton="📂 Load File", title="Seleccionar Archivo", 
                    initialdir=None, filetypes=None, 
                    entry_width=40, b_split=False):
        """
        Crea un FDialoger.
        - entry_width(int): El tamaño de la caja de texto.
        - b_split=False (default): empaqueta Entry+Button dentro de un Frame y devuelve el Frame.
        - b_split=True: devuelve los widgets sueltos (entry, button) para que draw() los coloque
          en celdas independientes de la matriz.
        
        """
        if b_split:
            # Modo suelto: los widgets nacen directamente en self.frame
            fd = FDialoger(
                parent      = self.frame,
                texto_boton = texto_boton,
                title       = title,
                initialdir  = initialdir,
                filetypes   = filetypes,
                entry_width = entry_width,
            )
            # Devolvemos los widgets para que el usuario los distribuya en la matriz
            
            return fd.entry, fd.btn

        else:
            contenedor = ttk.Frame(self.frame)
            fd = FDialoger(
                parent      = contenedor,
                texto_boton = texto_boton,
                title       = title,
                initialdir  = initialdir,
                filetypes   = filetypes,
                entry_width = entry_width,
            )
            fd.entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
            fd.btn.pack(side="left")
            # Delegación: Lo que ocurre aquí es monkey patching básico: 
            # le estás pegando métodos al Frame como si fueran susyos.
            # fdlg_widget.get_ruta = lambda: fd.get_ruta()
            # ahora se puede usar los metodos de FileDialoger en el Frame contenedor
            contenedor.get_ruta            = fd.get_ruta
            contenedor.get_ruta_abreviada  = fd.get_ruta_abreviada
            contenedor.set_ruta            = fd.set_ruta
            contenedor.entry               = fd.entry
            contenedor.btn                 = fd.btn
            
            return contenedor




# ██████████████████████████████████████████
# █████████████ EJEMPLO DE USO █████████████
# ██████████████████████████████████████████
# if __name__ == "__main__":
#     root = tk.Tk()
#     # root.geometry("800x300")
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     # Estructura: 
#     F1 = Nivel_2(root, shape="5x6", padx=15, pady=7)
#     print(f"Filas: {F1.filas}, Columnas: {F1.columnas}")
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     # ■ Todos los widgets se crean en level_1 (frame devuelve level_1 siempre)
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     lbl_nom  = tk.Label(F1.frame, text='Nombre: ', anchor='w')
#     txt_nom  = tk.Entry(F1.frame)
#     lbl_ape1 = tk.Label(F1.frame, text='Apellido1: ')
#     txt_ape1 = tk.Entry(F1.frame)
#     lbl_ape2 = tk.Label(F1.frame, text='Apellido2: ')
#     txt_ape2 = tk.Entry(F1.frame)
#     btn_add = tk.Button(F1.frame, text="Añadir")
#     btn_upt = tk.Button(F1.frame, text="Actualiza")
#     btn_del = tk.Button(F1.frame, text="Borrar")
#     scrollbar = tk.Scrollbar(F1.frame, orient=tk.VERTICAL)
#     listbox = tk.Listbox(F1.frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
#     lbl_sc = tk.Label(F1.frame, text='Slide Val: ')
#     var_sc = tk.DoubleVar(value=5)
#     scale = tk.Scale(F1.frame, from_=0, to=10, resolution=1, variable=var_sc, orient=tk.HORIZONTAL, length=150, font=('Arial', 8))
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     # ■ Matriz que dicta la posición FINAL (prevalencia)
#     #    Da igual en qué fila los creaste con row(), draw() los manda donde toca
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     matrix = [
#         [lbl_nom,  txt_nom, "+", "+", "+", "_"       ],   # Fila 0
#         [lbl_ape1, txt_ape1, "_", lbl_ape2, txt_ape2 ],   
#         ['-' , listbox, '+', '+', '+', '-'],
#         [lbl_sc, scale, '+', '+', '+', '+', '+'],
#         [btn_add,  btn_upt, "+", "_", btn_del ],
#     ]    
#     F1.draw(matrix)
#     # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
#     print("\n--- MAPA DE DRAW ---")
#     for entry in F1._draw_map:
#         print(entry)
#     # ______________________
#     F1.frame().config(bg="lightgray")
#     # ______________________
#     F1.family.formar("textos", [txt_nom, txt_ape1, txt_ape2,])
#     F1.family.formar("crud", [btn_add, btn_upt, btn_del,])
#     # ______________________
#     textos = F1.family.familiares('textos')
#     for i, t in enumerate(textos):
#         t.delete(0, tk.END)
#         t.insert(1, f"Hello Texto {i}")
#     # █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ 
#     root.mainloop()
#     # █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ █ ■ 