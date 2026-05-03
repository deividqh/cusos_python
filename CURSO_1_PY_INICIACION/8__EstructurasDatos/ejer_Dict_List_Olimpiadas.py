""" Ejercicio Diccionarios y Listas """

# El Comité Olímpico nos ha proporcionado los datos del medallero olímpico de la siguiente manera:
# Pais;oro;plata;bronce\n
# Estados Unidos de América;40;44;42\n
# República Popular de China;40;27;24\n
# Japón;20;12;13
 
# Nuestra empresa necesita mostrar los datos en forma de diccionario, siendo el resultado esperado así:
# {
# 'Estados Unidos de América': {'oro': '40', 'plata': '44', 'bronce': '42'}, 
# 'República Popular de China': {'oro': '40', 'plata': '27', 'bronce': '24'}, 
# 'Japón': {'oro': '20', 'plata': '12', 'bronce': '13'}
# }

# • Realizar un programa que permita este objetivo.
medallero="Pais;oro;plata;bronce\nEstados Unidos de América;40;44;42\nRepública Popular de China;40;27;24\nJapón;20;12;13"
listStrings=medallero.split('\n')
listKey=[]          
diccResultado={}
listDlistResultados=[]
for i,n in enumerate(listStrings):
    if i==0:
        head = n
        listHead =n.split(";")      # ['oro', 'plata', 'bronce']
        listHead.reverse()          # ['bronce' , 'plata', 'oro' , "Pais"]
        listHead.pop()              # ['bronce' , 'plata', 'oro']   
        listHead.reverse()          # ['oro', 'plata', 'bronce']
    else:        
        listPais=n.split(";")
        listPais.reverse()                  # ['40','44','42',"Estados Unidos"]
        listKey.append(listPais.pop())      # ['42','44','40']      pop() borray + devuelve 
        listPais.reverse()                  # ['40','44','42']
        listDlistResultados.append(listPais)

# al salir de este bucle tengo:
print(listHead)     # listHead=['oro', 'plata', 'bronce']
print(listKey)      # listKey = ["Estados Undios", "China", "Japon"] 
print(listDlistResultados)  # listDlistResultados [['40','44','42'], ['40','27','24'],...]  


# --------------------------------------------------------
# 'Japón': {'oro': '20', 'plata': '12', 'bronce': '13'}
# --------------------------------------------------------
# diccResultado[key]=value | donde (k)"China" , (v)={ (k)listHead (v)listDlistResultados }
# Tengo 2 diccionarios uno interno y otro externo.
for i, n in enumerate(listKey):
    p=listKey[i]                            #"Estados Unidos" y preparo diccResultado[p]
    listMed = listDlistResultados[i]        #['40','44','42']

    # Ahora tengo la "Estados Unidos" y  listHead["oro", "plata", "bronce"] y [40, 44, 42]    
    diccValor={}
    for j,key in enumerate(listHead):
        diccValor[key]=listMed[j]           # Esto cruza oro con 40, plata con 44 y crea el dict

    # (k)=p, (v)=diccValor
    diccResultado[p]=diccValor

print("\n")
print("Solucion 1")
print(diccResultado)
print()

rangoFilas=range(len(listKey))  
rangoColumnas = range(len(listDlistResultados[i]))

# ------------- POR LISTA DE COMPRENSION Y SIN CHATGPT ;)
# Esto es como recorrer filas y columnas listKey = Filas, listMed = columnas

# diccResultado={ listKey[i]:{listHead[j]:listDlistResultados[i][j] } for i in rangoFilas
#                                                                     for j in rangoColumnas
# }

# Esto tiene buena pinta, Pero me devuelve: {'Estados Unidos de América': {'bronce': '42'}, 
#               'República Popular de China': {'bronce': '24'}, 'Japón': { 'bronce': '13'}}
# Asi que lo cambio por esto a ver si suena la flauta.........y suena!!!! ;)
print("Solucion 2.....Listas de Comprension")
diccResultado={ listKey[i]:{listHead[j]:listDlistResultados[i][j] for j in rangoColumnas} for i in rangoFilas                                                                    
}
print(diccResultado)


# Compresion de listas
""" Consiste en una construcción que permite crear listas a partir de otras listas.
listaResultado = [ Accion for item in listaData ]

Cada una de estas construcciones consta de una expresión que determina cómo modificar
el elemento de la lista original, 
seguida de una o varias clausulas for y opcionalmente una o varias clausulas if. 

lista2 = [n ** 2   for  n   in  lista1]   ===>  1-Para cada n en lista1 haz n ** 2
                                                2-Lo conviertes en una lista entre []
                                                3-Lo almacenas en lista2

lista2 = [n for n in lista if n % 2.0 == 0] ==> Conservar solo los números que son pares

l = [0, 1, 2, 3]
m = ['a', 'b']

n = [s * v for s in m
           for v in l
           if v > 0]
Esta construcción sería equivalente a una serie de for-in anidados:
l = [0, 1, 2, 3]
m = [a, b]
n = []
for s in m:
    for v in l:
        if v > 0:
            n.append(s*v)
"""

