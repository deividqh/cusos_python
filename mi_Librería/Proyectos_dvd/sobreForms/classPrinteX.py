# ==============================================================================
# C L A S S    P R I N T E X 
# ==============================================================================
# [rowformat] Admite una cadena con formato '{:<num1}{:<num2}{:<num3}{:<numN}' 
#                                           ' {:<30}  {:<15}  {:<25}'
# >>> signnifica: 
#     (':') Inicio de opciones de formato
#     ('<') alineado a la izquierda
#     (30) numero de espacios reservados para esa columna

# >>> print('{:<30}{:<15}{:<25}'.format("Nombre", "Edad", "Ocupación"))
# ==============================================================================
class PrinteX():
    """ 
    Quiero con esta clase dar formato a la impresion en terminal.
    Quiero formar tablas 
    Recibir una lista de titulos
    Recibir una lista de lista de str de columnas-titulo.
    Imprimir en funcion de la cantidad de titulos y formatear una salida standar.
    """
    def __init__(self, listaTitulo, listaDatos, esAjustado=True, nombrePrinteX=''):        
        """ 
        Espera ("Tit1", "Tit2", "Tit3") ,  ( (2, 3, 4) , (5, 6, 7) ,.... ) )
        """
        if self.validaEntrada(listaTitulo, listaDatos)==False: 
            print("Error de Entrada")
            return None

        self.listaTitulo=listaTitulo
        self.listaDatos=listaDatos       

        # self.strformato=self.getFormato(listaTitulo=self.listaTitulo, listaDatos=self.listaDatos, esAjustado=esAjustado)
        self.Impr(listaTitulo=self.listaTitulo, 
                listaDatos=self.listaDatos, 
                esAjustado=esAjustado, nombrePrinteX=nombrePrinteX)

    # ___________________________________        
    def getFormato(self, listaTitulo=None, listaDatos=None, esAjustado=False):
        """ 
        Establece el formato según la listaTitulo pasada, que es una lista de str tipo:
        >>> listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "FilaR", "ColumR"]        
        -Puede ser un formato ajustado = True al tamaño maximo de CADA COUMNA o ajustado = False, se ajuta al tamaño del maximo str de la lista
        
        -Se Basa en saber cuantas columnas quieres(listaTitulos) y formatear cada linea al formato generado dinamicamente.
        >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        totalLen=0
        strformato=''
        if esAjustado==True:
            listaMaxCol = self.__maximoXColumna(listaTitulo=listaTitulo, listaDatos=listaDatos)
            listaMaxCol = [item+2 for item in listaMaxCol]
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(listaMaxCol[i]) + "}"
            
            # totalLen = sum(listaMaxCol) + len(listaMaxCol)
            totalLen = sum(listaMaxCol)
            # totalLen+=2
        else:
            maximo = self.__get_maximo(listaTitulo, listaDatos)        
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(maximo) + "}"

            totalLen = maximo

        # print(strformato)
        return strformato, totalLen
    # ___________________________________
    def validaEntrada(self, listaTitulo=None, listaDatos=None):
        """ 
        Valida que listaTitulo es una lista de str
        Valida que listaDatos es una lista de lista de str o diccionario de listas de str
        Devuelve True/False                                    
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        # primera Validacion
        if not isinstance(listaTitulo, list): return None
        if not isinstance(listaDatos, list): return None

        # Convierte a String los elementos de listatitulo
        try:
            for item in listaTitulo:
                str(item)
        except Exception as e:
            print(e)
            return None
        # Valida que todos los elementos de listaDatos son diccionario
        for item in listaDatos:
            if not isinstance(item, dict): 
                return None
        


        # Validacion interna de cada diccionario:
        # listaDatosStr=[]
        # for item in listaDatos:
        #     for key, value in item.items():
        #         for data in value.values():
        #             listaDatosStr.append(str(data))
        listaDatosStr=[str(data) for item in listaDatos 
                                    for key, value in item.items() 
                                        for data in value.values()]
        
        
        
        
        return True
    # ___________________________________
    def Impr(self, listaTitulo=None, listaDatos=None, esAjustado=False, nombrePrinteX=''):
        """ 
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        # SE ESTABLECE LA CADENA STR DE FORMATO()
        self.strformato, sumaTotChar=self.getFormato(listaTitulo=listaTitulo, 
                                                     listaDatos=listaDatos, 
                                                     esAjustado=esAjustado)        
        # _________
        # Encabezado        
        print(f'{str(nombrePrinteX).upper()}')
        numChar=len(nombrePrinteX)+2
        print(f'{'='*numChar}')

        print(self.strformato.format(*listaTitulo))   
        if esAjustado==False:
            maximo = self.__get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
            
        # _________
        # Datos
        for iterador in listaDatos:
            if isinstance(iterador, dict):
                """ Si recibe un diccionario, se intenta convertir en "key"+"values" """
                listaData = [[key, item] for key, item in iterador.items()]
                self.__imprListaDatos(listaListStr=listaData)
        
            elif isinstance(iterador, list) or isinstance(iterador, tuple):
        
                self.__imprListaDatos(listaDatos=iterador)
        
            else:
                return None
        # _________
        # Fin
        if esAjustado==False:
            maximo = self.__get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
    
    def __maximoXColumna(self, listaTitulo, listaDatos):
        """ 
        Retorna una lista con el máximo número de caracteres de cada columna.
        """
        # Inicia la lista `retorno` con las longitudes de cada título en `listaTitulo`
        retorno = [len(titulo) for titulo in listaTitulo]

        # Recorre las filas en `listaDatos` y compara con el máximo de cada columna
        for fila in listaDatos:
            for columna, item in enumerate(fila):
                retorno[columna] = max(retorno[columna], len(str(item)))
        
        return retorno


    # ___________________________________
    # Imprime en consola con un formato alineado. 
    def __imprListaDatos(self, listaDatos=None):
        """ 
        Def: Imprime en la Terminal CON FORMATO
        -Calculando la longitud maxima para alinear correctamente.
        listaDatos tiene que ser un list de str
        """        
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaDatos: return None
        try:               
            print(self.strformato.format(*listaDatos))
        except Exception as e:
            print(f'Error: {e}')
            return False
        else:
            return True
    # _________________________
    def __imprTitulos(self, listaTitulo=None):
        print(self.strformato.format(*listaTitulo))   
        print("-"*len(listaTitulo)*(self.maximo))     #Linea de corte
    # _________________________
    def __get_maximo(self,listaTitulo=None, listaDatos=None):
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None
        # _____________________
        # Recojo datos de listaTitulo
        longTitulo=len(listaTitulo)
        max_len_titulo=self.__getMaxLenListaStr(listaTitulo)
        # _____________________
        # Recojo datos de listaDatos
        # Funcion Recursiva para Recorrer listas y devolver el str mas largo
        max_len_datos=self.__maxLenRcsv(listaDatos)
        # _____________________
        # CALCULO EL MAXIMO DE ESPACIO 
        maximo=max_len_titulo if max_len_titulo>=max_len_datos else max_len_datos 
        return maximo+1
    # ________________________
    def __maxLenRcsv(self, iterador):
        listaCadenas=self.___listRcsv(iterador=iterador)
        if listaCadenas:
            listaLen=[len(string) for string in listaCadenas]
            return max(listaLen)
    # ________________________
    # Calcula la maxima longitud de un titulo o un genero en la tupla de peliculas
    def __getMaxLenListaStr(self, iterador):
        listLargos=[len(item) for item in iterador]        
        # Como ya tengo una lista con solo números, puedo aplicar max()         
        max_longitud = max(listLargos)        
        return max_longitud
    # ________________________
    # Busqueda recursiva por un iterador lista
    def ___listRcsv(self, iterador, retorno=None):
        
        if retorno==None: retorno=[]        

        if isinstance(iterador, list) or isinstance(iterador, tuple):
            for subList in iterador:
                self.___listRcsv(subList, retorno)
        else:
            retorno.append(iterador)
        return retorno

        pass