import re

def ejer4(cad):
    cad=cad.strip()
    patron = r'^(\w+)@(\w+)$'    
    palabra=re.match(patron, cad)
   
    return palabra.group(1), palabra.group(2)

cad=input('Intro mail.....')
dia=input('Intro dia nacimiento.....')


nombre, resto=ejer4(cad)
print(nombre+dia+'@'+resto)
