import os
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# No se usa en el ejercicio, esto es sólo pruebas.
from listTOdict_Tcld import listTOdict_byTcld_ToString as LTDBYT


os.system('cls')
# ___________________________________
# Funcion de validator para entrar unna lista de str y salir un diccionaario de claves los 
# valores de la lista y valor las entradas de usuario(str).
# --------------------------------
# newDict = LTDBYT.listTOdict_byTcld_ToString(['listTOdict_byTcld_ToString','Diccionario','siempre','string'])
# print(newDict)
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# Da el mismo resultado que listTOdict_byTcld_ToString (diccionario de str:str)
# --------------------------------
# twoDict=LTDBYT.listTOdict_TcldPlus(listaStrKeys=['TcldPlus()','Sin ListDef','Tipado Out','PermiteNull en Teclado'],                                   
#                                     permiteNulo=True,
#                                     esCapital=False)
# print(twoDict)
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
twoDict=LTDBYT.listTOdict_TcldPlus(listaStrKeys=['TcldPlus','Sin ListDef()','Tipado Out', 'Valores x Defecto'],                                   
                                    listaDef= [(int,True),(float, False),(str, False)],
                                    permiteNulo=True,
                                    esCapital=False)
print(twoDict)
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
oneDict=LTDBYT.listTOdict_BYTcld_SUPERPlus( listaStrKeys=['listTOdict_BYTcld_SUPERPlus()', 'ListaDef','Tipado In Intro By Tcldo','permiteNulo'],
                                    listaDef= [(int,True),(float, False),(str, False)],
                                    permiteNulo=True,
                                    esCapital=False )
print(oneDict)
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# Una funcion para reunirlas a todas, un anillo unico de poder para destruir el mundo
twoDict=LTDBYT.index(listaStrKeys=['index()','Cuanto','Quieres','entrar?'],
                                    listaDef= [(int, True), (float, False), (str, False)],
                                    permiteNulo=True,
                                    esCapital=False)
print(twoDict)
# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# Una funcion para reunirlas a todas, un anillo unico de poder para destruir el mundo
twoDict=LTDBYT.index(listaStrKeys=['Cuanto','Quieres','entrar?'],
                                    permiteNulo=True,
                                    esCapital=False)
print(twoDict)
