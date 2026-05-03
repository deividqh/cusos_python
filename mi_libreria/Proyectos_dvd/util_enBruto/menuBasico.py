# Llamada a una funcion desde otro archivo:
# ------------------------------------------
# from ..dvd import RAM
# result= RAM.MenuLista(menu)    

# ----------MENU BASIC--------------
# menu=["SALIR", "XXX", "YYY"]
def MenuLista(menu):
    salir=["SALIR"]
    menu=salir+menu
    print(menu)
    # while (True):
        # Imprime Menu:
    print ('-'*18,'\nMenu')    
    for index,opc in enumerate(menu):
        print (f'{index}....{opc}')
    print ('-'*18)
    
    # Selecciona Opcion:
    i=abs(int(input("Intro opcion... ")))        
    
    if i>len(menu): return -1

    return i 



