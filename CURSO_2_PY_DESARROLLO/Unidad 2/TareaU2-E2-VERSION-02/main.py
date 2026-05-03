from biblioteca import Biblioteca
from libro import Libro
import re, os

from fromdvd.menuDvd import MenuDvd
from fromdvd.listTOdictTCLD import listTOdict_byTcld as LTD

def main():
    menuPPAL=["Añadir libro","Buscar libro","Ver All Books"]
    biblio=Biblioteca()
    while True:
        # _____________
        # Muestra el Menu PPal
        opcion=MenuDvd(menu=menuPPAL, tituloMenu="Introduce una opción", char_1='-',char_2='-',char_3='=' )
        # _______________
        # Intro Libro
        if opcion==None:
            break
        elif opcion == 1:
            introLibro=LTD.byTcld(listaStrKeys=["titulo", "autor", "num Paginas"],listaDef=[(str,False), (str,False), (int,False)],esCapital=True)
            try:
                libro = Libro(autor=introLibro['autor'],titulo=introLibro['titulo'],num_paginas=introLibro['num Paginas'])
                if libro:
                    esAgregado=biblio.agregar_libro(libro=libro)
                    if not esAgregado:
                        raise errorDvd(f"libro( {libro.titulo} ) ya está en la Biblioteca", 101)
            except errorDvd as errdvd:
                print(f'ERROR: {errdvd.msg}')
            except Exception as e:
                 print(f"Libro add ERROR: {e}")                
            else:
                print(f"\nLibro: {libro}")
        # _______________
        # Buscar Libro
        elif opcion == 2:
            tituloBusca=LTD.byTcld(listaStrKeys=["Titulo a Buscar"] , listaDef=[(str,False)], msgIntro='Introduce el', esCapital=True)
            try:
                libroBuscado = biblio.buscar_libro(titulo=tituloBusca["Titulo a Buscar"])
                if libroBuscado:
                    print(f"\n{libroBuscado}")
                else:                
                    raise errorDvd(f" \"{str(tituloBusca["Titulo a Buscar"]).title()}\" No encontrado", 102)            
            except errorDvd as err:
                print(f'\n-ERROR: {err.msg}\n-CODE:({err.cod})')
        # _______________
        # Salir del Menu Ppal
        elif opcion == 3:
            biblio.imprime_All()
        # _______________
        # Salir del Menu Ppal
        elif opcion == 4:
            break

    print(f"\n{'-'*25}\nSaliendo de la Biblioteca\n{'-'*25}")

# __________________
class errorDvd(Exception):
    def __init__(self, msg, cod):
        self.msg=msg
        self.cod=cod
        super().__init__(f'codigo Error:{self.cod}: {self.msg}')
# __________________
if __name__ == "__main__":
    os.system('cls')
    main()