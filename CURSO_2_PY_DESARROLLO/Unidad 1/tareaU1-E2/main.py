import os
import menuDvd as menu
from deportes.deportistas import Deportista

def subMenu_Mostrar(objDEPTA=None, indexDeporte=None):
    """ 
    Def => Menu para Mostrar un jugador individual o los datos de todos los jugadores de un deporte
    """    
    if objDEPTA==None or indexDeporte==None: return 
    listaDeportes=objDEPTA.getListDeportes()
    listaEstadista=[f'Jugador Individual de {listaDeportes[indexDeporte]}',f'All Data de {listaDeportes[indexDeporte]}']                    
    while True:
        menu_MOSTRAR = menu.MenuDvd(menu=listaEstadista, 
                                     tituloMenu="J U G A D O R   O   D E P O R T E",
                                    num_char=35,                                    
                                    char_1='-', char_2='-', char_3='-')
        if menu_MOSTRAR==0 or menu_MOSTRAR==None:
            break       #Salida del bucle

        elif menu_MOSTRAR==1:
            print(f'\nMostrar Individual {listaDeportes[indexDeporte]}')
            # *************************************
            # Pide nombre del Deportista a buscar
            # *************************************
            nombreDeportista=input(f'Intro Nombre Deportista de {listaDeportes[indexDeporte]} a Buscar.... ')

            dictDeportista=objDEPTA.buscar(strKey=nombreDeportista)
            # print(dictDeportista) if dictDeportista else print(f'{nombreDeportista} :(')
            if dictDeportista:
                if dictDeportista['deporte']==listaDeportes[indexDeporte]:
                    objDEPTA.imprimir(dictDeportista=dictDeportista) 
                else:
                    print(f"\nBuscar {'.'*5} {nombreDeportista} match!! pero no Juega {listaDeportes[indexDeporte]} :(")
            else:
                print(f"\nBuscar {'.'*5} {nombreDeportista} :( ")
                    
        
        elif menu_MOSTRAR==2:
            print(f'\nMostrar All Data de {listaDeportes[indexDeporte]}')
            for dictDeportista in objDEPTA.listaDeportistas:
                if dictDeportista['deporte']==listaDeportes[indexDeporte]:
                    objDEPTA.imprimir(dictDeportista=dictDeportista)

            break
        else:
            continue
    

# _________________________
def main():
    
    # Creo el objeto Deportista
    objDEPTA = Deportista()    

    """ Pruebas de getters y setters de los valores de la clase Sport 
        Si, me he motivado, si, (LOL)
    """
    # listadiccDeportes=objDEPTA.getListDictSport()
    # listaTorneosByDeporte=objDEPTA.getListTorneosByDeporte('basquet')
    # indexByDeporte=objDEPTA.getIndexByDeporte('basquet')
    # listaTorneosByIndex=objDEPTA.getListTorneosByIndex(1)
    # strDeporteByIndex = objDEPTA.getDeporteByIndex(1)    
    # diccDeporte=objDEPTA.getDictSport('basquet')
    # diccDeporte=objDEPTA.getDictSport(1)
    pass
    # ___________________________________
    # Funcion de validator para entrar unna lista de str y salir un diccionaario de claves los 
    # valores de la lista y valor las entradas de usuario(str).
    # -----------------------------------
    # _________________________________
    # from validator import ValidReg as VReg
    # newDict = VReg.listTOdict_byTcld_ToString(['Cuanto','Quieres','Entrar'])
    # print(newDict)

    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado)
    # No se usa en el ejercicio, esto es sólo pruebas.
    from listTOdict_Tcld import listTOdict_byTcld_ToString as listToDict
  
  
    oneDict=listToDict.listTOdict_BYTcld_SUPERPlus(listaStrKeys=['Cuanto','Quieres','entrar?'],
                                        listaDef= [ (int, True), (float, False), (str, False) ],
                                        esLock=True,
                                        esCapital=False)

    # oneDict=listToDict.listTOdict_TcldPlus(listaStrKeys=['Cuanto','Quieres','entrar?'],
    #                                     listaDef= [ (int, True), (float, False), (str, False) ],
    #                                     esLock=True,
    #                                     esCapital=False)
    print(oneDict)
    pass    
    # _________________________________
    # Creo la lista de str de Deportes
    listaDeportes=objDEPTA.getListDeportes()
    listaDeportes=[str(n).capitalize() for n in listaDeportes]
    pass
    # _________________________________
    # Creo la lista str menuPpal
    listaMenu=[ f"Crear Jugador {n}" for n in listaDeportes ]
    # for n in listaDeportes:
    #     listaMenu.append(f"Crear Jugador {n}")
    listaMenu.append("Mostrar Datos")
    pass

    # *********************
    # Muestra el Menu PPAL
    # *********************
    while True:
        menu_PPAL=menu.MenuDvd(menu=listaMenu, 
                                tituloMenu="Menu  D E P O R T I S T A S - Tarea U1 - E2", 
                                num_char=45,
                                char_1='-', char_2='=', char_3='-')
        if menu_PPAL==0 or menu_PPAL==None: # Salir del menu Ppal
            break        
        elif 1 <= menu_PPAL <= len(listaMenu)-1:
            objDEPTA.add(menu_PPAL)     

        elif menu_PPAL==4:
            # ****************************
            # SubMenu Que Deporte Mostrar 
            # ****************************
            while True:
                menu_SPORT = menu.MenuDvd(  menu=listaDeportes,
                                            tituloMenu= "M O S T R A R   D A T O S", 
                                            num_char=28,
                                            char_1='-', char_2='-', char_3='-')

                if menu_SPORT==0 or menu_SPORT==None:
                    break   #Salida del bucle.                
                elif 1 <= menu_SPORT <= len(listaDeportes):                    
                    # ************************************  
                    # SubMenu Mostrar Jugador o Deporte
                    # ************************************  
                    subMenu_Mostrar(objDEPTA=objDEPTA, indexDeporte=menu_SPORT-1)
                else:
                    continue

    print('\n'+'*'*40+"\nSaliendo de la Tarea U1 - E2......Chaooooo"+'\n'+'*'*40)

# _________________________
if __name__ == "__main__":
    os.system('cls')    
    # ---- Empezamos!!
    main()