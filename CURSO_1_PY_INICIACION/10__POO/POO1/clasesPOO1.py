import datetime as dt

class Disco():
    contador=0
    def __init__(self, nombre,hOpen, hJornada=8, cod_vest=False):
        self.nombre=nombre         
        self.hOpen=hOpen    # Falta vaidacion o tratamiento excep. de momento me fío de que me digan "hh:mm"
        self.hJornada=hJornada
        self.cod_vest=cod_vest
        self.objDTIni = dt.datetime.strptime(self.hOpen, "%H:%M")
        # Uso el metodo replace de datetime para reemplazar la fecha por defecto por la del dia de hoy
        self.objDTIni=self.objDTIni.replace( year=dt.datetime.now().year, 
                                             month=dt.datetime.now().month, 
                                            day=dt.datetime.now().day  )

        # --- A partir de la hora de inicio le sumo lo que dura la jornada de la discoteca
        jornada = dt.timedelta(hours=self.hJornada)
        # --- Creacion de la fechaHora de cierre.
        self.objDtClose = self.objDTIni + jornada
        self.hClose=self.objDtClose.time().strftime("%H:%M")
        
    def __str__(self):
        return f'Taberna: {self.nombre}\tHorario, Desde: {self.hOpen} Hasta Las {self.hClose}'

    # NO FUNCIONA LA SOBRECARGA :(         PREGUNTAR A LORETO.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # O MIRA, YA TENGO ALGO QUE ME INTERESA EL FINDE ;)
    # Quizá igualando a none el parametro  y validando isisnstance[1param(str), 
    #       2 param(int, int)] o none? 
    #       Y SI ME PONGO: UNA LISTA, UNA TUPLA....NO, ESTO ME HUELE A QUE NECESITA 
    #       UNOS TIPOS ACORDADOS(PEJ "HH:MM" Y int(HHH), int(MM)) y luego 
    #       EXCEPCIONES(try except)......mmmmmmmm

    # La discoteca abre de momento todos los días    
    # def esAbierta(self, laHora=dt.datetime.now().strptime("%H:%M")):        
    #     """ 
    #     Def: Para saber si la Disco esta abierta o cerrada. Se pueden introducir los parametros o no y tomará la hora y minutos actuales.
    #     Es una funcion sobrecargada de esAbierta.
    #     Args:
    #         [laHora] opcional, valor por defecto ("horaNow():minNow()")
    #     Return: devuelve booleano si la Discoteca instanciada esta abierta o cerrada
    #     """
    #     # --- dateTime de hoy-ahora
    #     dtHoyAhora=dt.datetime.now()
    #     # --- ...y le meto la hora y minutos. Como es un str lo que entra. 
    #     ctimeLaHora = dt.datetime.strptime(laHora, "%H:%M"
    #     if isinstance(laHora, str):
    #         dtLaFecha = dtHoyAhora.replace(hour=ctimeLaHora.hour, minute=ctimeLaHora.minute)
    #     else:
    #         return None

    #     # ---------- comparacion de fechaHora de apertura y cierre con hoy-Ahora
    #     if self.objDTIni <= dtLaFecha <= self.objDtClose:
    #         print(";)", self.objDTIni , dtLaFecha , self.objDtClose, sep="\n\t")
    #         return True
    #     else:
    #         print(":(", self.objDTIni , dtLaFecha , self.objDtClose, sep="\n\t")
    #         return False
    # -------------------------------------
    def esAbierta(self, laH=dt.datetime.now().hour, elM=dt.datetime.now().minute):        
        """ 
        Def: Para saber si la Disco esta abierta o cerrada. Se pueden introducir los parametros o no y tomará la hora y minutos actuales.
        Args:
            [laH] opcional, valor por defecto int(hora actual)
            [elM] opcional, valor por defecto int(minutos actual)
        Return: devuelve booleano si la Discoteca instanciada esta abierta o cerrada
        """
        # --- dateTime de hoy-ahora
        dtHoyAhora=dt.datetime.now()
        # --- ...y le meto la hora y minutos introducidos o no
        if 0 <= laH <=23:
            if 0 <= elM <=59:
                dtLaFecha=dtHoyAhora.replace(hour=laH, minute=elM)
            else:
                return None
        else:
            return None

        # ---------- comparacion de fechaHora de apertura y cierre con hoy-Ahora
        if self.objDTIni <= dtLaFecha <= self.objDtClose:
            print(";)", self.objDTIni , dtLaFecha , self.objDtClose, sep="\n\t")
            return True
        else:
            print(":(", self.objDTIni , dtLaFecha , self.objDtClose, sep="\n\t")
            return False
    # -------------------------------------
    # Definir si la disco tiene codigo de vestimenta o pasa cualquiera.    
    def esCod_Vest(self):
        pass

    def restaHorasDias():
        # Hora de entrada: viernes a las 23:00
        entrada = datetime(2024, 10, 11, 23, 0, 0) 
        
        # Hora de salida: sábado a las 3:00 (día siguiente)
        salida = datetime( 2024, 10, 12, 3, 0, 0)  
        
        # la diferencia entre dos fechas devuelve un objeto 'timedelta'
        diferencia = salida - entrada
        print(diferencia)
        diferencia = entrada - salida
        print(diferencia)
        # Mostrar la diferencia en horas y minutos
        horas, resto = divmod(diferencia.seconds, 3600)
        minutos = resto // 60
        print(f"Estuviste en la discoteca por {horas} horas y {minutos} minutos.")

    
# ------------------------------


class Cultivo():
    contador=0
    def __init__(self, nombre, variedad, fechaSiembra, fechaCosecha , estado = 'No iniciado'):
        self.nombre=nombre         
        self.variedad=variedad
        self.fechaSiembra=fechaSiembra 
        self.fechaCosecha=fechaCosecha
        self.estado=estado        
        
    def __str__(self):
        return f'Nombre del Cultivo: {self.nombre}\tvariedad: {self.variedad}'

    def iniCosecha(self):
        pass
    def finCosecha(self):
        pass
    def diasToCosecha(self):
        pass

# ------------------------------

class Autor():
    contador=0
    def __init__(self, nombre, annoNac):
        self.nombre=nombre         
        self.annoNac=annoNac
        
    def __str__(self):
        return f'Nombre Autor: {self.nombre}\tNacimiento: {self.annoNac}'


class Libro():
    contador=0
    def __init__(self, titulo, autor, annoPubli, leido=False):
        self.nombre=titulo         
        self.autor=autor         
        self.annoPubli=annoPubli         
        self.leido=leido         
        
        
    def __str__(self):
        return f'Nombre Autor: {self.nombre}\tNacimiento: {self.annoNac}'
    def esLeido():
        pass
    def cambiarLeido(leido=False):
        pass