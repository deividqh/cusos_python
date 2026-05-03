from biblioteca import Biblioteca
from libro import Libro
import re, os

def menu():
    print("\nOpcion 1: Añadir libro")
    print("Opcion 2: Buscar libro")
    print("Opcion 3: Ver All Books")
    print("Opcion 4: Salir")

def main():
    biblio=Biblioteca()
    while True:
        # _____________
        # Muestra el Menu PPal
        menu()
        opcion = input("Introduce una opción... ")        
        # _____________
        # Validacion Intro Teclado
        try: 
            opcion = int(opcion)
        except:
            continue
        patron = r'^[1-4]$'        
        if not re.match(pattern=patron, string=str(opcion)):
            continue
        # _______________
        # Intro Libro
        elif opcion == 1:
            titulo = input("Introduce el titulo...  ").strip()
            autor = input("Introduce el autor... ").strip()
            while True:
                n_paginas = input("Introduce el numero de paginas... ")
                # Validacion Intro Teclado
                patronNumPag = r'^[\d]+$'        
                if re.match(pattern=patronNumPag, string=str(n_paginas)):
                    break                
            try:
                libro = Libro(autor=autor,titulo=titulo,num_paginas=n_paginas)
                if libro:
                    esAgregado=biblio.agregar_libro(libro=libro)
                    if not esAgregado:
                        raise errorDvd(f"libro( {libro.titulo} ) ya está en la Biblioteca", 101)
            except errorDvd as errdvd:
                print(f'ERROR: {errdvd.msg}')
            except Exception as e:
                 print(f"Libro add ERROR")                
            else:
                print(f"\nLibro: {libro}")
        # _______________
        # Buscar Libro
        elif opcion == 2:
            while True:
                titulo = input("Introduce el Titulo a Buscar... ").strip()
                if titulo != '':
                    break
            try:
                libroBuscado = biblio.buscar_libro(titulo=titulo)
                if libroBuscado:
                    print(f"\n{libroBuscado}")
                else:                
                    raise errorDvd(f" \"{str(titulo).title()}\" No encontrado", 102)            
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

class errorDvd(Exception):
    def __init__(self, msg, cod):
        self.msg=msg
        self.cod=cod
        super().__init__(f'codigo Error:{self.cod}: {self.msg}')
        

if __name__ == "__main__":
    os.system('cls')
    main()