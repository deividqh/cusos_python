# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# from classXindeX import XindeX        # ■ XINDEX A PELO
from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from colorama import Fore, Style, init  # ■ COLORAMA PARA COLORES EN TERMINAL....por si se quiere usar colores para 'ayudas'
import os               # SISTEMA OPERATIVO(PARA LIMPIAR LA TERMINAL)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import multiprocessing

# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █          LLAMADA AL MENU
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 

# ■■■■■■■■ INSTANCIO EL OBJETO ■■■■■■■■■ 
The_X_Men = Over_Main(tipo_index='a', b_mode_all=True, b_loop=True )

def main():
    # global The_X_Men

    # ■ ■ ■ ■ CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS 
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, 
                    lst_items = [ 
                    ("Familia" , main_familia),
                    ("Pestañas" , main_pestanas), 
                    ("Formulario Row_Form(la base)" , main_row_form), 
                    ("Formulario Row_Fix  " , main_row_fix), 
                    ("Formulario Row_Draw (el bueno)" , main_row_draw), 
                    ("Me pone un mixto?" , mixto), 
                    ])
    
    # ■ ■ ■ ■ Lo dejo de ejemplo.... ipadre(Familia) = indice de donde cuelga este sub-menu en el padre(Menu1)
    # The_X_Men.addX( titulo='fam', padre='Menu1'   , ipadre='Familia'    , 
    #                 lst_items = [ 
    #                 ("main familia", main_familia) , 
    #                 ])    
    
    # ■ ■ ■ ■  LLAMO A MYSTYCA PARA VISUALIZAR EL MENU 
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " Formularios DVD " , pad_x=5 )

    # ■■■■■ RETORNO DE MYSTYCA (Opcional)
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")

# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █          FUNCIONES DEFINIDAS EN EL MENU
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 

def main_familia():
    from ui_tk.Familia import Familia
    import tkinter as tk
    root = tk.Tk()
    Frame1 = tk.Frame(root, background='#111111')
    Frame1.pack()
    F = Familia()

    btn_add = tk.Button(Frame1, text="Añadir")
    btn_add.pack()
    btn_del = tk.Button(Frame1, text="Borrar")
    btn_del.pack()
    txt_nom = tk.Entry(root)
    txt_nom.pack(padx=10, pady=10)
    txt_nom.insert(0, "Juan")
    # Registro
    F.family('botones_control', [ btn_add , btn_del ])
    F.family('entradas', [txt_nom])
    F.familiares('botones_control')[0].config(bg="lightgray")
    # --- PRUEBAS DE LLAMADA DIRECTA ---
    F('botones_control')        # Esto funciona gracias a __call__
    F()                         # Muestra el resumen
    # root.withdraw() # Cerramos la ventana de test
    root.mainloop() # Cerramos la ventana de test
    pass

def main_pestanas():
    from ui_tk.pestanas_dicc import StepByStab 
    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Sistema de Pestañas Secuenciales")
    ventana.geometry("680x350")
    # Configuración de las pestañas a añadir. key es el nombre corto y value es el Título de la UI.
    config = {
        "dat": "Datos",
        "split": "Split",
        "alg": "Algoritmo/Modelo",
        "met": "Métricas",
        "graf": "Gráficas"
    }
    TABS = StepByStab(ventana, config)
    TABS.pack(fill="both", expand=True, padx=10, pady=10)

    # ✔️ INYECTANDO CONTROLES EN LAS PESTAÑAS (Usando las llaves custom)     
    # ■ ■ Pestaña Datos 
    p_datos = TABS.get_p("dat")
    ttk.Label(p_datos, text="■ Configuración de Datos del Modelo", font=("Arial", 11, "bold")).pack(pady=10)
    ttk.Entry(p_datos).pack(pady=5)
    # ■ ■ Pestaña Split 
    p_split = TABS.get_p("split")
    ttk.Label(p_split, text="■ Proporción del Split (Train/Test)", font=("Arial", 11, "bold")).pack(pady=10)
    ttk.Scale(p_split, from_=0, to=100, orient="horizontal").pack(fill="x", padx=30, pady=5)
    # ■ ■ Pestaña Algoritmo 
    p_alg = TABS.get_p("alg")
    ttk.Label(p_alg, text="■ Selección de Algoritmo", font=("Arial", 11, "bold")).pack(pady=10)
    
    # ■ PANEL DE CONTROL GLOBAL ESTI SE TIENE QUE ELIMINAR.
    # ■ SOLO VALE PARA MANTENER LAS FUNCIONES go_next y blok_from.
    panel_control = ttk.Frame(ventana)
    panel_control.pack(fill="x", padx=10, pady=10)
    
    # Botón Avanzar: Detecta la pestaña actual dinámicamente y avanza
    btn_avanzar = ttk.Button(
        panel_control,
        text="Validar y Avanzar ➡️",
        command=lambda: TABS.go_next( TABS.notebook.index("current") )
    )
    btn_avanzar.pack(side="left", padx=5, expand=True, fill="x")
    # Botón Bloquear: Bloquea todo el camino que esté por delante de la pestaña actual
    btn_bloquear = ttk.Button(
        panel_control,
        text="🔒 Bloquear Siguientes",
        command=lambda: TABS.blok_from( TABS.notebook.index("current") + 1 )
    )
    btn_bloquear.pack(side="left", padx=5, expand=True, fill="x")
    ventana.mainloop()
    pass

def main_row_form():
    import tkinter as tk
    from Pruebas_Forms.Row_Form import Nivel_2
    root = tk.Tk()
    root.geometry("680x200")
    # ■ Creamos la estructura
    alt_config = [6, 6,  6 , 6,  6, 6]
    F1 = Nivel_2(root, cols_by_fila=[6, 6,  6 , 6,  6, 6], padx=15, pady=7)
    # F1 = Nivel_2(root, shape="4x6", padx=15, pady=7)
    # ■ Creamos widgets y los asigno a una fila del frame F1
    lbl_nom = tk.Label(F1.row(1), text='Nombre: ')
    txt_nom = tk.Entry(F1.row(1))    
    lbl_ape = tk.Label(F1.row(2), text='Apellido: ')
    txt_ape = tk.Entry(F1.row(2))    
    btn_add = tk.Button(F1.row(3), text="Añadir")
    btn_del = tk.Button(F1.row(3), text="Borrar")
    btn_upt = tk.Button(F1.row(3), text="Actualiza")
    # ■ Posicionamos
    # F1.add(lbl_ape, column= 0)
    F1.set_row(1, lbl_nom, '_', '_' , txt_nom)
    F1.set_row(2, lbl_ape, txt_ape)
    F1.set_row(3, btn_add, btn_upt , "_", "_", "_",btn_del)
    F1.frame().config(bg="lightgray")
    root.mainloop()
    pass

def checkbox_estado():
    # El método .get() obtiene el valor actual (1 si está marcado, 0 si no)
    if var_chk.get() == 1:
        checkbox.config(text="¡Casilla marcada!")
    else:
        checkbox.config(text="Casilla desmarcada")

def main_row_fix():
    """ Dibuja un Frame Tkinter en una ventana con un dibujo de la distribución.    
    Tienen  que coincidir la fila definida en row con el dibujo en draw.    
    """
    from ui_tk.row_fix import Nivel_2
    import tkinter as tk
    from tkinter import ttk  # Importa los componentes modernos
    root = tk.Tk()
    root.geometry("800x350")
    # Crear estructura shape
    F1 = Nivel_2(root, shape="10x6", padx=10, pady=8)    
    print(f"Filas: {F1.filas}, Columnas: {F1.columnas}")    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ Crear widgets • Es importante colocar la fila ro_row
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    lbl_nom  = tk.Label(F1.row(0), text='Nombre: ')
    txt_nom  = tk.Entry(F1.row(0))
    # ■ 
    lbl_ape1 = tk.Label(F1.row(1), text='Apellido1: ')
    txt_ape1 = tk.Entry(F1.row(1))
    lbl_ape2 = tk.Label(F1.row(1), text='Apellido2: ')
    txt_ape2 = tk.Entry(F1.row(1))
    # ■ 
    var_chk = tk.IntVar()
    checkbox = tk.Checkbutton(F1.row(2), text="soy CheckButton", variable=var_chk, command=checkbox_estado )
    var_sc = tk.DoubleVar(value=5)
    slide = tk.Scale(F1.row(2), from_=0, to=10, resolution=1, variable=var_sc, orient=tk.HORIZONTAL, length=150, font=('Arial', 8))
    # ■ 
    combo = ttk.Combobox(F1.row(2), values=["dark_background", "ggplot", "bmh", "seaborn-v0_8-whitegrid"], state="readonly")
    combo.current(0)
    # ■ 
    btn_add = tk.Button(F1.row(4), text="Añadir")
    btn_upt = tk.Button(F1.row(4), text="Actualiza")
    btn_del = tk.Button(F1.row(4), text="Borrar")
    # ■ 
    scrollbar = tk.Scrollbar(F1.row(5), orient=tk.VERTICAL)
    listbox = tk.Listbox(F1.row(5), selectmode=tk.SINGLE)
    # ■■■■■■■■■■■■■■■■■■■■■■ 
    # ■ Matriz de dibujo
    # ■■■■■■■■■■■■■■■■■■■■■■ 
    matrix = [
        [lbl_nom,  txt_nom , '+'  , '+'  , '+'     ],  # Fila 0
        [lbl_ape1, txt_ape1, "+", lbl_ape2, txt_ape2  , '+'],  # Fila 1
        [combo, '_', slide , '_', checkbox, '_'],                                                    # Fila 2 (vacía)
        [listbox, '+', '+', '+', '+', '+'],                               
        [btn_add,  btn_upt,  "_", '_',  "_",  btn_del      ],  # Fila 4
    ]    
    F1.draw(matrix)  
    # F1.frame().config(bg="lightgray")
    root.mainloop()

def main_row_draw():
    """ Dibuja un Frame Tkinter en una ventana con un dibujo de la distribución.
    level_1 es el frame donde van todos los widgets, luego se reparten con draw.
    muy comoda de incorporar elementos.
    """
    from ui_tk.row_draw import Nivel_2
    import tkinter as tk
    from tkinter import ttk  # Importa los componentes modernos

    root = tk.Tk()
    # root.geometry("800x500")
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■     
    F1 = Nivel_2(root, shape="5x6", padx=15, pady=7)    
    # print(f"Filas: {F1.filas}, Columnas: {F1.columnas}")
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■     
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
    # ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • 
    # ■ Matriz que dicta la posición FINAL (prevalencia)
    #    Da igual en qué fila los creaste con row(), draw() los manda donde toca
    # ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • ■ • 
    matrix = [
        [lbl_nom,  txt_nom, "+", "+", "+", "_"       ],
        [lbl_ape1, txt_ape1, "_", lbl_ape2, txt_ape2 ],   
        ['-' , listbox, '+', '+', '+', '-'],              
        [],                                             
        [btn_add,  btn_upt, "+", "_", btn_del ],   
    ]
    F1.draw(matrix)
    # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■     
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■ asocia nombre a grupo de widgets.
    F1.family.formar("textos", [txt_nom, txt_ape1, txt_ape2,])
    F1.family.formar("crud", [btn_add, btn_upt, btn_del,])

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■ Aplica los comandos de los widgets limpiamente en otro archivo.
    import comandos_ui_tk as cuitk
    btn_del.config(command=lambda: cuitk.limpiar_textos( F1.family.familiares('textos') ))
    btn_add.config(command=lambda: cuitk.mostrar_alerta( "Texto de Alerta de Prueba" ))

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■ Ver el mapa generado de 'la familia'.
    print("\n--- MAPA DE DRAW ---")
    for entry in F1._draw_map:
        print(entry)
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■ Cacha el frame level_1 y le cambio el estilo.
    F1.frame.config(bg="lightgray")
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■ Cacho los widgets de una familia y opero sobre ellos.
    textos = F1.family.familiares('textos')
    for i, t in enumerate(textos):
        t.delete(0, tk.END)
        t.insert(1, f"Hello Texto {i}")

    # • • • — — — • • •
    root.mainloop()
    # • • • — — — • • •

def mixto():
    """ Quiero poner una de pestañas y en cada pestaña un Frame al menos de prueba """
    from ui_tk.pestanas_dicc import StepByStab 
    from ui_tk.row_draw import Nivel_2
    import comandos_ui_tk as cuitk

    import tkinter as tk
    from tkinter import ttk
    ventana = tk.Tk()
    ventana.title("Sistema de Pestañas Secuenciales")
    ventana.geometry("680x350")
    # Configuración de las pestañas a añadir. key es el nombre corto y value es el Título de la UI.
    configuracion_pestanas = {
        "dat": "Datos",
        "split": "Split",
        "alg": "Algoritmo/Modelo",
        "met": "Métricas",
        "graf": "Gráficas"
    }
    TABS = StepByStab(ventana, configuracion_pestanas)
    TABS.pack(fill="both", expand=True, padx=10, pady=10)
    
    # ■ PANEL DE CONTROL GLOBAL ESTI SE TIENE QUE ELIMINAR.
    # ■ SOLO VALE PARA MANTENER LAS FUNCIONES go_next y blok_from.
    panel_control = ttk.Frame(ventana)
    panel_control.pack(fill="x", padx=10, pady=10)

    # Botón Avanzar: Detecta la pestaña actual dinámicamente y avanza
    btn_avanzar = ttk.Button(
        panel_control,
        text="Validar y Avanzar ➡️",
        command=lambda: TABS.go_next( TABS.notebook.index("current") )
    )
    btn_avanzar.pack(side="left", padx=5, expand=True, fill="x")
    # Botón Bloquear: Bloquea todo el camino que esté por delante de la pestaña actual
    btn_bloquear = ttk.Button(
        panel_control,
        text="🔒 Bloquear Siguientes",
        command=lambda: TABS.blok_from( TABS.notebook.index("current") + 1 )
    )
    btn_bloquear.pack(side="left", padx=5, expand=True, fill="x")

    # ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ 
    F1 = Nivel_2(TABS.get_p('dat'), shape="5x6", padx=15, pady=7)    
    # ■ WIDGETS
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
    # ■■■■■■■■■  MATRIZ
    matrix = [
        [lbl_nom,  txt_nom, "+", "+", "+", "_"       ],
        [lbl_ape1, txt_ape1, "_", lbl_ape2, txt_ape2 ],   
        ['-' , listbox, '+', '+', '+', '-'],              
        [],                                             
        [btn_add,  btn_upt, "+", "_", btn_del ],   
    ]
    # ■■■■■■■■■  DIBUJO
    F1.draw(matrix)
    # • • • • • • • • • • • • • • asocia nombre a grupo de widgets.
    F1.family.formar("textos", [txt_nom, txt_ape1, txt_ape2,])
    F1.family.formar("crud", [btn_add, btn_upt, btn_del,])
    # • • • • • • • • • • • • • • Aplica los comandos de los widgets limpiamente en otro archivo.
    btn_del.config(command=lambda: cuitk.limpiar_textos( F1.family.familiares('textos') ))
    btn_add.config(command=lambda: cuitk.mostrar_alerta( "Texto de Alerta de Prueba" ))

    # • • • — — — • • •
    ventana.mainloop()
    # • • • — — — • • •

# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# • • • • • • • • • • • • • • • • • INICIO • • • • • • • • • • • • • • • • • • • 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
# █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 
if __name__ == "__main__":
    # • Fundamental para que los sub-procesos creados no hagan bucle.
    multiprocessing.freeze_support()
    # • Limpio la terminal 
    os.system('cls')    
    main() 
