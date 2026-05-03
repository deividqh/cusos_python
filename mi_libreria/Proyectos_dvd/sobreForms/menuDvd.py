# Llamada a una funcion desde otro archivo:
# ------------------------------------------
# from ..dvd import RAM
# result= RAM.MenuLista(menu)    

# ----------MENU BASIC--------------
# menu=["SALIR", "XXX", "YYY"]

# No se usa
def MenuDiccionario(menu, tituloMenu):
    if not isinstance(menu,dict): return -1
    salir={"SALIR": 0}
    # Asi puedes adjuntar por el principio (y recibir en una funcion) un diccionario(**), una lista se envia así(*)
    menuSalir={**salir, **menu}
    # al pasar menu por referencia, cambia en la funcion que lo llama tb. 
    # y no lo retorno sino que lo cambio aqui.
    menu=menuSalir
    # print(menuSalir)
    # while (True):
        # Imprime Menu:
    
    # Estas cossa de python son la pera
    print ('\n'+'-'*9,tituloMenu,'-'*9)    
    for index,tit in enumerate(menuSalir):
        print (f'{index}....{tit}')
    print ('-'*22)
    
    # Selecciona Opcion:
    i=input("Intro opcion... ")
    if i.isdigit():
        i=abs(int(i))
    else:
        return -1

    return i
# _________________________________
# Esta es la que se usa. Con listas
# =================================
def MenuDvd(menu, tituloMenu="M E N U", 
            msgItem='Intro Opcion...', 
            num_char=40,
            char_1='-', char_2='-', char_3='-'):
    """ 
    Devuelve un menu. Añade la opcion de salir.
    [menu]: lista de str con los textos del menu.

    """
    salir=["SALIR"]
    menu=salir+menu    
    # Imprime Menu:
    # print('\n'+char_1*40+'\n'+tituloMenu+'\n'+char_2*40)
    print(f'\n{char_1*num_char}\n{tituloMenu}\n{char_2*num_char}')
    for index,opc in enumerate(menu):
        print (f'{index}....{opc}')
    print (f'{char_3*num_char}')    
    
    while(True):
        # Selecciona Opcion:        
        i=input(f"{msgItem}")    
        # Si todo lo introducido en la cadena son digitos = True
        try:
            if i.isdigit():
                i=abs(int(i))
                if i==0: return None
                if i>len(menu): 
                    continue
                else:                
                    return i
            else:
                continue
        except Exception:
            continue
