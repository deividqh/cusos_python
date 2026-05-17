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
                    ("Modulo 01" , None),
                    ("Modulo 02" , None), 
                    ("Modulo 03" , None), 
                    ("ESTYLE UI" , None) ] )
    
    The_X_Men.addX( titulo='ej_mod1', padre='Menu1'   , ipadre='Modulo 01'    , 
                    lst_items = [ 
                    ("Ejercicio 1", None) , 
                    ("Ejercicio 2" , None) 
                    ])    
    
    The_X_Men.addX( titulo='estilos', padre='Menu1' , ipadre='ESTYLE', 
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

# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    
    multiprocessing.freeze_support()
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
