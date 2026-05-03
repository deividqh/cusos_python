import os
# _____________________________________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
from listTOdict_Tcld import listTOdict_byTcld as LTD


def main():
    print(f'P R U E B A S   L I S T T O D I C T _ B Y T C L D\n{'='*50}')

    # ___________________________________
    print("""
-Crea un Diccionario (K)strKey (V)strValue
    -No permite '' (Nulo)
    -No permite Configuracion
""")
    # newDict = LTD.toString(listaStrKeys=['toString()','(Key)str','(Value)str'])
    # print(newDict)
    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado)
    # Da el mismo resultado que toString (diccionario de str:str)
    # --------------------------------
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] de str (sin listaDef)
    -diccionario resultante es str  (sin listaDef)
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    # twoDict=LTD.byDef(listaStrKeys=['byDef()','Sin ListDef','Tipado Out','PermiteNull en Teclado'],                                   
    #                     permiteNulo=True,
    #                     esCapital=False)
    # print(twoDict)

    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado) 
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] con Valores por Defecto
    -diccionario resultante es tipado  (con listaDef)  
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    # twoDict=LTD.byDef(listaStrKeys=['byDef()','sin ListDef()','tipado Out', 'valores x Defecto'],                                   
    #                     listaDef= [(int,True),(float, False),(str, False)],
    #                     permiteNulo=True,
    #                     esCapital=False)
    # print(twoDict)
    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado)
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo(strValue)]
    -diccionario resultante es Tipado al introducir el dato  (con listaDef)
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")

    oneDict=LTD.byTcld( listaStrKeys=['byTcld()', 'ListaDef','Tipado In Intro By Tcldo','permiteNulo'],
                        listaDef= [(int,True),(float, False),(str, False)],
                        permiteNulo=True,
                        esCapital=False
                    )
    print(oneDict)
    



if __name__ == "__main__":
    os.system('cls')
    main()