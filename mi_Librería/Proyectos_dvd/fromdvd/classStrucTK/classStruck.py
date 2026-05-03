import tkinter as tk
import copy

class MirrowStrucTK():
    """ 
    >>> Ejemplo Uso:
    >>> listaEstructura=[
            ["c:0", ["f:0","f:1","f:3"]], 
            ["c:1", "c:3"], 
            ["c:2"]
        ]
    SttK=MirrowStrucTK(listaEstructura=listaEstructura)
    """
    def __init__(self, listaEstructura):
        self.listaEstructura=listaEstructura
        self.numFilas=len(self.listaEstructura)
        self.cuentaListas=0
        self.numListasInternas=self.level(self.listaEstructura)
        # print(f'ClassMirrowStrucTK, Numero de Listas Totales: {self.cuentaListas}')
        # print(f'ClassMirrowStrucTK, Numero de filas de listaEstructura: {self.numFilas}')
        # print(f'ClassMirrowStrucTK, Numero de Listas internas Validas(>1 elemento): {self.cuentaListas-self.numFilas}')        
        
        # ______________________
        # Copia independiente de listaEstructura. 
        # import copy
        self.listaValues=copy.deepcopy(self.listaEstructura)
        # print(f'\nlistaValues = {self.listaValues}')
        # ______________________
        # Creo la listaKeys, que es la base de todos los elementos que hay en la listaEstructura
        self.listaKeys=self.getLista_ByEstructura(lista=self.listaEstructura)
        # print(f'\nlistaKeys = {self.listaKeys}')
        # ______________________
        # Creo el diccionario de key(listaKeys) , value(posicion)
        self.dictEstructura={key:self.getPosicion_ByObj(lista=listaEstructura, objBuscado=str(key)) for key in self.listaKeys}        
        # print(f'\nDiccionario (key-posicion)\n{self.dictEstructura}')        
        # ______________________
        # Validacion de la estructura(c o f ; repetidos):
        if self.validaEstructura()==False: 
            print("Estructura No Registrada")
            self.listaEstructura=None
            self.numFilas=None
            self.cuentaListas=None
            self.numListasInternas=None
            self.listaValues=None
            self.listaKeys=None
            self.dictEstructura=None
        else:
            print("Estructura Registrada ;)")
        pass
    
    def __str__(self):
        tit=f'\n{'*'*30} IMPRIMIR DATOS MirrowStrucTK {'*'*30}\n'
        uno=f'Numero de Items: {self.numFilas}\n'
        dos=f'Estructura: {self.listaEstructura}\n'
        tres=f'listaKeys: {self.listaKeys}\n'
        tres=f'listaValues: {self.listaValues}\n'
        cuatro=f'Diccionario key:posicionEstruct: \n{self.dictEstructura}\n'
        cinco=f'Numero de listas internas: {self.cuentaListas}\n'
        seis=''
        for i, item in enumerate(self.listaEstructura):
            seis=seis+(f'item {i}: {item}\n')
        fin=f'{'='*90}'
        return tit+uno+dos+tres+cuatro+cinco+seis+fin


    def getFila(self, indexFila):
        """ 
        Def: obtiene una sola item, pasada como argumento.
        """
        if 0<=indexFila<len(self.listaEstructura):
            return self.listaEstructura[indexFila]
        pass

    def copiarLista(self, lista):
        # Si el elemento es una lista, realiza una copia recursiva
        if isinstance(lista, list):
            return [self.copiarLista(sublista) for sublista in lista]
        # Si no es una lista, devuelve el elemento directamente
        else:
            return lista

    # ===============================
    def validaEstructura(self):
        conjListaElementos=set(self.listaKeys)

        listaChanges=[]
        if len(self.listaKeys)!=len(conjListaElementos):
            print("Error, Elemento Repetido")
            return False
        else:
            for i,key in enumerate(self.listaKeys):
                filcol=key.split(sep=':')                
                if str(filcol[0]).lower()=='c' or str(filcol[0]).lower()=='f':
                    continue
                else:
                    listaChanges.append([i, key])
        pass
        if listaChanges:
            # print(listaChanges)
            print("\nErrores entrada en listaEstructura")
            for i in range(len(listaChanges)):
                posicion=self.getPosicion_ByObj(objBuscado=listaChanges[i][1])
                nivel=len(posicion)

                print(f'indice en listaKeys: {listaChanges[i][0]} - valor: {listaChanges[i][1]} => [valores válidos: c ó f]')
            return False

        return True

    # ===============================
    def level(self, lista):
        """ 
        Def: Funcion Recursiva, Que cuenta el numero de listas que hay en una lista pasada.
        """        
        resultado = []  # Lista para almacenar todos los elementos
        # self.cuentaListas=0
        for elemento in lista:
            if isinstance(elemento, list):
                if len(elemento)==1:    #No cuenta con las listas de un sólo elemento
                    pass
                else:
                    self.cuentaListas+=1

                self.level(elemento)
        
        return self.cuentaListas

    # ===============================
    def getPosicion_ByObj(self, objBuscado, lista=None, posicion=None):
        if posicion is None:
            posicion = []  # Inicializar la posicion como una lista vacía
        if not lista: lista=self.listaEstructura

        for indice, elemento in enumerate(lista):
            # Agregar el índice actual a la posicion
            NewPosicion = posicion + [indice]

            if isinstance(elemento, list):
                # Llamar recursivamente si el elemento es otra lista
                resultado = self.getPosicion_ByObj(objBuscado=objBuscado, 
                                                    lista=elemento, 
                                                    posicion=NewPosicion)
                if resultado is not None:
                    return resultado  # Si se encontró el objBuscado, devolver la posicion                
            elif elemento == objBuscado:
                return NewPosicion  # Devolver la posicion si se encontró el objBuscado

        return None  # Devolver None si no se encontró el objBuscado en esta lista

    # ===============================
    def getItem_ByPosicion(self, lista, posicion):
        elemento = lista
        try:
            for indice in posicion:
                elemento = elemento[indice]  # Navega al siguiente nivel usando el índice
            return elemento
        except (IndexError, TypeError):
            return None

    # =============================== no usada
    def set_theList_ByPosicion(self, lista, posicion, NewValue):
        item = lista
        reList=[]
        try:
            for indice in posicion:
                item = item[indice]  # Navega al siguiente nivel usando el índice

            print(lista[0][1][0])
            lista[0][1][0]=True
            print(lista[0][1][0])
        except (IndexError, TypeError) as e:
            print(e)
            return None

    # ===============================
    def getLista_ByEstructura(self, lista):
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
                resultado.extend(self.getLista_ByEstructura(elemento))
            else:
                # Añadir elementos que no son listas directamente a resultado
                resultado.append(elemento)

        return resultado

    # ===============================
    def update(self, viejo_valor, nuevo_valor):
        # 1ª Forma
        posicion_valor = self.getPosicion_ByObj(viejo_valor)
        # 2ª Forma
        if viejo_valor in self.listaKeys:
            posicion_valor = self.dictEstructura[viejo_valor]
        else:
            return False

        if not posicion_valor: return False
        self.__updateItem(lista=self.listaValues, posicion=posicion_valor, nuevo_valor=nuevo_valor)
        if not self.listaValues: 
            return False
        return True
        
    # ===============================
    def __updateItem(self, lista, posicion, nuevo_valor):
        """ 
        Def: Actualiza un valor en la copia de listaEstructura de valores listaValues
        se pasa una lista posicion y 
        """
        elemento = lista
        try:
            # Navegar hasta el penúltimo nivel
            for i in range(len(posicion) - 1):
                elemento = elemento[posicion[i]]
            # Cambiar el valor en la posición especificada
            elemento[posicion[-1]] = nuevo_valor
            return lista
        except (IndexError, TypeError):
            return None    
    
    
    # =========================================
    def printEstructura(self):
        for i, item in enumerate(self.listaEstructura):
            print(f'item {i}: {item}')
