""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""
        #Cte para cuando se pide la opcion al usuario.
SALIR='<<<'
# ============================================================================================
# ============================================================================================
class MenuDvd():
    """ 
    Def: Define las partes esenciales de un menu Simple:  Head | Titulo | Cuello | Filas Body | Pie    
    Fila Body:  X_n__ | __n__ | __n_X | X_item__ | item | __item_X 
    """
    __TAB='    '
    __OPT=''
    CHAR_HEAD='-' 
    CHAR_CUELLO='-' 
    CHAR_PIE='-'
    NUM_CHAR=40                     
    X__NUM=''
    NUM__X='' 
    X__ITEM='' 
    ITEM__X=''
    STR_INTRO_DATA='Intro Opt..... '
    def __init__(self, titulo, lst_Item, lst_func=None):        
        # __________________________
        """ RECOGE LOS VALORES """
        self.titulo     = titulo                # El titulo e indice del menu. es la CABEZA
        self.lst_Item = lst_Item      # La cadena de Texto que conforma un Item del Menu. CUERPO 
        if lst_func==None:
            pass
            self.lst_func=[None for i in range(len(self.lst_Item))]
        else:
            self.lst_func   = lst_func              # La funcion que se pasa asociada por posicion al Item de lst_Item

        # ____________________________________________
        """ Before-After num    Before-After item  """
        self.X__num    = MenuDvd.__OPT           # Lo que va BEFORE del Numero 
        self.num__X    = MenuDvd.NUM__X           # Lo que va AFTER del Numero
        self.X__item = MenuDvd.__TAB           # Lo que va BEFORE del Item
        self.item__X = MenuDvd.ITEM__X        # Lo que va AFTER del Item

        # Style ______________________________
        self.char_head  = MenuDvd.CHAR_HEAD     # 1º caracter que se repite num_char veces. es el SOMBRERO
        self.char_cuello= MenuDvd.CHAR_CUELLO   # 2º caracter que se repite num_char veces. es la PAJARITA 
        self.char_pie   = MenuDvd.CHAR_PIE      # 2º caracter que se repite num_char veces. es el ZAPATOS
        self.num_char   = MenuDvd.NUM_CHAR      # Numero de caracteres que hay de los char --------------
        
        # Texto Input ________________________
        self.introData = MenuDvd.STR_INTRO_DATA
        # _____________________________________________________________
        """ GENERA EL ENTORNO: La linea de CABECERA - CUELLO - PIE """
        self.cabecera, self.pie = self.formar_entorno()
        # _____________________________________________________________
        """ GENERA LA LISTA DE NUMERACION"""
        self.lst_numeracion=[i for i in range(len(self.lst_Item))]
        # ___________________________________
        """ CARGA LAS LISTAS DE BEFORE-AFTER """
        self.lst__X_num=[]           #Lista de los caracteres que van antes del Numero del item.
        self.lst__num_X=[]           #Lista de los caracteres que van depues del Numero del item.
        self.lst__X_item=[]     #Lista de los caracteres que van antes del Item
        self.lst__item_X=[]     #Lista de los caracteres que van Despues del Item        
        for i in range(len(lst_Item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # ___________________________________________________
        """ VALIDACION DE TAMAÑO DE LISTAS. IGUALAR TODAS A:  self.lst_Item       """
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst_func)
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst_numeracion)
        # Entorno____________
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst__X_num)
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst__num_X)
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst__X_item)
        self.igualarListas(listaKeys=self.lst_Item, listaToReLong=self.lst__item_X)        
        # __________________________________
        """ GENERACION DEL DICCIONARIO  """        
        Itrtr_valor_dicc = tuple(zip(self.lst_Item, self.lst_func))            
        """ >>> 1º ==> Creo una tupla con el par lst_Item, lst_func xa formar el self.dicc_menu
        """
        val_dicc_menu={self.lst_numeracion[i]:valor_dicc  for i, valor_dicc in enumerate(Itrtr_valor_dicc)}                                          
        """>>> 2º ==> { 2 : ( 'Sales' , compraProd ) } ==> (2) numeracion ('Sales') titulo-menu (compraProd) funcion sin parentesis
        """        
        self.dicc_menu={self.titulo:val_dicc_menu}
        """ 3º ==> D I C C I O N A R I O R E S U L T A D O 
        >>> {'TituloDicc':  { 1: ( 'item_1' , func_item_1 ) } }   ==> Se genera 1 por Menu.
        >>> {               { 2: ( 'item_2' , func_item_2 ) } }   
        >>> {               { N: ( 'item_N' , func_item_N ) } }   """
        
        # print(self.dicc_menu)
        # __________________________________
        """ GENERACION DE LA LINEA DE SALIR  """        
        self.salir=self.get_row_Salir()
        # print(self.salir)
        
        """ SALIR en formato Valor de:  self.dicc_menu. 
        No lo incluyo en el diccionario general pq en un sub-menu no puede aparecer salir. 
        Salir es una característica del MenuDvd. Solo puede haber un salir."""

    def __str__(self):                
        return self.FrankY(bSalir=True, bHead=True, bBody=True, bPie=True, esNumerado=True)

    # __________________________________________________________________
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM, )
    def style(self, char_head= CHAR_HEAD, 
                    char_cuello=CHAR_CUELLO , 
                    char_pie=CHAR_PIE       , 
                    num_char= NUM_CHAR      , 
                    X__num   = X__NUM         ,
                    num__X   = NUM__X         , 
                    X__item= X__ITEM      ,
                    item__X= ITEM__X      ,
                    introData=STR_INTRO_DATA):

        # Asigna los nuevos valores_________________
        if char_head:   self.char_head  = char_head
        if char_cuello: self.char_cuello= char_cuello
        if char_pie:    self.char_pie   = char_pie        
        if num_char:    self.num_char   = num_char
        if X__num:       self.X__num      = X__num
        if num__X:       self.num__X      = num__X
        if X__item:    self.X__item   = X__item
        if item__X:    self.item__X   = item__X
        if introData:   self.introData  = introData
        # Inicia____________________________
        self.lst__X_num      = []
        self.lst__num_X       = []
        self.lst__X_item   = []
        self.lst__item_X    = []
        # Reset de los lst_______________________
        for i in range(len(self.lst_Item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # Reset de la cabecera y pie __________________
        self.cabecera, self.pie = self.formar_entorno()
    # _____________
    # Retorna 4 espacios
    def get_TAB(self):
        return self.__TAB
    # _____________
    # CABEZA Y PIE
    def formar_entorno(self):
        cabecera=f'\n{ self.char_head * self.num_char }\n{ self.titulo }\n{ self.char_cuello * self.num_char }'                
        pie=f'{self.char_pie*self.num_char}'
        return cabecera, pie
    # ___________________________
    # STRING DEL CUERPO EN LINEA
    def get_str_Body(self, esNumerado=True):
        """ >>> Def: Devuelve una cadena de impresion con el menu. un menu con cabecera, cuerpo y pie.
        [esNumerado]: Si quieres un menú numerado o no.
        """
        # if bVertical==True:
        #     saltoLinea='\n'
        # else:
        #     saltoLinea=''
        cuerpo=f''
        for i,item_menu in enumerate(self.lst_Item):      
            cuerpo += (f'{ self.lst__X_num[i] if esNumerado==True else '' }')                # 'Opt-'
            cuerpo += (f'{ self.lst_numeracion[i] if esNumerado==True else '' }')            # 1            
            cuerpo += (f'{ str(self.lst__num_X[i]) if esNumerado==True else '' }')            # '-'
            cuerpo += (f'{ str(self.lst__X_item[i]) if self.lst__X_item[i] else '' }')    # TAB('    ')
            cuerpo += (f'{item_menu}')                                                      # 'Casa'
            cuerpo += (f'{ str(self.lst__item_X[i]) if self.lst__item_X[i] else '' }')      # __TAB + "Loren ipsum"
            """
             la última iteracion no imprime el \n """
            cuerpo += (f'{'\n'}')                        if i<(len(self.lst_Item)-1) else ''
        pass        
        return cuerpo
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_Row_Body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=f''
        if 0 <= row < len(self.lst_Item):
            for i , item_menu in enumerate(self.lst_Item):            
                if i == row :
                    fila_menu += f'{ self.lst__X_num[i]          if esNumerado==True else f'' }'         # 'Opt-'                   
                    fila_menu += f'{ self.lst_numeracion[i]     if esNumerado==True else f'' }'         # 1         
                    fila_menu += f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }'         # '-'
                    fila_menu += f'{ str(self.lst__X_item[i])  if self.lst__X_item[i] else f'' }'     # TAB('    ')
                    fila_menu += f'{ item_menu }'                                                       # 'Casa'
                    fila_menu += f'{ str(self.lst__item_X[i])   if self.lst__item_X[i] else f'' }'      # TAB + 'Def: Loren ipsum'
                    
                    return fila_menu
            pass
        pass
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_lst_row_body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=[]
        if 0 <= row < len(self.lst_Item):
            for i , item_menu in enumerate(self.lst_Item):            
                if i == row :
                    fila_menu.append (f'{ self.lst__X_num[i]             if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ self.lst_numeracion[i]       if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__num_X[i])        if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__X_item[i])    if self.lst__X_item[i] else f'' }')
                    fila_menu.append ( f'{ item_menu }')                                                  
                    fila_menu.append ( f'{ str(self.lst__item_X[i])     if self.lst__item_X[i] else f'' }') 
                    
                    return fila_menu
            pass
        pass
    # _______________________________________
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU con Tantas piezas como partes tenga la filaa.
    def get_matriz(self):
        lst_matriz=[]
        for i  in range(self.lst_Item):            
            lst_matriz.append(self.get_lst_row_body(row=i, esNumerado=True))
        return lst_matriz
    # ______________
    # FILA DE SALIR
    def get_row_Salir(self):
        salir =  f'{ self.lst__X_num[0] }'       # 'Opt-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{'EXIT'}'                   # 'SALIR'
        salir += f'{ self.lst__num_X[0] }'        # '-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{ MenuDvd.__TAB }'           # TAB('    ')
        salir += f'{'...pulsa (\'<<<\')'}'                    # ZERO ( 0 )
        salir += f'{MenuDvd.__TAB}'             # Explicativo. se puede omitir.
        salir += f'{''}'                        # Lugar de la funcion para devolver el formato de 7

        return salir
    # __________________
    # IGUALA LAS LISTAS
    def igualarListas(self, listaKeys, listaToReLong):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.igualarListas(listaKeys=listaKeys, listaToReLong=listaTipos)        
        listaKeys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor. Aun así se retorna
        """
        if len(listaKeys)==len(listaToReLong):
            return listaToReLong
        elif len(listaKeys)>len(listaToReLong):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[None for i, (k) in enumerate(listaKeys) if i >= len(listaToReLong)]
            listaToReLong=listaToReLong+listaNewTipos
            print(listaToReLong)
        else:
            print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la listaToReLong")
            longListaTipos = len(listaToReLong)
            longListaKeys  = len(listaKeys)
            for i in range(longListaKeys , longListaTipos ):
                listaToReLong.pop()

        return listaToReLong
        pass
    # _____________
    # INPUT SEGURO.
    def pide_data_usuario(self, objMenu):
        respuesta=None
        while(True):
            i=input(f"{self.introData}")    
            try:
                if i == SALIR:          # A PULSADO  '<<<' ....SALIR
                    return None
                if i.isdigit():
                    i=abs(int(i))
                    if i > len(objMenu.lst_Item): 
                        continue
                    else:                                            
                        respuesta =  i
                        break
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        pass
        return respuesta
    # _________________________________________
    # DEVUELVE LAS PARTES DEL MENU QUE QUIERAS
    def FrankY(self, bSalir=True, bHead=True, bBody=True, bPie=True, esNumerado=True):
        lst_cabeza=[]
        retorno = ''
        if bHead:   lst_cabeza.append( f'{self.cabecera}' )
        if bSalir:  lst_cabeza.append( self.get_row_Salir() )       
        if bBody:   
            for i in range(len(self.lst_Item)):
                lst_cabeza.append(self.get_Row_Body(row=i, esNumerado=True))
        if bPie:    lst_cabeza.append( self.pie )

        """ Juntamos todas las piezas reunidas """
        for i, parte_Franky in enumerate(lst_cabeza):
            retorno += str(parte_Franky)
            retorno += '\n' if i<(len(lst_cabeza)-1) else ''
        return retorno
    # _________
    # ESTATICA    
    def MDicc(dicc_menu, tituloMenu):
        if not isinstance(dicc_menu,dict): return -1
        salir={"SALIR": 0}
        # Asi puedes adjuntar por el principio (y recibir en una funcion) un diccionario(**), una lista se envia así(*)
        menuSalir={**salir, **dicc_menu}
        # al pasar dicc_menu por referencia, cambia en la funcion que lo llama tb. 
        # y no lo retorno sino que lo cambio aqui.
        dicc_menu=menuSalir
        # print(menuSalir)
        # while (True):
            # Imprime dicc_menu:
        
        # Estas cossa de python son la pera
        print ('\n'+'-'*9,tituloMenu,'-'*9)    
        for index,tit in enumerate(menuSalir):
            print (f'{index}....{tit}')
        print ('-'*22)
        
        # Selecciona Opcion:
        i=input("Intro opcion... ")
        if i.isdigit():
            i=abs(int(i))
        else:
            return -1

        return i
    # _____________________________________________________
    # ESTATICA PARA CREAR MENUS RAPIDOS DE UNA LINEA PADRE Y DEVUELVE UN RESULTADO PARA SER RECOGIDO EN EL MAIN
    def MList(lst_item_menu, tituloMenu="M E N U", 
                msgItem='Intro Opcion...', 
                num_char=40,
                char_head='-', char_cuello='-', char_pie='-'):
        """ 
        Devuelve un lst_item_menu. Añade la opcion de salir.
        [lst_item_menu]: lista de str con los textos del lst_item_menu.

        """
        salir=["SALIR"]
        lst_item_menu=salir+lst_item_menu    
        # Imprime lst_item_menu:
        # print('\n'+char_head*40+'\n'+tituloMenu+'\n'+char_cuello*40)
        print(f'\n{char_head*num_char}\n{tituloMenu}\n{char_cuello*num_char}')
        for index,opc in enumerate(lst_item_menu):
            print (f'{index}....{opc}')
        print (f'{char_pie*num_char}')    
        
        while(True):
            # Selecciona Opcion:        
            i=input(f"{msgItem}")    
            # Si todo lo introducido en la cadena son digitos = True
            try:
                if i.isdigit():
                    i=abs(int(i))
                    if i==0: return None
                    if i>len(lst_item_menu): 
                        continue
                    else:                
                        return i
                else:
                    continue
            except Exception:
                continue


# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
""" 
(*)Tipos de Menus que se intentan conseguir:
    -------------------------   head
    Menu1                       titulo
    -------------------------   cuello
    opt 1.....loren ipsum1  
        opt 1.1 loren ipsum_N
        opt 1.2 loren ipsum_M
    opt 2.....loren ipsum2
        opt 2.1 loren ipsum_U
        opt 2.2 loren ipsum_N
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    _________________________   pie
    intro opcion:.....          
    -------------------------

    View(titulo, withConfig=False, ExecFunc=False, bControl=False)

    -Muestra un Menu sencillo(withConfig) y devuelve el control(ExecFunc) para que el usuario actue en el main(). se ejecuta sin hilos(bControl)
xxxxxxxxxxxxxxxxxxxxxxxxxxx otra opcion xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    Menu2
    -------------------------
    opt 1.....loren ipsum1
        opt 1.1 loren ipsum_N
            opt 1.1.1 loren ipsum_M
            opt 1.1.2 loren ipsum_U
    opt 2.....loren ipsum2
        opt 2.1 loren ipsum_U
        opt 2.2 loren ipsum_N
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    _________________________
    intro opcion:..... 
    
    View(titulo, withConfig=False, ExecFunc=True, bControl=False)
xxxxxxxxxxxxxxxxxxxxxxxxxx otra opcion xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    -------------------------
    Menu1
    -------------------------
    opt 1.....loren ipsum1
    opt 2.....loren ipsum2
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    xxxxxxxxxxxxxxxxxxxxxxxxx
    intro opcion:.....  """        
from enum import Enum as TIT_FUNC
class Tit_Func(TIT_FUNC):
    TIT=0
    FUNC=1

from enum import Enum as MASTER_INDEX
class PADRE_IND(MASTER_INDEX):
    PADRE=0
    INDEX=1
""" 
>>> for tit_dicc, master_index in self.dicc_xgenx.items():
        if master_index[PADRE_IND.PADRE]==master_busca: pass
"""

class XindiceX(MenuDvd):
    """ 
    >>> Def: Gestiona una lista de menus y sub menus y los muestra por Terminal.
    instancia: ElMenuXX=XindiceX()
    add:    Añade un menu con dos listas, una de Titulos y otra Opcional de funciones a Exec con cada titulo en 1:1
    cofig:  Configura la Escalera del Indice: Menu|Padre|indice_en_el_padre
    View:   Muestra un Menu: 1-Con Genetica/Sin Genetica, 2-Vuelve/Se Ejecuta 3-Control Sobre Estilos 4-
    """ 

    def __init__(self):
        """ >>> Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        """        

        """ >>>  """
        self.lst_menuXX=[]
        """ >>> Lista de objetos MenuDvd que mantiene un lst_Item,  dicc_menu(num_n:[strMenu_n, func_n])  """

        self.lst_titulosXX=[]
        """ >>> Lista de titulos introducidos. Me permite validar rapido  """

        self.dicc_xgenx={}
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """
        
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # 1-AÑADE UN MENU AL GESTOR                                   (Crea un MenuDvd)
    def add(self, titulo, lst_Item, lst_func=None):     
        """  """
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_Item=lst_Item, lst_func=lst_func)
            # print(new_menu)
        except Exception as e:
            print(e)
            return None


        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)

        print(f'Load Menu {titulo} Ok ;)')
        return new_menu
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # 2-CONFIGURA LA RELACION PADRE HIJO(INDICE) DEL MENU         (dicc_xgenx)
    def config(self, titulo, suPadre=None, indexInPadre=None): 
        """ >>> Configura la relacion de los menus. 
        Maneja el dicc_xgenx que es el que gestiona la genealogía.
        """
        if not titulo in self.lst_titulosXX:   return None
        if suPadre ==None and indexInPadre==None:
            self.dicc_xgenx[titulo]=[None, None]
            """ Es un puro Master!!!  """

        elif suPadre == None and indexInPadre!=None:
            self.dicc_xgenx[titulo]=[None, None]            
            """ Es un Master Fuerte pero confundido, le sobra el index """

        elif suPadre != None and indexInPadre==None:
            newIndex=self.busca_index_free(titulo_key=titulo, master_buscado=suPadre)            
            """ es un Sub Puro ????? esta machacando al anterior pq no da con el index libre"""
            if newIndex:
                self.dicc_xgenx[titulo]=[suPadre, newIndex]
            else:
                return False
        elif suPadre != None and indexInPadre!=None and str(indexInPadre).isdigit():
            """ es un Sub Selector Puro y machaca todo lo que pilla."""
            self.dicc_xgenx[titulo]=[suPadre, indexInPadre]
        else:
            """ Error No posible, pero lo dejo por legible.....o no ;) """
    # _______________________________________________       
    # RETORNA UN OBJ MENUDVD POR MEDIO DE SU TITULO             (obtiene el MenuDvd )
    def get_menudvd(self, titulo):
        """ >>> Retorna un objeto MenuDvd x su str titulo. """
        if titulo in self.lst_titulosXX:
            for menu in self.lst_menuXX:
                if str(menu.titulo) == str(titulo):
                    return menu
    # _________________
    # BUSCA INDEX FREE.                                         (Busca un indice libre.... en revision)
    def busca_index_free(self, titulo_key,  master_buscado ):
        """ >>> Busca en el diccionario de configuracion << self.dicc_xgenx >> , un index libre(el siguiente). 
        Retorna: None si Error | indice para insertar si todo OK """
        lst_indexes=[]



        for tit_dicc, par_master_idx in self.dicc_xgenx.items():
            if master_buscado == par_master_idx[PADRE_IND.PADRE.value]:
                lst_indexes.append(par_master_idx[PADRE_IND.INDEX.value])
        
        # Cuando sale del bucle espero tener una lista de los index del master.
        if lst_indexes:
            try:
                max_index=max(lst_indexes)
                new_index=max_index+1
                if new_index>len(self.dicc_xgenx.keys()): 
                    return None
                return new_index
            except Exception as e:
                print(f'Error: {e} ')
                return None    
        else:
            return 1    #Todos los menus empiezan las opciones en 1 y el 0 es Salir.
    # ________________________________________________________
    # BUSCA EN dicc_xgenx E IMPRIME TODOS LOS MENUS EN ORDEN.   (W.I.P.)
    def impr_Rcrsv(self, titulo, indice=None):
        """ >>> self.dicc_xgenx ==> titulo(key):(valor)(esHijo, index)  """
        # if indice==None:            
        retorno=[]
        for i, (tit_dicc, xgenx) in enumerate(self.dicc_xgenx):
            for soyPadre, index in xgenx:
                if titulo == soyPadre:
                    if indice==None: 
                        indice = index
    # ___________________________________________
    # ELIMINA REPETIDOS DE UNA LISTA USANDO SET....             (No usada)
    def lst_sin_repetidos(self, lst_to):
        """ Elimina los repetidos de la lista con un set """
        if isinstance(lst_to, list):
            set_lst_to=set(lst_to)
            lst_set = list(set_lst_to)
            return lst_set
    # 3-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # MUESTRA UN MENU.  LLAMADA EXTERNA                         (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones)
    def View(self, titulo, withConfig=False, execFunc=False):
        """ >>> Def: Muestra Un Menu al Usuario por el titulo del menu que ha tenido que ser añadido con self.add()                    
        [withConfig]: False: sin Configuracion: Menu Sin Sub-menus | True: Menu Con Sub-menus. 
        [execFunc]: False: retorna el valor para ser tratado | True: Ejecuta la funcion pasada como argumento en self.add()
        """
        # ___________
        # Validacion:
        if self.validacion_show(titulo=titulo, withConfig=withConfig) == False : 
            return None
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        menu_dvd=self.get_menudvd(titulo=titulo)
        """ That's Me!!         OBJ-MENU-PPAL    """        
        lst_hijos = self.get_lst_hijosX(titulo=titulo)        
        """ Mis Hijos/as!!      Orgullo de padre """        
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if withConfig==True:
            """ 
            ................. PRINT SUB-MENUS 
            """
            print(f'{menu_dvd.FrankY(bSalir=True, bHead=True, bBody=False, bPie=False, esNumerado=False)}')
            """ IMPR  Cabeza + Titulo + Cuello  + SALIR """
            if  lst_hijos: 
                for i in range(len(menu_dvd.lst_Item)):
                    print(menu_dvd.get_Row_Body(row=i, esNumerado=True))
                    for hijo in lst_hijos:
                        if hijo['index'] == i:
                            self.XindeX(menuDvd=hijo['menuDvd'])
                pass
                print(f'{menu_dvd.FrankY(bSalir=False, bHead=False, bBody=False, bPie=True, esNumerado=False)}')
                
                respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)
                """ 
                >>> PIDE DATO AL USUARIO. HASTA Q INTRO 0 (SALIR) U OPT-MENU | OPT: [ExecFunc , return int].   
                """            
                # ________________________
                # EJECUTAMOS O RETORNAMOS
                return self.Terminator(menu_dvd=menu_dvd, respuesta=respuesta, execFunc=execFunc)                                   
                           
            elif not lst_hijos:
                """................ Muestra el MENU del Tiron pq aunque entra por Config, NO Tiene Hijos """
                print(menu_dvd.FrankY(bSalir=True, bHead=True, bBody=True, bPie=True, esNumerado=True))
                respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)
                return self.Terminator(menu_dvd=menu_dvd,  respuesta=respuesta, execFunc=execFunc )
        elif withConfig == False:            
            """ 
            ................ MUESTRA UN MENU DEL TIRON 
            """
            """ >>> PRINT MENU """            
            print(menu_dvd.FrankY(bSalir=True, bHead=True, bBody=True, bPie=True, esNumerado=True))
            """ >>> Pide Data USUARIO. Hasta Intro 0 (SALIR) U (int)Opt-Menu | OPT: [ExecFunc , return int].            """            
            respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)
            """ >>> Terminator ejecuta la funcion asignada o retorna la Opt pedida al Usuario."""
            return self.Terminator(menu_dvd=menu_dvd,  respuesta=respuesta, execFunc=execFunc )
        pass
    # _________________________________________
    # RCRSV Q MUESTRA EL MENU MAS PROFUNDO DEL CAMINO 
    def XindeX(self, menuDvd, level=None):
        """ S U  1ª  V E Z  """
        if level==None:
            level = 0            
        level += 1
        """ 
        E M P E Z A M O S !!!! """
        lst_hijos = self.get_lst_hijosX(titulo=menuDvd.titulo)        
        if lst_hijos: 
            for i in range(len(menuDvd.lst_Item)):

                for hijo in lst_hijos:
                    
                    self.XindeX(menuDvd=hijo['menuDvd'], level=level)
        else:
            """ MUESTRA UN MENU DEL TIRON """
            menuDvd.style( X__num = menuDvd.get_TAB()*2 + str(menuDvd.X__num) )
            print(menuDvd.FrankY(bSalir=False, bHead=False, bBody=True, bPie=False, esNumerado=True))
    # ____________________________________
    # 1ª VALIDACION DEL METODO SELF.View
    def validacion_show(self, titulo, withConfig):
        if titulo not in self.lst_titulosXX: 
            print(f'ERR-VAL:: {titulo}  no esta en self.lst_titulosXX')
            return False                
        if titulo not in self.dicc_xgenx and withConfig==True: 
            print(f'ERR-VAL:: {titulo} no esta en self.dicc_xgenx')
            return False
        return True
    # __________________________
    # MUESTRA UN MENU DEL TIRON
    def Show_All(self, menu_dvd , execFunc=False,  bSalir=True, bHead=True, bBody=True, bPie=True, esNumerado=True):        
        print(menu_dvd.FrankY(bSalir=bSalir, bHead=bHead, bBody=bBody, bPie=bPie, esNumerado=True))
        """ MUESTRA UN MENU DEL TIRON 
        """
        respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)
        """ PIDE DATO AL USUARIO. HASTA Q INTRO 0 (SALIR) U OPT-MENU | OPT: [ExecFunc , return int].   
        """            
        return self.Terminator(menu_dvd=menu_dvd,  respuesta=respuesta, execFunc=execFunc )
        """ >>> Terminator ejecuta la funcion asignada o retorna la Opt pedida al Usuario.
        """
    # _______________________________________________________________
    # Analiza las respuestas y toma una opcion en funcion de execFunc
    def Terminator(self, menu_dvd,  respuesta, execFunc):
        """  """
        if respuesta == None:
            """ SALIR """
            return respuesta
        elif respuesta != None:
            if execFunc==False: 
                """ OPT RETORNA"""
                return respuesta
            else:
                """ OPT EXEC FUNC """                    
                return menu_dvd.dicc_menu[menu_dvd.titulo][respuesta][Tit_Func.FUNC.value]()                
    # _____________________________________________________
    # DEVUELVE UN LIST DE HIJOS COMPROBANDO EN DICC_XGENX
    def get_lst_hijosX(self, titulo):
        """ >>> LISTA CON MIS HIJOS DE PRIMERA GENERACION. Recorre el dicc_xgenx y recoge 
        [Retorno]: una lista de diccionarios (key):str-titulo (value):(MenuDvd)menudvd_hijo
        """
        lst_hijos=[]
        for tit, padre_index in self.dicc_xgenx.items():
            if titulo == padre_index[PADRE_IND.PADRE.value]:
                menudvd_hijo = self.get_menudvd(titulo=tit)
                lst_hijos.append({  'titulo':tit,
                                    'menuDvd':menudvd_hijo, 
                                    'padre':titulo,
                                    'index':padre_index[PADRE_IND.INDEX.value]
                                })                
            pass
        pass    
        if lst_hijos: 
            return lst_hijos
        else: 
            return None        
    # _____________________________________________________
    # DEVUELVE UN LIST DE HIJOS COMPROBANDO EN DICC_XGENX
    def get_lista_num_Valid():
        pass

# ============================================================================================
# ============================================================================================
import threading
import time
import tkinter as tk   
# ============================================================================================
# ============================================================================================
""" MotorMain ?? """
class MotorIndeX(XindiceX):
    def __init__(self):
        super().__init__()
        self.hilos = {}  # Diccionario para controlar los hilos activos

    def start(self, tituloMenu, withConfig=True, bAllControl=False, delay=0.3):
        """
        Inicia el menú y decide cómo gestionar el control de las funciones.
        - tituloMenu: El menú que se desea ejecutar.
        - withConfig: Define si usa la configuración de relaciones.
        - bAllControl: Define si la función toma todo el control del flujo.
        - delay: Tiempo entre ejecuciones para tareas recurrentes (solo si no toman el control).
        """
        menu = next((menu for menu in self.lst_menuXX if menu.titulo == tituloMenu), None)
        if not menu:
            print(f"Menú '{tituloMenu}' no encontrado.")
            return

        # Obtener la función asociada al menú
        opciones = menu.dicc_menu
        print("\nOpciones disponibles:")
        for key, (opcion, func) in opciones.items():
            print(f"{key}. {opcion}")
        print("0. SALIR")

        respuesta = input("\nSelecciona una opción: ")
        if not respuesta.isdigit() or int(respuesta) not in opciones:
            print("Opción inválida.")
            return

        respuesta = int(respuesta)
        if respuesta == 0:
            return

        # Obtener función asociada
        _, func = opciones[respuesta]

        # Si `bAllControl` es True, ejecuta la función directamente en el flujo principal
        if bAllControl:
            print(f"Ejecutando '{opciones[respuesta][0]}' con control total...")
            func()
            print("Control devuelto al menú principal.")
            return

        # Gestión de hilos para ejecución en paralelo
        if tituloMenu in self.hilos and self.hilos[tituloMenu].is_alive():
            print("Deteniendo hilo anterior...")
            self.hilos[tituloMenu].stop()

        def tarea():
            print(f"Ejecutando '{opciones[respuesta][0]}' en un hilo separado...")
            while True:
                func()
                time.sleep(delay)

        hilo = threading.Thread(target=tarea, daemon=True)
        self.hilos[tituloMenu] = hilo
        hilo.start()

    def stop(self, tituloMenu):
        """Detiene el hilo asociado a un menú."""
        if tituloMenu in self.hilos and self.hilos[tituloMenu].is_alive():
            print(f"Deteniendo hilo '{tituloMenu}'...")
            self.hilos[tituloMenu].stop()
            self.hilos.pop(tituloMenu, None)
        else:
            print(f"No hay hilo activo para '{tituloMenu}'.")

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
""" 
class MotorIndex(XindiceX):
    def __init__(self):
        super().__init__()
        self.hilos = {}  # Diccionario para controlar los hilos activos
        if thread==None:
            #Auto Gestion de Hilos
            self.thread = None
            # self.thread = threading.Thread(target=self.func)
        else:
            # El hilo lo gestiona el main
            self.thread = thread

    # _________________________________________________
    # INICIA UN HILO PARA CADA ELEMENTO DEL MENU.
    def start(self, tituloMenu, withConfig=True, is_form=False, delay=0.3):
        
        # Def: 
        # - [tituloMenu]: El menú que se desea ejecutar.
        # - [withConfig]: Define si usa la configuración de relaciones.
        # - [is_form]: Define si la tarea es un formulario.
        # - [delay]: Tiempo entre ejecuciones para tareas recurrentes.
       
        menu = next((menu for menu in self.lst_menuXX if menu.titulo == tituloMenu), None)
        if not menu:
            print(f"Menú '{tituloMenu}' no encontrado.")
            return

        # Obtener la función asociada al menú
        opciones = menu.dicc_menu
        print("\nOpciones disponibles:")
        for key, (opcion, func) in opciones.items():
            print(f"{key}. {opcion}")
        print("0. SALIR")

        respuesta = input("\nSelecciona una opción: ")
        if not respuesta.isdigit() or int(respuesta) not in opciones:
            print("Opción inválida.")
            return

        respuesta = int(respuesta)
        if respuesta == 0:
            return

        # Obtener función asociada
        _, func = opciones[respuesta]

        # Gestión de hilos
        if tituloMenu in self.hilos and self.hilos[tituloMenu].is_alive():
            print("Deteniendo hilo anterior...")
            self.hilos[tituloMenu].stop()

        def tarea():
            if is_form:
                print("Iniciando formulario...")
                form = func()
                form.mainloop()
            else:
                print("Ejecutando tarea inmediata...")
                while True:
                    func()
                    time.sleep(delay)

        hilo = threading.Thread(target=tarea, daemon=True)
        self.hilos[tituloMenu] = hilo
        hilo.start()
    # _________________________________________________
    # PARA UN HILO DESDE EL MENU.
    def stop(self, tituloMenu):
        # Detiene el hilo asociado a un menú.
        if tituloMenu in self.hilos and self.hilos[tituloMenu].is_alive():
            print(f"Deteniendo hilo '{tituloMenu}'...")
            self.hilos[tituloMenu].stop()
            self.hilos.pop(tituloMenu, None)
        else:
            print(f"No hay hilo activo para '{tituloMenu}'.")

"""