from enunciadosPOO1 import ejer01, ejer02, ejer03, ejer04
from clasesPOO1 import Disco as Dvd

if __name__=='__main__':    
    import os
    os.system('cls')
# ----------------------
print(".......LA DISCOTECA......\n"+ejer01)
disco1=Dvd("La Taberna del Irlandes", "23:00", 8)

if disco1.esAbierta()==True:
    print(";) Que Bueno, está abierta ahora mismo!! Vamos?")
else:
    newHora=23 ; newMin=30    
    bAbierta=disco1.esAbierta(laH=newHora, elM=newMin)
    if bAbierta==True:
        print(f";) No me viene ahora mismo pero me puedo pasar a las {newhora}:{newMin}  Vamos?")
    elif bAbierta==None:
        print("Error en Parametros de entrada ")
    else:
        print(f"No me viene bien ni ahora ni a las {newHora}:{newMin}")
    

