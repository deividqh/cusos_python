# Ejercicios Listas

#Para Limpiar la terminal con  os.system('cls') 
import os           

# Para usar el paquete dvd
import sys
proyecto_ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(f'proyecto file: {proyecto_ruta}')
sys.path.append(proyecto_ruta)
# Impresion de los path metidos en el sys de python y comprobar que está metido el proyecto.
print("Rutas en sys.path:")
for ruta in sys.path:
    print(ruta)

# Uso del paquete dvd.menuDvd, le meto una lista y me genera un menú y devuelve la opcion elegida.
from dvd.menuDvd import MenuDvd

# Lista_D_tuplas(str(usuario), password)
# Listado de todos los usuarios por defecto. Los añadidos son dinamicos.
listUsuarios=[  ('admin', 1), 
                ('def', 2), 
                ('ami', "ami")
            ]

# lista de listas de peliculas. las que se añaden se añaden dinamicamente.
# Todo tiene que estar en upper(xa las comparaciones posteriores)
tuplePeliculas = (("Heredaras el Viento","judicial", 10),
    ("Psicosis","aventura", 20),
    ("Fracture","judicial", 30),
    ("mar","drama", 40),
    ("fuego","Aventura", 50),
    ("viento","drama", 60),
    ("tierra","romance", 70)
    )

# 4-lista de listas [usuario, [favoritas]]
listFavoritas=[]

# CtePara el numero de asteriscos(*) en los print()
AS=40

# Definicion de una Enumeracion(para no tener que usar index). 
    # 1-Hay que importar:  from enum import Enum 
    # 2-Se define una clase. no hay tipo Enum. 
    # 3-Uso: dP.PELI
from enum import Enum

# Xa listUsuarios
class tU(Enum):
    US=0
    PW=1
# Xa tuplePeliculas
class dP(Enum):
    PELI = 0
    AUTOR = 1
    ANNO = 2

def Loretix():    
    os.system('cls')   
    
    bMatch=False
    while(True):
        print('\nLoretux Video: (Pulsa 0 para Salir)')
        introUsu=input('Intro Usuario......')
        # Validacion Exit
        if introUsu=='0': break
        introPassw=input('Intro Contraseña......')
        if introPassw=='0':  break
        # Recorro la lista (usuarios,password)
        for i, (usu, passw) in enumerate(listUsuarios):
            if introUsu==usu and introPassw==str(passw):
                bMatch=True                
                if usu==listUsuarios[0][tU.US.value]:
                    entraAdministrador(listUsuarios[i])                    
                else:
                    entraUsuario(listUsuarios[i])
                break

        # Imprime error si no lo encuentra (bMatch==false) y si lo encuentra no hace nada(None).            
        print(f':(  :(  Usuario:<{introUsu}> \t Password: <{introPassw}>  :(  :(  ') if bMatch==False else None
    # Ha pulsado 0    
    print("\n"+"*"*30+"\n"+"Saliendo de Loretixxxxx   :(\n"+"*"*30)


# Entran los valores una lista (*) [usuario , contraseña]
# Crea un menu de usuario y usa una lista de peliculas.
def entraUsuario(*usuario):
    # cls en la terminal
    os.system('cls')
    # Recojo los datos de la entrada
    argUsu=usuario[0][tU.US.value]
    argPassw=usuario[0][tU.PW.value]
    # Bienvenida y Menu de Acciones
    print(f"\nBienvenido {usuario[0][tU.US.value]} !!\n")
    menuUsuario=["Buscar película por título",
                "Buscar películas por género",
                "Cambiar contraseña de usuario",
                "Crear listas de películas favoritas que se quiere ver",
                "Mostrar la lista de películas favoritas",
                "Ver Todas las Peliculas"
                ]

    bMatch=False
    while(True):
        i=MenuDvd(menuUsuario, "Menu del Usuario")        
        if i==None: 
            return
        elif i==1:
            introTitulo=input("Busca X Titulo.... ")
            # ----- devuelve una lista con el resultado o none
            listResultado=getPeliculaLike(introTitulo, True)            
            if listResultado==None: 
                print ("*"*AS)
                print(f"Pelicula {introTitulo} NO Encontrada :( ")
                print ("*"*AS)
                continue
            else:
                print ("*"*AS)
                for (n, g, d) in listResultado:
                    print (f'Nombre: {n} \tGenero: {g} \tAño: {d}')
                print ("*"*AS)            
        elif i==2:
            # Esto de python es la pera. 
            # Esto funciona igual que en Titulo(pero con el nombre completo)....Brutal!!! 
            gen=input("Intro Genero.... ")
            print ("*"*AS)
            for n, g, d in tuplePeliculas: 
                if g.upper()==gen.upper():
                    bMatch=True
                    print (f'Nombre: {n} \tGenero: {g} \tAño: {d}')
            print(f"Genero {gen} NO Encontrado :(\n"+'*'*AS) if bMatch==False else print ("*"*AS)    

        elif i==3:
            newPassw=input("Intro nueva Contraseña.... ")

            for idx,(u, p) in enumerate(listUsuarios):
                if str(u)==argUsu:
                    # Como es una lista permite cambios, pero sus miembros son tuplas, 
                    # entonces casteo las tuplas a listas y así las cambio
                    # Ademas son tuplas y no las tengo que reconvertir a tupla pq fuera de la funcion se mantienen(probar).
                    listUsuarios[idx]=list(listUsuarios[idx])
                    listUsuarios[idx][tU.PW.value]=newPassw
                    print("\n"+"*"*AS,f"\nContraseña Vieja: {argPassw} :(\nContraseña Nueva: {newPassw} ;)\n"+"*"*AS)
                    break                

        elif i==4:
            print("Add Pelicula Favorita:")
             # Creo una lista con los usuarios para crear el menu.
            menuXaFav=[]
            for n in tuplePeliculas:
                menuXaFav.append(n[dP.PELI.value])                
            
            # print (menuXaFav)
            fav=MenuDvd(menuXaFav, "Elige pelicula Favorita")            
            if fav==None: continue

            # tengo la pelicula!! (fav-1 pq en el menu añado la opcion salir como 0)
            print(f"num: {fav}, pelicula: {tuplePeliculas[fav-1][dP.PELI.value]}")
            peliculaToAdd=tuplePeliculas[fav-1][dP.PELI.value]

            # AHORA PUEDO....
            # 1- Creo que lo que molaría sería un diccionario de listas (k)listUsuarios[nombreUsuario], (v)[favorita1]

            # 2-Tb puedo modificar listUsuarios y pasar From: [(usuario, contraseña)] To: (usuario, contraseña, [favoritas]) 

            # 3-Crear una copia dinamica de listaUsuarios con la configuracion nueva (usuario, [favoritas])
            # Esto creo que se ajusta mas al ejercicio: Crear variable global listaFavoritas
            # Carga de listFavoritas del usuario que entra:
            bMatch=False
            for u,p in listUsuarios:
                for peli in tuplePeliculas:
                    # Busco al usuario 
                    if u==argUsu:
                        bMatch=True
                        # Si la pelicula Introducida es una pelicula de la lista, 
                        # la añado a favoritas junto con el usuario.
                        if peli[dP.PELI.value]==peliculaToAdd:
                            listFavoritas.append([u, list(peli)])
                            break
                if bMatch==True: break   #Si lo encuentra y lo ha añadido Sale del bucle
            
            # print(listFavoritas)
            print("Pelicula Add ;)") if bMatch==True else None
        
        elif i==5:
            print("Tus Peliculas Favoritas:")

            for u,p in listUsuarios:
                for usu, (pe, ge, an) in listFavoritas:
                    if argUsu==u and u==str(usu):
                        print(f"Pelicula: {pe} \tGenero: {ge} \t Año: {an}")
        elif i==6:  
            verPeliculas()
        else:
            continue


# Entra una lista (*)
# Crea un menu de administracion y usa la lista de peliculas para Add/Upt/Del
def entraAdministrador(*admin):
    menuAdmin=  ["Agregar una nueva película",
                "Modificar el contenido de la lista de películas",
                "Eliminar una película de la lista",
                "Ver Todas las Peliculas"
                ]
    

    listPeliculas=[]
    
    # Se declara que se va a usar la variable global, si no, 
    # cualquier aparicion en esta funcion la toma como variable local.
    global tuplePeliculas

    while(True):
        i=MenuDvd(menuAdmin, "Menu de Administracion")
        # Salida del bucle
        if i==None: 
            break
        elif i==1:
            print("Add Pelicula")            
            # Entrada de usuario
            introPelicula = input("Intro Nombre Pelicula.....")
            introGen = input("Intro Genero.....")
            introAnno = abs(int(input("Intro Año de Realizacion.....")))

            # Creo list(datos introducidos)
            listIntro=[introPelicula, introGen, introAnno]
            # Convierto la tuple_D_tuple en list_D_tuple(Tengo que poner [global tuplePeliculas] para poder hacer esto)
            listPeliculas=list(tuplePeliculas)            
            # Añade la lista a la lista_D_tuple
            bMatch=addListPeliculas(listPeliculas, listIntro)
            # Mensaje de salida
            print("Insercion Ok ;)") if bMatch==True else print("Pelicula ya Insertada :( ")
            
            # Y todo vuelve a  la normalidad
            tuplePeliculas=tuple(listPeliculas)
        
        elif i==2:
            menuNombresPeli=getListTitulos()
            idx=MenuDvd(menuNombresPeli, tituloMenu="Elije Pelicula a Modificar")
            if idx==None: continue
            
            # Creo una lista(listCambios) con la pelicula elegida.
            listCambios=list(tuplePeliculas[idx-1])            
            # 1-Se crean los menus de la modificacion 
            # 2-Carga listCambios(por Referencia)
            # Devuelve None si el usuario ha pulsado Salir(=0)
            if setListCambiosToUpt(listCambios, "Elige Modificar Titulo/Genero/Año") == None:
                print("Modificacion :(")
                continue
            
            # Convierto la tuple_D_tuple en list_D_tuple(Tengo que poner valor global)
            listPeliculas=list(tuplePeliculas)            
            # a la Lista de Peliculas le meto la lista Cambiada en la misma posicion que tenía y la borro.
            listPeliculas[idx-1]=listCambios
            del listCambios
            # Y todo vuelve a la normalidad
            tuplePeliculas=tuple(listPeliculas)
            # Mensaje de Salida
            print("Modificacion :)")

        elif i==3:
            print("Eliminar")
            # obtengo una lista de nombres de peliculas
            menuNombresPeli=getListTitulos()
            if menuNombresPeli==None: 
                continue

            idx=MenuDvd(menuNombresPeli, tituloMenu="Elije Pelicula a Eliminar")
            if idx==None: continue

            # Convierto la tuple_D_tuple en list_D_tuple(Tengo que poner valor global)
            listPeliculas=list(tuplePeliculas)            
            # Borro el indice elegido
            listPeliculas.pop(idx-1)
            
            # Y todo vuelve a la normalidad
            tuplePeliculas=tuple(listPeliculas)
            # Mensaje de Salida
            print("Eliminacion OK :)")
            print(f"{tuplePeliculas(idx-1)(dP.PELI.value)} Eliminacion OK :)")

        elif i==4:
            verPeliculas()
            continue


# Devuelve Una List de los nombres de las peliculas
def getListTitulos():
    menuNombresPeli=[]
    for p in tuplePeliculas:
        menuNombresPeli.append(p[dP.PELI.value])

    if len(menuNombresPeli)>0: 
        return menuNombresPeli
    else:
        return None

# Crea la lista para modificar una pelicula en 
# Entra un list(nombrePeli, GeneroPeli, AñoPeli) y str titulo del Menu 
# Carga los Cambios y los retorna
def setListCambiosToUpt(listNewPeli, tituloMenu):
    while(True):
        i=MenuDvd(listNewPeli, tituloMenu=tituloMenu)
        # Cuando Sale(=0) retorna todos los cambios de la lista. 
        # Tiene que retornar, eso de que pasa byRef(si la retornas pasa byRef pero si no la retornas no)????
        if i==None: 
            return listNewPeli
        elif i==1:
            nuevo=input("Introduce Nuevo Titulo.....")                
            listNewPeli[dP.PELI.value]=nuevo
            # return listNewPeli
        elif i==2:
            nuevo=input("Introduce Nuevo Genero.....")                
            listNewPeli[dP.AUTOR.value]=nuevo        
            # return listNewPeli
        elif i==3:
            nuevo=input("Introduce Nuevo Año.....")
            listNewPeli[dP.ANNO.value]=nuevo
            # return listNewPeli
        else:
            continue

# Add una list(pelicula, genero, año) a la lista de peliculas.
# Valida que no esté repetida.
# No hago validacion del año
def addListPeliculas(listPeliculas, listIntro):
    # Valida que no esté duplicada(Hasta que veamos los Conjuntos)
    
    peli=str(listIntro[dP.PELI.value])
    anno=str(listIntro[dP.ANNO.value])

    if isDuplicada(listPeliculas, peli, anno)==False:
        listPeliculas.append(listIntro)
        return True

    return False

# Devuelve true/false si la pelicula existe en Titulo y año
def isDuplicada(listPeliculas, peli, anno):
    for [p, g, a] in listPeliculas:        
        if ((peli.upper()==str(p).upper()) and 
            (anno.upper()==str(a).upper())):                    
            return True

    return False


# Imprime las peliculas en consola
def verPeliculas():
    print("Biblioteca:")
    print("*"*AS)
    for p, g, d in tuplePeliculas:
        print(f'Nombre: {p}\tGenero: {g}\tAño: {d}')
    print("*"*AS)

# entra Pelicula y devuelve: 1- Una lista_D_lista(p,g,a) con isLike a True 
#                           2- Una lista_D_lista(p,g,a) si isLike = False pero de un solo elemento o 
#                           3- None en caso de no Validar o no Encontrar
def getPeliculaLike(tituloToSearch='', isLike=False):
    listaRetorno=[]
    if tituloToSearch.strip()=='':
        return      
    else:
        for n in tuplePeliculas:
            if isLike==False:
                if str(n[dP.PELI.value]).upper()==str(tituloToSearch).upper():
                    listaRetorno.append(n)
                    return listaRetorno
            else:
                peliEnLista=str(n[dP.PELI.value]).upper()
                tituloToSearch=tituloToSearch.upper()

                if peliEnLista.find(tituloToSearch) != -1:
                    listaRetorno.append(n)

        if (len(listaRetorno) > 0):
            return listaRetorno
        else:
            return None

    
# --------- index Loretix
# --------- index Loretix
# --------- index Loretix
Loretix()



