

"""
Ejercicio 4. Crea un programa para calcular la superficie y el volumen de una
esfera, dado su radio.

a) superficie = 4 * PI * radio al cuadrado

b) volumen = 4/3 * PI* radio al cubo

"""
PI=3.1416
r=input ("Intro radio..... ")
r=float(r)
#print(type(r))
sf=4*PI*r
#sf=float(sf)
print(type(sf))
print ("superficie ",sf)
v=(r**3*4/3*PI)
print(type(v))
print("volumnen" , v)

