import copy

""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""

from enum import Enum as Column
class COL(Column):    
    SP_I =0 ;   A = 0      # Espacio Inicial
    X__NUM  =1; B = 1      # Pre-num
    NUM     =2; C = 2      # Num
    NUM__X  =3; D = 3      # Pos-num
    __TAB   =4; E = 4      # TAB
    X__ITEM =5; F = 5      # Pre-Item
    ITEM    =6; G = 6      # Item
    ITEM__X =7; H = 7      # Pos-Item
    SP_F    =8; I = 8      # Espacio Final

import string

class Tablero():
    """ crea una lista de diccionarios. Cada diccionario tiene 9 columnas. de la A a la I.
    Hay que generar tantas filas como sea necesareo rellenando el valor con None o con '' 
    Se tiene que poder acceder al tablero a una posicion [0][A] pejemplo para leer y escribir"""
    pass
    def __init__(self, num_total_columnas, num_total_filas = 10 , valor_inicial='-'):
        self.dicc_min = {letra: idx for idx, letra in enumerate(string.ascii_lowercase)}
        """ dict que tiene key:'a' value:0 , key:'b' value:1 ... """
        self.dicc_may = {letra: idx for idx, letra in enumerate(string.ascii_uppercase)}
        """ >>> dict que tiene key:'A' value:0 , key:'B' value:1 ... 
        Se puede acceder en cualquier momento de la clase y te devuelve el valor numerico de una letra
        >>>numCol=self.dict['C'] ; print(numCol) | Resultado >>> 3 """

        self.num_cols = num_total_columnas        
        self.num_fils = num_total_filas

        self.dicc_Cols = { f'{c}':' - ' for c in range(self.num_cols)}
        """ >>> dicc (key):numero_columna (value): '-'   X   num_cols (...de 0 a num_cols)"""

        self.tablero = [copy.deepcopy(self.dicc_Cols) for f in range(self.num_fils)]
        """ Aquí está el marco excel: Es una lista de diccionarios que conforman una fila. 
        self.tablero[2][3] => fila 2, columna 3 |  self.tablero[2][self.dicc_may['C']] => fila 2, columna 3
        """
        self.strformato = f''   #Para la impresion
        pass
        self.init_tablero(value=valor_inicial)
    
    def __str__(self):
        for dicc_fila in self.tablero:
            print(*dicc_fila)

    def init_tablero(self, value='-'):
        for i, lst_fila in enumerate(self.tablero):
            for j in range(self.num_cols):
                self.xls(i, j, value)
        self.impr_3()

    def reset(self, num_total_columnas, num_total_filas = 10 ):
        self.dicc_min={}
        self.dicc_may={}
        self.num_cols=0
        self.dicc_Cols={}
        self.tablero=[]

        self.dicc_min = {letra: idx for idx, letra in enumerate(string.ascii_lowercase)}
        self.dicc_may = {letra: idx for idx, letra in enumerate(string.ascii_uppercase)}

        self.num_cols = num_total_columnas        
        self.num_fils = num_total_filas
        self.dicc_Cols = { f'{c}':' - ' for c in range(self.num_cols)}   
        # un diccionario que es un número como key de un diccionario inicializado a ' - '

        self.tablero = [copy.deepcopy(self.dicc_Cols) for f in range(self.num_fils)]

    def xls(self, fil, col, valor=None):
        """ 
        VALIDACION FILA-COLUMNA """
        if not isinstance(col, int): 
            if isinstance(col, str): 
                col=self.from_Str_To_NumCol(col)
            if not isinstance(col, int): return None
        else:
            if  0 <= col < self.num_cols :
                pass
            else:
                return None
        # FILA
        if not isinstance(fil, int): return None
        0 > fil > self.num_fils
        if 0 > fil > self.num_fils:  return None
        """ 
        RECORREMEOS EL TABLERO """
        for i, dicc_fila in enumerate(self.tablero):
            if i == fil:
                if not valor==None:
                    dicc_fila[str(col)]=valor       # Pone un valor
                else:
                    return dicc_fila[str(col)]      # Devuelve un valor
        pass
        # 
        # Impresion de validacion
        # for i, dicc_fila in enumerate(self.tablero):
        #     print(dicc_fila)
    
    def from_Str_To_NumCol(self, letra):
        """ Entra una 'C' y sale un 3 """
        if self.valid_COL(columna=letra)==False: return None
        if letra in self.dicc_min:
            return self.dicc_min[letra]
        elif letra in self.dicc_may:
            return self.dicc_may[letra]
        else: 
            return None

    def __get_dicc_fila(self, fila):
        """ Devuelve el dicc que se corresponde con una fila en la list self.tablero """
        for f , dicc_cols in enumerate(self.tablero):
            if f == fila:
                return dicc_cols
    
    def get_lst_dicc_Rows(self, filaFrom, filaTo):
        if filaFrom > filaTo: 
            return None
        if  (0 > filaFrom > len(self.tablero)):
            return None
        lst_rango=[]
        for f, dicc_cols in enumerate(self.tablero):
            if  filaFrom <= f <=filaTo:
                lst_rango.append(dicc_cols)
        
        # print(lst_rango)
        return lst_rango
    # _____________________________________
    def get_lst_strV_Row(self, filaBusca):
        """ Obtiene una lista de str de values de self.tablero 
        """
        if not self.valid_ROW(fila=filaBusca): return None
        lst_rtrn=[]
        for f, dicc_cols in enumerate(self.tablero):
            if  f == filaBusca:
                return dicc_cols.values()       
    
    def from_numfila_To_lst(self, numfila):
        if self.valid_ROW(numfila)==False: return None
        dicc_fila = self.get_lst_dicc_Rows(numFila, numFila)
        if dicc_fila:
            lst_rtrn=[str(value) for key, value in dicc_fila ]
        print(lst_rtrn)
        return lst_rtrn
        pass
    # =============================
    # VALIDACIONES_________________
    def valid_ROW(self, fila):
        if self.valid_Form_fil==False: 
            return False
        else:
            if self.valid_Log_fil==False:
                return False
        return True
    def valid_COL(self, columna):
        if self.valid_Form_col==False: 
            return False
        else:
            if self.valid_Log_col==False:
                return False
        return True
    def valid_Form_fil(self, fila):
        """ Validacion en Fila: Solo vale int o str. Tiene que estar entre 0 y el numero de filas
        Retorno:  """
        try:
            fila=int(fila)
            return True            
        except Exception as e:
            print(e)
            return False
    def valid_Form_col(self, col):
        """ 
        VALIDACION COLUMNA En forma numerica o Letra. 
        REturn: False si error o el dato swap si Formato correcto en el limite adecuado."""
        if not isinstance(col, int): 
            if isinstance(col, str): 
                num_col=self.from_Str_To_NumCol(str(col).upper())
                if num_col:
                    return True
                else:
                    return False
            else: 
                return False
        else:
            if not isinstance(col, str): 
                return False
            else:
                return True
    def valid_Log_fil(self, fila):
        if 0 <= fila < len(self.tablero):                
            return True
        else:
            return False
    def valid_Log_col(self, num_col):
        if 0 <= num_col < self.num_cols:
            return True
        else:
            return False

    def from_Celda_To_RowCol(self, celda):
        """ >>> From 'C:4' To fila 4, columna 3 """
        if not isinstance(celda, str): return None
        lst_celda=celda.split(sep=':', maxsplit=-1)
        if not lst_celda: return None
        if len(lst_celda)!=2: return None
        if str(lst_celda[0]).strip().isdigit(): 
            fila    = lst_celda[0]
            columna = lst_celda[1]
        else:
            """ EMPIEZA CON COLUMNAS """
            columna = lst_celda[0]            
            fila    = lst_celda[1]

        if self.valid_Form_fil(fila=fila) == False: return None
        if self.valid_Form_col(columna=columna) == False: return None
        return fila, columna
    
    # IMPR_____________
    def impr_1(self):
        for i, dicc_fila in enumerate(self.tablero):
            print(dicc_fila)
    # IMPR_____________
    def impr_2(self, lst_rango=None):
        if lst_rango==None: lst_rango=self.tablero
        if not lst_rango or not isinstance(lst_rango, list):  return None

        for i, dicc_fila in enumerate(lst_rango):
            for col, valor in dicc_fila.items():
                if valor == '': 
                    impr_v = '-'
                else:
                    impr_v = valor

                print(f'{impr_v}', end='')
            print()
    # IMPR_____________
    def impr_3(self, numSP=5, fila=None ):
        # SE ESTABLECE LA CADENA STR DE FORMATO()
        strformato = self.getFormato(int_tamaño_columna=numSP)        
        if not isinstance(fila, int): return ':('
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if fila==None:
            for i in range(len(self.tablero)):
                lst_filas=self.get_lst_strV_Row(filaBusca=i)
                print(strformato.format(*lst_filas))
        else:
            for i in range(len(self.tablero)):
                if fila == i:
                    lst_filas=self.get_lst_strV_Row(filaBusca=i)
                    print(strformato.format(*lst_filas))
                    return
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    # FORMATO IMPR_____________
    def getFormato(self, int_tamaño_columna=5):        
        # -Se Basa en saber cuantas columnas quieres(listaTitulos) y formatear cada linea al formato generado dinamicamente.
        # >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  
        totalLen=0
        strformato=''
        for i in range (self.num_cols):
            strformato += "{:<" + str(int_tamaño_columna) + "}"
        # print(strformato)
        return strformato
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================          

class Rangos(Tablero):
    def __init__(self):
        self.rango = []
        self.lst_rango=[]
        pass
    def set_rango(self, celdaIni, celdaFin):
        pass

    def ini_rango(self, rango):
        pass

    def copy_rango(self, celdaIni, celdaFin):
        pass
    
    def paste_rango(self, lst_rango):
        pass
        return True

    

    
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================

SALIR='<<<'     #Cte para cuando se pide la opcion al usuario.



# ============================================================================================
# ============================================================================================
class MenuDvd():
    """ 
    Def: Define las partes esenciales de un menu Simple:  Head | Titulo | Cuello | Filas Body | Pie    
    Fila Body:  X_n__ | __n__ | __n_X | X_item__ | item | __item_X 

        HAY QUE INTEGRARLO CON TABLERO Y RANGO
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
    def __init__(self, titulo, lst_Intro, fraseHead=''):        
        # ___________________
        # RECOGE LOS VALORES
        self.titulo     = titulo                # El titulo e indice del menu. es la CABEZA

        self.lst_item, self.lst_func = self.valid_unpack(lst_Intro=lst_Intro)
        """ VALIDA LA ESTRUCTURA DE LISTAS Y DESEMPAQUETA LOS ITEMS Y LAS FUNCIONES 
        """
        if not self.lst_item and not self.lst_func:
            print(f'Error:: Estructura NO Valida: {lst_Intro} ')
            print(f'.... Recuerda: (item) Tiene que ser un String y de momento sin repetidos y (funcion) se escribe sin los parentesis y None es un valor Válido ')                
            return None
        # ______________________________________________________
        """ La Frase Que se pone en la Impresion del Menu: """
        if fraseHead=='':
            self.fraseHead=self.titulo
        else:
            self.fraseHead=fraseHead

        # ____________________________________________
        """ Before-After num    Before-After item  .... CACHA LAS CONSTANTES  """
        self.X__num    = MenuDvd.__OPT           # Lo que va BEFORE del Numero 
        self.num__X    = MenuDvd.NUM__X           # Lo que va AFTER del Numero
        self.X__item = MenuDvd.__TAB           # Lo que va BEFORE del Item
        self.item__X = MenuDvd.ITEM__X        # Lo que va AFTER del Item
        self.char_head  = MenuDvd.CHAR_HEAD     # 1º caracter que se repite num_char veces. es el SOMBRERO
        self.char_cuello= MenuDvd.CHAR_CUELLO   # 2º caracter que se repite num_char veces. es la PAJARITA 
        self.char_pie   = MenuDvd.CHAR_PIE      # 2º caracter que se repite num_char veces. es el ZAPATOS
        self.num_char   = MenuDvd.NUM_CHAR      # Numero de caracteres que hay de los char --------------
        
        # Texto Input ________________________
        self.introData = MenuDvd.STR_INTRO_DATA        
        self.dicc_sombrero, self.dicc_cabeza, self.dicc_cuello , self.dicc_pie = self.formar_entorno()
        """ GENERA:     SOMBRERO - CABEZA  - CUELLO - PIE .... SOLO FALTA EL CUERPO 
        """        
        self.lst_numeracion_rltv=[i for i in range(len(self.lst_item))]
        """ GENERA LA LISTA DE NUMERACION
        """
        # CARGA LAS LISTAS DE BEFORE-AFTER
        self.lst__X_num=[]           #Lista de los caracteres que van antes del Numero del item.
        self.lst__num_X=[]           #Lista de los caracteres que van depues del Numero del item.
        self.lst__X_item=[]     #Lista de los caracteres que van antes del Item
        self.lst__item_X=[]     #Lista de los caracteres que van Despues del Item        
        for i in range(len(self.lst_item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
    
        # __________________________________
        self.dicc_salir=self.get_dicc_row_Salir()        
        """ GENERACION DE LA LINEA DE SALIR  
        """                
        self.matriz_body=self.get_lst_dicc_cuerpo()
        """ >>> matriz posicional del cuerpo del menu objMenuXX.matriz_body[2]['num'] 
        """
        self.lst_dicc_Franky=[]
        """ >>> Matriz Con Todo Incluido: desde el sombrero hasta el pie.....para FranKy
        """
        self.lst_dicc_Franky.append(self.dicc_sombrero)
        self.lst_dicc_Franky.append(self.dicc_cabeza)
        self.lst_dicc_Franky.append(self.dicc_cuello)
        self.lst_dicc_Franky.append(self.dicc_salir)
        self.lst_dicc_Franky.append(self.matriz_body)
        self.lst_dicc_Franky.append(self.dicc_pie)
        # _____________________________
        # GENERACION DEL DICCIONARIO         
        val_dicc_menu={self.lst_numeracion_rltv[i]:tit_func  for i, tit_func in enumerate(self.lst_item)}                                          
        """>>> 1º ==> { 2 : ( 'Sales' , compraProd ) } ==> (2) numeracion ('Sales') titulo-menu (compraProd) funcion sin parentesis
        """        
        self.dicc_menu={self.titulo:val_dicc_menu}
        """ 2º ==> D I C C I O N A R I O R E S U L T A D O 
        >>> {'TituloMenu':  { 1: ( 'item_1' , func_item_1 ) } }   ==> Se genera 1 por Menu.
        >>> {               { 2: ( 'item_2' , func_item_2 ) } }   
        >>> {               { N: ( 'item_N' , func_item_N ) } }   """
        

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
        for i in range(len(self.lst_item)):
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
        sombrero= f'\n{ self.char_head * self.num_char }'
        cabeza= f'\n{self.fraseHead }'
        cuello= f'\n{self.char_cuello * self.num_char }'
        pie=    f'{self.char_pie*self.num_char}'

        
        dicc_sombrero={'spi': f'{''}' , 
                        'X__num':   f'\n{ self.char_head * self.num_char }', 
                        'num':f'{''}','num__X':f'{''}','tab':f'{''}','X__item':f'{''}','item':f'{''}','item__X':f'{''}',
                        'spf':f'{''}'
                        }
        dicc_cabeza={'spi': f'{''}' , 
                        'X__num':   f'\n{ self.fraseHead }', 
                        'num':f'{''}','num__X':f'{''}','tab':f'{''}','X__item':f'{''}','item':f'{''}','item__X':f'{''}',
                        'spf':f'{''}'
                        }
        dicc_cuello={'spi': f'{''}' , 
                        'X__num':   f'\n{ self.char_cuello * self.num_char }', 
                        'num':f'{''}','num__X':f'{''}','tab':f'{''}','X__item':f'{''}','item':f'{''}','item__X':f'{''}',
                        'spf':f'{''}'
                        }
        dicc_pie={'spi': f'{''}' , 
                        'X__num':   f'\n{ self.char_pie*self.num_char }', 
                        'num':f'{''}','num__X':f'{''}','tab':f'{''}','X__item':f'{''}','item':f'{''}','item__X':f'{''}',
                        'spf':f'{''}'
                        }

        # return sombrero, cabeza, cuello, pie
        return dicc_sombrero, dicc_cabeza, dicc_cuello, dicc_pie
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
    # MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM Matricial MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_str_row_body(self, row, esNumerado=True):
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
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_dicc_Row(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        # fila_menu=[]
        dicc_row={}
        if 0 <= row < len(self.lst_item):
            for i , item in enumerate(self.lst_item):            
                if i == row :
                    dicc_row={'spi':    f'', 
                              'X__num': f'{ self.lst__X_num[i]            if esNumerado==True else f'' }', 
                              'num':    f'{ self.lst_numeracion_rltv[i]       if esNumerado==True else f'' }' ,
                              'num__X': f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }' , 
                              'tab':    f'{self.__TAB}' , 
                              'X__item':f'{ str(self.lst__X_item[i])     if self.lst__X_item[i] else f'' }' , 
                              'item':   f'{ item                         if item else f'' }' , 
                              'item__X':f'{ str(self.lst__item_X[i])     if self.lst__item_X[i] else f'' }', 
                              'spf':    f''
                              }
                    # fila_menu.append ( dicc_row )                                                  
                    
                    return dicc_row
            pass
        pass
    # _______________________________________
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU con Tantas piezas como partes tenga la filaa.
    def get_lst_dicc_cuerpo(self):
        lst_matriz=[]
        for i  in range(len(self.lst_item)):            
            lst_matriz.append(self.get_dicc_Row(row=i, esNumerado=True))
        return lst_matriz
    # ___________________________
    def excel(self, fila=3, columna=COL.G):
        matriz_excel = self.get_lst_dicc_cuerpo()
        print(matriz_excel[fila][columna])
        return matriz_excel[fila][columna]
    # ___________________________
    def setV(self, fila, col, valor):
        matriz_excel[fila][col]=valor
    # ___________________________
    def get_num_filasX(self):
        return len(matriz_excel)
    # ___________________________
    def get_num_columnsX(self):
        return len(lst_matriz[0].keys())
    # ___________________________
    def __get_dicc_fila(self, fila):
        if 0 <=fila<len(matriz_excel):
            return matriz_excel[fila]
    # ___________________________
    def get_list_fila(self, fila):
        if 0 <=fila<len(matriz_excel):
            matriz_lst=[value for _ , value in matriz_excel[fila].items() ]
            return matriz_lst
    # ______________
    # FILA DE SALIR
    def get_dicc_row_Salir(self):
        dicc_row={'spi': f'', 
            'X__num': f'{''}', 
            'num':    f'{'<<<'}' ,
            'num__X': f'{''}' , 
            'tab':    f'{self.__TAB}' , 
            'X__item':f'{''}' , 
            'item':   f'{'Salir'}' , 
            'item__X':f'{''}', 
            'spf':    f'{''}'
            }
        return dicc_row
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
    def FrankY(self,bSombrero=False, bCabeza=False, bCuello= False, bSalir=False, bBody=False, bPie=False):
        self.lst_dicc_Franky

        lst_Franky=[]
        retorno = ''
        if bSombrero: lst_Franky.append( f'{self.sombrero}')
        if bCabeza: lst_Franky.append( f'{self.cabeza}' )
        if bSalir: lst_Franky.append( self.get_dicc_row_Salir() )       
        if bBody:   
            for i in range(len(self.lst_item)):
                lst_Franky.append(self.get_str_row_body(row=i, esNumerado=True))
        if bPie:    lst_Franky.append( self.pie )

        """ Juntamos todas las piezas reunidas """
        for i, parte_Franky in enumerate(lst_Franky):
            retorno += str(parte_Franky)
            retorno += '\n' if i<(len(lst_Franky)-1) else ''
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
    # ____________________________________
    # VALIDA LA ESTRUCTURA DE ENTRADA 
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
                        lst_FNC.append(funcion)
            else:
                return None, None
            
            return lst_ITM, lst_FNC
        except:
            return None, None
        pass

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================

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
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
class XindiceX(MenuDvd):
    
    def __init__(self):
        """ >>> Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        """        

        """ >>>  """
        self.lst_menuXX=[]
        """ >>> Lista de objetos MenuDvd que mantiene un lst_item,  dicc_menu(num_n:[strMenu_n, func_n])  """

        self.lst_titulosXX=[]
        """ >>> Lista de titulos introducidos. Me permite validar rapido  """

        self.dicc_xgenx={}
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """
    # 1-AÑADE UN MENU AL GESTOR                                   (Crea un MenuDvd)
    def add(self, titulo, lst_item, fraseHead=''):     
        """ SIN REPETIDOS.....en revisio """
        if titulo in self.lst_titulosXX: return False

        try:
            new_menu = MenuDvd(titulo=titulo, lst_Intro=lst_item, fraseHead=fraseHead)
            if new_menu.lst_item == None: return None
        except Exception as e:
            print(e)
            return None


        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)

        print(f'Load Menu {titulo} Ok ;)')
        return new_menu
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
    # RETORNA UN OBJ MENUDVD POR MEDIO DE SU TITULO             (obtiene el MenuDvd )
    def get_menudvd(self, titulo):
        """ >>> Retorna un objeto MenuDvd x su str titulo. """
        if titulo in self.lst_titulosXX:
            for menu in self.lst_menuXX:
                if str(menu.titulo) == str(titulo):
                    return menu
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
                                    'ind_en_padre':padre_index[PADRE_IND.INDEX.value]
                                })                
            pass
        pass    
        if lst_hijos: 
            return lst_hijos
        else: 
            return None        
    # DEVUELVE UN LIST DE HIJOS COMPROBANDO EN DICC_XGENX
    def get_lista_num_Valid():
        pass
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????
# CAMBIAR POR EL CODE DE CLASSMENUDVDX.PY ????????????????????????????????????????????????????????



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