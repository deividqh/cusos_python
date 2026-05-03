import os           
from enum import Enum

import tkinter as tk
import threading

from sobreFormularios.form_BBDD import Form_BBDD
from sobreFormularios.formPosMov import FormPosMov


# ====================================================================================
# DEF: MAIN QUE DEFINE UN FORMULARIO Y UN Menu   M U L T I - H I L O  en Terminal.
#     -El menú no induce el multi-hilo. Se muestra a la par que el formulario.
#     -
# ====================================================================================
# ==============================================================
# ==============================================================
# OBJETIVOS:1(Ppal)-Seleccionar una base de datos
#           2-Obtener el nombre y numero de tablas. -> ComboBox
#           3-Seleccionar Tabla con ComboBox. 
#           4-Ver tabla en un TreeView con un C.R.U.D. 
#           5-Seleccionar filas y Visualizar datos en TextBox -> CRUD

""" NOTA: Todo tiene que ser   M u l t i H i l o   desde el principio... Lista de Roots(Ventanas-Tablas) """
# --------------------------------------------------------------
#           6-Poder hacer consultas sql con un textBox y button sobre la tabla seleccionada.
#           7-Mostrar informacion sobre la columna( PK, NULL/NOT NULL, FK(tablaForanea) )
#           8-Mostrar cambas basico de tablas con relaciones y flechas. 
# ==============================================================
# ==============================================================
# ###########
def main():

    # ============= raiz para el SERVIDOR
    root = tk.Tk()
    root.title("Formulario DinaDvB")
    # ============= Formulario Vacío en movimiento y posicionado 
    """ 
    import formPosMov
    Formmove= formPosMov.FormPosMov(root)
    # Borrar, solo para pruebas
    root.mainloop()
    """
    FormDB=Form_BBDD(root=root)
    """ 
    FServidor.OpenVentanaDownRight("Servidor Creado pero no mainloop aun")     
    """    
    # =================================    
    # Muestra el Formulario Cliente y servidor en hilos separados para que se ejecuten al mismo tiempo. 
    # Esto lo hago pq el Formulario Toma el Control al hacer mainloop y no puedo tener los dos a la vez.
    hiloMenu  = threading.Thread(target=mainMenu())
    hilo_form_BBDD = threading.Thread(target=root.mainloop())

    # Esto puede no ponerse???
    hiloMenu.start()
    hilo_form_BBDD.start()

    # Esto puede no ponerse???
    hilo_form_BBDD.join()
    hiloMenu.join()

    print("T H E   E N D ::: Proyect-Dvd ( DinaDvB ) Avanza Diseño y Visualizacion de Datos con Python")
    # ____________________
    # Hasta que no se cierra el formulario no se ejecuta este código.
    # Y Cada ventana Toma el Control (Luego se ejecuta una después de la otra)
    # app.OpenVentanaUpRight("Que Pacha!!")
    # app.OpenVentanaDownRight("Que Que Pacha!!")
# ====================================================================

def mainMenu():
    print('\n BIENVENIDO AL  M E N U - D I N A D B  ')


    listaMenuPuebas=["Opt_1  \t(DESC_1)", 
                    "Opt_2:  \t(DESC_2)" , 
                    "Opt_3:  \t(DESC_3)", 
                    "Opt_4:  \t(DESC_4)"
                    ]
    while True:
        respuesta=T(menu=listaMenuPuebas, tituloMenu="D I N A D B")
        if respuesta==None:
            print('\n\nS A L I E N D O ......\n\n')
            break
        elif respuesta==1:
            print('\n')
        elif respuesta==2:
            print('\n')
        elif respuesta==3:
            print('\n')
        elif respuesta==4:
            print('\n')            
        elif respuesta==5:
            print('\n')
        elif respuesta==6:
            print('\n')
        else:
            continue
        






# ******************************
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main()
    
