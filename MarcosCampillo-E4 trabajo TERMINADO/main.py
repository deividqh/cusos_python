# import funciones
from funciones import *


def main():

    while True:           
        try:                      # Añado un try y except para que no pongan chorradas
            ast = "*"
            opcion = int(input(f"{ast*30}\n1. Menú de propietarios\n2. Menú de mascotas\n3. Menú de visitas\n4. Facturación\n5. Salir\n{ast*30}\nElige una opción: "))
            if opcion == 1:                                    # Modifico la creación porque era un jaleo
                menu_propietarios()
            elif opcion == 2:            # Se añade la función para ver la lista completa. Pero hay que poner un for, no a lo bruto
                menu_mascotas()        
            elif opcion == 3:
                menu_visitas()
            
            elif opcion == 4:
                menu_faturacion()
                pass
            elif opcion == 5:
                break

            else:
                opcion = int(input("Elige una opción válida: "))    # Si pones un número diferente te devuelve al input
        
        except Exception as e:
            print(e)
            print("Introduce un número del 1 al 5")
                        # Te devuelve al menú de inicio hasta que eliges algo decente (que no sea una letra)

if __name__ == "__main__":
    main()