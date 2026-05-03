class Cliente():
    contador=0
    def __init__(self, nombre, edad, dni, peso, altura, sexo='H'):
        self.dictClientesRam={}
        pass

    def __str__(self):
        pass

    
    def addCliente(self, nombre, edad, dni, peso, altura, sexo='H'):
        """
        Añade un cliente en el diccionario de clientes.
        """
        self.dictClientesRam={'nombre':nombre,'edad':edad, 'dni':dni, 'peso':peso, 'altura':altura, 'sexo':sexo}
        contador +=1
        pass

    def delCliente(self, nombredni):
        """
        Elimina un cliente en el diccionario de clientes.
        """
        pass

    def updateCliente(self, nombredni):
        """
        Busca un cliente en el diccionario de clientes.
        Si lo encuentra le cambia los datos. (ya veré si con un menu o con una lista o diccionario)
        """
        pass

    def esMayor(self, nombredni):
        """
        Devuelve True o False si el cliente buscado es mayor de edad o menor.
        """
        pass

    def buscaSexo(self, nombredni):
        """
        Devuelve el sexo del cliente por su nombre o por su dni
        """
        pass
    
    def menuCliente(self, listaMenu):
        """
        Define el menu de acciones sobre el cliente.
        """
        pass
    
class ClienteNutricion(Cliente):
    """
    Hereda de un cliente y le añade la funcionalidad de nutricion calcularImc()
    """
    def __init__(self, nombre, edad, dni, peso, altura, sexo='H'):
        super().__init__(nombre, edad, dni, peso, altura, sexo='H')
        print(super())
        pass

    def __str__(self):
        pass

    def calcularImc(self, nombredni):
        """
        Calcula el Indice de masa corporal Imc=peso/altura**2
        de un cliente e imprime. 
        
        nombre - sexo - altura - imc
        """
        pass
