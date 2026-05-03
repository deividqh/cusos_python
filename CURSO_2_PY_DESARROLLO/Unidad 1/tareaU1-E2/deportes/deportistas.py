from validator import ValidReg as ValE

class Sport():
    __listaTenis=['Gran Slam', 'Tierra Batida']
    __listaBasquet=['Olimpiadas', 'NBA']
    __listaFutbol=['Mundial']
    __listaTorneos={*__listaTenis,*__listaBasquet,*__listaFutbol}    #No la uso
    def __init__(self):        
        """ 
        Constructor de clase Sport => 
        incorporará algunas de las características comunes que tienen los deportistas.
        """
        self.__listDictSport=[]     #Diccionario ppal de la clase Sport
        
        dictSport={'deporte':'tenis','torneo':Sport.__listaTenis}
        self.__listDictSport.append(dictSport)
        
        dictSport={'deporte':'basquet','torneo':Sport.__listaBasquet}
        self.__listDictSport.append(dictSport)

        dictSport={'deporte':'futbol','torneo':Sport.__listaFutbol}
        self.__listDictSport.append(dictSport)
 

    def __str__(self):
        None
    
    # ***********
    # Getters & Setters
    # ***********
    def getListDictSport(self):
        return self.__listDictSport          
    
    # ***********
    # Getters de la Clase Sport
    # ***********
    def getListTorneosByDeporte(self, strKey=''):
        """ 
        Def => devuelve un diccionario Sport por la Clave('Deporte')    
        """
        strKey=strKey.strip()
        listReturn =  [deporte['torneo'] for deporte in self.__listDictSport                                 
                                            if deporte['deporte'] == strKey ]
        return listReturn if listReturn else None
    
    def getListDeportes(self):
        """ 
        Def => Devuelve la lista de los deportes 
            listaDeportes = []
            for n in self.__listDictSport:
                listaDeportes.append(n['deporte'])
        """
        listaDeportes=[n['deporte'] for n in self.__listDictSport]
        return listaDeportes  if listaDeportes else None          
    
    def getListTorneosByIndex(self, index=0):
        """ 
        Def => Devuelve la lista de los Torneos que tiene un deporte segun el indice de entrada.
        index => el indice de self.__listDictSport        
            # listaTorneos = []
            # for i,n in enumerate(self.__listDictSport):
            #     if i==index: 
            #         listaTorneos.append(n['torneo'])
        """
        listaTorneos=[ v for i,dictDeporte in enumerate(self.__listDictSport)
                            for v in dictDeporte.values()
                                    if i==index]
        
        return listaTorneos[1]  if listaTorneos[1] else None          
    
    def getDeporteByIndex(self, index=0):
        """ 
        Def => Devuelve deporte segun el indice de entrada.
        index => el indice de self.__listDictSport        
        """
        deporte=[ n['deporte'] for i,n in enumerate(self.__listDictSport) if i==index]
        return ''.join(deporte) if deporte else None

    def getIndexByDeporte(self, strKey):
        """ 
        Def =>  index = getIndexByDeporte('tenis') 
        Devuelve la posicion del deporte pasado en self.___listDictSport
        [strkey] => str, deporte('tenis', 'futbol'... )
        """
        if not strKey in self.getListDeportes(): return None
        for i,n in enumerate(self.__listDictSport):
            if str(n['deporte']).upper()==str(strKey).upper(): 
                return i
        return -1

    def getDictSport(self, strKey):
        """ 
        Obtiene el diccionario  de la key pasada como argumento. 
        strKey => Puede ser un indice o un deporte
        """
        # Si entra indice
        if isinstance(strKey,int): 
            strKey=self.getDeporteByIndex(strKey)
            if not strKey: return None
        # Si entra deporte
        dictRetorno={k:v for n in self.__listDictSport 
                            for k,v in dict(n).items()
                                if n['deporte']==strKey}

        return dictRetorno if dictRetorno else None

class Deportista(Sport):
    """
    Noto que tengo problemas con el polimorfismo. 
    Creo que esto tiene que ser mas sencillo. 
    Este codigo esta muy bien, pero siento que me he alejado del motivo del ejercicio.
    Preguntar Loreto

    Ejemplo de self.listaDeportistas:
    [{  'nombre': 'jordan', 
        'edad': 34, 
        'titulos': [{'torneo': 'Olimpiadas', 'numtitulos': 2}, {'torneo': 'NBA', 'numtitulos': 6}],
        'caracteristicas': 'la cabra'
    }]
    """
    def __init__(self):
        
        super().__init__()

        # Los datos que se van a pedir de los Deportistas por teclado al usuario
        self.listaIntro=['nombre', 'edad', 'titulos', 'caracteristicas', 'deporte']

        # lista de diccionarios deportista PPal de la app
        self.listaDeportistas=[]    

    def __str__(self):
        return self.getListDictSport()
    
    # ***********
    # Getters & Setters
    # ***********
    def getListaIntro(self):
        return self.listaIntro
    # ***********
    # C.R.U.D
    # ***********
    def introData(self, listaIntro, diccRAM=None, indexTitulo=0):
        """ 
        Def: Pide los datos del diccionario al usuario y los valida.        
        [listaIntro] => Es una lista con los datos a guardar de los deportista.
        [diccRAM] => En caso de Update, se introduce el diccRAM a actualizar.
                     En caso de Add, no se introduce o None.
        Return: diccionario con los valores asignados por teclado a las claves pasadas.
        None si hay algún error.

        obj_1.introData(obj_1.getlistaSport())
        """
        # if listaIntro==self.__listaSport:
        #     pass
        # for n in listaIntro:
        #     pass
        dictReturn={}
        print('Intro Data Deportista')
        # _______
        if 'nombre' in listaIntro:
            while True:
                nombre=input("Intro Nombre........").strip()
                # _________________
                # Obligatorio
                if nombre=='':
                    if diccRAM:
                        nombre=diccRAM['nombre']
                        break
                    else:
                        continue
                else:
                    if ValE.esFrase(nombre): break
                    else: continue
            dictReturn['nombre']=nombre
        # _______
        if 'edad' in listaIntro:
            while True:
                edad=input("Intro Edad........").strip()
                # _________________
                # No Obligatorio. (Si pulsa Intro).
                if edad == '':
                    if diccRAM:
                        edad=diccRAM['edad']
                    break                    
                else:
                    edad = ValE.esInt(edad)
                    if edad: break
                    else: continue

            dictReturn['edad']=edad
        # _______
        if 'titulos' in listaIntro:
            listDictTitulos=[]
            listTorneos = self.getListTorneosByIndex(index=indexTitulo-1)
            # newDict = VReg.listTOdict_byTcld_ToString(listTorneos)
            
            for torneo in listTorneos:
                while True:
                    numtitulos=input(f"Intro Número de {torneo}........ ").strip()
                    numtitulos = ValE.esInt(numtitulos)
                    dictTitulos={}
                    if numtitulos:
                        dictTitulos['torneo']=torneo
                        dictTitulos['numtitulos']=numtitulos
                        listDictTitulos.append(dictTitulos)
                        break                            
                    else:
                        continue               

            dictReturn['titulos']=listDictTitulos

        # _______
        if 'caracteristicas' in listaIntro:
            while True:
                caracteristicas = input("Intro caracteristicas(Opcional)........").strip()
                if caracteristicas == '':
                    if diccRAM:
                        caracteristicas=diccRAM['caracteristicas']
                    break
                # _________________
                # Frase
                else:
                    if ValE.esFrase(caracteristicas): break
                    else: continue
            dictReturn['caracteristicas']=caracteristicas
        # ______________________
        # Una vez recojo los datos Los meto en un diccionario y retorno
        return dictReturn

    def add(self, indexDeporte):
        """
        Añade 
        [indexDeporte] => Int, es el indice del diccionario dictSport de la clase padre.

        'nombre', edad, [strTitulos], caracteristicas
        """        
        deporte = self.getDeporteByIndex(indexDeporte-1)

        dictRAM=self.introData(self.listaIntro, None, indexDeporte)  #Introduccion de los datos de self.__listaIntro
        dictRAM['deporte']=deporte
        self.listaDeportistas.append(dictRAM)

        print(f"\n{'_'*40}\n{dictRAM['nombre']} add OK")    
        return dictRAM
    
    def delete(self, strKey):
        """
        Elimina 
        """
        diccRAM=self.buscar(strKey=strKey)
        if not diccRAM:
            return None
        dictRetorno = ValE.copyDict(diccRAM)

        self.listaDeportistas.pop(self.buscarIndex(strKey))
        return dictRetorno
    
    def update(self, strKey):
        """
        Actualiza
        [strKey] = str nombre o dni del diccRAM a actualizar
        """            
        diccRAM=self.buscar(strKey=strKey)
        if not diccRAM:
            print(f'deportista {strKey} no Encontrado')
            return None

        # Genero una lista de keys con los datos a recoger
        listaUpdate=['nombre', 'edad' , 'titulos' , 'caracteristicas']
        # ____________
        # Recibe un diccionario de datos validados de la lista introducida como key
        dictUpdate = self.introData(listaIntro=listaUpdate, diccRAM=diccRAM)
        # ____________
        # Recorro la lista de actualizacion y actualizo los datos en diccRAM
        for lu in listaUpdate:
            diccRAM[lu]=dictUpdate[lu]
        
        # Ver resultado....borrar.............quiero validar si al cambiar en diccRAM cambia en la lista.
        return diccRAM
    
    def buscar(self, strKey):
        """ 
        Def => Busca un diccionario en la lista de diccionario de deportistas         
        [strKey] => str clave a buscar.
        Retorno => dict de la lista de diccionarios.
        None si no lo encuentra.
        """
        for n in self.listaDeportistas:
            if str(strKey).lower() == str(n['nombre']).lower(): return n
        return None

    def imprimir(self, dictDeportista):
        print(f"\n{str(dictDeportista['nombre']).capitalize()} - {dictDeportista['deporte']} - {dictDeportista['edad']} años ")
        for palmares in dictDeportista['titulos']:            
            print(f"\t{palmares['torneo']}, Numero Títulos: {palmares['numtitulos']}")            
        print(f"\tComment: {dictDeportista['caracteristicas']}")
    
    def printAll(self, strDeporte):
        for deportista in self.listaDeportistas:
            self.imprimir(deportista)


    


    

    