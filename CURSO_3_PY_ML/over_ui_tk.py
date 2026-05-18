# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# from classXindeX import XindeX        # ■ XINDEX A PELO
from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from colorama import Fore, Style, init  # ■ COLORAMA PARA COLORES EN TERMINAL....por si se quiere usar colores para 'ayudas'
import os               # SISTEMA OPERATIVO(PARA LIMPIAR LA TERMINAL)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import multiprocessing

# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████

# 1- INSTANCIO EL OBJETO ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
The_X_Men = Over_Main(tipo_index='a', b_mode_all=True, b_loop=True )

def main():
    global The_X_Men

    # ■- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ▄▄▄▄▄▄▄▄▄▄▄▄
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, 
                    lst_items = [ 
                    ("Familia" , None),
                    ("Pestañas" , None), 
                    ("Row_Form" , None), 
                    ("ESTYLE UI" , None) ] )
    
    The_X_Men.addX( titulo='fam', padre='Menu1'   , ipadre='Familia'    , 
                    lst_items = [ 
                    ("main familia", main_familia) , 
                    ])    
    
    The_X_Men.addX( titulo='pest', padre='Menu1'   , ipadre='Pestañas'    , 
                    lst_items = [ 
                    ("main pestañas", main_pestanas) , 
                    ])    
    The_X_Men.addX( titulo='rforms', padre='Menu1'   , ipadre='Row_Form'    , 
                    lst_items = [ 
                    ("main rForms", main_row_form) , 
                    ])    
    
    The_X_Men.addX( titulo='estilos', padre='Menu1' , ipadre='ESTYLE UI', 
                    lst_items = [ ("Switch Modo Exec", set_style) , 
                    ("Estilo del Marco" , cambiar_estilo_marco), 
                    ])    
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FORMA LARGA Y MAS ANTIGUA.
    # ■ AÑADE Y CONFIGURA - es el camino largo... o por partes.
    # The_X_Men.addX(titulo='subXindex', lst_items=[ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", parametros ), ("Ejemplos Uso" , None ) ])
    # The_X_Men.config(titulo='subXindex' , suPadre='Menu1' , indexInPadre='Info XindeX' )    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " Indice Curso Python Machine L. " , pad_x=5 )

    # 5- RETORNO DE MYSTYCA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")


# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████

def set_style():
    global The_X_Men
    if The_X_Men.get_b_mode_all() == True:
        b_mode_all = False
    else:
        b_mode_all = True
    The_X_Men.set_style(b_mode_all = b_mode_all)
    print(f'::: MODO {f'Directorio Switch  To ► Exec-All' if b_mode_all == True else f'Exec-All  Switch To ► Directorio'}  ::: ')
    

def cambiar_estilo_marco():
    global The_X_Men    
    sdata = Sdata.get_data(key_dict='S', tipo=str, msg_entrada='Nombre Estilo(franky/default/unicode/doble/vacio/moderno/elegante)', permite_nulo=False)
    The_X_Men.F_RANK_Y.style(estilo=sdata['S'])
    The_X_Men.F_RANK_Y_DEF.style(estilo=sdata['S'])
    print(f'::: Estilo Marco cambiado a {sdata["S"]} ::: ')


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

    # Tu configuración limpia en un solo sitio
    config = {
        "dat": "Datos",
        "split": "Split",
        "alg": "Algoritmo/Modelo",
        "met": "Métricas",
        "graf": "Gráficas"
    }

    TABs = StepByStab(ventana, config)
    TABs.pack(fill="both", expand=True, padx=10, pady=10)

    # --- INYECTANDO CONTROLES EN LAS PESTAÑAS (Usando tus llaves custom) ---
    
    # Pestaña Datos
    p_datos = TABs.get_p("dat")
    ttk.Label(p_datos, text="📂 Configuración de Datos del Modelo", font=("Arial", 11, "bold")).pack(pady=10)
    ttk.Entry(p_datos).pack(pady=5)

    # Pestaña Split
    p_split = TABs.get_p("split")
    ttk.Label(p_split, text="✂️ Proporción del Split (Train/Test)", font=("Arial", 11, "bold")).pack(pady=10)
    ttk.Scale(p_split, from_=0, to=100, orient="horizontal").pack(fill="x", padx=30, pady=5)

    # Pestaña Algoritmo
    p_alg = TABs.get_p("alg")
    ttk.Label(p_alg, text="🤖 Selección de Algoritmo", font=("Arial", 11, "bold")).pack(pady=10)


    # --- PANEL DE CONTROL GLOBAL (Los botones de antes) ---
    panel_control = ttk.Frame(ventana)
    panel_control.pack(fill="x", padx=10, pady=10)

    # Botón Avanzar: Detecta la pestaña actual dinámicamente y avanza
    btn_avanzar = ttk.Button(
        panel_control,
        text="Validar y Avanzar ➡️",
        command=lambda: TABs.avanzar_a_siguiente(
            TABs.notebook.index("current")
        )
    )
    btn_avanzar.pack(side="left", padx=5, expand=True, fill="x")

    # Botón Bloquear: Bloquea todo el camino que esté por delante de la pestaña actual
    btn_bloquear = ttk.Button(
        panel_control,
        text="🔒 Bloquear Siguientes",
        command=lambda: TABs.bloquear_pestanas_desde(
            TABs.notebook.index("current") + 1
        )
    )
    btn_bloquear.pack(side="left", padx=5, expand=True, fill="x")

    ventana.mainloop()

    pass

def main_row_form():
    import tkinter as tk
    from ui_tk.Row_Form import Nivel_2
    root = tk.Tk()

    # ■ Creamos la estructura
    alt_config = [6, 6,  6 , 6,  6, 6]
    L2 = Nivel_2(root, cols_by_fila=alt_config, padx=15, pady=7)

    # ■ Creamos widgets y los asigno a una fila del frame L2
    lbl_nom = tk.Label(L2.to_row(1), text='Nombre: ')
    txt_nom = tk.Entry(L2.to_row(1))    
    lbl_ape = tk.Label(L2.to_row(2), text='Apellido: ')
    txt_ape = tk.Entry(L2.to_row(2))    
    btn_add = tk.Button(L2.to_row(3), text="Añadir")
    btn_del = tk.Button(L2.to_row(3), text="Borrar")
    btn_upt = tk.Button(L2.to_row(3), text="Actualiza")
    
    # L2.order([])
    # ■ Posicionamos
    # L2.add(lbl_ape, column= 0)
    # L2.add(txt_ape, column= 1)
    # L2.add(lbl_nom, column= 4)
    # L2.add(txt_nom, column= 5)
    # L2.add(btn_add, column= 0)
    # L2.add(btn_del, column= 1)
    # L2.add(btn_upt, column= 5)
    
    L2.set_row(1, lbl_nom, '_', '_' , txt_nom)
    L2.set_row(2, lbl_ape,  '_', '_', '_', '_', txt_ape)
    L2.set_row(3, btn_add, btn_upt , "_", "_", "_",btn_del)
    
    L2.get_Frame().config(bg="lightgray")
    
    root.mainloop()
    pass



# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    
    multiprocessing.freeze_support()
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
