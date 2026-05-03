"""
Ejercicio 4: La pizzería “Pizza Paradiso” ofrece pizzas vegetarianas y no
vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
a continuación.
• Ingredientes vegetarianos: Pimiento, cebolla, champiñones, ...
• Ingredientes no vegetarianos: Pepperoni, Jamón, atún, …

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o
no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija


El programa debe preguntar al usuario cuantos ingredientes quiere elegir, y
mostrárselos, hasta un total de 3 ingredientes.
Se debe mostrar el contenido de la pizza: Tomate, queso y los ingredientes
extras.

"""


uno=int(input("Intro pizza= 1(vg) o = 2(noVg?)....."))
print(type(uno))
FIJOS="....y tomate y queso"
if uno==1:
    print   ("Vegetal!!  Pimiento, cebolla, champiñones ")
    b=int(input("Intro Cuantos ingredientes......"))
    
    if (b>3 or b<0):    print ( ":(")
    elif b==1:          print ("Pimientos", FIJOS)
    elif b==2:          print ("Pimientos, cebolla", FIJOS)
    elif b==3:          print ("Pimientos, cebolla y champiñones", FIJOS)
    else:               print (":(")
elif uno ==2:
    print("No vegetal!! toma peperoni jamoncito y atun")
    b=int(input("Intro Cuantos ingredientes......"))
    
    if (b>3 or b<0) and type(b)=="<class 'int'>":
        print (":(")
    elif b==1: print ("peperoni ", FIJOS)
    elif b==2: print ("peperoni jamoncito ", FIJOS)
    elif b==3: print ("peperoni jamoncito y atun", FIJOS)
    else: print (":(1")

else:
    print( ":(" )

