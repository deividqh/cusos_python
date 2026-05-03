# Llamada a una funcion desde otro archivo:
# ------------------------------------------
# from ..dvd import RAM
# result= RAM.MenuLista(menu)    

# ----------MENU BASIC--------------
# menu=["SALIR", "XXX", "YYY"]
def MenuLista(menu, tituloMenu):
    salir=["SALIR"]
    menu=salir+menu    
    # Imprime Menu:
    # print(f'-'*9, end='')
    # print(f'{tituloMenu}', end='')
    # print(f'-'*9)    
    print('\n'+'*'*40+tituloMenu+'\n'+'*'*40)
    for index,opc in enumerate(menu):
        print (f'{index}....{opc}')
    print ('-'*40)    
    
    while(True):
        # Selecciona Opcion:
        i=input("Intro opcion... ")    
        # Si todo lo introducido en la cadena son digitos = True
        if i.isdigit():
            i=abs(int(i))
            if i==0: return None
            if i>len(menu): 
                continue
            else:                
                return i
        else:
            continue
    

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

def MenuDvd(menu, tituloMenu="Menu"):
    if isinstance(menu, list):        
        return MenuLista(menu, tituloMenu)
    elif isinstance(menu,dict):
        return MenuDiccionario(menu, tituloMenu)