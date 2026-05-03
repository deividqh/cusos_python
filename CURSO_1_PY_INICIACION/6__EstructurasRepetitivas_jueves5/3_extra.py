"""
 1. Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta.        
"""
s=100
menu="IntroOpcion:\n1.Consultar $$\n2.Retirar $$ \n3.Ingresar $$\n4.Salir"
print (menu)
while (True):
    i=abs(int(input("Intro opcion \n")))
    if i==4: break
    if i==1:
        #print ("Saldo = ", s)
        True
    elif i==2:
        r=abs(int(input("Cuanto quieres Retirar \n")))
        if r>s: 
            print("No puedes retirar mas de lo que tienes :(");
            continue
        else:
            s=s-r
            #print("SAldo = ", s)
    elif i==3:
        r=abs(int(input("Cuanto quieres Ingresar? \n")))
        s=s+r
            
    else:
        continue

    print("SAldo = ", s)