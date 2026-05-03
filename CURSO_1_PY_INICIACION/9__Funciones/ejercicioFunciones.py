# Ejercicios de Funciones 1 
print("""
1. Escribir una función que muestre por pantalla el saludo ¡Hola amiga!
cada vez que se la invoque.
""")
def holaAmiga():
    print("hola amiga")
holaAmiga()
print('-'*40,'\n')

print("""
2. Escribir una función que reciba un número entero positivo y devuelva su
factorial. (Multiplicar todos los números enteros y positivos que hay entre
el número máximo que queramos y el número 1.) """)
def ejer2(n):    
    x = [n*i for i in range(1,n)]
    return sum(x)
print(ejer2(4))
print('-'*40,'\n')

print("""
3. Escribir una función que calcule el total de una factura tras aplicarle el
IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a
aplicar, y devolver el total de la factura. Si se invoca la función sin
pasarle el porcentaje de IVA, deberá aplicar un 21%.
""")
def totalFact(base):
    if not str(base).isdigit:
        return None
    else:
        base=float(base)
    return base*0.21 + base
print(totalFact(50.00))

print('-'*40,'\n')

print("""
4. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
indicando si la dirección es válida o no, valiéndose de una función para
decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
""")
def validaMail(mail):
    if str(mail).find("@") != -1:
        return True
    else:
        return False
    
nmail = input("Intro mail.....")
print (validaMail(nmail))

print("""
5. Solicitar números al usuario hasta que ingrese el cero. Por cada uno,
mostrar la suma de sus dígitos (utilizando una función que realice dicha
suma).""")
def sumadigit(m):
    m=str(m)
    return len(m)

while(True):
    n=input("intro numero....")
    if not n.isdigit(): 
        if n[1:].isdigit and (n[0]=='-' or n[0]=='+'):
            n=abs(int(n))
        else:
            continue    
    if n=='0': break
    print(sumadigit(n))


    
print("""
6. Crear un programa que le diga al usuario que ingrese un número entero
e informar si es primo o no.
""")
def esPrimo(m):
    listaFactores=[2, 3, 5, 7 , 11, 13, 17, 19, 23, 29]
    for x in listaFactores:
        if m%x==0:
            return False
    return True

n=int(input("intro numero...."))
if esPrimo(n)==True:
    print('Primo')
else:
    print('No Primo')

# Ya me he enterado de la solucion mejor:
    # se hace un range al numero introducido desde 2  
    # Se hace introNum%i(del range) y si da 0 no es primo
# Pero como no se me ocurrió a mi, sino me lo dijeron, dejo esta solucion que es medio optima 
# y se puede ir completando la lista aunque nunca será perfecta si puede ser 
# 'selectiva' de un numero determinado de numeros primos(listaFactores).

print("""
7. Crear un programa que pidiendo al usuario su nombre completo y su dni
con letra, cree un identificador para cada usuario.
a. Controlar que usuario no introduce el nombre vacío.
b. Se puede controlar que dni sea correcto
c. Por cada socio se debe imprimir su identificador único, el cual
      -+++++++++++                                                                                                                                                                                               estará formado por: el primer nombre, la cantidad de letras del
primer apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Loreto Pelegrín Castillo
DNI: 11111111H
Loreto8111
 """)
# import os
# os.system('cls')
import re       

# Funcion que Recube un DNI(8num(?)letra) y devuelve el dni en una tupla(numero, letra). 
# Puedes meter guion, barraInvertida, espacio....entre el número y la letra.

def extract_dni_values(dni):      
    pattern = r"^(\d{8})[-.\s]?([a-zA-Z])$"
    # (\d{8})       8 digitos (0 a 8-1)
    # [-.\s]?       (guion o punto o espacio en blanco opcionales)
    # ([A-Z])       :Letra Mayuscula de la A a la Z.
    # [A-Za-z]      :Letra del alfabeto en mayúscula o minúscula.  
       
    match = re.match(pattern, dni)
    if match:
        number = match.group(1)
        letter = match.group(2)
        return number, letter
    else:
        return None, None

print("CALCULO DE DNI")
name=input("intro Nombre....")
dni=input("intro DNI....")
if name.strip() !="" and dni.strip() != "":
    numero, letra = extract_dni_values(dni)
    if numero == None or letra == None:
        print("dni erroneo")
    else:
        print(f"Numero= {numero}\nLetra= {letra}")
        print(f'Tres Primeros números = {numero[:3]}')
else:
    print("Error de Entrada")





