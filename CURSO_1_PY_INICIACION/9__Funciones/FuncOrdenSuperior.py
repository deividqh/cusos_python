# ------------------Funciones de Orden Superior
""" Funciones de Orden Superior se refiere al uso de funciones como si de 
un valor cualquiera se tratara, posibilitando el pasar funciones como 
parámetros de otras funciones o devolver funciones como valor de retorno.
Esto es posible porque, en Python todo son objetos. Y las funciones no son una excepción. """

def saludar(lang):
    def saludar_es():
        print ('Hola')   
    def saludar_en():
        print ('Hi')    
    def saludar_fr():
        print ('Salut')
    lang_func ={'es': saludar_es,
                'en': saludar_en,
                'fr': saludar_fr
    }
    return lang_func[lang]

f = saludar('es')
f()

# Como el valor de retorno de saludar es una función, como hemos visto, esto quiere decir 
# que f es una variable que contiene una función. Podemos entonces llamar a la función 
# a la que se refiere f de la forma en que llamaríamos a cualquier otra función, añadiendo 
# unos paréntesis y, de forma opcional, una serie de parámetros entre los paréntesis.

# ....y es equivalente a:
# En este caso el primer par de paréntesis indica los parámetros de la función saludar, 
# y el segundo par, los de la función devuelta por saludar.
saludar("fr")() 


# --------------------------filter(function, sequence)
# La funcion filter verifica que los elementos de una secuencia cumplan una determinada condición,
# devolviendo una secuencia con los elementos que cumplen esa condición.
#  Es decir, para cada elemento de sequence se aplica la función function; 
#  si el resultado es True se añade a la lista y en caso contrario se descarta.
def es_par(n):
    return (n % 2.0 == 0)
l = [1, 2, 3]
l2 = filter(es_par, l)

# --------------------------Funciones lambda
# El operador lambda sirve para crear funciones anónimas en línea. Al ser funciones anónimas, 
# es decir, sin nombre, estas no podrán ser referenciadas más tarde.
# Las funciones lambda se construyen mediante el operador lambda, los parámetros de la función
#  separados por comas (atención, SIN paréntesis), dos puntos (:) y el código de la función.
l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)