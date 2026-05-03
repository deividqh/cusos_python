import re

class listTOdict_byTcld_ToString():
    """ 
    Def => entra una list de str y devuelve esa list como keys de un diccionario y los values son 
    pedidos por Teclado. Se pueden pasar el [tipoDato, PERMITENULL] en una lista de lista o lista de tupla
    [Ejemplo de uso]:
    >>> from listTOdict_Tcld import listTOdict_byTcld_ToString as listToDict
    >>> oneDict=listToDict.listTOdict_TcldPlus(
                                    listaStrKeys=['Cuanto','Quieres','Entrar?'],
                                    listaDef= [(int,True), (float,False), (str,False)],
                                    permiteNulo=True,
                                    esCapital=False)
    >>> print(oneDict)
        
        [Resultado] => {'Cuanto': 5, 'Quieres': 5.0, 'Entrar?': '5'}
    """
    def __init__(self):
        """ 
        Constructor: 
        """
        pass
    def __str__(self):
        pass
        # ____________________
    
    def index(listaStrKeys=True, listaDef=None, byTcld=True, msgIntro='Intro', permiteNulo=False, esCapital=False):
        """ 
        Tiene que ser la única funcion que se tiene que llamar.
        """
        if permiteNulo==True:
            listTOdict_byTcld_ToString.listTOdict_BYTcld_SUPERPlus(listaStrKeys, listaDef, msgIntro, permiteNulo, esCapital)
        else:
            listTOdict_byTcld_ToString.listTOdict_TcldPlus(listaStrKeys, listaDef, msgIntro, permiteNulo, esCapital)
    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. No Permite Nulo
    # ********************
    @staticmethod
    def __introData_listTOdict_ByTcld(strValor):
        # permiteNulo=True
        valorLista = str(strValor.group()).capitalize()
        while True:
            retorno = input(f'intro {valorLista}..... ')
            # No Permite espacio vacio
            if retorno == '': 
                continue
            else:   
                break
        
        return retorno
    @staticmethod
    def listTOdict_byTcld_ToString(listaStrKeys=True):
        """ 
        Def => Devuelve un diccionario Segun una lista pasada como argumento pidiendo datos al usuario y almacenandolos en una lista. 
        No permite Introducir Vacio ( '' )
        listaStrKeys => [str] que son las keys del diccionario de retorno.
        Retorno => diccionario (k) los valores de listaStrKeys (v)Los valores str de los datos pedidos x Teclado. 
                None si algo va mal.
        
        Ejemplo => dict2 = listTOdict_byTcld_ToString.listTOdict_byTcld_ToString( ['nombre','dni' ,'tlf'] )

        Mejora: Introducir tratamiento de errores y 
                Introducir validacio de datos
        """
        if not isinstance(listaStrKeys, list): return None
        # patron = r'^[\w#$%/()\s]+$'
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'

        dictRetorno={ strKey:re.sub(patron, listTOdict_byTcld_ToString.__introData_listTOdict_ByTcld, strKey) 
                      for strKey in listaStrKeys }
        # print(dictRetorno)    
        return dictRetorno
    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
    # ********************
    @staticmethod
    def __intro_TcldPlus(strValor, options=None):
        """ 
        Llamada desde listTOdict_TcldPlus. 
        Se ejecuta para pedir datos al usuario y devolver el valor.
        Se pueden crear distintas opciones 
        [options] => diccionrio con pares clave:valor que se generan en la funcion listTOdict_TcldPlus y aqui se obtienen y tratan

        Ejemplo => dict2 = listTOdict_byTcld_ToString.listTOdict_TcldPlus( ['nombre','dni' ,'tlf'] , permiteNulo=True )        
        """
        # _____________________
        options = options or {}
        # _____________________
        permiteNulo = options.get('permiteNulo', False)  # Obtén 'permiteNulo' con un valor predeterminado de False
        esCapital = options.get('capital', False)  # Obtén 'permiteNulo' con un valor predeterminado de False
        msgIntro = options.get('msgIntro', False)  # Obtén 'permiteNulo' con un valor predeterminado de False

        # _____________________
        if esCapital:
            valorLista = str(strValor.group()).capitalize()
        else:
            valorLista = str(strValor.group())
        # _____________________
        while True:
            retorno = input(f'intro {valorLista}..... ')
            if retorno == '' and not permiteNulo:
                continue
            elif retorno == '' and permiteNulo:
                break
            else:
                # Validación o transformación adicional aquí
                break
        
        return retorno
    # ***************************************************
    # Funcion Que hace Tipado del diccionario una vez introducidos todos los datos.
        # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
        # Lo mas importate es que el analisis se hace Después de introducir los datos.
    # ***************************************************
    @staticmethod
    def listTOdict_TcldPlus(listaStrKeys, listaDef=None, permiteNulo=False, msgIntro='Intro', esCapital=False):
        """         
        Devuelve un diccionario solicitando datos al usuario según las claves de 'listaStrKeys' pero con los datos tipados
        
        Es una version del anterior pero añadiendo los datos a pasar a la funcion con lambda.
        ademas se permitenn mas datos en el dicicionario de entrada options y luego 
        se reciben en la funcion dedicada
        
        [listaStrKeys]  => lista de str que son las claves del diccionario de retorno.        
        [listaDef] => lista de listas/tuplas: 
                      (classType)[tipo], (bool)[permiteNulo] => [(int, True), (float, False),...]         
        [permiteNulo] => bool. =True Permite Nulo ByDef; =False, No permite Nulo ByDef.         
        [msgIntro] =>  str. Formato del menú de entrada. Es el mensaje antes de los valores de la lista.
        [esCapital] => bool. Formato del menú de entrada. Si quieres que las claves de la lista sean mostradas en may

        >>> Ejemplo => 
         dictRetorno = {
         strKey : re.sub(patron, 
                    lambda match: listTOdict_byTcld_ToString.__intro_TcldPlus(match, options), 
                    strKey) 
                    for strKey in listaStrKeys
        >>> 
        >>> re.sub (pattern, repl, string, count=0, flags=0)
         repl    => Cadena de texto o función con el valor que reemplazará las coincidencias del patrón en la cadena.
         string  => La cadena en la que se realizará la búsqueda y el reemplazo
         count (opcional) => Número máximo de reemplazos a realizar. Si se establece en 0, reemplazará todas las coincidencias
         flags (opcional) => Modificadores de la expresión regular, como re.IGNORECASE para hacer la búsqueda sin diferenciar entre mayúsculas y minúsculas.
        
        Esto crea un diccionario de (key)'nombre','dni' ,'tlf' (values) str y ''
        >>>    from validator import listTOdict_byTcld_ToString as VReg
        >>>    otherDict = VReg.listTOdict_TcldPlus(listaStrKeys=['Cuanto','Quieres','Entrar?'], permiteSp=True, esCapital=False)
        >>>    print(otherDict)
        """
        if not isinstance(listaStrKeys, list): 
            return None
        # ______________________
        # Patron valido: todos los caracteres,  n caracteres 
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        # ______________________
        # Opciones a pasar a la funcion __intro_TcldPlus().
        # Crear mas pares clave:valor para introducir mas parametros.
        options = { 'msgIntro':msgIntro,                # msgIntro strKey.... + introTeclado 
                    'permiteNulo': permiteNulo,                   # =True Permite Nulo Out of Teclado-> byDefecto,
                                                        # =False NO Permite Nulo Out of Teclado-> byDefecto
                    'capital':esCapital                 #letra capital para el valor de la key en el menú.
                    }
        # ______________________
        # Creo un diccionario con los argumentos opcionales que le quiero pasar a la 
        # funcion __intro_TcldPlus para que procese los datos introducidos.
        dictRetorno = {
            strKey:re.sub(patron, lambda match: listTOdict_byTcld_ToString.__intro_TcldPlus(match, options), strKey) for strKey in listaStrKeys
        }
        # _____________________
        # Esto hace que cuando se pasa una lista de Definicion [[int, True], [int, True], [int, True]] por Ejemplo
        # te devuelva el diccionario tipado.

        if dictRetorno:
            if listaDef:
                return listTOdict_byTcld_ToString.__tiparDiccionario(  diccionario = dictRetorno,
                                                            listaTipos  = listaDef)
            else:
                return dictRetorno
                
        else:
            return None
    
    # Valida las listas de entrada 
    def validaListasEntrada(listaKeys, listaDef):
        # Validamos listaKeys
        try:
            if isinstance(listaKeys, list) :
                for unaKey in listaKeys:
                    if isinstance(unaKey, str):
                        pass
        except:
            return None
        pass
        # Ahora validamos listaDef
        try:
            if isinstance(listaDef, list) :
                for unPar in listaDef:
                    for unaKey, unValor in listaDef:
                        if isinstance(unaKey, type):
                            pass
                        if isinstance(unValor, bool):
                            pass
        except:
            return None
        pass

    def __tiparDiccionario(diccionario, listaTipos):
        """ 
        Quiero Tipar el diccionario creado en listTOdict_TcldPlus proveniente de una lista de string
        donde todos los valores del diccionario son string.
        La idea que tengo es pasar una lista de listas [ [int, True] , [float, False] , [str, False] ]
                           
        >>> key_1:[intro_1, tipo_1  , True/False]
            key_2:[intro_2, listatipo_2  , True/False]
            key_n:[intro_n, listatipo_n  , True/False]

            Si el tipado da error, tengo que corregir a string
        """

        # _________________
        listaKeys=dict(diccionario).keys()
        listaVals=dict(diccionario).values()
        # _________________
        # IGUALA LA LONGITUD DE LAS LISTAS 
        # En funcion de listaKeys. (cambia la longitud de listaTipos)
        listaTipos=listTOdict_byTcld_ToString.__igualarListas(listaKeys=listaKeys, listaToReLong=listaTipos)
        # _________________
        # Ahora se recorre la lista de valores y se re-tipan: 
        listaValoresTipados=[]
        TIPO=0
        PERMITENULL=1       
        for i, valor in enumerate(listaVals):            
            # if PERMITENULL==False:            
            # ________________
            if listaTipos[i][TIPO]==int:
                try:
                    listaValoresTipados.append(int(valor))
                except Exception:
                    listTOdict_byTcld_ToString.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaTipos[i][PERMITENULL], tipo=listaTipos[i][TIPO])
            # ________________
            elif listaTipos[i][TIPO]==float:
                try:
                    listaValoresTipados.append(float(valor))                        
                except Exception:
                    listTOdict_byTcld_ToString.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaTipos[i][PERMITENULL], tipo=listaTipos[i][TIPO])
            # ________________
            elif listaTipos[i][TIPO]==str:                    
                listaValoresTipados.append(str(valor))
            # ________________
            elif listaTipos[i][TIPO]==bool:
                try:
                    listaValoresTipados.append(bool(valor))
                except Exception:
                    listTOdict_byTcld_ToString.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaTipos[i][PERMITENULL], tipo=listaTipos[i][TIPO])
            # ________________
            else:                    
                try:
                    listaValoresTipados.append(str(valor))
                except Exception:
                    listaValoresTipados.append(valor)
        # print(listaValoresTipados)
        pass
        # Ahora tengo una lista con los valores ya tipados.
        # y Compongo el diccionario con la listaKeys y listaValoresTipados.

        # =======================
        # 2 Formas de hacer el diccionario: 1-listas Comprension 2-zip()
        # _______________________
        # diccionarioRetorno={
        #     keyDicc:valorTipado for i, keyDicc in enumerate(diccionario)
        #                         for j, valorTipado in enumerate(listaValoresTipados) 
        #                             if i==j
        # }
        # print(diccionarioRetorno)        
        # _______________________
        diccionarioRetorno = dict(zip(listaKeys, listaValoresTipados))
        # print(diccionarioRetorno)
        pass
        return diccionarioRetorno

    def __igualarListas(listaKeys, listaToReLong):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.__igualarListas(listaKeys=listaKeys, listaToReLong=listaTipos)
        
        listaKeys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor.
        """
        if len(listaKeys)==len(listaToReLong):
            print("misma longitud")
        elif len(listaKeys)>len(listaToReLong):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[[str,False] for i, (k) in enumerate(listaKeys) if i >= len(listaToReLong)]
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

    def __excepcionTipado(permiteNulo, valor, tipo, lista):
        """ 
        Def => Pone los valores por defecto en la lista pasada, según el tipo que se pase.
        Es llamada cuando se produce una excepcion.
        """
        # _________________
        # SI permiteNulo , NO Valor => Hay que asignar un valor por defecto.
        if permiteNulo==True and valor == '':
            listTOdict_byTcld_ToString.__byDef(tipo=tipo, lista=lista)
        # _________________
        # SI permiteNulo, SI Valor(error de tipo)   => No va a dar problemas de conversión pq el valor venía de ser str
        elif permiteNulo==True and valor != '':
            if isinstance(valor, tipo):
                lista.append(tipo(valor))
            else:
                listTOdict_byTcld_ToString.__byDef(tipo=tipo, lista=lista)
        # _________________
        # NO permiteNulo, NO Valor. Acepta Nulo ('')
        elif permiteNulo==False and valor == '':
            lista.append(str(valor))
        # _________________
        # NO permiteNulo, SI Valor
        elif permiteNulo==False and valor != '':
            if isinstance(valor, tipo):
                lista.append(tipo(valor))
            else:
                listTOdict_byTcld_ToString.__byDef(tipo=tipo, lista=lista)           

    def __validarTipo(valor, tipo_dato):
        if isinstance(valor, tipo_dato):
            print(f"{valor} es de tipo {tipo_dato.__name__}")
            return True
        else:
            print(f"{valor} no es de tipo {tipo_dato.__name__}")
            return False

    def __byDef(tipo, lista):
        if tipo==int:
            lista.append(0)     #Valor por defecto
        elif tipo==float:
            lista.append(0.0)   #Valor por defecto
        elif tipo==str:
            lista.append('')    #Valor por defecto de str
        elif tipo==bool:
            lista.append(False) #Valor por defecto de bool(es engañoso)
        else:
            lista.append(None)  #Valor por defecto
        pass
    
    # *******************************************
    # Igual que listTOdict_TcldPlus() pero obliga (permiteNulo=True) a introducir el dato desde el  teclado correctamente

    # Funcion Que hace Tipado del diccionario EN EL MOMENTO DE ESCRIBIR LOS DATOS.
        # OBLIGA A INTRODUCIR EL DATO CORRECTO.
        # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
        # Lo mas importate es que el analisis se hace en el momento de Introducir los datos.
    # *******************************************
    @staticmethod
    def listTOdict_BYTcld_SUPERPlus(listaStrKeys=True, listaDef=None, msgIntro='Intro', permiteNulo=False, esCapital=False):
        """          
        Convierte una lista de entrada en un diccionario (key): valor lista ; (values): introTeclado.
        Te hace tipado si se introduce una lista de tipo(tipo),permiteNull(boolean) despues de introducir
        el dato, por lo que te obliga a meter el dato correcto.
        """
        # Validacion
        if not isinstance(listaStrKeys, list): 
            return None
        pass
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        pass
        # Diccionario de parametros 
        
        options = { 'msgIntro':msgIntro ,                
                    'permiteNulo': permiteNulo ,     
                    'capital':esCapital }
        pass
        dictRetorno = {
            strKey:re.sub(patron, 
                        lambda match: listTOdict_byTcld_ToString.__intro_BYTcldSuperPlus(match, listaDef[index] , options),
                        strKey) 
                        for index, strKey in enumerate(listaStrKeys)}
        pass
        # ______________
        # Retorno:
        if dictRetorno:
            if listaDef:
                # lo tipa y lo retorna
                return listTOdict_byTcld_ToString.__tiparDiccionario( diccionario = dictRetorno, listaTipos = listaDef )
            else:
                # Si no hay definicion de tipos/Nulos se queda con diccionario de (k)str (v)str
                return dictRetorno
        else:
            return None

    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
    # ********************
    @staticmethod
    def __intro_BYTcldSuperPlus(strValor, definicion, options=None):
        """ 
        Llamada desde listTOdict_BYTcld_SUPERPlus()
        
        >>> Ejemplo => dict2 = listTOdict_byTcld_ToString.listTOdict_TcldPlus( ['nombre','dni' ,'tlf'] , permiteNulo=True )        
        """
        # __________________
        # Validacion
        options = options or {}
        # __________________
        # Recogida de datos de entrada (se crean en la llamada)
        # permiteNulo = options.get('permiteNulo', False)  
        msgIntro  = options.get('msgIntro', False)  
        esCapital = options.get('capital', False)  
        # __________________
        TIPO=0
        PERMITENULL=1
        pass
        # print(definicion)
        # print(definicion[TIPO])
        # print(definicion[PERMITENULL])
        pass

        # __________________
        # Formato del texto para preguntar por Teclado
        if esCapital:
            valorLista = str(strValor.group()).capitalize()
        else:
            valorLista = str(strValor.group())
        pass

        # __________________
        # Pedimos datos por Teclado
        while True:
            retorno = input(f'{msgIntro} {valorLista}..... ')
            if retorno == '' and definicion[PERMITENULL]:
                break
            elif retorno == '' and not definicion[PERMITENULL]:
                continue
            else:
                try:
                    retorno=definicion[TIPO](retorno)                    
                except:
                    continue
                else:
                    break
        return retorno