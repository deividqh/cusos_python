# Ejercicios Listas

#Para Limpiar la terminal con  os.system('cls') 
import os           

# Lista_D_tuplas(str(usuario), password)
# Listado de todos los usuarios por defecto. Los añadidos son dinamicos.
listUsuarios=[  ('admin', 1), 
                ('def', 2), 
                ('ami', "ami")
            ]

# lista de listas de peliculas. las que se añaden se añaden dinamicamente.
tuplePeliculas = (("Heredaras el Viento","judicial", "1952"),
    ("Noises Off","comedia", 1988),
    ("12 hombres sin piedad","judicial", 1970),
    ("Psicosis","drama psicologico", 1950),
    ("Ciudadano Kane","Aventura", 1968),
    ("Star Wars","Ciencia Ficcion", 1978),
    ("Apocalipsis Now","Belica", 1980),
    ("Ciudad de Dios","drama", 1980),
    ("12 hombres sin piedad","drama", 2020)
    )

# 4-lista de listas [usuario, [favoritas]]
listFavoritas=[]

# CtePara el numero de asteriscos(*) en los print()
AS=40

from enum import Enum

# Xa listUsuarios
class tU(Enum):
    US=0
    PW=1
# Xa tuplePeliculas
class dP(Enum):
    TITULO = 0
    GENERO = 1
    ANNO = 2

def Loretix():    
    os.system('cls')   
    
    bMatch=False
    while(True):
        print("*"*AS+"\n"+"*"*AS+'\nLoretux Video: (Pulsa 0 para Salir)'+"\n"+"*"*AS)
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
    os.system('cls')

    # Recojo los datos de la entrada
    argUsu=usuario[0][tU.US.value]
    argPassw=usuario[0][tU.PW.value]

    # Bienvenida y Menu de Acciones
    print(f"\nBienvenido/a {usuario[0][tU.US.value]} !!\n")
    menuUsuario=["Buscar película por título",
                "Buscar películas por género",
                "Cambiar contraseña de usuario",
                "Crear listas de películas favoritas que se quiere ver",
                "Mostrar la lista de películas favoritas",
                "Ver Todas las Peliculas"
                ]

    bMatch=False
    while(True):
        i=MenuLista(menuUsuario, "Menu del Usuario")        
        if i==None: 
            return
        elif i==1:
            introTitulo=input("Busca X Titulo.... ")
            # ----- devuelve una lista con el resultado o none
            listResultado=getListPeliculaLike( introTitulo, dP.TITULO.value , True)            

            print ("*"*AS)
            if listResultado != None: 
                for (n, g, d) in listResultado:
                    print (f'Nombre: {n} \tGenero: {g} \tAño: {d}')
            else:
                print(f"Pelicula {introTitulo} NO Encontrada :( ")
            print ("*"*AS)            

        elif i==2:
            # Muestro los generos al usuario
            print('-'*AS)
            imprimeTuplePeliculas(tuplePeliculas, False, True, False)
            print('-'*AS)

            introGen=input("Intro Genero.... ")
            # ----- devuelve una lista con el resultado o none
            listResultado=getListPeliculaLike(  txtToSearch=introGen, 
                                                conceptPelicula=dP.GENERO.value, 
                                                isLike=True)
            print ("*"*AS)
            if listResultado != None: 
                for (n, g, d) in listResultado:
                    print (f'Nombre: {n} \tGenero: {g} \tAño: {d}')
            else:
                print(f"Genero {introGen} NO Encontrada :( ")
            print ("*"*AS)            

        elif i==3:
            newPassw=input("Intro nueva Contraseña.... ")

            for idx,(u, p) in enumerate(listUsuarios):
                if str(u)==argUsu:
                    listUsuarios[idx]=list(listUsuarios[idx])
                    listUsuarios[idx][tU.PW.value]=newPassw
                    print("\n"+"*"*AS,f"\nContraseña Vieja: {argPassw} :(\nContraseña Nueva: {newPassw} ;)\n"+"*"*AS)
                    break                

        elif i==4:
            print("Add Pelicula Favorita:")
           
            listadoPeliculas=getReListTuplePelicula(tuplePeliculas,  True, True, True)
            listEnUnString=getListString(tuplePeliculas, bFormato=True)

            fav=MenuLista(listEnUnString, "Elige pelicula Favorita") 
            del menuXaFav           
            if fav==None: continue

            peliculaToAdd=tuplePeliculas[fav-1][dP.TITULO.value]

            # Crear una copia dinamica de listaUsuarios con la configuracion nueva (usuario, [favoritas])
            # Carga de listFavoritas del usuario que entra:
            bMatch=False
            for u,p in listUsuarios:
                for peli in tuplePeliculas:
                    # Busco al usuario 
                    if u==argUsu:
                        bMatch=True
                        if peli[dP.TITULO.value]==peliculaToAdd:
                            listFavoritas.append([u, list(peli)])
                            break
                if bMatch==True: break   #Si lo encuentra y lo ha añadido Sale del bucle            
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
        i=MenuLista(menuAdmin, "Menu de Administracion")
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
            idx=MenuLista(menuNombresPeli, tituloMenu="Elije Pelicula a Modificar")
            if idx==None: continue
            
            # Creo una lista(listCambios) con la pelicula elegida.
            listCambios=list(tuplePeliculas[idx-1])            
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

            idx=MenuLista(menuNombresPeli, tituloMenu="Elije Pelicula a Eliminar")
            if idx==None: continue
            titulo=list(tuplePeliculas)[idx-1][dP.TITULO.value]

            # Convierto la tuple_D_tuple en list_D_tuple(Tengo que poner valor global)
            listPeliculas=list(tuplePeliculas)            
            # Borro el indice elegido
            listPeliculas.pop(idx-1)
            
            # Y todo vuelve a la normalidad
            tuplePeliculas=tuple(listPeliculas)
            # Mensaje de Salida
            print("Eliminacion OK :)")
            print(f"{titulo} Eliminacion OK :)")

        elif i==4:
            print('-'*AS*2)
            imprimeTuplePeliculas(tuplePeliculas, True, True , True)
            print('-'*AS*2)

# Devuelve Una List de los nombres de las peliculas
def getListTitulos():
    menuNombresPeli=[]
    for p in tuplePeliculas:
        menuNombresPeli.append(p[dP.TITULO.value])

    if len(menuNombresPeli)>0: 
        return menuNombresPeli
    else:
        return None

# Crea la lista para modificar una pelicula en 
# Entra un list(nombrePeli, GeneroPeli, AñoPeli) y str titulo del Menu 
# Carga los Cambios y los retorna
def setListCambiosToUpt(listNewPeli, tituloMenu):
    while(True):
        i=MenuLista(listNewPeli, tituloMenu=tituloMenu)
        if i==None: 
            return listNewPeli
        elif i==1:
            nuevo=input("Introduce Nuevo Titulo.....")                
            listNewPeli[dP.TITULO.value]=nuevo
            # return listNewPeli
        elif i==2:
            nuevo=input("Introduce Nuevo Genero.....")                
            listNewPeli[dP.GENERO.value]=nuevo        
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
    peli=str(listIntro[dP.TITULO.value])
    anno=str(listIntro[dP.ANNO.value])
    if isDuplicada(listPeliculas, peli, anno)==False:
        listPeliculas.append(listIntro)
        return True
    return False

# Devuelve true/false si la pelicula existe en Titulo y Año
def isDuplicada(listPeliculas, peli, anno):
    for [p, g, a] in listPeliculas:        
        if ((peli.upper()==str(p).upper()) and (anno.upper()==str(a).upper())):                    
            return True

    return False

# Imprime las peliculas en consola con un formato alineado. 
def verPeliculas():
    maxTit=getMaxLenPeliculas(tuplePeliculas, dP.TITULO.value)+5
    maxGen=getMaxLenPeliculas(tuplePeliculas, dP.GENERO.value)+2
    maxAnn=getMaxLenPeliculas(tuplePeliculas, dP.ANNO.value)+2

    # rowformat Admite una cadena con formato '{:<num1}{:<num2}{:<num3}{:<numN}'
    formatoStrFila = "{:<" + str(maxTit) + "} {:<" + str(maxGen) + "} {:<" + str(maxAnn) + "}"
     
    # Zona de Impresion:
    print()     #Linea en blanco
    # Encabezado.
    print(formatoStrFila.format("Titulo", "Genero", "Anno"))    

    print("-"*(maxTit+maxGen+maxAnn+4))
    # Imprime las filas
    for pelicula in tuplePeliculas:
        titulo = pelicula[dP.TITULO.value]
        genero = pelicula[dP.GENERO.value]
        anno = pelicula[dP.ANNO.value]
        print(formatoStrFila.format(titulo, genero, anno))

    print("*"*(maxTit+maxGen+maxAnn+4))

# devuelve una list_D_list con (pelicula,genero,año) o (pelicula,genero) o (genero) o....
def getReListTuplePelicula(tuplePelis, bTit=True , bGen=False, bAnn=False):
    if bTit==False and bGen==False and bAnn==False: return None
    
    listRetorno=[]
    for tupleP in tuplePelis:
        listGetIntro=[]     #a cada iteracion se crea uno nuevo.
        
        if bTit==True: listGetIntro.append(tupleP[dP.TITULO.value])
        if bGen==True: listGetIntro.append(tupleP[dP.GENERO.value])
        if bAnn==True: listGetIntro.append(tupleP[dP.ANNO.value])

        listRetorno.append(listGetIntro)    
    return listRetorno

# Calcula la maxima longitud de un titulo o un genero en la tupla de peliculas
def getMaxLenPeliculas(argTupla, argIdx=1):
    # Validaciones iniciales de tupla y de indice
    # print(len(argTupla[0]))
    if len(argTupla)<=0:return None
    if argIdx<0 or argIdx>=len(argTupla[0]):return None    

    # Lista donde meto los numeros de las longitudes del argumento pasado como parametro.
    listLargos = []
    for tupla in argTupla:
        longitud_elemento = len(str(tupla[argIdx]))  # Convertir a string y calcular longitud. esto hace que no haya que validar los tipos.
        listLargos.append(longitud_elemento)
    
    # Como ya tengo una lista con solo números, puedo aplicar max()         
    max_longitud = max(listLargos)        
    return max_longitud    

# entra Pelicula y devuelve: 1- Una lista_D_lista(p,g,a) con isLike a True 
#                           2- Una lista_D_lista(p,g,a) si isLike = False pero de un solo elemento o 
#                           3- None en caso de no Validar o no Encontrar
def getListPeliculaLike(txtToSearch='',conceptPelicula=0, isLike=False):
    listaRetorno=[]
    if txtToSearch.strip()=='':
        return      
    else:
        for n in tuplePeliculas:
            if isLike==False:
                # if str(n[dP.TITULO.value]).upper()==str(txtToSearch).upper():
                if str(n[conceptPelicula]).upper()==str(txtToSearch).upper():
                    listaRetorno.append(n)
                    return listaRetorno
            else:
                peliEnLista=str(n[conceptPelicula]).upper()
                txtToSearch=txtToSearch.upper()

                if peliEnLista.find(txtToSearch) != -1:
                    listaRetorno.append(n)

        if (len(listaRetorno) > 0):
            return listaRetorno
        else:
            return None

# ---------- CREA UN MENU CON UN TITULO --------------
# Recibe una list_D_str- Ñe añade la opcion Salir al final y Te pide elegir opcion.
#   Valida el resultado y retorna el resultado o None(Salir del Menú)
#   menu=["SALIR", "XXX", "YYY"]
# Devuelve: 0 (devuelve None) o un indice del menu.
def MenuLista(menu, tituloMenu, bSalir=True):
    # Valida bSalir y añade o no la opcion Salir
    if bSalir==True:
        salir=["SALIR"]
        menu=salir+menu    
    
    # Imprime Menu:
    print ('-'*9,tituloMenu,'-'*9)    
    for index,opc in enumerate(menu):
        print (f'{index}....{opc}')
    print ('-'*40)    
    
    while(True):
        # Selecciona Opcion:
        i=input("Intro opcion... ")    
        # Si todo lo introducido en la cadena son digitos = True
        if i.isdigit():
            i=abs(int(i))
            if i==0: return None
            if i>len(menu): 
                continue
            else:                
                return i
        else:
            continue

# Recibe: tuplePeliculas, bFormato(True/False)
# Devuelve: un list con un solo string por fila => listRetorno(stringResultado) y formateado
def getListString(listadoPeliculas, bFormato=True):    
    if len(listadoPeliculas)<=0: return None
    nColumnas=len(listadoPeliculas[0])

    listUnString=[]
    if bFormato==False:
        for n  in listadoPeliculas:
            listUnString.append('    '.join(map(str,n)))
        return listUnString
    else:
        formatoStrFila=''
        for i in range(nColumnas):
            maxCol=getMaxLenPeliculas(listadoPeliculas, i)+4 #Establezco en 4 la separacion
            formatoStrFila += "{:<" + str(maxCol) + "}"
       
        # Retorno
        listRetorno=[]
        if nColumnas==1:
            for [i] in listadoPeliculas:
                #  print(formatoStrFila.format(i))
                 listRetorno.append(formatoStrFila.format(i))
            return listRetorno

        elif nColumnas==2:
            for [i, j] in listadoPeliculas:    
                # print(formatoStrFila.format(i, j))
                listRetorno.append(formatoStrFila.format(i, j))
            return listRetorno

        elif nColumnas==3:
            for [i, j, k] in listadoPeliculas:    
                # print(formatoStrFila.format(i, j, k))           
                listRetorno.append(formatoStrFila.format(i, j, k))
            return listRetorno
        
        else:
            return None
           
# Esta funcion no se ejecuta el programa, son solo pruebas que hago       
def pruebasReList():
    # Sacando e imprimiendo la list de la list devuelta por getReListTuplePelicula
    listadoPeliculas=getReListTuplePelicula(tuplePeliculas, True, False, True)
    for n  in listadoPeliculas:
        print(n)

    # Sacando cada Row en una sola str
    listUnString=[]
    for n  in listadoPeliculas:
        listUnString.append('    '.join(map(str,n)))

    print(listUnString)

    for n in listUnString:
        print (n)

    # Otra Forma desempaquetando
    listadoPeliculas=getReListTuplePelicula(tuplePeliculas, True, False, True)
    for [i, j] in listadoPeliculas:
        print(i,j)    
        
    # Con Formato
    listadoPeliculas=getReListTuplePelicula(tuplePeliculas, True, False, True)
    formatoStrFila = "{:<" + str(25) + "} {:<" + str(10) + "}"
    for [i, j] in listadoPeliculas:    
        print(formatoStrFila.format(i, j))

    # Otra forma
    listadoPeliculas=getReListTuplePelicula(tuplePeliculas, True, True, False)    
    for n  in listadoPeliculas:
        print(n[dP.TITULO.value])
        print(n[dP.GENERO.value])
        # print(n[dP.ANNO.value])     #Casca

# Uso las dos funciones que he creado antes ( getReListTuplePelicula y getListString ) 
# para Generar una lista automatica y con formato de las columnas que elijas para mostrar.
def imprimeTuplePeliculas(tuplePeliculas, bTit=False, bGen=False, bAnn=False):    
    
    # Obtiene un list con las columnas elegidas de tuplePeliculas
    listadoPeliculas=getReListTuplePelicula(tuplePeliculas, bTit=bTit, bGen=bGen, bAnn=bAnn)
    
    # Recibe un list y lo convierte en un list_d_1string y con formato Tabla
    listEnUnString=getListString(listadoPeliculas=listadoPeliculas, bFormato=True)
    
    # Ahora solo tenemos que imprimir el list de un string 
    for n in listEnUnString:
        print (n)

# --------- index Loretix
# --------- index Loretix
# --------- index Loretix
Loretix()



