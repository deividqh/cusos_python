import os

import menuDvd as menu
from clientes import ClienteNutricion as ClienteNut

# ______________________
def main():
    listaKeys=['nombre', 'edad', 'dni', 'peso', 'altura', 'sexo']
    objClienteNut = ClienteNut(listaKeys)
    # __________________
    while True:
        listaMenu=["Add Cliente", "Updte Cliente", "Delete Cliente", "Busca Cliente", "Lista Clientes"]
        i=menu.MenuDvd(listaMenu, "\nMenu Nutricion IMC => tareaU1-E1")
        if i==None:
            break
        elif i==1:
            print('ADD')
            newClient = objClienteNut.addCliente()
            if newClient:
                print(f"{newClient['nombre']} {newClient['dni']} ADD OK")  
            else:
                print('Error ADD')
        elif i==2:
            nombredni = input("UPD - Intro Nombre o Dni....").strip()
            cliente = objClienteNut.updateCliente(nombredni)
            print(f"\n{cliente['nombre']} {cliente['dni']} UPDT OK') if cliente else print(f'Error UPDT {nombredni}")
        elif i==3:
            nombredni = input("DEL - Intro Nombre o Dni....").strip()
            cliente = objClienteNut.delCliente(nombredni)
            print(f"\n{cliente['nombre']} {cliente['dni']} DEL OK') if cliente else print(f'Error DEL {nombredni}")
        elif i==4:
            nombredni = input("SEARCH - Intro Nombre o Dni....").strip()
            cliente = objClienteNut.searchCliente(nombredni)
            if cliente:
                imc = objClienteNut.calcularImc(nombredni)
                sexo = objClienteNut.getSexo(nombredni)
                esMayor = objClienteNut.esMayor(nombredni)
                if imc > 0:
                    print(f"\n{cliente['nombre']} - sexo: {sexo} - {esMayor} de edad - I.M.C.=> {imc}")
                else:
                    print(f"\n No puedo calcular el IMC del Cliente {cliente['nombre']} ({cliente['dni']})=> peso:{cliente['peso']} , altura: {cliente['altura']}")
            else:
                print(f'\nCliente {nombredni} no Encontrado :(')
        elif i==5:
            print('\nListado de clientes:')
            for n in objClienteNut.listaClientes:
                print(str(n))
        else:
            continue
    
    print('\n'+'*'*40+"\nSaliendo de la App I.M.C......Chaooooo"+'\n'+'*'*40)

# _________________________
if __name__ == "__main__":
    os.system('cls')    
    # ---- Empezamos!!
    main()