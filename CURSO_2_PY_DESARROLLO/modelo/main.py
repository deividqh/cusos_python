import os
import clientes as cli
import menuDvd as menu


# _________________________
def main():
    listaMenu=["Add Cliente", "Updte", "Delete", "Imprime Cliente", "Sexo?"]
    while True:
        i=menu.MenuDvd(listaMenu, "Menu Nutricion IMC => tareaU1-E1")
        print(f'Opcion introducida {i}')
        if i==0 or i==None:
            break
        elif i==1:            
            # newClient=cli.ClienteNutricion("Antonio", 18, '50854788V', 70, 1.80, 'M')
            pass
        elif i==2:
            # Busca cliente
            # Actualiza datos cliente
            pass
        elif i==3:
            # Busca clienteos cliente
            # Borra cliente
            pass
        elif i==4:
            # Busca cliente
            # Imprime cliente
            pass
        elif i==5:
            # Busca cliente
            # Imprime el sexo del cliente
            pass
        else:
            continue


# _________________________
if __name__ == "__main__":
    os.system('cls')    
    # ---- Empezamos!!
    main()