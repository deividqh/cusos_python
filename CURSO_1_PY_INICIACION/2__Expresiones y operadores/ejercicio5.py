

"""
Ejercicio 5. La escala Celsius es centígrada, 100 divisiones separan el punto de
congelación del punto de ebullición del agua. En la escala Fahrenheit de los
anglosajones, estos dos puntos están separados por 180 grados. La escala de
Kelvin es una escala absoluta utilizada en ciencias. Cree un programa para
convertir de grados centígrados a Kelvin y Fahrenheit. Solicite al usuario la
cantidad de grados centígrados para convertirlos usando las siguientes tablas de
conversión:
kelvin = celsius + 273
fahrenheit = celsius * 18/10 + 32
"""
PI=3.1416
c=input ("Intro grados C..... ")
c=int(c)
#print(type(r))
k=c+273
f=c*18/10+32
print(f"kelvin " ,{k},"\nfarenheit ",{f})
