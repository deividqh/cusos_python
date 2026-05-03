from validator import ValidReg as VReg

class Cliente():
    def __init__(self, listaIntro):        
        self.listaClientes=[]           #Lista de clientes de 1 instancia.
        self.listaIntro = listaIntro    #Lista con los nombres de las keys del diccioario de cliente.

        # dictClienteRAM=Cliente.introData(self.listaIntro)  #Introduccion de los datos de self.listaIntro

        # self.dictLastCliente = dictClienteRAM   
        # Añade el diccionario de cliente en la listaClientes
        # self.listaClientes.append(dictClienteRAM)   

    def __str__(self):
        pass
    
    # def introList(self, lista):
    #     for n in lista:
    def getListaClientes(self):
        return self.listaClientes

    def introData(self, listaIntro, cliente=None):
        """ 
        Def: Pide los datos del diccionario al usuario y los valida.        
        [listaIntro] => Es una lista con las keys del diccionario de Clientes.
        [cliente] => En caso de Update, se introduce el cliente a actualizar.
                     En caso de Add, no se introduce o None.
        Return: diccionario con los valores asignados por teclado a las claves pasadas.
        None si hay algún error.
        objCliNutr.introData(objCliNutr.getListaClientes())
        """
        # if listaIntro==self.listaClientes:
        #     pass
        # for n in listaIntro:
        #     pass
        dictReturn={}
        print('Intro Data Cliente')
        # _______
        if 'nombre' in listaIntro:
            while True:
                nombre=input("Intro Nombre........").strip()
                # _________________
                # Obligatorio
                if nombre=='':
                    if cliente:
                        nombre=cliente['nombre']
                        break
                    else:
                        continue
                else:
                    if VReg.esFrase(nombre): break
                    else: continue
            dictReturn['nombre']=nombre
        # _______
        if 'dni' in listaIntro:
            while True:
                dni=input("Intro DNI........").strip()
                # _________________
                # Obligatorio
                numero, letra = VReg.partirDNI(dni)
                if numero==None or letra==None:
                    continue
                else:
                    dni=numero+'-'+letra.upper()
                    break
            dictReturn['dni']=dni
        # _______
        if 'edad' in listaIntro:
            while True:
                edad=input("Intro Edad........").strip()
                # _________________
                # No Obligatorio. (Si pulsa Intro).
                if edad == '':
                    if cliente:
                        edad=cliente['edad']
                    break                    
                else:
                    edad = VReg.esInt(edad)
                    if edad: break
                    else: continue

            dictReturn['edad']=edad
        # _______
        if 'peso' in listaIntro:
            while True:
                peso=input("Intro Peso........").strip()
                # _________________
                # No Obligatorio. (Si pulsa Intro).
                if peso == '': 
                    if cliente:
                        peso=cliente['peso']
                    break
                else:
                    peso = VReg.esFloat(peso)
                    if peso: break
                    else: continue

            dictReturn['peso']=peso
        # _______
        if 'altura' in listaIntro:
            while True:
                altura=input("Intro Altura........").strip()
                # _________________
                # No Obligatorio. (Si pulsa Intro). 
                # Si existe ese cliente le asigno su anterior valor. si no, ingresa ''
                if altura == '': 
                    if cliente:
                        altura=cliente['altura']
                    break
                else:
                    altura = VReg.esFloat(altura)
                    if altura: break
                    else: continue
            dictReturn['altura']=altura
        # _______
        if 'sexo' in listaIntro:
            while True:
                sexo = input("Intro sexo('H' o 'M')........").strip().upper()
                if sexo == '':
                    if cliente:
                        sexo=cliente['sexo']
                    else:
                        sexo='H'
                    break
                # _________________
                # Obligatorio entre dos valores
                else:
                    if VReg.estaEnLista(sexo, ['H', 'M']): break
                    else: continue
            dictReturn['sexo']=sexo
        # ______________________
        # Una vez recojo los datos Los meto en un diccionario y retorno
        return dictReturn
        # return {'nombre':nombre,'edad':edad, 'dni':dni, 'peso':peso, 'altura':altura, 'sexo':sexo}

    def addCliente(self):
        """
        Añade un cliente en el diccionario de clientes.
        """
        # _______________
        # Introduccion de los datos X teclado
        dictClienteRAM=self.introData(self.listaIntro)  
        self.listaClientes.append(dictClienteRAM)       

        return dictClienteRAM

    def delCliente(self, nombredni):
        """
        Elimina un cliente en el diccionario de clientes.
        """
        cliente=self.searchCliente(nombredni=nombredni)
        if not cliente:
            return None
        clienteRetorno = VReg.copyDict(cliente)

        self.listaClientes.pop(self.searchIndexCliente(nombredni))
        return clienteRetorno
        # print (f'Cliente {cliente['nombre']} Eliminado OK')

    def updateCliente(self, nombredni):
        """
        Busca un cliente en el diccionario de clientes.  
        Si lo encuentra le cambia los datos. (ya veré si con un menu o con una lista o diccionario)
        [nombredni] = str nombre o dni del cliente a actualizar
        """            
        cliente=self.searchCliente(nombredni=nombredni)
        if not cliente:
            print(f'Cliete {nombredni} no Encontrado')
            return None

        # Genero una lista de keys con los datos a recoger
        listaUpdate=['nombre', 'edad' , 'peso' , 'altura' , 'sexo']
        # ____________
        # Recibe un diccionario de datos validados de la lista introducida como key
        dictUpdate = self.introData(listaIntro=listaUpdate, cliente=cliente)
        # ____________
        # Recorro la lista de actualizacion y actualizo los datos en cliente
        for lu in listaUpdate:
            cliente[lu]=dictUpdate[lu]
        
        # Ver resultado....borrar.............quiero validar si al cambiar en cliente cambia en la lista.
        return cliente

    def esMayor(self, nombredni):
        """
        Devuelve True o False si el cliente buscado es mayor de edad o menor.
        [nombredni] = str nombre o dni del cliente a actualizar
        """
        cliente=self.searchCliente(nombredni=nombredni)
        if cliente:
            return 'Mayor' if cliente['edad']>=18 else 'Menor'

    def getSexo(self, nombredni):
        """
        Def => Devuelve el sexo del cliente por su nombre o por su dni
        [nombredni] => str nombre o dni del cliente a actualizar
        Retorno => 'Mujer', 'Hombre'
        """
        cliente=self.searchCliente(nombredni=nombredni)
        if cliente:
            return 'Mujer' if cliente['sexo'] == 'M' else 'Hombre'

    def searchCliente(self, nombredni):
        """ 
        Def => Busca un cliente en el diccionario de clientes y 
        devuelve la clave y el indice o None si no lo encuentra
        [nombredni] => str nombre o dni del cliente a actualizar
        Retorno => dict cliente de la lista de clientes.
        None si no lo encuentra.
        """
        for n in self.listaClientes:
            if nombredni == n['nombre']: return n
            if nombredni == n['dni']:    return n
        return None

    def searchIndexCliente(self, nombredni):
        """ 
        Def => Busca un cliente en el diccionario de clientes y 
        devuelve la clave y el indice o None si no lo encuentra
        [nombredni] => str nombre o dni del cliente a actualizar
        Retorno => dict cliente de la lista de clientes.
        None si no lo encuentra.
        """
        for i,n in enumerate(self.listaClientes):
            if nombredni == n['nombre']: return i
            if nombredni == n['dni']:    return i
        return None

class ClienteNutricion(Cliente):
    """
    Hereda de un cliente y le añade la funcionalidad de nutricion calcularImc()
    """
    def __init__(self, listaIntroCliente):
        # ______________
        # Llamo al constructor del padre
        super().__init__(listaIntroCliente)
        self.listaIntroCliente=listaIntroCliente

    def __str__(self):
        pass

    def calcularImc(self, nombredni):
        """
        Calcula el Indice de masa corporal Imc=peso/altura**2
        de un cliente e imprime. 
        
        nombre - sexo - altura - imc
        """
        cliente=self.searchCliente(nombredni=nombredni)
        if not cliente:
            print(f'Cliente{nombredni} No Encontrado :( ')
            return 0
        if cliente['peso']=='':
            peso = 0
        else:
            peso = float(cliente['peso'])
        if cliente['altura']=='':
            altura=0
        else:
            altura= float(cliente['altura'])
            
        if altura==0 or peso==0:
            IMC = -1
        else:
            IMC = round(peso/(altura**2), 2)
        return IMC

