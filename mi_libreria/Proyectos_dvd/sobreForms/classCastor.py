# Para hacer copias profundas de una lista
import os
import copy
from classPrinteX import PrinteX as PrntX
from enum import Enum as WHT
class What(WHT):
    VALOR=-1
    LIST=1
    TUPLE=2
    SET=3
    DICT=10
    ITRTR=1000


# ======================================= LISTAS DE ESTRUCTURAS DE PRUEBAS ==========================================
# ======================================= LISTAS DE ESTRUCTURAS DE PRUEBAS ==========================================
# ======================================= LISTAS DE ESTRUCTURAS DE PRUEBAS ==========================================
lst_0=[1,2,3]
lst_1=[4,5,6]
lst_2=[7,8,9]
# __________________________
# Lista de diccionarios(k)str(v)XXX  ..........(XXX Puede ser un Objeto)

# valor_1 = lst_X[1]['k1']
lst_A=[ {'k0':0}, {'k1':1}, {'k2':2 }]
lst_A=[ {'k0':0}, 
        {'k1':1}, 
        {'k2':2}    ]
# __________________________
# valor_list_1 = lst_X [1] ['k1']
lst_B=[ { 'k0':lst_0 }, { 'k1':lst_1 }, { 'k2':lst_2 } ]
lst_B=[ { 'k0':lst_0 }, 
        { 'k1':lst_1 }, 
        { 'k2':lst_2 }     ]
# valor_4(objeto)=lst_X[1]['k1'][1] 
lst_C=[ { 'k0':[1,2,3] }, { 'k1':[4,5,6] }, { 'k2':[7,8,9] } ]
lst_C=[ { 'k0':[1,2,3] }, 
        { 'k1':[4,5,6] },
        { 'k2':[7,8,9] }     ]

lst_D = [ {'id': 1, 'nombre': 'A', 'edad': 25},{'id': 2, 'nombre': 'B', 'edad': 30},{'id': 3, 'nombre': 'C', 'edad': 22} ]
lst_D = [   {'id': 1, 'nombre': 'A', 'edad': 25},
            {'id': 2, 'nombre': 'B', 'edad': 30},
            {'id': 3, 'nombre': 'C', 'edad': 22}        ]

lst_E = [  {'id': 1, 'nombre': 'A', 'tlf': [11, 111]},{'id': 2, 'nombre': 'B', 'tlf': [22, 222]},{'id': 3, 'nombre': 'C', 'tlf': [33, 333]}]
lst_E = [  {'id': 1, 'nombre': 'A', 'tlf': [11, 111]},
            {'id': 2, 'nombre': 'B', 'tlf': [22, 222]},
            {'id': 3, 'nombre': 'C', 'tlf': [33, 333]}        ]

# ................................list2=list-dict -dict
# Acceso a lst_1(list) = list( lst_X [1] ['k1'] ['vY'])
lst_U=[ { 'k0':{'vX':lst_0} }, { 'k1':{'vY':[lst_1]} }, { 'k2':{'vZ':[lst_2]} }  ]
lst_U=[ { 'k0':{'vX':lst_0} }, 
        { 'k1':{'vY':[lst_1]} }, 
        { 'k2':{'vZ':[lst_2]} }     ]

# ____________________________________________
"""     S E R I E -V-   DICCIONARIOS ENLAZADOS 
"""
lst_V=[ { 'k1':{'vX':[1,2,3]} }, { 'k1':{'vY':[4,5,6]} }, { 'k1':{'vZ':[7,8,9]} } , ... ]
lst_V = [
    {'k1': {'vX': [1, 2, 3]}},
    {'k2': {'vY': [4, 5, 6]}},
    {'k3': {'vZ': [7, 8, 9]}}   ]
""" 
>>> DEF:   """

lst_V_1 = [
    {'k1': {'vX': [1, 2, 3]}},
    {'k1': {'vX': [4, 5, 6]}},
    {'k1': {'vX': [7, 8, 9]}}   ]
""" 
>>> DEF:   """

lst_V_2 = [
    {'k1': {'vA': [1, 2, 3]}},
    {'k1': {'vB': [4, 5, 6]}},
    {'k1': {'vB': [7, 8, 9]}}   ]
""" 
>>> DEF:   """

lst_V_3 = [
    {'k1': {'vA': [1, 2, 3]}},
    {'k1': {'vB': [4, 5, 6]}},
    {'k1': {'vC': [7, 8, 9]}}   ]
""" 
>>> DEF:   """


# ___________________________________________________________________
"""     S E R I E -X- VEGETAL CON POLLO
"""
lst_X = [
    {'k1': [ { 'vX': [1, 2, 3] } , ['v3', 'v4'] ] },
    {'k2': [ { 'vY': [4, 5, 6] } , 'v3'       ] },
    {'k3': [ { 'vZ': [7, 8, 9] }            ] }
    ]
lst_X_01 = [
    {'k1': [{'vX':[1,2,3]},[6,9]]},
    {'k2': [{'vY':[4,{'km':8},5]},7]},
    {'k3':9}
    ]
""" 
>>> DEF: Esto me suena a   xml  a   json a  filas(dicc) y column(Itrtr)   """

# ??????????????????????????????????????????????????????????????????????????????????????????????????????
# ??????????????????????????????????????????????????????????????????????????????????????????????????????


# _____________________________________________________________________
""" S E R I E -TX-   T A X O N O M I A ==> 1 LISTA con 3 DICT enlazados

En si mismas son  estructuras SI LE DAMOS UN SENTIDO ;)
>>> [lst_Y] , es la misma estructura repetida 3 veces, a partir de ahí......
"""
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
lst_TAX = [
    {'k1':{'xA':{'k2':['v1','v2','v3']}}},  
    {'k1':{'xA':{'k2':['v4','v5','v6']}}},  
    {'k1':{'xA':{'k2':['v7','v8','v9']}}}   ]
""" 
>>> DEF: || Tipo (k1) || Sub-Tipo-1(xA) || Sub-Tipo-2 (k2) ..... VALOR
... un mismo individuo, diferentes casos. Estructura repetida."""

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
lst_TAX_0 = [
    {'k1':{'xA':{'k2':['v1','v2','v3']}}},  
    {'k1':{'xA':{'k3':['v4','v5','v6']}}},  
    {'k1':{'xA':{'k4':['v7','v8','v9']}}}   ]
"""
>>> DEF: || Tipo (k1) || Sub-Tipo(xA) || Categoria(k2,k3,k4) || VALOR """

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
lst_TAX_1 = [
    {'k1':{'vA':{'k4':['v1','v2','v3']}}},  
    {'k1':{'vB':{'k5':['v4','v5','v6']}}},  
    {'k1':{'vC':{'k6':['v7','v8','v9']}}}   ]
"""
>>> DEF: || Tipo (k1) || Sub-Tipo(xA) || Categoria(k2,k3,k4) || VALOR """

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
lst_TAX_2 = [
    {'k1':{'vA':{'k4':['v1','v2','v3']}}},  
    {'k2':{'vB':{'k4':['v4','v5','v6']}}},  
    {'k2':{'vC':{'k6':['v7','v8','v9']}}}   ]
"""
>>> DEF: ||  ||  ||  || VALOR """

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
lst_TAX_3 = [
    {'k1':{'vA':{'k4':['v1','v2','v3']}}},  
    {'k2':{'vB':{'k5':['v4','v5','v6']}}},  
    {'k3':{'vC':{'k6':['v7','v8','v9']}}}   ]
"""
>>> DEF: ||  ||  ||  || VALOR """


# _____________________________________________________________________
"""
 S E R I E -TX-   T A X O N O M I A ==> 1 LISTA con 3 DICT enlazados
"""

# valor_24(objeto) = lst_X [2] ['k1'] ['vZ'] ['sub2'] [0]
lst_Z = [
    {'k1': {'vX': {'sub1': [1, 2, 3], 'sub2': [18, 19, 20]}}},  # Subtipo vX con sub-subtipos sub1 y sub2
    {'k1': {'vY': {'sub1': [4, 5, 6], 'sub2': [21, 22, 23]}}},  # Subtipo vY con sub-subtipos sub1 y sub2
    {'k1': {'vZ': {'sub1': [7, 8, 9]}}}   ]

# ==========================================================================
# CLASE  CAJAS de KARLOS - Castor(): 
# Cacha Estructuras de datos y las cataloga y diferencia de los datos 
# ==========================================================================
class Castor(): 
    """ 
    >>> Ejemplo Uso:
    >>> listaEstructura=[
            ["c:0", ["f:0","f:1","f:3"]], 
            ["c:1", "c:3"], 
            ["c:2"]
        ]
    SttK=CajasEspejo(listaEstructura=__lst_Castor)
    """
    TAB='  '    #Lo uso para formato
    def __init__(self, listaEstructura):
        # print()
        self.__lst_Castor = listaEstructura        
        # print(self.__lst_Castor)
        """ >>> Lista PPAL de la Clase. 
        >>> Contiene la Estructura de Entrada. 
        >>> De esta variable salen todas las demás.
        """        
        os.system('cls')
        """ 
        ('L E V E L ') """
        self.num_iterators=0
        """ >>> Contador dedicado a las funcion recursiva level. Contadores de Pasos de Iteradores """
        self.num_dicc=0        
        """ >>> Contadores dedicado a las funcion recursiva level. Contadores de Pasos de Diccionarios """

        self.niveles=self.level(self.__lst_Castor)
        """ >>> Profundidad en __lst_Castor.        """
        print('\n\nRetorno Level(): ')
        print(self.niveles)

        # ___________________        
        print("\nC O P I A   P R O F U N D A (self.lst_copy_lst_Castor)")
        self.__copy_lst_Castor=copy.deepcopy(self.__lst_Castor)
        print(self.__copy_lst_Castor)
        """ >>> Copia profunda de self.__lst_Castor.  import copy
        """        
        print('\nL I S T A _ K E Y S V A L U E S ')
        self.lst_keysValues=[]
        """ >>> Lista de str. Lista PLANA de los datos de self.__lst_Castor. 
        Es la Base de todos los elementos que hay en la self.__lst_Castor         """
        self.lst_keysValues=self.get_lst_keysValues(elemento=self.__lst_Castor)        
        print('\nRetorno de lst_keyValues:')
        self.toPrint(lstlst_valores=self.lst_keysValues,lst_width_colum=[20, 20, 20], lst_head=['Item','esValue?','Paso'])  
        
        print('\nD I C C   E S T R U C T U R A')
        self.dictEstructura={}
        # self.dictEstructura={key:self.getPosicion_ByObj(lista=listaEstructura, objBuscado=str(key)) for key in self.lst_keysValues}        
        """ >>> Diccionario de key(lst_keysValues) pejm 'c:3' , value(posicion en formato lista, pejem [1,0,0,3]) """
        print(self.dictEstructura)
        # ______________________
        # self.dictEstructura={key:self.getPosicion_ByObj(lista=__lst_Castor, objBuscado=str(key)) for key in self.lst_keysValues}        
        print('\nV A L I D   A P P   C O D E ')
        self.lst_valid_char=['c', 'f']
        """ >>> lista de los caracteres válidos para la aplicacion enfileitor. 
        ...Para otro tipo de uso hay que actualizar este valor con getters and setters
        """
        print(self.lst_valid_char)

        
        print('D I C C   D A T A')
        # self.dicc_data_rcsv=self.getData_RCSV(self.__lst_Castor)
        """ >>> DICCIONARIO DE DATOS TOTAL de self.__lst_Castor.
        Ya se puede sacar todo de aquí!! 
        """       
        pass
        
        # 'CONTADORES DE PASOS DE RECURSIVIDAD'
        self.paso=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.BaseRCSV(). Funcion Recursiva. No hace nada, es el ppio.   """
        self.cuentaRcsvImpr=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.get_lst_dataStr(). Funcion Recursiva. 
        >>> self.get_lst_dataStr() da una lista de str. En deshuso. Cambiada por self.imprDiccDATA()
        """
        self.cuentaRcsvDicc=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.getData_RCSV(). Funcion Recursiva.  """
        pass
        self.elemento_copy=[]
        """ >>> es un elemento que se usa de momento en self.level_basic_2()
        Sirve par hacer tareas de copia segura para control de la recursividad.
        """
        pass

     # ____________________
    # PARA IMPRIMIR TODOS LOS DATOS DE LA CLASE....FALTA COMPLETAR.
    def __str__(self):
        tit=f'\n{'*'*30} IMPRIMIR DATOS CajasEspejo {'*'*30}'
        uno=f'Numero de Items: {self.numFilas}'
        dos=f'Estructura: {self.__lst_Castor}'
        tres=f'lst_keysValues: {self.lst_keysValues}'
        siete=f'__copy_lst_Castor: {self.__copy_lst_Castor}'
        cuatro=f'Diccionario (key):(posicionEstruct): \n{self.dictEstructura}'
        cinco=f'Numero de listas internas: {self.num_iterators}'
        seis=''
        for i, item in enumerate(self.__lst_Castor):
            seis=seis+(f'item {i}: {item}\n')
        fin=f'{'='*90}'
        return '\n'+tit+'\n'+uno+'\n'+dos+'\n\n'+tres+'\n'+siete+'\n'+cuatro+'\n'+cinco+'\n'+seis+'\n'+fin

    def get_lst_Castor(self):
        return self.__lst_Castor
    def set_lst_Castor(self, newListaEstructura):        
        self.__init__(newListaEstructura)
        return self.__lst_Castor

    # # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR >
    # BASE RECURSIVA(No usada).... L o   p r i m e r o ,   f u e   e l   V E R B O 
    # # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR >
    def  BaseRCSV(self, item, cuenta=None):        
        """ 
        Base para Recorrer Toda la Lista Recursivamente!!!!!
        identifica el tipo list o str, key de lst_keysValues
        Aquí tengo un contador global (self.paso) dedicado y un (cuenta) de ejemplo
        [item] es una lista de algo o algo de algo.
        [cuenta] indica el nivel de profundidad desde la lista inicial(item)
        
        """
        if cuenta==None: 
            cuenta=0        
            self.paso=0

        self.paso +=1
        cuenta +=1
        # ________________    
        if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            for subList in item:
                self.BaseRCSV(subList, cuenta)        
        elif isinstance(item, dict):
            for key, value in item.items():
                self.BaseRCSV(value, cuenta)
        else:            
            print(f'Item: {item} - cuenta: {cuenta} - Contador: {self.paso}')
    
    # # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # LISTA DE DICCIONARIO DE DATOS...sobre la Base Recursiva
    def getData_RCSV(self, item, level=None, retorno=None):        
        """ 
        -Usa la Base para Recorrer Toda la Lista Recursivamente!!!!!
        [item]: Es la Lista a Recorrer Recursivamente. self.__lst_Castor, pero puede ser cualquiera.
        [level]: NO INTRODUCIR EN LA LLAMADA A LA FUNCION. Sirve para calcular el nivel de profundidad, 
        [retorno]: NO INTRODUCIR EN LA LLAMADA A LA FUNCION. Lista de diccionarios (k):keyStrucTK  (v):level, cuentaRecursiva, listaPosicion, 2 primeras cooordenadas, 2 últimas coordenadas, FilaAbsolua , Fila/Columna Relativa. 
        """
        # _____________________________
        # Inicializo los parametros de entrada. IMPORTANTE!!: No values en la llamada
        if level==None: 
            level=0        
            self.cuentaRcsvDicc=0
        if retorno==None: retorno=[]

        self.cuentaRcsvDicc+=1
        if isinstance(item, list):
            level+=1
            for subList in item:
                self.getData_RCSV(item=subList, level=level, retorno=retorno)
        else:
            # _____________________
            # Cojo Datos:
            polposition=self.getPosicion_ByObj(str(item))
            if not polposition: 
                return None
            coord1=polposition[0]
            coord2=polposition[1]
            # _____________________
            # Dos últimas coordenadas
            coord3=polposition[-2]
            coord4=polposition[-1]
            # _____________________
            # OBTIENE EL VALOR DEL ELEMENTO EN __copy_lst_Castor
            valor_item=self.getValue(datoBusca=str(item))
            # _____________________
            # Imprime los datos de las Vueltas que va Dando
            printitem = (f'Item: {item} - Level: {level} - Contador: {self.cuentaRcsvDicc}')
            print_posicion=(f'- Posicion: {polposition}')
            fila_columna=(f' - Fila Abs: {coord1} - coord2: {coord2} - pre-last: {coord3} - last: {coord4} - valor: {valor_item}')
            # print(printitem+print_posicion+fila_columna)
            # _____________________
            # Creo el diccionario con los datos recogidos
            # diccRetorno={str(item):[level, self.cuentaRcsvDicc, polposition, coord1, coord2, coord3, coord4, valor_item]}
            diccRetorno={str(item):[level, self.cuentaRcsvDicc, polposition, coord1, coord2, coord3, coord4, valor_item]}
            # _____________________
            # Añado el diccionoario a la lista retorno
            retorno.append(diccRetorno)

        return retorno
    # ===============================
    # GET lst_keysValues
    def getListaPlana_ByEstructura(self, lista):
        """ 
        Def: Genera una lista de str con todos los elemntos de la lista pasada.
        Es una funcion recursiva: Se basa en que si elemento es str se añade a una lista de retorno,
        y si es lista, el resultado la tiene que añadir(extend), pero la recorre llamandose a si misma.

        Va recorriendo item por item encontrando elemento por elemento.
        """
        resultado = []  # Lista para almacenar todos los elementos

        for elemento in lista:
            if isinstance(elemento, list):
                # Llamada recursiva para aplanar la sublista y extender el resultado
                resultado.extend(self.getListaPlana_ByEstructura(elemento))
            else:
                # Añadir elementos que no son listas directamente a resultado
                resultado.append(elemento)

        return resultado
    
    # ===============================
    # RETORNA UN VALOR DE self.__copy_lst_Castor por una keyStrucTK o indice
    def getValue(self, datoBusca):
        """ 
        [datoBusca]: puede ser: (1-)Un keyStrucTK  (2-)Un indice leido de izquierda a derecha en lst_keysValues
        >>> Retorno: (1-)un VALOR de self.__copy_lst_Castor (2-)None si no Encuentra Nada.
        >>> ejemplo: (1-)getValue("c:3") (2-)getValue(5)
        """
        if isinstance(datoBusca, int):            
            if 0<=datoBusca<=len(self.lst_keysValues):
                keyStrtk=self.lst_keysValues[datoBusca]
                """>>> Si me pasa un indice, se busca 1º en self.lst_keysValues el nombre de la keyStrtk('c:x')
                """
                posicion_busca=self.dictEstructura.get([keyStrtk], None)
            else:
                return None
            pass
        elif isinstance(datoBusca, str):            
            if datoBusca in self.dictEstructura:
                posicion_busca=self.dictEstructura[datoBusca]
            else:
                return None
        # posicion_busca=self.dictEstructura.get([datoBusca], None)
        valor_busca=self.getItem_ByPosicion(lista=self.__copy_lst_Castor, posicion=posicion_busca)
        return valor_busca
    
    # ===============================
    # CALCULA EL NIVEL DE PROFUNDIDAD EN self.__lst_Castor.
    def level(self, elemento):
        """ 
        >>> Def: primer filtro hacia la tripa de la estructura (self.level_XX).      
        [elemento] en la llamada = self.__lst_Castor. 
        <item> puede ser un ITERADOR o un NO ITERADOR 
        """
        self.num_iterators=0
        self.num_dicc=0
        retorno_rcrsv=[]
        if isinstance(elemento, dict):
            print(f"{'-'*15}Ini Arbol Diccionario--")
            
            for key, valor_dicc in elemento.items():
                # ____________________________________________________
                retorno_rcrsv=self.level_XX(elemento=valor_dicc)            
                print(f'keyPpal= {key}  - Rcrsv return =  {retorno_rcrsv} ')

            print(f'{'-'*15} Fin Arbol Diccionario')

        elif isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):            
            """ 
            PRUEBAS DE RECURSIVIDAD....ES UN PROCESO. PARTO DE opt_1 y voy avanzando.... dejo el proceso.
            """
            print(f"{'-'*15}INI  Proceso R C R S V ... iterador list ... L E V E L()\n")

            # for i,item in enumerate(elemento):
            # retorno_rcrsv.append(self.level_XX(elemento=item))
            """ opt_1-TRATO LAS FILAS(APPEND) Y GESTIONO EL RESULTADO  """
            # retorno_rcrsv=self.level_XX(elemento=elemento)                    
            """ opt_2-LE PASO TODO EL ELEMENTO ENTERO Y RECOJO EL RESULTADO. """
            # retorno_rcrsv=self.level_XX_01(elemento=elemento)            
            """ opt_3-VISITA LEVE PARA  VER   I T E R A C I O N E S """
            # retorno_rcrsv=self.level_XX_02(elemento=elemento)
            """ opt_4-VISITA LEVE AMPLIADA """
            # retorno_rcrsv=self.level_XX_03(elemento=elemento)
            """ opt_5-VISITA LEVE AMPLIADA PLUS"""
            # retorno_rcrsv=self.level_BB(elemento=elemento)
            """ opt_5-VISITA LEVE AMPLIADA PLUS"""
            # retorno_rcrsv=self.level_XX_04(elemento=elemento)
            """ opt_6-VISITA FORMATEADA """
            # retorno_rcrsv=self.level_XX_05(elemento=elemento)
            """ opt_7-VISITA FORMATEADA Y MULTIRETORNO """
            retorno_rcrsv=self.level_XX_clean(elemento=elemento)
            """ opt_7-VISITA FORMATEADA Y MULTIRETORNO """
            
            print(f'\n{'-'*15} FIN  Proceso R C R S V .... iterador list ... L E V E L()')
            
            if retorno_rcrsv:
                print(f'Resumen Global del Retorno:::: len: {len(retorno_rcrsv)} - vueltas: {self.paso} - num_dicc: {self.num_dicc} - num_itrtr= {self.num_iterators} ')
            pass
        else:
            print(""" Error de datos.... 
            Msg: Aqui no se pueden meter cualquier dato, solo Iteradores y diccionarios
            Accion: Inicializar y retorno_rcrsv """)
            return None

        # retorno_rcrsv=self.num_dicc
        return retorno_rcrsv

        print('----------- F I N   L E V E L ')

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # CALCULA EL NIVEL DE PROFUNDIDAD EN __lst_Castor.
    def level_XX(self, elemento, cuenta=None, retorno=None):
        """ 
        >>> Def: Funcion Recursiva, Que cuenta el numero de listas que hay en una lista pasada.        
        [elemento] en la llamada = self.__lst_Castor. 
        <item> puede ser un ITERADOR o un NO ITERADOR     """
        # _______________________
        # Pasa sólo la 1ª VUELTA(Inicialización)
        if cuenta==None and retorno==None:
            cuenta=0 
            retorno=[]
            if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):
                self.num_iterators +=1    #cuenta el numero de iteradores list, set, tuple
                # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                # retorno.append(self.level_XX(elemento, cuenta))                
                retorno.append(['lista', elemento, self.num_iterators])
                print(elemento)

            elif isinstance(elemento, dict):
                self.num_dicc +=1
                lista_par = elemento.items()
                # 0=key y 1=valor
                for par in lista_par():
                    par[0]  #key
                    par[1]  #valor
                    retorno.append( ['key'+par[0], par[1] , self.num_dicc] )
                    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    print(f'\nkey: {par[0]}  \t value: {par[1]} \t num-dicc: {self.num_dicc} ')
                
                print('Fin Lista-Par')
            else:
                print(f' valor = {elemento} ')
                retorno.append([elemento, self.num_dicc, self.num_iterators])
                return retorno
        # _______________________
        # Empezamos!!!!!!!!!!!!!!
        cuenta +=1
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # Vuelta 1+n
        for item in elemento:
            if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
                self.num_iterators += 1        
                retorno.append(['lista', elemento, self.num_iterators])
                # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                self.level_XX(elemento=item, cuenta=cuenta, retorno=retorno)

            elif isinstance(item, dict):
                self.num_dicc += 1                
                lista_par = elemento.items()
                # 0=key y 1=valor
                for par in lista_par():
                    par[0]  #key
                    par[1]  #valor
                    retorno.append( [par[0], par[1] , self.num_dicc] ) 
                    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    self.level_XX(elemento=par[1], cuenta=cuenta, retorno=retorno)
            else:
                retorno.append([elemento, self.num_dicc, self.num_iterators])
                print(f'valor = {item} cuenta: {cuenta} - num_itrtrs: {self.num_iterators} - num_dicc: {self.num_dicc} ')
        
        print('FIN Itrdr')        
        return retorno
    
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva Básica para hacer pruebas de recorrido 
    def level_XX_01(self, elemento, cuenta=None, retorno=None):
        if cuenta==None and retorno==None:
            cuenta=0
            retorno=[]
        cuenta+=1
        if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) or isinstance(elemento, dict):
            print(f'ITERADOR {elemento}\t...CUENTA: {cuenta} ')
            for item in elemento:
                retorno.append(type(item))
                self.level_XX_01(elemento=item, cuenta=cuenta, retorno=retorno)
        else:
            retorno.append(elemento)
        pass
        print(f'RETORNO(itera_tot o valor):  VALOR: {elemento} \t...CUENTA= {cuenta}')
        return retorno

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 2
    def level_XX_02(self, elemento, cuenta=None, retorno=None):
        """ Def: Recorre Recursivamente la Estructura.....evolucion de level_XX_01
        >>> [elemento]: Itrtr/Val. La primera vez es la Estructura.
        >>> [cuenta]: NO INTRO. Cuenta el nivel interno de iteracion.
        >>> [retorno]: NO INTRO. list para guardar lo que se quiera. en este caso se guarda el tipo/valor de elemento.
        >>> [globals]: self.elemento_copy, lista xa copia. (podría ser local como retorno.)
        >>> [globals]: self.num_iterators, numero de Itrtr de la Estructura.
        >>> [globals]: self.num_dicc , Numero de diccionarios encontrados en la Estructura.
        """        
        if cuenta==None and retorno==None:
            cuenta=0
            retorno=[] 
            self.elemento_copy=elemento           
            # self.elemento_copy=copy.deepcopy(elemento)
            self.paso=0
        cuenta+=1
        self.paso+=1

        if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) or isinstance(elemento, dict):
            print(f'{'_'*80}\n ITERADOR', end='....')            
            """ 
            Add From: Diferencia entre iterador y diccionario            """
            if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):
                self.num_iterators +=1
                print(f'LIST: {elemento} ...CUENTA: ( {cuenta} ) ...desde la 1ª')                
            
            elif isinstance(elemento, dict):
                self.num_dicc +=1
                print(f'DICT: {elemento} ...CUENTA: ( {cuenta} ) ...desde la 1ª')
                # ____________________________
                lst_pares = elemento.items()                                
                """ >>> Def: Obtengo la lista de pares (clave,valor) """
                
                # Recorro cada par del diccionario. par[0]=keys, par[1]=values
                for pares in lst_pares:
                    """ >>> El   S I G  P A S O   H A C I A  level_basic_3 es el desarrollo de pares[1], 
                    haciendo una 2ª llamada a la recursividad. 
                    """
                    print(f'{'\t'*(cuenta-1)}key: {pares[0]} - value: {pares[1]} ')
            """ 
            Add Tooooooooooooooooooooooooooooooooooooooooooooooooooooo   """
            for item in elemento:
                retorno.append( type(item) )
                self.level_XX_02(elemento=item, cuenta=cuenta, retorno=retorno)           
        else:
            print(f'{'\t'*(cuenta-1)}VALOR: {elemento} \t\t...CUENTA: ( {cuenta} ) ...desde la 1ª')
            retorno.append(elemento)
        pass
        if elemento==self.elemento_copy:
            print('\n.............. ULTIMA VUELTA....aqui, codigo antes de retornar a level()')
        print(f'{'(==)'*(cuenta)}RETORNO(Itrtr/Val) {elemento} \tde...CUENTA= {cuenta}')            
        
        return retorno
    
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 3
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def level_XX_03(self, elemento, cuenta=None, retorno=None):
        """ Def: Recorre Recursivamente la Estructura.....evolucion de level_XX_01
        >>> [elemento]: Itrtr/Val. La primera vez es la Estructura.
        >>> [cuenta]: NO INTRO. Cuenta el nivel interno de iteracion.
        >>> [retorno]: NO INTRO. list para guardar lo que se quiera. en este caso se guarda el tipo/valor de elemento.
        >>> [globals]: self.elemento_copy, lista xa copia... (podría ser local como retorno.)
        >>> [globals]: self.num_iterators, numero de Itrtr de la Estructura.
        >>> [globals]: self.num_dicc , Numero de diccionarios encontrados en la Estructura.
        """        
        if cuenta==None and retorno==None:
            cuenta=0
            retorno=[] 
            self.elemento_copy=elemento           
            self.paso=0
        cuenta+=1
        self.paso+=1        

        if  (isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) or 
            isinstance(elemento, dict)):

            print(f'{'_'*80}\n ITERADOR', end='....')

            if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):
                """  
                I T R T R  """
                self.num_iterators +=1
                print(f'LIST: {elemento} ...CUENTA: ( {cuenta} ) ...FROM 1ª')                
            
            elif isinstance(elemento, dict):
                """ 
                D I C C I O N A R I O  """
                self.num_dicc +=1
                print(f'DICT: {elemento} ...CUENTA: ( {cuenta} ) ...FROM 1ª')
                # ____________________________
                lst_pares = elemento.items()                                
                """ >>> Def: Obtengo la lista de pares (clave,valor) """
                
                # Recorro cada par del diccionario. par[0]=keys, par[1]=values
                for pares in lst_pares:                    
                    """ 
                    Add From: Cuando nos encontramos con un Diccionario....profundizamos un poco mas y podremos ver toda la estructura:
                    -pares[1] simboliza el valor de la key de un diccionario.
                    -Hecho así por si me conviene hacer un paso previo de convertir a lista el par de tuplas de items()"""
                    print(f'{'\t'*(cuenta-1)}key: {pares[0]} - value: {pares[1]} ')

                    valor_dicc=pares[1]
                    if (isinstance(valor_dicc, list) or isinstance(valor_dicc, tuple) or 
                        isinstance(valor_dicc, set) or isinstance(valor_dicc, dict) ): 

                        retorno.append(type(valor_dicc))
                        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        self.level_XX_03(elemento=valor_dicc, cuenta=cuenta, retorno=retorno)
                        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                    else:
                        print(f'{'\t'*(cuenta-1)}VALOR_D: {elemento} \t\t...CUENTA: ( {cuenta} ) ...FROM 1ª')
                        retorno.append(elemento)                    
                    pass
                    
                    """ 
                    Add Tooooooooooooooooooooooooooooooooooooooooooooooooooooo

                    >>> El   S I G   P A S O   H A C I A  level_basic_4 es FORMATEAR UNA SALIDA
                    Utilizado para ver bien los datos impresos. (format.)
                    >>> strformato += "{:<" + str(num) + "}"     =>XXX
                    >>> print(self.strformato.format(contenido en misma XXX que strformato))  
                    >>> ... y añadir el contador de pasos general self.paso"""
                    pass
                pass
            pass
            for item in elemento:
                retorno.append( type(item) )
                # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                self.level_XX_03(elemento=item, cuenta=cuenta, retorno=retorno)           
                # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            pass
        else:
            # print(f'{'\t'*(cuenta-1)}VALOR: {elemento} \t\t...CUENTA: ( {cuenta} ) ...desde la 1ª')
            print(f'{'\t'}VALOR: {elemento} \t\t...CUENTA: ( {cuenta} ) ...desde la 1ª')
            retorno.append(elemento)
        pass
        
        
        if elemento==self.elemento_copy:
            print('\n.............. ULTIMA VUELTA....aqui, codigo antes de retornar a level()')
        print(f'{'(==)'*(cuenta)}RETORNO(Itrtr/Val) {elemento} \tde...CUENTA= {cuenta}')
            
        return retorno

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 4
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def level_XX_04(self, elemento, cuenta=None, lst_return_type=None):
        """ Def: Recorre Recursivamente la Estructura.....SALIDA FORMATEADA
        >>> [elemento]: Itrtr/Val. La primera vez es la Estructura.
        >>> [cuenta]: NO INTRO. Cuenta el nivel interno de iteracion.
        >>> [lst_return_type]: NO INTRO. list para guardar lo que se quiera. en este caso se guarda el tipo/valor de elemento.
        >>> [globals]: self.elemento_copy, lista xa copia... (podría ser local como lst_return_type.)
        >>> [globals]: self.num_iterators, numero de Itrtr de la Estructura.
        >>> [globals]: self.num_dicc , Numero de diccionarios encontrados en la Estructura.
        
        >>> I M P R I M I R   F I L A S 
            listaWidth = [20,20,20]
            listaValores=[True,5,25]
            self.imprime_row(listaValores=listaValores, listaWidth=listaWidth, listaAmigos=['(k)']) 
        
        """      
        # ================================================================================
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if cuenta==None and lst_return_type==None:
            # Inicializo            
            cuenta=0
            lst_return_type=[] 
            # ________________________________
            # Para Calcular la ultima Vuelta comparo elemento con el que me reservo aqui: elemento_copy
            self.elemento_copy=elemento           
            self.paso=0
            pass
            # ______________________________________
            # Mensaje de BienVenida al Constructor
            print(f'\nBienvenido al Motor ::: E l e m e n t o   a   c o n s t r u i r ::: ')
            print(f'\n{elemento}\n')
            # ____________________
            # Cabecera a Imprimir
            listaTitulos=['[Itrtr,Value]:', 'Level -> 1 ' , 'Pasos' ]
            self.imprime_row(listaValores=listaTitulos)
            print(f' {'-'*50}')

        # ================================================================================
        # CONTADORES DE PASO, GLOBALES Y RELATIVOS(cuenta)
        cuenta+=1
        self.paso+=1

        # ================================================================================
        # AQUÍ EMPIEZA TODO..... A Rebuscarrr!!!!     .....preguto si es Itrtr ( Iterator )
        if  (isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) or 
            isinstance(elemento, dict)):
            """ 
            >>> Solo Me interesa grabar los valores ...y marcar los pasos por los itrtr's  """
            if(isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) ):               
                self.num_iterators +=1
                self.imprime_row(listaValores=['(l)', cuenta, self.paso], listaAmigos=[f'{'(-)'*cuenta}'] )
                """ 
                >>> Solo Me interesa grabar los valores ...y marcar los pasos por los itrtr's  """
                for item in elemento:
                    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    lst_return_type.append(type(item))
                    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                    self.level_XX_04(elemento=item, cuenta=cuenta, lst_return_type=lst_return_type)
            
            elif isinstance(elemento, dict):
                self.num_dicc +=1                                
                lst_pares = elemento.items()                                
                """ 
                >>> Lista de pares (clave,valor) del elemento... xa tener acceso a cada valor y su key.
                """                
                # Recorro cada par del diccionario. par[0]=keys, par[1]=values
                for pares in lst_pares:                    
                    """ >>> pares = k , v  ...luego pares[0]=k y pares[1]=v   
                    """                    
                    key_dicc  =pares[0]
                    """ >>> pares[0] key del dict. str
                    """
                    valor_dicc=pares[1]
                    """ >>> pares[1] value del dict...que puede ser un itrtr o un valor
                    """                    
                    self.imprime_row(listaValores=[key_dicc, cuenta, self.paso], listaAmigos=['(k) '] )                    
                    if (isinstance(valor_dicc, list) or isinstance(valor_dicc, tuple) or 
                        isinstance(valor_dicc, set) or isinstance(valor_dicc, dict) ):                    
                        
                        self.imprime_row(listaValores=['(all)', cuenta, self.paso] )                    

                        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                        lst_return_type.append(type(valor_dicc))
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                        self.level_XX_04(elemento=valor_dicc, cuenta=cuenta, lst_return_type=lst_return_type)
                    else:
                        """ 
                        V A L O R """
                        self.imprime_row(listaValores=[valor_dicc, cuenta, self.paso], listaAmigos=['(v) '] )
                        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                        lst_return_type.append(elemento)
                    pass                    
                pass
            pass
        else:
            """ 
            V A L O R """
            self.imprime_row(listaValores=[elemento, cuenta, self.paso], listaAmigos=[f'{'(-)'*cuenta} '])
            # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            lst_return_type.append(elemento)       
        pass        
        if elemento==self.elemento_copy:
            print('\n.............. Ultima Vuelta!!....[Code aquÍ ... Antes de retornar a level()]')
        
        """ 
        print('\n[Code aquÍ ... entre llamadas rcrsvs ( Itrtr's ) ].....OJO, NO es la última antes del retorno') 
        print(f'{'(==)'*(cuenta)} Retorno(Itrtr/Val)')  
        """
        
        """ 
        >>> UPDT:.. INTENTAR RETORNAR 2+ LISTAS DESEMPAQUETANDOLAS EN LA LLAMADA PADRE O CONTENIDAS EN EL lst_return_type y extendidas antes del retorno final...
        """
        # Hay veces que el tren pasa mas de una vez....
        return lst_return_type

    def level_BB(self, elemento, cuenta=None, lst_rtrn_type=None):
        """ Def: Recorre Recursivamente la Estructura.....SALIDA RE-FORMATEADA

        NO IMPRIMO LOS: DICT - LIST - TUPLE - SET - solo imprimo-key y value y la relacion
        """      
        # Inicializo las variables en la primera vuelta  
        if cuenta==None and lst_rtrn_type==None:
            cuenta=0
            lst_rtrn_type=[] 
            self.elemento_copy=elemento           
            self.paso=0
            pass
            strformato = "{:<30}{:<30}{:<30}"
            cabecera1=f'| KEY/VALOR';       cabecera2=f'| 1º -> LEVEL';     cabecera3=f'| CONT-PASO'
            print(strformato.format(cabecera1, cabecera2, cabecera3))            
            print(f'{'-'*50}')
            pass
        # Contadores de paso, global y relativo(cuenta).
        cuenta+=1
        self.paso+=1        

        if  (isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set) or 
            isinstance(elemento, dict)):

            # print(f'{'>'*50}')
            # print('>>>>> ITERADOR..... ')
            if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):               
                """ >>> Def: Cuando nos encontramos con un Iterator(Itrtr):  """                    
                self.num_iterators +=1
            elif isinstance(elemento, dict):
                """ >>> Def: Cuando nos encontramos con un Diccionario:  """                    
                self.num_dicc +=1                
                lst_pares = elemento.items()                                
                """ >>> Def: Obtengo la lista de pares (clave,valor) """
                # __________________________________                
                # Recorro cada par del diccionario. par[0]=keys, par[1]=values
                for pares in lst_pares:                    
                    strformato ="{:<30}{:<30}{:<30}"
                    key=f'Key:{pares[0]}'  
                    pasos=f'{self.paso}'
                    val=f'Value:{pares[1]}' 
                    print(strformato.format( '(k)'+key+''+ cuenta + pasos))   
                    pass
                    valor_dicc=pares[1]
                    if (isinstance(valor_dicc, list) or isinstance(valor_dicc, tuple) or 
                        isinstance(valor_dicc, set) or isinstance(valor_dicc, dict) ):                    
                        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                        lst_rtrn_type.append(type(valor_dicc))
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                        self.level_XX_05(elemento=valor_dicc, cuenta=cuenta, lst_rtrn_type=lst_rtrn_type)
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                    else:
                        # 
                        strformato = "{:<30}{:<30}{:<30}";msg=f'{elemento}';cuen=f'{cuenta}';pasos=f'{self.paso}'
                        print(strformato.format(msg, cuen, pasos))   
                        # aaaaaaaa
                        lst_rtrn_type.append(elemento)                    
                    pass                                                 
                
        else:
            strformato = "{:<30}{:<30}{:<30}"; 
            msg=f'<< {elemento} >>'; cuen=f'{cuenta}'; pasos=f'{self.paso}'
            print(strformato.format(msg, cuen, pasos))
            # aaaaaaaaaaaaaaaaaaaaaaaa
            lst_rtrn_type.append(elemento)
        pass
        if elemento==self.elemento_copy:
            print('\n.............. ULTIMA VUELTA....[codigo aqui antes de retornar a level()]')

        strformato="{:<30}{:<30}{:<30}"
        msg=f'{'(*)'*(cuenta)} RETORNO(Itrtpr/Val){elemento}'; cuen=f'{cuenta}'; pasos=f'{self.paso}'
        print(strformato.format(msg, cuen, pasos))

        # =================            
        return lst_rtrn_type
        # =================            

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 5
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def level_XX_05(self, elemento, cuenta=None, lst_return_type=None):
        """ Def: Recorre Recursivamente la Estructura.....LO QUE ENTRA
        >>> [elemento]: Itrtr/Val. La primera vez es la Estructura.
        >>> [cuenta]: NO INTRO. Cuenta el nivel interno de iteracion.
        >>> [lst_return_type]: NO INTRO. list para guardar lo que se quiera. en este caso se guarda el tipo/valor de elemento.
        >>> [globals]: self.elemento_copy, lista xa copia... (podría ser local como lst_return_type.)
        >>> [globals]: self.num_iterators, numero de Itrtr de la Estructura.
        >>> [globals]: self.num_dicc , Numero de diccionarios encontrados en la Estructura.
        
        >>> I M P R I M I R   F I L A S 
            listaWidth = [20,20,20]
            listaValores=[True,5,25]
            self.imprime_row(listaValores=listaValores, listaWidth=listaWidth, listaAmigos=['(k)']) 
        
        """      
        # ================================================================================
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if cuenta==None and lst_return_type==None:
            # Inicializo            
            cuenta=0
            lst_return_type=[] 
            # ________________________________
            # Para Calcular la ultima Vuelta comparo elemento con el que me reservo aqui: elemento_copy
            self.elemento_copy=elemento           
            self.paso=0
            pass
            # ______________________________________
            # Mensaje de BienVenida al Constructor
            print(f'\nBienvenido al Motor ::: E l e m e n t o   a   c o n s t r u i r ::: ')
            print(f'\n{elemento}\n')
            # ____________________
            # Cabecera a Imprimir
            listaTitulos=['[Itrtr,Value]:', 'Level -> 1 ' , 'Pasos' ]
            self.imprime_row(listaValores=listaTitulos)
            print(f' {'-'*80}')

        # ================================================================================
        # CONTADORES DE PASO, GLOBALES Y RELATIVOS(cuenta)
        cuenta+=1
        self.paso+=1

        # ================================================================================
        # AQUÍ EMPIEZA TODO..... A Rebuscarrr!!!!     .....preguto si es Itrtr ( Iterator )        
        # ==============================================================
        tipo_elemento = self.what_i_am(elemento=elemento, bItrtr=True)

        if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
            """ 
            >>> Solo Me interesa grabar los valores ...y marcar los pasos por los itrtr's  """                    
            if tipo_elemento == What.ITRTR:         
                """ 
                ITRTR """
                self.num_iterators +=1
                self.imprime_row(listaValores=['(L)', cuenta, self.paso], listaAmigos=[f'{'(#)'*cuenta}'] )
                for item in elemento:
                    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    lst_return_type.append(type(item))
                    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                    self.level_XX_05(elemento=item, cuenta=cuenta, lst_return_type=lst_return_type)  
            elif tipo_elemento == What.DICT:
                """ 
                DICCIONARIO """
                self.num_dicc +=1                                
                lst_pares = elemento.items()                                
                """ >>> Lista de pares (clave,valor) del elemento... xa tener acceso a cada valor y su key.
                """                
                for pares in lst_pares:                    
                    """ >>> pares = k , v  ...luego pares[0]=k y pares[1]=v """                    
                    key_dicc  =pares[0]
                    """ >>> pares[0] key del dict. str
                    """
                    valor_dicc=pares[1]
                    """ >>> pares[1] value del dict...que puede ser un itrtr o un valor
                    """                    
                    self.imprime_row(listaValores=['(k) '+key_dicc, cuenta, self.paso], listaAmigos=[f'{'(-)'*cuenta} '] )                    
                    # ==============================================================
                    tipo_valor = self.what_i_am(elemento=valor_dicc, bItrtr=True)    
                    
                    if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
                        """ 
                        ITRTR """
                        # self.imprime_row(listaValores=['(all)', cuenta, self.paso] )
                        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                        lst_return_type.append(type(valor_dicc))
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                        self.level_XX_05(elemento=valor_dicc, cuenta=cuenta, lst_return_type=lst_return_type)
                    elif tipo_elemento == What.VALOR:
                        """ 
                        V A L O R """
                        self.imprime_row(listaValores=['(v) '+valor_dicc, cuenta, self.paso], listaAmigos=[f'{'(-)'*cuenta} '])
                        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                        lst_return_type.append(elemento)
                    pass                    
                pass
        elif tipo_elemento == What.VALOR:        
            """ 
            V A L O R """
            self.imprime_row(listaValores=[elemento, cuenta, self.paso], listaAmigos=[f'{'(-)'*cuenta} '])
            # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            lst_return_type.append(elemento)       
        pass
        if elemento==self.elemento_copy:
            print('\n.............. Ultima Vuelta!!....[Code aquÍ ... Antes de retornar a level()]')        
        """ >>> print('\n[Code aquÍ ... entre llamadas rcrsvs ( Itrtr's ) ].....OJO, NO es la última antes del retorno')   """
        # Hay veces que el tren pasa mas de una vez....
        return lst_return_type

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 6
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def level_XX_clean(self, elemento, cuenta=None, lst_return_type=None):
        """ Def: Recorre Recursivamente la Estructura.....LIMPIA        """      
        
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if cuenta==None and lst_return_type==None:
            cuenta=0
            lst_return_type=[] 
            self.elemento_copy=elemento           
            self.paso=0
            print(f'\n{elemento}\n')
            listaTitulos=['Item','Camino...', 'Level->1' , 'Pasos' ]
            self.imprime_row(listaValores=listaTitulos)
            print(f' {'-'*80}')
        
        # CONTADORES DE PASO, GLOBALES Y RELATIVOS(cuenta)
        cuenta+=1
        self.paso+=1
        
        # AQUÍ EMPIEZA TODO..... A Rebuscarrr!!!!     .....preguto si es Itrtr ( Iterator )        
        tipo_elemento = self.what_i_am(elemento=elemento, bItrtr=True)
        if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
            """ ITRTR - DICT  """
            if tipo_elemento == What.ITRTR: 
                """ ITRTR """        
                self.num_iterators +=1
                # ______________________________________
                self.imprime_row(listaValores=['-',' [', cuenta, self.paso], listaAmigos=['', f'{'(_)'*cuenta}'] )
                for item in elemento:
                    lst_return_type.append(type(item))
                    self.level_XX_clean(elemento=item, cuenta=cuenta, lst_return_type=lst_return_type)  
            elif tipo_elemento == What.DICT:
                """ DICT """
                self.num_dicc +=1                                
                lst_pares = elemento.items()                                
                for pares in lst_pares:                    
                    key_dicc   = pares[0]
                    valor_dicc = pares[1]
                    # ______________________________________
                    self.imprime_row(listaValores=[key_dicc,'(K)'+Castor.TAB+str(key_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'] )                    
                    tipo_valor = self.what_i_am(elemento=valor_dicc, bItrtr=True)                        
                    if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
                        """ ITRTR - DICT  """
                        lst_return_type.append(type(valor_dicc))
                        self.level_XX_clean(elemento=valor_dicc, cuenta=cuenta, lst_return_type=lst_return_type)
                    elif tipo_elemento == What.VALOR:
                        """ VALOR """
                        self.imprime_row(listaValores=[valor_dicc,'(V)'+Castor.TAB+str(valor_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
                        lst_return_type.append(elemento)
        elif tipo_elemento == What.VALOR:        
            """ VALOR """
            self.imprime_row(listaValores=[elemento,' = '+str(elemento), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
            lst_return_type.append(elemento)       
        if elemento==self.elemento_copy:
            print('\n.............. Ultima Vuelta!!....[Code aquÍ ... Antes de retornar a level()]')        
        return lst_return_type

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva 7
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def get_lst_keysValues(self, elemento, cuenta=None, lst_return=None):
        """ Def: Recorre Recursivamente la Estructura.....Devuelve: las keys y los values de dict, y los values de list        """      
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if cuenta==None and lst_return==None:
            cuenta=0
            lst_return=[] 
            self.elemento_copy=elemento           
            self.paso=0
            print(f'\n{elemento}\n')
            listaTitulos=['Item','Camino', 'Level->1' , 'Pasos' ]
            self.imprime_row(listaValores=listaTitulos)
            print(f' {'-'*80}')
        # CONTADORES DE PASO, GLOBALES Y RELATIVOS(cuenta)
        cuenta+=1
        self.paso+=1
        # AQUÍ EMPIEZA TODO..... A Rebuscarrr!!!!     .....preguto si es Itrtr ( Iterator )        
        tipo_elemento = self.what_i_am(elemento=elemento, bItrtr=True)        
        if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
            """ ITRTR-DICT  """
            if tipo_elemento == What.ITRTR:
                """ ITRTR """         
                self.num_iterators +=1                
                for item in elemento:
                    self.get_lst_keysValues(elemento=item, cuenta=cuenta, lst_return=lst_return)  
            elif tipo_elemento == What.DICT:
                """ DICT """
                self.num_dicc +=1                                
                lst_pares = elemento.items()                                
                for pares in lst_pares:                    
                    key_dicc   = pares[0]
                    valor_dicc = pares[1]
                    # _______________________________________________
                    lst_return.append({key_dicc:[False, self.paso]})
                    self.imprime_row(listaValores=[key_dicc,'(K)'+Castor.TAB+str(key_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'] )                                        
                    tipo_valor = self.what_i_am(elemento=valor_dicc, bItrtr=True)                        
                    if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
                        """ ITRTR """
                        self.get_lst_keysValues(elemento=valor_dicc, cuenta=cuenta, lst_return=lst_return)
                    elif tipo_elemento == What.VALOR:
                        """ VALOR """
                        self.imprime_row(listaValores=[valor_dicc,'(V)'+Castor.TAB+str(valor_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
                        # ________________________________________________
                        lst_return.append({valor_dicc:[True, self.paso]})        
        elif tipo_elemento == What.VALOR:        
            """ VALOR """
            self.imprime_row(listaValores=[elemento,' = '+str(elemento), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
            # ______________________________________________
            lst_return.append({elemento:[True, self.paso]})       
        if elemento==self.elemento_copy:
            print('\n.............. Ultima Vuelta!!....[Code aquÍ ... Antes de retornar a level()]')        
        return lst_return

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # E S Q U E L E T O N    RCRSV
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def esqueleton_rcrsv(self, val_itrtr_dicc=None, lst_return=None, bool_catcher=False):
        """  >>> Def: Esqueleto recursivo para recorrer toda la estructura de diccionarios e iterators.   """
        # ______________________________________________________________________________
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if lst_return is None and val_itrtr_dicc is None and bool_catcher==False:
            lst_return = []                                   
            val_itrtr_dicc=self.__lst_Castor
            self.paso=0 ; self.num_iterators=0 ; self.num_dicc =0
        # _____________________________________________________________________
        # S e m a f o r o    xa controlar situaciones 'especiales' (comodin) ;)
        if bool_catcher==True:
            """ Aquí, codigo  y Acabo retornando el semaforo"""
            bool_catcher=False
        # C O N T A D O R E S   DE PASO, GLOBALES Y RELATIVOS(cuenta)
        self.paso+=1        
        # A Q U Í   E M P I E Z A    TODO..... a R e b u s c a r r r  !!!! Arrampla con lo que veas y generoso no seas!! (Piratas del Caribe)
        # ____________________________________________________________________
        tipo_elemento = self.what_i_am(elemento=val_itrtr_dicc, bItrtr=True)
        if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
            """ ITRTR-DICT  """
            if tipo_elemento == What.ITRTR:
                """ ITRTR """         
                self.num_iterators +=1                
                for val_itrtr in val_itrtr_dicc:
                    pass
                    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                    self.esqueleton_rcrsv(  val_itrtr_dicc=val_itrtr, 
                                            lst_return=lst_return, 
                                            bool_catcher=bool_catcher)
            elif tipo_elemento == What.DICT:
                """ DICT """
                self.num_dicc +=1                                
                lst_pares = val_itrtr_dicc.items()                                
                for pares in lst_pares:                    
                    key_dicc   = pares[0]
                    valor_dicc = pares[1]
                    """ Aqui se guarda la key de cada elemento de a lista de keys """
                    # ____________________________________________________________
                    tipo_valor = self.what_i_am(elemento=valor_dicc, bItrtr=True)
                    if tipo_valor == What.ITRTR or tipo_elemento == What.DICT:
                        """ ITRTR - DICT """                        
                        pass
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                        self.esqueleton_rcrsv(  val_itrtr_dicc=valor_dicc,                                                 
                                                lst_return=lst_return, 
                                                bool_catcher=bool_catcher)
                    elif tipo_elemento == What.VALOR:
                        """ VALOR """
                        pass
        elif tipo_elemento == What.VALOR:        
            """ VALOR """
            pass
        if val_itrtr_dicc==self.elemento_copy:
            # Ultima Vuelta!!....[Code aquÍ ... Antes de retornar]')
            pass
        return lst_return

    """ 
    Def: Devuelve una lista de posiciones haasta llegar al Objeto. Es la base de las busquedas de datos en __lst_Castor
    [key_castor_busca]: una key_castor , pejempl "c:3"
    >>> [elemento]: NO USAR EN LA LLAMADA. __lst_Castor la lista Inicial.
    >>> [lst_camino]: NO USAR EN LA LLAMADA
    >>> Retorno: lista de int. Pejem: [0,1,0] representa las posiciones en __lst_Castor
    """
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # Recursiva Que Recorre la Estructura y devuelve el camino hasta llegar a un valor.
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    def get_posicion_key(self, key_castor_busca, elemento=None, lst_camino=None):
        # 1ª  V U E L T A   R C R S V   .... inicializo las variables (solo la 1ª vez)
        if lst_camino is None and elemento is None:
            lst_camino = []                                   
            elemento=self.__lst_Castor        
        # C O N T A D O R E S   DE PASO, GLOBALES Y RELATIVOS(cuenta)
        self.paso+=1

        # A Q U Í   E M P I E Z A  TODO .... A R e b u s c a r r r  ! .....preguto si es Itrtr ( Iterator )        
        tipo_elemento = self.what_i_am(elemento=elemento, bItrtr=True)        
        if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
            """ ITRTR-DICT  """
            if tipo_elemento == What.ITRTR:
                """ ITRTR """         
                self.num_iterators +=1                
                for i, item in enumerate(elemento):
                    new_posicion= lst_camino + [i]
                    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                    resultado = self.get_posicion_key(key_castor_busca=item, elemento=elemento, lst_camino=lst_camino)
                    # ________________________  
                    if resultado is not None:
                        return resultado

            elif tipo_elemento == What.DICT:
                """ DICT """
                self.num_dicc +=1                                
                lst_pares = elemento.items()                                
                for pares in lst_pares:                    
                    key_dicc   = pares[0]
                    valor_dicc = pares[1]
                    # _______________________________________________
                    # lst_return.append({key_dicc:[False, self.paso]})
                    # self.imprime_row(listaValores=[key_dicc,'(K)'+Castor.TAB+str(key_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'] )                                        
                    print(f'Key Found {key_dicc} ')
                    tipo_valor = self.what_i_am(elemento=valor_dicc, bItrtr=True)                        
                    if tipo_elemento == What.ITRTR or tipo_elemento == What.DICT:
                        """ ITRTR """
                        # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                        self.get_posicion_key(elemento=valor_dicc, cuenta=cuenta, lst_return=lst_return)
                    elif tipo_elemento == What.VALOR:
                        """ VALOR dict"""
                        pass
                        # self.imprime_row(listaValores=[valor_dicc,'(V)'+Castor.TAB+str(valor_dicc), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
                        # lst_return.append({valor_dicc:[True, self.paso]})        
        elif tipo_elemento == What.VALOR:        
            """ VALOR itrtr"""
            return new_posicion
            # self.imprime_row(listaValores=[elemento,' = '+str(elemento), cuenta, self.paso], listaAmigos=['', f'{'(-)'*cuenta}'])
            # ______________________________________________
            # lst_return.append({elemento:[True, self.paso]})       
        if elemento==self.elemento_copy:
            # print('\n.............. Ultima Vuelta!!....[Code aquÍ ... Antes de retornar a level()]')
            pass
        return None


    # ===============================
    # Obtiene la POSICION de una key_castor_busca (key en la Estrucutura Inicial, key_castor)
    def get_posicion_key2(self, key_castor_busca, elemento=None, posicion=None):
       
        if posicion is None and elemento is None:
            posicion = []                                   
            elemento=self.__lst_Castor            
        for indice, elemento in enumerate(elemento):
            NewPosicion = posicion + [indice]
            """ >>> Agrego el índice actual a la lista posicion 
            """
            if isinstance(elemento, list):
                # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
                resultado = self.get_posicion_key2(key_castor_busca=key_castor_busca, elemento=elemento, posicion=NewPosicion)
                if resultado is not None:
                    return resultado                 
            
            elif elemento == key_castor_busca:
                return NewPosicion 
        """ 
        >>> Devolver None si no se encontró el key_castor_busca en esta lista """
        return None  


    # ___________________________________________________________________
    #  W H A T    I    A M 
    def what_i_am(self, elemento, bItrtr=True):        
        """ 
        Entra un objeto o un iterador y da una respuesta de Enum
        -1: Objeto o Valor | 100: list | 200: tuple | 300: set | 400: dict | 90: simple dict | 10: simple itrtr(iterator) 
        queSoy=self.what_i_am(elemento=lst_valores, bItrtr=True)
            if queSoy==What.ITRTR:
                pass
            elif queSoy==What.DICT:
                pass
            elif queSoy==What.VALOR:
                pass
        """
        if bItrtr==True:
            if isinstance(elemento, list) or isinstance(elemento, tuple) or isinstance(elemento, set):
                return What.ITRTR
            elif isinstance(elemento, dict):
                return What.DICT
            else:
                return What.VALOR
        else:
            if isinstance(elemento, list):
                return What.LIST
            elif isinstance(elemento, tuple):
                return What.TUPLE
            elif sinstance(elemento, set):
                return What.SET
            elif isinstance(elemento, dict):
                return What.DICT
            else:
                return What.VALOR

    # ==============================================================================================
    # T O   P R I N T 
    # ==============================================================================================
    def imprime_row(self, listaValores, listaWidth=[15,35,10,10], listaAmigos=None):

        if len(listaValores)!=len(listaWidth):
            pass
        str_formato = self.__format_formato(lst_width_colum=listaWidth)
        lst_print=[]
        if listaAmigos:
            listaAmigos=self.igualar_tam_lst(lstMolde=listaValores, lstToTransform=listaAmigos)
            lst_print = [ listaAmigos[v] + '' + str(valor) for v, valor in enumerate(listaValores)]
        else:
            lst_print = [str(valor) for valor in listaValores]

        print(str_formato.format( *lst_print ))   

    def igualar_tam_lst(self, lstMolde, lstToTransform, valor_defecto=''):
        """ 
        Def: Iguala la longitudes con respecto a [lstMolde], completando si hace falta con ''
        Retorno: Devuelve la listaToTransform, cambiada.
        """
        long_modelo = len(lstMolde)
        if len(lstToTransform) < long_modelo:
            lstToTransform.extend([valor_defecto] * (long_modelo - len(lstToTransform)))
        else:
            lstToTransform = lstToTransform[:long_modelo]
        return lstToTransform
    
    def convert_to_lstlst_valores(self, estructura):
        """ La idea es convertir todo a lista..... frozeset , items()  """
        """ En otro caso, en ppio es para imprimir las listas de resultados que se generan en esta clase. """
        pass
    
    def toPrint(self, lstlst_valores, lst_width_colum, lst_head=None, num_separador=100, listaAmigos=None):
        if lst_head:
            self.imprime_row(listaValores=lst_head, listaWidth=lst_width_colum, listaAmigos=listaAmigos)
        print(f'{'-'*num_separador}')
        for lst_valores in lstlst_valores:
            queSoy=self.what_i_am( lst_valores )
            if queSoy==What.ITRTR:
                self.imprime_row(listaValores=lst_valores, listaWidth=lst_width_colum, listaAmigos=listaAmigos)                
            elif queSoy==What.DICT:
                # Guardo la key en una lista.                
                lst_str_dicc=[*lst_valores.keys()]
                # A la lista anterior le añado el value
                lst_str_dicc.extend(*lst_valores.values())                
                # Lo convierto todo en string.
                lst_str_dicc=[str(str_dicc) for str_dicc in lst_str_dicc]
                # Imprimo el resultado.
                self.imprime_row(listaValores=lst_str_dicc, listaWidth=lst_width_colum, listaAmigos=listaAmigos)                
                pass
            elif queSoy==What.VALOR:
                return None

        pass

    def __format_formato(self, lst_width_colum):
        strformato=''
        for width in lst_width_colum:
            strformato+= "{:<"+str(width)+"}"
        
        return strformato
    
    def __imprime_all(self, lst_valores, strFormato):        
        print(strFormato.format(*lst_valores))
# ===================================================================
# ===================================================================


# MENU INICIO-======================
os.system('cls')
print('\nW E L C O M E   T O  <<  C A S T O R  >>  C L A S S ')
objDraw=Castor(lst_X_01)

print('\nBASE RCRSV')
objDraw.BaseRCSV(objDraw.get_lst_Castor())


listaMenuPuebas=[
                
                "viewlevel():               \t(Devuelve una lista de tipos hasta llegar a los valores)" , 
                "level_XX():                \t()", 
                "level_XX_01():             \t()", 
                "level_XX_02():             \t()", 
                "level_XX_03():             \t()", 
                "level_XX_04()              \t()",
                "level_BB()                 \t()",
                "level_XX_05()              \t()",
                "level_XX_clean()           \t()",
                "get_lst_keysValues()       \t()",
                'esqueleton_rcrsv()         \t()',
                'get_posicion_key           \t()',
                


                ]
while True:
    respuesta=MENU(menu=listaMenuPuebas, tituloMenu="Enfileitor")
    if respuesta==None:
        print('\nS A L I E N D O    D E   E N F I L E I T O R......')
        break
    elif respuesta==1:
        pass
    elif respuesta==2:
        pass
    elif respuesta==3:
        pass
    elif respuesta==4:
        pass
    elif respuesta==5:
        pass
    elif respuesta==6:
        pass
    else:
        continue


        # print('\nB A S E   R E C U R S I V A  (DEPURACION)')
        # viewlevel(SttK)

        # print('\nI N I C I A L I Z A   V A L U E S')
        # initX(SttK)        

        # print(f'\nP R I N T E X', end='\t')
        # PrinteX(SttK)
        
        # print('\nG E T   I N F O   SKELETON  ')
        # getInfo(SttK)

        # print('\nG E T  V A L U E')
        # getX(SttK)        

        # print('\nA C T U A L I Z A   V A L O R')
        # uptX(SttK)
