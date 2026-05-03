# Principales códigos de formato (strftime):
    # %Y: Año completo (2024)
    # %m: Mes (01-12)
    # %d: Día del mes (01-31)
    # %H: Hora (00-23)
    # %M: Minutos (00-59)
    # %S: Segundos (00-59)

from datetime import date

def ejemplo_date():
    # Obtener la fecha de hoy
    hoy = date.today()
    print("Hoy es:", hoy, "tipo:",type(hoy) )

    # Crear una fecha específica
    fecha_nacimiento = date(1990, 4, 15)
    print("Fecha de nacimiento:", fecha_nacimiento, "tipo:",type(fecha_nacimiento))

    # Comparar fechas
    resultado = fecha_nacimiento < hoy
    resultado = hoy - fecha_nacimiento
    resultado = fecha_nacimiento - hoy
    
    print(f"Resultado: {resultado}, tipo: {type(resultado)}")
    if fecha_nacimiento < hoy:
        print("La fecha de nacimiento es anterior a hoy.")
    else:
        print("La fecha de nacimiento es posterior o igual a hoy.")

ejemplo_date()
# ------------------------------------------
from datetime import time

def ejemplo_time():
    # Crear una hora específica
    hora_comida = time(13, 30, 0)  # 13:30:00
    print("Hora de la comida:", hora_comida, "tipo: ", type(hora_comida))

    # Acceder a los componentes de la hora
    print(f"Hora: {hora_comida.hour}, Minuto: {hora_comida.minute}, Segundo: {hora_comida.second}")
    print("Tipo de hora: ",type(hora_comida.hour))
ejemplo_time()
# ------------------------------------------
from datetime import datetime

def ejemplo_datetime():
    # Obtener la fecha y hora actual
    ahora = datetime.now()
    print("Fecha y hora actuales:", ahora, "tipo: ", type(ahora))

    # Crear un objeto datetime específico
    evento = datetime(2023,12, 25, 10, 0, 0)  # 25 de diciembre de 2023, 10:00:00
    print("Fecha y hora del evento:", evento, "tipo: ", type(evento))


    # Comparar con la fecha y hora actual
    if evento > ahora:
        print("El evento es en el futuro.")
    else:
        print("El evento es en el pasado.")

ejemplo_datetime()
# ------------------------------------------
from datetime import datetime, timedelta

def ejemplo_timedelta():
    # Diferencia de 5 días
    diferencia = timedelta(days=5)
    print(type(diferencia))    
    print(diferencia)

    # Sumar esa diferencia a la fecha actual
    diaHoy=datetime.now().date().day
    hoy = datetime.now()
    futuro = hoy + diferencia
    print("Fecha actual:", hoy)
    print("Fecha en 5 días:", futuro)

    # Restar días
    pasado = hoy - diferencia
    print("Fecha hace 5 días:", pasado)

ejemplo_timedelta()
# ------------------------------------------
from datetime import datetime

def ejemplo_strftime():
    ahora = datetime.now()
    # Formato personalizado: Día/Mes/Año - Hora:Minuto
    formateado = ahora.strftime("%d/%m/%Y - %H:%M")
    print("Fecha y hora formateadas:", formateado)

ejemplo_strftime()
# ------------------------------------------

from datetime import datetime, timedelta

def calcular_diferencia_horaria():
    # Hora de entrada: viernes a las 23:00
    entrada = datetime(2024, 10, 11, 23, 0, 0)  # Suponiendo un viernes 11 de octubre de 2024
    
    # Hora de salida: sábado a las 3:00 (día siguiente)
    salida = datetime( 2024, 10, 12, 3, 0, 0)  # Suponiendo sábado 12 de octubre de 2024
    
    # la diferencia entre dos fechas devuelve un objeto 'timedelta'
    diferencia = salida - entrada
    print(diferencia)
    diferencia = entrada - salida
    print(diferencia)
    # Mostrar la diferencia en horas y minutos
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos = resto // 60
    print(f"Estuviste en la discoteca por {horas} horas y {minutos} minutos.")

calcular_diferencia_horaria()