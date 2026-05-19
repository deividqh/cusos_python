import tkinter as tk
from tkinter import ttk  # Importa los componentes modernos

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
    def family(self, nombre_familia: str, widgets: list = [], b_del: bool = False):
        if nombre_familia not in self.d_family and not b_del:
            self.d_family[nombre_familia] = []
        
        if b_del:
            if nombre_familia in self.d_family:
                for w in widgets:
                    if w in self.d_family[nombre_familia]:
                        self.d_family[nombre_familia].remove(w)
        else:
            for w in widgets:
                if w not in self.d_family[nombre_familia]:
                    self.d_family[nombre_familia].append(w)
    
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
# TEST OPERATIVO
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
#     F.family('botones_control', [ btn_add , btn_del ])
#     F.family('entradas', [txt_nom])
#     F.familiares('botones_control')[0].config(bg="lightgray")
#     # --- PRUEBAS DE LLAMADA DIRECTA ---
#     F('botones_control')        # Esto funciona gracias a __call__
#     F()                         # Muestra el resumen

#     root.mainloop() # Cerramos la ventana de test

class Nivel_2:
    """ 
    Mete los elementoes en level_1 por lo que NO tienes que definir la fila en el momento de la creación.
    De esta forma al definir el objeto puedo pasarle simplemente frame (level_1)
    dibujas el formulario con draw y ahí se define la posición definitiva de los widgets. 
    Es mas cuadrado que row_fix porque define cada espacio.
    """
    def __init__(self, root, title="Formulario", ancho=300, alto=450, 
                 num_filas=None, cols_by_fila=1, padx=5, pady=5, shape=None):
        self.root = root
        self.root.title(title)
        self.padx = padx
        self.pady = pady
        self.level_2 = {}      # Diccionario de filas existentes (metadatos)

        self.family = Familia()
        
        self.columnas = None   # Guarda el número de columnas (para shape)
        self._draw_map = []    # ← Mapa de posiciones tras draw()
        self.level_1 = tk.Frame(self.root)
        self.level_1.pack(fill="both", expand=True, padx=self.padx, pady=pady)
        
        # --- Procesar shape "filasxcolumnas" ---
        if shape is not None:
            try:
                filas_str, cols_str = shape.lower().split('x')
                num_filas = int(filas_str.strip())
                self.columnas = int(cols_str.strip())
                cols_by_fila = [self.columnas] * num_filas
            except ValueError:
                raise ValueError(f"Formato de shape inválido: '{shape}'. Use formato 'filasxcolumnas' (ej: '4x6')")
        
        self.max_rows = len(cols_by_fila) if isinstance(cols_by_fila, list) and len(cols_by_fila) > 0 else 0
        
        if num_filas or (isinstance(cols_by_fila, list) and len(cols_by_fila) > 0):
            self._build_structure(cols_by_fila)

    def _build_structure(self, cols_config):
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
        Legacy: posiciona en level_1.
        """
        if 'sticky' not in kwargs:
            kwargs['sticky'] = "we"
        widget.grid(in_=self.level_1, row=row, column=column, **kwargs)
        return widget

    def _set_row(self, row, *items, **kwargs):
        """
        Legacy: posiciona widgets en una fila específica de level_1.
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
    

    # ============================================================
    # MÉTODO draw / drow — LA MATRIZ PREVALECE
    # ============================================================
    def draw(self, matrix):
        """
        • Recibe una matriz de widgets (todos hijos de level_1).
        • La posición en la matriz PREVALECE sobre cualquier grid anterior.        
        • Guarda un mapa interno self._draw_map con la situación final:
        [
            {'fila': 0, 'columna': 0, 'widget': lbl_nom, 'tipo': 'widget', 'span': 1},
            {'fila': 0, 'columna': 1, 'widget': txt_nom, 'tipo': 'widget', 'span': 1},
            ...
        ]        
        Reglas:
            - None o []: fila vacía (se omite).
            - "_", "-" : celda vacía → Frame vacío con padx.
            - "+": colspan del widget real más cercano a la izquierda.
            - Widget real: grid_forget() + grid(in_=level_1, row=fila, column=col).
        """
        self._draw_map = []
        
        for row_idx, row_data in enumerate(matrix):
            # ■ ■ Fila vacía 
            if row_data is None or (isinstance(row_data, (list, tuple)) and len(row_data) == 0):
                continue            
            if not isinstance(row_data, (list, tuple)):
                continue            
            # ■ ■  No se admiten filas dinámicas 
            if row_idx not in self.level_2:
                raise IndexError(
                    f"La fila {row_idx} no existe en la estructura. "
                    f"Filas disponibles: 0..{self.max_rows-1}."
                )            
            # ■ ■ Si es fila spacer, no se colocan widgets
            if self.level_2[row_idx]['type'] == 'spacer':
                continue   

            # ■ ■ Me meto en cada fila row_data
            col_idx = 0     # puntero de las columnas.
            placed = []     # Tracking interno para colspan: {'type', 'widget', 'col', 'span'}            
            for item in row_data:
                # ── Celda vacía ──
                if item is None or item in ( "_" , "-" ):
                    empty_frame = tk.Frame(self.level_1, width=self.padx)
                    empty_frame.grid(in_=self.level_1, row=row_idx, column=col_idx, sticky="we")
                    
                    placed.append({'type': 'empty', 'widget': empty_frame, 'col': col_idx, 'span': 1})
                    self._draw_map.append({
                        'fila': row_idx, 'columna': col_idx, 
                        'widget': empty_frame, 'tipo': 'empty', 'span': 1
                    })
                    col_idx += 1
                    continue
                
                # ── Colspan "+" ──
                if item == "+":
                    target = None
                    target_pos = None
                    
                    # Buscar último widget real a la izquierda (saltando solo otros "+")
                    for k in range(len(placed) - 1, -1, -1):
                        p = placed[k]
                        if p['type'] == 'widget':
                            target = p['widget']
                            target_pos = k
                            break
                        elif p['type'] == 'empty':
                            break
                    
                    if target is not None:
                        old_span = placed[target_pos].get('span', 1)
                        new_span = old_span + 1
                        placed[target_pos]['span'] = new_span
                        target.grid_configure(columnspan=new_span)
                        
                        # Actualizar span en el mapa
                        for m in self._draw_map:
                            if m['widget'] is target:
                                m['span'] = new_span
                                break
                    
                    col_idx += 1
                    continue
                
                # ── Widget real: la matriz prevalece ──
                item.grid_forget()
                item.grid(in_=self.level_1, row=row_idx, column=col_idx, sticky="we")
                
                placed.append({
                    'type': 'widget', 'widget': item, 
                    'col': col_idx, 'span': 1
                })
                self._draw_map.append({
                    'fila': row_idx, 'columna': col_idx,
                    'widget': item, 'tipo': 'widget', 'span': 1
                })
                col_idx += 1
        
        return self
    

# ==========================================
# EJEMPLO DE USO
# ==========================================
if __name__ == "__main__":
    
    root = tk.Tk()
    # root.geometry("800x300")

    # Estructura: 5 filas x 6 columnas
    F1 = Nivel_2(root, shape="5x6", padx=15, pady=7)
    
    print(f"Filas: {F1.max_rows}, Columnas: {F1.columnas}")

    # ■ Todos los widgets se crean en level_1 (frame devuelve level_1 siempre)
    lbl_nom  = tk.Label(F1.frame, text='Nombre: ', anchor='w')
    txt_nom  = tk.Entry(F1.frame)
    
    lbl_ape1 = tk.Label(F1.frame, text='Apellido1: ')
    txt_ape1 = tk.Entry(F1.frame)
    lbl_ape2 = tk.Label(F1.frame, text='Apellido2: ')
    txt_ape2 = tk.Entry(F1.frame)
    
    btn_add = tk.Button(F1.frame, text="Añadir")
    btn_upt = tk.Button(F1.frame, text="Actualiza")
    btn_del = tk.Button(F1.frame, text="Borrar")

    scrollbar = tk.Scrollbar(F1.frame, orient=tk.VERTICAL)
    listbox = tk.Listbox(F1.frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    
    # ■ Matriz que dicta la posición FINAL (prevalencia)
    #    Da igual en qué fila los creaste con row(), draw() los manda donde toca
    matrix = [
        [lbl_nom,  txt_nom, "+", "+", "+", "_"       ],   # Fila 0
        [lbl_ape1, txt_ape1, "_", lbl_ape2, txt_ape2 ],   # Fila 1
        ['-' , listbox, '+', '+', '+', '-'],                                                      # Fila 2 (vacía)
        None,                                                    # Fila 3 (vacía)
        [btn_add,  btn_upt, "+", "_", btn_del ],   # Fila 4
    ]
    
    F1.draw(matrix)
    
    # Ver el mapa generado
    print("\n--- MAPA DE DRAW ---")
    for entry in F1._draw_map:
        print(entry)
    
    # F1.frame().config(bg="lightgray")
    
    root.mainloop()