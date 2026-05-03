""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""
        #Cte para cuando se pide la opcion al usuario.
SALIR='<<<'
from enum import Enum as Column
class COL(Column):    
    SP_I    = 0 ; A = 0      # Espacio Inicial
    X__NUM  = 1 ; B = 1      # Pre-num
    NUM     = 2 ; C = 2      # Num
    NUM__X  = 3 ; D = 3      # Pos-num
    __TAB   = 4 ; E = 4      # TAB
    X__ITEM = 5 ; F = 5      # Pre-Item
    ITEM    = 6 ; G = 6      # Item
    ITEM__X = 7 ; H = 7      # Pos-Item
    SP_F    = 8 ; I = 8      # Espacio Final

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

    def __init__(self, titulo, lst_item, lst_func=None, fraseHead=''):               
        """ RECOGE LOS VALORES """
        self.titulo     = titulo                # El titulo e indice del menu. es la CABEZA
        self.lst_item = lst_item      # La cadena de Texto que conforma un Item del Menu. CUERPO 
        if lst_func==None:
            pass
            self.lst_func=[None for i in range(len(self.lst_item))]
        else:
            self.lst_func   = lst_func              # La funcion que se pasa asociada por posicion al Item de lst_item
        # ______________________________________________________
        """ La Frase Que se pone en la Impresion del Menu: """
        if fraseHead=='':
            self.fraseHead=self.titulo
        else:
            self.fraseHead=fraseHead
        # ____________________________________________
        """ Before-After num    Before-After item  """
        self.X__num    = MenuDvd.__OPT          # Lo que va BEFORE del Numero 
        self.num__X    = MenuDvd.NUM__X         # Lo que va AFTER del Numero
        self.X__item = MenuDvd.__TAB            # Lo que va BEFORE del Item
        self.item__X = MenuDvd.ITEM__X          # Lo que va AFTER del Item
        # Style ______________________________
        self.char_head  = MenuDvd.CHAR_HEAD     # 1º caracter que se repite num_char veces. es el SOMBRERO
        self.char_cuello= MenuDvd.CHAR_CUELLO   # 2º caracter que se repite num_char veces. es la PAJARITA 
        self.char_pie   = MenuDvd.CHAR_PIE      # 2º caracter que se repite num_char veces. es el ZAPATOS
        self.num_char   = MenuDvd.NUM_CHAR      # Numero de caracteres que hay de los char --------------
        
        # Texto Input ________________________
        self.introData = MenuDvd.STR_INTRO_DATA
        # _____________________________________________________________
        """ GENERA EL ENTORNO: La linea de CABECERA - CUELLO - PIE """
        # self.cabecera, self.pie = self.formar_entorno()
        self.sombrero, self.cabeza, self.cuello, self.pie = self.formar_entorno()
        # _____________________________________________________________
        """ GENERA LA LISTA DE NUMERACION"""
        self.lst_numeracion_rltv=[i for i in range(len(self.lst_item))]
        # ___________________________________
        """ CARGA LAS LISTAS DE BEFORE-AFTER """
        self.lst__X_num=[]           #Lista de los caracteres que van antes del Numero del item.
        self.lst__num_X=[]           #Lista de los caracteres que van depues del Numero del item.
        self.lst__X_item=[]     #Lista de los caracteres que van antes del Item
        self.lst__item_X=[]     #Lista de los caracteres que van Despues del Item        
        for i in range(len(lst_item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # ___________________________________________________
        """ VALIDACION DE TAMAÑO DE LISTAS. IGUALAR TODAS A:  self.lst_item       """
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst_func)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst_numeracion_rltv)
        # Entorno____________
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__X_num)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__num_X)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__X_item)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__item_X)        
        # __________________________________
        """ GENERACION DEL DICCIONARIO  """        
        Itrtr_valor_dicc = tuple(zip(self.lst_item, self.lst_func))            
        """ >>> 1º ==> Creo una tupla con el par lst_item, lst_func xa formar el self.dicc_menu
        """
        val_dicc_menu={self.lst_numeracion_rltv[i]:valor_dicc  for i, valor_dicc in enumerate(Itrtr_valor_dicc)}                                          
        """>>> 2º ==> { 2 : ( 'Sales' , compraProd ) } ==> (2) numeracion ('Sales') titulo-menu (compraProd) funcion sin parentesis
        """        
        self.dicc_menu={self.titulo:val_dicc_menu}
        """ 3º ==> D I C C I O N A R I O R E S U L T A D O 
        >>> {'Titulo Menu':  { : ( 'item_1_menu' , func_item_1 ) } }   ==> Se genera 1 por Menu. 
        Es de donde tiene que coger self.Terminator la informacion para ejecutar al funcion."""
        
        # print(self.dicc_menu)
        # __________________________________
        """ GENERACION DE LA LINEA DE SALIR  """        
        self.salir=self.get_row_Salir()
    
    def __str__(self):                
        return self.FrankY(bSalir=True, bCabeza=True, bCuerpo=True, bPie=True, esNumerado=True)
    # ____________________________________
    # VALIDA LA ESTRUCTURA DE ENTRADA (...llamada desde AddX)
    def valid_unpack(self, lst_Intro):
        """  
        >>> Opcion 1:
        lst_titulos = ["Tit-1", "Tit-2" , "Tit-3" ]
        lst_FNC    = ["func-1", "func-2" , "func-3" ]

        >>> Opcion 2:
        lst_titulos    = [ ('Tit-1',func-1), ('Tit-2', func-2) , ('Tit-3', func-3) ]
        """
        lst_ITM = []
        lst_FNC = []
        try:
            if isinstance(lst_Intro, list) or isinstance(lst_Intro, tuple):                
                for titulo, funcion in lst_Intro:
                    """ TITULO """
                    if not isinstance(titulo, str): 
                        print(f'Error en la Estructura de {lst_Intro} \nLos titulos deben ser String....revisa por favor ')
                        return None, None
                    else:
                        lst_ITM.append(titulo)
                    """ FUNCION """
                    if not callable(funcion):       # VALIDA FUNCION
                        if funcion != None:         # PERMITE NONE
                            return None, None
                        else:
                            lst_FNC.append(None)    
                    else:
                        lst_FNC.append(funcion)
            else:
                return None, None
            
            return lst_ITM, lst_FNC
        except:
            return None, None
        pass
    # ____________________________________________________________________
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM)
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
        for i in range(len(self.lst_item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # Reset de la cabecera y pie __________________
        # self.cabecera, self.pie = self.formar_entorno()
        self.sombrero, self.cabeza, self.cuello, self.pie = self.formar_entorno()
    # ___________________
    # Retorna 4 espacios
    def get_TAB(self):
        return self.__TAB
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
        for i,item_menu in enumerate(self.lst_item):      
            cuerpo += (f'{ self.lst__X_num[i] if esNumerado==True else '' }')                # 'Opt-'
            cuerpo += (f'{ self.lst_numeracion_rltv[i] if esNumerado==True else '' }')            # 1            
            cuerpo += (f'{ str(self.lst__num_X[i]) if esNumerado==True else '' }')            # '-'
            cuerpo += (f'{ str(self.lst__X_item[i]) if self.lst__X_item[i] else '' }')    # TAB('    ')
            cuerpo += (f'{item_menu}')                                                      # 'Casa'
            cuerpo += (f'{ str(self.lst__item_X[i]) if self.lst__item_X[i] else '' }')      # __TAB + "Loren ipsum"
            """
             la última iteracion no imprime el \n """
            cuerpo += (f'{'\n'}')                        if i<(len(self.lst_item)-1) else ''
        pass        
        return cuerpo
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_strRow_Body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    fila_menu += f'{ self.lst__X_num[i]          if esNumerado==True else f'' }'         # 'Opt-'                   
                    fila_menu += f'{ self.lst_numeracion_rltv[i]     if esNumerado==True else f'' }'         # 1         
                    fila_menu += f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }'         # '-'
                    fila_menu += f'{ str(self.lst__X_item[i])  if self.lst__X_item[i] else f'' }'     # TAB('    ')
                    fila_menu += f'{ item_menu }'                                                       # 'Casa'
                    fila_menu += f'{ str(self.lst__item_X[i])   if self.lst__item_X[i] else f'' }'      # TAB + 'Def: Loren ipsum'
                    
                    return fila_menu
            pass
        pass
    # ____________________
    # El item de una fila
    def get_item_row_body(self, row):
        """ >>> Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    return f'{ item_menu }'      
        # ____________________
    # El item de una fila
    def get_numRltv_row_body(self, row):
        """ >>> Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , numRltv in enumerate(self.lst_numeracion_rltv):            
                if i == row :
                    return f'{ numRltv }'                    
              
    # ____________________________________________
    # DEVUELVE UNA FILA DEL MENU En formato lista
    def get_lst_row_body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=[]
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    fila_menu.append ( f'{ self.lst__X_num[i]           if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ self.lst_numeracion_rltv[i]       if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__X_item[i])     if self.lst__X_item[i] else f'' }')
                    fila_menu.append ( f'{ item_menu }')                                                  
                    fila_menu.append ( f'{ str(self.lst__item_X[i])     if self.lst__item_X[i] else f'' }') 
                    
                    return fila_menu
            pass
        pass
    # ______________
    # FILA DE SALIR
    def get_row_Salir(self):
        salir =  f'{ self.lst__X_num[0] }'       # 'Opt-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{'Para Salir pulsa <<<'}'                   # 'SALIR'
        salir += f'{ self.lst__num_X[0] }'        # '-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{ MenuDvd.__TAB }'           # TAB('    ')
        salir += f'{''}'                    # ZERO ( 0 )
        salir += f'{MenuDvd.__TAB}'             # Explicativo. se puede omitir.
        salir += f'{''}'                        # Lugar de la funcion para devolver el formato de 7

        return salir
    # _____________
    # CABEZA Y PIE
    def formar_entorno(self):
        # cabecera=f'\n{ self.char_head * self.num_char }\n{ self.fraseHead }\n{ self.char_cuello * self.num_char }'                
        # pie=f'{self.char_pie*self.num_char}'
        # return cabecera, pie
        sombrero=f'\n{ self.char_head * self.num_char }'
        cabeza=f'{self.fraseHead }'
        cuello=f'{self.char_cuello * self.num_char }'
        pie = f'{self.char_pie*self.num_char}'
        return sombrero, cabeza, cuello , pie
    # ______________________________________
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU con Tantas piezas como partes tenga la filaa.
    def get_matriz(self):
        lst_matriz=[]
        for i  in range(self.lst_item):            
            lst_matriz.append(self.get_lst_row_body(row=i, esNumerado=True))
        return lst_matriz
    # __________________
    # IGUALA LAS LISTAS
    def igualarListas(self, listaKeys, listaToReLong, valorRelleno=None):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        [valorRelleno]: en caso de que listaKeys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
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
            # print(listaToReLong)
        else:
            # print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la listaToReLong")
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
                    if i > len(objMenu.lst_item): 
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
    def FrankY(self, bSombrero=False, bCabeza=False, bCuello=False, bSalir=False ,  bCuerpo=False, bPie=False, esNumerado=False):
        lst_franky=[]
        retorno = ''
        if bSombrero:   lst_franky.append( f'{self.sombrero}' )
        if bCabeza:     lst_franky.append( f'{self.cabeza}' )
        if bCuello:     lst_franky.append( f'{self.cuello}' )
        if bSalir:      lst_franky.append( self.get_row_Salir() )       
        if bCuerpo:   
            for i in range(len(self.lst_item)):
                lst_franky.append(self.get_strRow_Body(row=i, esNumerado=True))
        if bPie:    lst_franky.append( self.pie )

        """ Juntamos todas las piezas reunidas """
        for i, parte_Franky in enumerate(lst_franky):
            retorno += str(parte_Franky)
            retorno += '\n' if i<(len(lst_franky)-1) else ''
        return retorno
    # __________________________________________________________________________________________________________
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
    # ________________________________
    # VALIDA LA ESTRUCTURA DE ENTRADA 
    def valida_estructura(listaTitulos, listaFunc):
        """  
        >>> Opcion 1:
        lst_titulos = ["Tit-1", "Tit-2" , "Tit-3" ]
        lst_func    = ["func-1", "func-2" , "func-3" ]

        >>> Opcion 2:
        lst_titulos    = [ ('Tit-1',func-1), ('Tit-2', func-2) , ('Tit-3', func-3) ]
        """
        try:
            if isinstance(listaTitulos, list) or isinstance(listaTitulos, tuple):
                for titulo in listaTitulos:
                    if not isinstance(titulo, str):
                        if isinstance(titulo, list)  or isinstance(titulo, tuple):
                            for titulo, funcion in listaDef:
                                if not isinstance(titulo, str):     # Obliga a Titulo String
                                    return False
                                if not callable(funcion):           # Obliga a Meter una funcion()
                                    if funcion != None:             # ... o None(en revision)
                                        return False
                                    pass
                                pass
                            pass
                        else:
                            return False
                    else:
                        return False
                    pass
                pass
            else:
                return False
        except:
            return False
        pass
        # Ahora validamos listaFunc(lista + funcion o None )
        try:
            if isinstance(listaFunc, list) :
                for funcion in listaFunc:
                    if not callable(funcion):
                        if funcion != None:             # ... o None(en revision)
                            return False
            else:
                return False
        except:
            return False
        pass

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

    def __init__(self, esLoop=True):
        """ >>> Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        [esLoop]: True=circular hasta Salida. | False=Sólo una ejecucion FALTA IMPLEMENTAR
        """        
        self.esLoop = esLoop    
        """ >>> Define si se sale por <<< o nos vale sólo para una ejecución...tb para definir mas adelante una última vuelta. 
        """
        self.pasos=0
        """ >>> Para las funciones recursivas Mystyca. Define las veces que se llama a la recursividad."""

        self.lst_menuXX=[]
        """ >>> Lista de objetos MenuDvd que mantiene un lst_item,  dicc_menu(num_n:[strMenu_n, func_n])  """

        self.lst_titulosXX=[]
        """ >>> Lista de titulos introducidos. Me permite validar rapido  """

        self.dicc_xgenx={}
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """

        self.respuestasValidas=[]
        """ >>> Listado de la pareja (menu_dvd, respuesta valida) """

        self.lstDicc_tit_rel_abs=[]
        """ lista de diccionarios item:[num_rel, num_val]"""
        
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # 1-AÑADE UN MENU AL GESTOR                                   (Crea un MenuDvd)
    def add(self, titulo, lst_item, lst_func=None):     
        """  Crea un Objeto MenuDvd"""
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_item=lst_item, lst_func=lst_func)
            # print(new_menu)
        except Exception as e:
            print(e)
            return None

        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)

        print(f'Load Menu {titulo} Ok ;)')
        return new_menu
    
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # 1-AÑADE UN MENU AL GESTOR                                   (Crea un MenuDvd)
    def addX(self, titulo, lst_Intro=None):             
        # ?????????????????????????????????????????????????????????????????????????
        lst_itemX, lst_funcX = self.valid_unpack(lst_Intro=lst_Intro)
        if not lst_itemX and not lst_funcX:
            print(f'Error:: Estructura NO Valida: {lst_Intro} ')
            print(f'.... Recuerda: (item) Tiene que ser un String y de momento sin repetidos y (funcion) se escribe sin los parentesis y None es un valor Válido ')                
            return None
        # ?????????????????????????????????????????????????????????????????????????

        """  """
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_item=lst_itemX, lst_func=lst_funcX)
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
            self.dicc_xgenx[titulo]=['-', '-']
            """ Es un puro Master!!!  """

        elif suPadre == None and indexInPadre!=None:
            self.dicc_xgenx[titulo]=['-', '-']            
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
    
    # ___________________________________________
    # ELIMINA REPETIDOS DE UNA LISTA USANDO SET....             (No usada)
    def lst_sin_repetidos(self, lst_to):
        """ Elimina los repetidos de la lista con un set """
        if isinstance(lst_to, list):
            set_lst_to=set(lst_to)
            lst_set = list(set_lst_to)
            return lst_set
        
    # _____________________________________
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def XlevelX(self, menuDvd, level=None):
        """ S U  1ª  V E Z  """
        if level==None:
            level = 0            
            lst_retorno=[]
            x_n = menuDvd.X__num
        level += 1
        print(f'MenuDvd: {menuDvd.titulo} - level: {level} ')
        """ 
        E M P E Z A M O S !!!! """
        lst_hijos = self.get_lst_dict_hijosX(titulo=menuDvd.titulo)        
        if lst_hijos: 
            for i in range(len(menuDvd.lst_item)):                
                menuDvd.style( X__num = x_n )
                menuDvd.style( X__num = menuDvd.get_TAB()*(level) + str(menuDvd.X__num) )
                print(menuDvd.get_strRow_Body(row=i, esNumerado=True))
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:
                        self.XindeX(menuDvd=hijo['menuDvd'], level=level)
                        menuDvd.style( X__num = x_n )
        else:
            if level==1: pass                # Entra la primera vuelta
            """ MUESTRA UN MENU DEL TIRON """
            menuDvd.style( X__num = menuDvd.get_TAB()*(level) + str(menuDvd.X__num) )
            print(menuDvd.FrankY(bCuerpo=True,  esNumerado=True))
            menuDvd.style( X__num = x_n )
        pass
    
    # 3-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # MUESTRA UN MENU.....................  LLAMADA EXTERNA   (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones)
    def Mystyca(self, titulo, withConfig=False, execFunc=False):    
        print('\nM Y S T Y C A')
        if self.validacion_show(titulo=titulo, withConfig=withConfig) == False : 
            return None
        # Cacha el Menu__________________________
        menu_dvd=self.get_menudvd(titulo=titulo)

        if withConfig==True and self.get_lst_dict_hijosX(titulo=menu_dvd.titulo):        #  PRINT SUB-MENUS 
            """ RECOGE DATOS """
            lst_columna= self.get_lst_columna_skin(menu_dvd=menu_dvd, columna=4)
            

            lst_menus_ord, lst_items , lst_nombres = self.Mystyca_Keys(menu_dvd=menu_dvd)
            self.ImprKeys(lst_menus_ord=lst_menus_ord , lst_items=lst_items , lst_nombres=lst_nombres)            

            lst_padres  = self.Mystyca_lst_padres(menu_dvd=menu_dvd)
            print('\nP A D R E S ')
            print(lst_padres)
            
            lst_eyes    = self.Mystyca_Eyes(menu_dvd=menu_dvd)            
            self.ImprEyes(lst_eyes=lst_eyes)
            # _________________________________   
            # GENERA 1ª MATRIZ DE IMPRESION. 
            lst_skin    = self.Mystyca_Skin(menu_dvd=menu_dvd)            
            # ________________________________
            # CAMBIA UN VALOR EN LA MATRIZ.
            """ 
            self.setV_skin(lst_skin=lst_skin, fila=1, columna=4, valor='dvd')
            """
            lst_prueba = [i for i in range(len(lst_columna))]
            """ 
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=lst_skin, columna=1, lst_newValues=lst_prueba)
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            Prueba para establecer toda una columna con los datos de una lista.(descomentar y ver resultado en ImprSkin)
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX """


            self.ImprSkin(lst_skin=lst_skin, numSP=12)
            
            lst_xgen    = self.Mystyca_XgenX(menu_dvd=menu_dvd)     
            self.ImprXgenX(lst_xgen=lst_xgen)
            """ Mystyca Mystyca Mystyca Mystyca Mystyca Mystyca """

            """ franky-franky-franky-franky franky franky franky franky franky franky franky franky """
            print(menu_dvd.FrankY(bSombrero=True, bCabeza=True, bCuello=True, esNumerado=True)) 
            # ==========================
            # IMPR DEL CUERPO DEL MENU
            for stock in lst_xgen:
                item_menu=stock[1]
                num_rel = stock[2]
                print( int(num_rel) * self.get_TAB() + item_menu )   


            # ???????????????????????????????????????????????????????????????????????????????
            # ???????????????????????????????????????????????????????????????????????????????
            """ Debo de conseguir la lista de las opciones validas """
            """ la lista de las opciones validas se a asigno a lst_skin con self.set_lst_columna_skin()"""
            """ la lista de opt validas es la que tiene que cachar pide_datos_usuario() para reconocer la opcion buena de la lista """
            """ en pide_datos_usuario: hay que poner una opcion '<' para que se repita el menu. mientras, sólo repetir la linea de 
                    pedir datos  
            """
            # ???????????????????????????????????????????????????????????????????????????????
            # ???????????????????????????????????????????????????????????????????????????????

            print('II')
            # Impr Cuerpo II ( el deseado )
            # for lstFila in lst_skin:
            #     print( int(lstFila[1]) * self.get_TAB() + lstFila[4] )
            """ 
            franky franky franky franky fra """
            print()
            print(menu_dvd.FrankY(bPie=True, bSalir=True)) 

            """ UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU """
            respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)   
            """ TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT """
            return self.Terminator(menu_dvd=menu_dvd, respuesta=respuesta, execFunc=execFunc)    # EJECUTAMOS O RETORNAMOS                           

        elif withConfig == False:            # MUESTRA UN MENU DEL TIRON            
            Mystyca_withOut(self, menu_dvd=menu_dvd, execFunc=execFunc)
        pass
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_Keys(self, menu_dvd, level=None, retorno=None, retorno2=None, retorno3=None):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[] ; self.pasos=0 ; retorno2=[]; retorno2=[]; retorno3=[]
        level += 1 ; self.pasos += 1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_item)):
                retorno.append(menu_dvd.titulo)
                retorno2.append(menu_dvd.get_item_row_body(i))
                retorno3.append(menu_dvd.get_numRltv_row_body(i))
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Keys(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno, retorno2=retorno2, retorno3=retorno3)
        elif not lst_hijos:
           for i, item in enumerate(menu_dvd.lst_item):
                retorno.append(menu_dvd.titulo)
                retorno2.append(menu_dvd.get_item_row_body(i))
                retorno3.append(menu_dvd.get_numRltv_row_body(i))
        # ___________________________________
        return retorno, retorno2, retorno3
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_lst_padres(self, menu_dvd, level=None, retorno=None, x_n=None, tituloMaster=None):
        if level==None and x_n==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; x_n = menu_dvd.X__num   ; retorno=[] ; self.pasos=0 ; tituloMaster=menu_dvd.titulo
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_item)):
                retorno.append(menu_dvd.get_item_row_body(row=i))                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_lst_padres(menu_dvd=hijo['menuDvd'] , level=level, tituloMaster=menu_dvd.titulo, retorno=retorno, x_n=x_n)
                    pass
        elif not lst_hijos:
           for i, item in enumerate(menu_dvd.lst_item):
                pass 
                # retorno.append()
                # retorno.append(menu_dvd.get_lst_row_body(row=i))
        return retorno

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_Eyes(self, menu_dvd, level=None, tituloMaster=None, retorno=None, ape=None):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[] ; self.pasos=0 ; tituloMaster=menu_dvd.titulo ; ape='' 
        level += 1 
        self.pasos+=1
        """ Contadores """
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)      
        """ Tengo al padre(menu_dvd, y a los hijos(lst_hijos)) 
        """  
        if  lst_hijos:         
            ape += str(level) + '.'
            for i in range(len(menu_dvd.lst_item)):
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))
                retorno.append((menu_dvd.get_item_row_body(i) , 
                                self.get_ind_en_padre(titulo=menu_dvd.titulo) ,
                                level, 
                                ape, 
                                menu_dvd.get_numRltv_row_body(i)
                                ))
                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Eyes(menu_dvd=hijo['menuDvd'] , level=level, tituloMaster=menu_dvd.titulo, retorno=retorno, ape=ape)
                    pass
        elif not lst_hijos:
            ape += str(level) + '.'
            aux = ape
            for i, item in enumerate(menu_dvd.lst_item):
                # retorno.append((menu_dvd.titulo , self.get_ind_en_padre(titulo=menu_dvd.titulo) , level, ape))
                # ape += str(level) + '.'
                retorno.append((menu_dvd.get_item_row_body(i) , 
                                self.get_ind_en_padre(titulo=menu_dvd.titulo) , 
                                level, 
                                ape, 
                                menu_dvd.get_numRltv_row_body(i)
                                ))
                # ape = str(level) + '.'
                ape = ''
                ape = aux
        return retorno 
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_Skin(self, menu_dvd, level=None, retorno=None):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ;  retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=False
            for i, item in enumerate(menu_dvd.lst_item):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
                # retorno.append(menu_dvd)
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Skin(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
        elif not lst_hijos:
            for i, item in enumerate(menu_dvd.lst_item):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
                # retorno.append(menu_dvd)
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))

        return retorno
    
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V   
    # -----------------------------------------------------------------------------------------------
    def Mystyca_XgenX(self, menu_dvd, level=None, retorno=None, tituloMaster=None):
        """ Recorre el arbol de Menus y devuelve un lst [nombreMenu, lista impresion, level, nombrePadre, indice_en_Padre]
        Usa principalmente lst_item y dicc_xgenx para """
        if level==None and  retorno==None:     # 1ª ENTRADA
            level=-1            
            retorno=[]
            self.pasos=0
            tituloMaster=menu_dvd.titulo
        level += 1
        self.pasos+=1
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=-1
            for i in range(len(menu_dvd.lst_item)):
                strFila=menu_dvd.get_strRow_Body(row=i, esNumerado=True)
                retorno.append((menu_dvd.titulo, 
                                strFila, 
                                level, 
                                self.get_padre(titulo=menu_dvd.titulo),  
                                self.get_ind_en_padre(titulo=menu_dvd.titulo)))
                # print(fila)
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_XgenX(menu_dvd=hijo['menuDvd'] , level=level, tituloMaster=menu_dvd.titulo, retorno=retorno)
        elif not lst_hijos:
            for i in range(len(menu_dvd.lst_item)):
                retorno.append((menu_dvd.titulo, 
                                menu_dvd.get_strRow_Body(row=i, esNumerado=True), 
                                level, 
                                self.get_padre(titulo=menu_dvd.titulo), 
                                self.get_ind_en_padre(titulo=menu_dvd.titulo)
                                ))
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))

        return retorno
    # _____________________________________
    # FROM nombre-titulo TO nombre-padre     
    def get_padre(self, titulo):
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo == tit: 
                    if padre_index[PADRE_IND.PADRE.value]:
                        return padre_index[PADRE_IND.PADRE.value]
                    else:
                        return None
    # __________________________________________
    # FROM nombre-titulo TO indice en el padre
    def get_ind_en_padre(self, titulo):
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo == tit: 
                    if padre_index[PADRE_IND.PADRE.value]:
                        return padre_index[PADRE_IND.INDEX.value]
                    else:
                        return None
    # ==============================================================================
    # SE EJECUTA Mystyca SIN CONFIGURACION.... MENU DE 1 NIVEL.
    # ==============================================================================
    def Mystyca_withOut(self, menu_dvd, execFunc):
        print(menu_dvd.FrankY(bSombrero=True, bCabeza=True, bCuelllo=True, esNumerado=True))
        
        for i in range(len(menu_dvd.lst_item)):
            print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))
        
        print(menu_dvd.FrankY(bSalir=True, bPie=True))
        respuesta = menu_dvd.pide_data_usuario(objMenu=menu_dvd)        
        return self.Terminator(menu_dvd=menu_dvd,  respuesta=respuesta, execFunc=execFunc )
    # ____________________________________
    # Llamada desde Mystyca. imprime una linea del 
    def print_row_Mystyca(self, menu_dvd, level, fila, esNumerado, x_n):
        menu_dvd.style( X__num = menu_dvd.get_TAB()*(level) + str(menu_dvd.X__num) )                    
        print(menu_dvd.get_strRow_Body(row=fila, esNumerado=esNumerado))
        menu_dvd.style( X__num = x_n )        
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
    def Show_All(self, menu_dvd , execFunc=False):                
        print(menu_dvd.FrankY(  bSombrero=True,
                                bCabeza=True,
                                bCuello=True,
                                bSalir=True,
                                bCuerpo=True, sNumerado=True, 
                                bPie=True))
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
    def get_lst_dict_hijosX(self, titulo):
        """ >>> LISTA CON MIS HIJOS DE PRIMERA GENERACION. Recorre el dicc_xgenx y recoge 
        [Retorno]: una lista de diccionarios con los datos sobre mis hijos en dicc_xgenx :
        (key):'titulo' (value):'titulo1'
        (key):'menuDvd' (value):(MenuDvd)menudvd_hijo
        (key):'padre' (value):'Menu_Titulos'
        (key):'ind_en_padre' (value): 2         (El lugar que ocupa en el padre)         
        """
        lst_hijos=[]
        for tit, padre_index in self.dicc_xgenx.items():
            if titulo == padre_index[PADRE_IND.PADRE.value]:
                menudvd_hijo = self.get_menudvd(titulo=tit)
                lst_hijos.append({  'titulo':tit,
                                    'menuDvd':menudvd_hijo, 
                                    'padre':titulo,
                                    'ind_en_padre':padre_index[PADRE_IND.INDEX.value]
                                })                
            pass
        pass    
        if lst_hijos: 
            return lst_hijos
        else: 
            return None        
    
    def ImprKeys(self, lst_menus_ord , lst_items, lst_nombres):
        print('\nM Y S T Y C A   K E Y S')
        for i in range(len(lst_menus_ord)):
            print(f'menu:{lst_menus_ord[i]} - item: {lst_items[i]} - nombre: {lst_nombres[i]} ')

    def ImprPadres(self):
        print('\nL S T _ P A D R E S ')
        lst_padres  = self.Mystyca_lst_padres(menu_dvd=menu_dvd)
        if not lst_padres: return ''
        for item in lst_padres:
            print(item , end=' | ')

    def ImprEyes(self, lst_eyes, numSP=16):
        print('\nM Y S T I C A   E Y E S   ')
        # menu_dvd=self.get_menudvd(titulo=titulo)
        # lst_eyes= self.Mystyca_Eyes(menu_dvd=menu_dvd)
        # =====================================================
        # Configura el formato ______________________
        lst_titulos=["-Item-", "-indeXPadre-", "-Level-", "-APE-", "levelRel"]
        self.igualarListas(listaKeys=lst_eyes, listaToReLong=lst_titulos, valorRelleno='-Loren-')
        formato_fila=''
        for i in range (len(lst_eyes[0])):
            formato_fila += "{:<" + str(numSP) + "}"    
        
        # Imprime titulos kernel ________________
        print(formato_fila.format(*lst_titulos))    
        print(f'{'-'*(len(lst_eyes[0])*numSP)}')
        # Imprime kernel ________________
        for lst_impr in lst_eyes:
            print(formato_fila.format(*lst_impr))
        pass

    def ImprSkin(self, lst_skin, numSP=16 ):
        print('\nM Y S T I C A   S K I N ')
        # =====================================================
        # Configura el formato ______________________
        lst_titulos=["-0-","-1-","-2-","-3-","-4-","-5-"]
        self.igualarListas(listaKeys=lst_skin, listaToReLong=lst_titulos, valorRelleno='-Loren-')
        formato_fila=''
        # for i in range (len(lst_titulos)):
        for i in range (len(lst_skin[0])):
            formato_fila += "{:<" + str(numSP) + "}"    
        # Imprime titulos kernel ________________
        print(formato_fila.format(*lst_titulos))    
        print(f'{'-'*(len(lst_skin[0])*numSP)}')   
        # Imprime kernel ________________
        for lst_impr in lst_skin:
            print(formato_fila.format(*lst_impr))
        pass    

    def ImprXgenX(self, lst_xgen, numSP=20):
        print('\nX G E N X   M Y S T I C A')
        
        # lst_XgenX=The_X_Men.Mystyca_XgenX(menu_dvd=Menu1)
        # =====================================================
        # Configura el formato ______________________
        lst_titulos=["YO", "Fila Print", "Level", "Padre", "1ª Apellido"]
        self.igualarListas(listaKeys=lst_xgen, listaToReLong=lst_titulos, valorRelleno='-Loren-')
        formato_fila=f''
        for i in range (len(lst_xgen[0])):
            formato_fila += "{:<" + str(numSP) + "}"    
        print(formato_fila.format(*lst_titulos))   
        print(f'{'-'*(len(lst_xgen[0])*numSP)}') 
        # Imprime lst_XgenX ____
        for lst_impr in lst_xgen:
            print(formato_fila.format(*lst_impr))
        pass
    # _____________________________________________________________________
    # OBTIENE UNA LISTA DE LOS VALORES DE LA COLUMNA PASADA en Mystyca-Skin.... DESDE 0.
    # Mystyca_Skin es una lista de lst_str <<lst_skin[fila][columna]>> Es una matriz.
    def get_lst_columna_skin(self, menu_dvd, columna):
        lst_skin    = self.Mystyca_Skin(menu_dvd=menu_dvd)
        # lst_rtrn = []
        # for fila in lst_skin:
        #     for i, col in enumerate(fila):
        #         if i == columna:
        #             lst_rtrn.append(col)
        #             break
        lst_rtrn=[ col  for fila in lst_skin for i, col in enumerate(fila) if i == columna]
        if lst_rtrn: return lst_rtrn

    # Pone valores de una lista en una columna.
    # .....para poner el nuevo indice en Mystyca_skin, que es la que se va a imprimir.
    # ......ese mismo nuevo indice es la numeracion absoluta que se tiene que checkear en Terminator.
    def set_lst_columna_skin(self, menu_dvd, lst_skin, columna, lst_newValues):
        # lst_skin    = self.Mystyca_Skin(menu_dvd=menu_dvd)
        lst_rtrn = []
        for i, lst_fila in enumerate(lst_skin):
            for j in range(len(lst_fila)):
                if j == columna:
                    lst_skin[i][j]=lst_newValues[i]
                    break        

    def setV_skin(self, lst_skin ,fila,  columna, valor):
        # lst_skin    = self.Mystyca_Skin(menu_dvd=menu_dvd)
        lst_rtrn = []
        for i, lst_fila in enumerate(lst_skin):
            for j in range(len(lst_fila)):
                if i == fila and j == columna:
                    lst_skin[i][j]=valor
                    return valor
                    
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