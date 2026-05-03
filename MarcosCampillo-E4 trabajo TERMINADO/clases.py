class Propietario:
    def __init__(self,id,nombre,dni,fechanacimiento,direccion,email):
        self.__id = id
        self.__nombre = nombre
        self.__dni = dni
        self.__fechanacimiento = fechanacimiento
        self.__direccion = direccion
        self.__email = email
    def get__id(self):
        return self.__id
    def get__nombre(self):
        return self.__nombre
    def get__dni(self):
        return self.__dni
    def get__fechanacimiento(self):
        return self.__fechanacimiento
    def get__direccion(self):
        return self.__direccion
    def get__email(self):
        return self.__email
    def set__id(self, nuevoid):
        self.__id = nuevoid
    def set__nombre(self, nuevonombre):
        self.__nombre = nuevonombre
    def set__dni(self, nuevodni):
        self.__dni = nuevodni
    def set__fechanacimiento(self, nuevafechanacimiento):
        self.__fechanacimiento = nuevafechanacimiento
    def set__direccion(self, nuevadireccion):
        self.__direccion = nuevadireccion
    def set__email(self, nuevoemail):
        self.__email = nuevoemail
    def __str__(self):
        return f"El cliente número {self.get__id()} D. {self.get__nombre()}, con DNI: {self.get__dni()}, nacido el {self.get__fechanacimiento()}, con domicilio en {self.get__direccion()} y correo {self.get__email()}"

class Mascota:
    def __init__(self,id,idpropietario,nombre,tipo,raza,fechanacimiento,peso,color):
        self.__id = id
        self.__idpropietario = idpropietario
        self.__nombre = nombre
        self.__tipo = tipo
        self.__raza = raza
        self.__fechanacimiento = fechanacimiento
        self.__peso = peso
        self.__color = color

    def get__id(self):
        return self.__id
    def get__idpropietario(self):
        return self.__idpropietario
    def get__nombre(self):
        return self.__nombre
    def get__tipo(self):
        return self.__tipo
    def get__raza(self):
        return self.__raza
    def get__fechanacimiento(self):
        return self.__fechanacimiento
    def get__peso(self):
        return self.__peso
    def get__color(self):
        return self.__color
    
    def set__id(self, nuevoid):
        self.__id = nuevoid
    def set__idpropietario(self, nuevoidpropietario):
        self.__idpropietario = nuevoidpropietario
    def set__nombre(self, nuevonombre):
        self.__nombre = nuevonombre
    def set__tipo(self, nuevotipo):
        self.__dni = nuevotipo
    def set__raza(self, nuevaraza):
        self.__raza = nuevaraza
    def set__fechanacimiento(self, nuevafechanacimiento):
        self.__fechanacimiento = nuevafechanacimiento
    def set__peso(self, nuevopeso):
        self.__peso = nuevopeso
    def set__color(self, nuevocolor):
        self.__ = nuevocolor

    def __str__(self):
        return f"La mascota número {self.get__id()} llamada: {self.get__nombre()} del tipo {self.get__tipo()} nacida el {self.get__fechanacimiento()} con peso {self.get__peso()} tiene color {self.get__color()}"


