import datetime as dt

horaINI="21:30:00" 
# horaINI=dt.time.strftime("%H:%M:%S")
objDTIni = dt.datetime.strptime(horaINI, "%H:%M:%S")
print("objDateTimeInicial:",objDTIni,", Tipo:",  type(objDTIni))           # <class 'datetime.datetime'>
# Al crear un datetime a partir de una hora. la fecha es 1900-1-1. 
# Uso el metodo replace de datetime para reemplazar la fecha por la del dia de hoy
objDTIni=objDTIni.replace(  year=dt.datetime.now().year, 
                            month=dt.datetime.now().month, 
                            day=dt.datetime.now().day
                        )
print("objDateTimeInicial:",objDTIni,", Tipo:",  type(objDTIni))           # <class 'datetime.datetime'>

# ------------ Así puedo sacar la hora de un objeto datetime
# horaIni=objDTIni.time()    
# print("HoraIni Sacada de ObjDTINI:",horaIni,", Tipo:",type(horaIni))            #<class 'datetime.time'>

# ------------ Así puedo sacar la fecha de un objeto datetime
# fechaIni=objDTIni.date()
# print("FechaINI sacada de objDTINI:",fechaIni,", Tipo: ",type(fechaIni))

# --- A partir de la hora de inicio le sumo lo que dura la jornada de la discoteca
jornada = dt.timedelta(hours=8)
objDtClose = objDTIni + jornada
print("\nobjDateTimeCierre:",objDtClose,", Tipo:",  type(objDtClose))           # <class 'datetime.datetime'>

# --- dateTime de hoy-ahora
dtHoyAhora=dt.datetime.now()
print("dtHoyAhora:",dtHoyAhora,", Tipo:",type(dtHoyAhora))           

# --- DateTime de dia-hora Construida ------------- >
# --- DateTime de dia-hora Construida ------------- >
#------------------- Crear una fecha específica
diaX = dt.date(2024, 10, 11)
print("Fecha X:", diaX, "tipo:",type(diaX))
#------------------- Crear una hora específica
horaX = dt.time(23, 30, 0)  # 13:30:00
print("Hora X:", horaX, "tipo: ", type(horaX))
#------------------- Crear un dateTime Específico a partir del date y del time..
objDtX=dt.datetime.combine(diaX, horaX)
# --- DateTime de dia-hora Construida -------------- ]
# --- DateTime de dia-hora Construida -------------- ]

# ---------- comparacion de fechaHora de apertura y cierre con hoy-Ahora
if objDTIni <= dtHoyAhora <= objDtClose:
    print(";)", objDTIni , dtHoyAhora , objDtClose, sep="\n\t")
else:
    print(":(", objDTIni , dtHoyAhora , objDtClose, sep="\n\t")



# ---------- Otra comparacion de fechaHora de apertura y cierre con dia-hora X Creada por mi.
if objDTIni <= objDtX <= objDtClose:
    print(";)", objDTIni , objDtX , objDtClose, sep="\n\t")
else:
    print(":(", objDTIni , objDtX , objDtClose, sep="\n\t")
# -----------------------------------------------------------------
