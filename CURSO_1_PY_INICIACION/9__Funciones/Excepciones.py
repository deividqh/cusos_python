# -------------------------------------------------
# ejemplo de sintaxis de try - exception          >                 
# -------------------------------------------------
try:
    num = 33
except (NameError, ValueError):
    print ('except (NameError), Se ejecuta cuando hay un error del tipo marcado, NameError, ValueError')
except:
    print ('except, Se ejecuta cuando hay una excepcion cualquiera, o NO del tipo marcado')
else:
    print ('else, Se ejecuta sólo si NO hay excepcion')
finally:
    print ('finally, Se ejecuta al final SIEMPRE (con y sin excepcion)(tareas de limpieza)')

# -------------------------------------------------
# ejemplo de sintaxis de try - exception          ]
# -------------------------------------------------

# -------------------------------------------------
# Crear y Lanzar nuestras propias excepciones.    >                 
# -------------------------------------------------
        # Basta crear una clase que herede de Exception o cualquiera de sus hijas y 
        # lanzarla con raise.
class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return 'Error ' + str(self.valor)

# 
try:
    resultado = 25              
    if resultado > 20:
        raise MiError(33)
except MiError as e:            
    print(e)
# -------------------------------------------------
# Crear y Lanzar nuestras propias excepciones.    ]
# -------------------------------------------------

# ---------------------------------------------------------------------------------
# Lanzar directamete una excepcion sin crear una clase que herede de exception    >
# ---------------------------------------------------------------------------------
def dividir(a, b):
    try:
        raise ValueError("Este es un ejemplo de excepción lanzada y que Pasa por Exceptio as e")
        resultado = a / b
    except ZeroDivisionError:  # Captura cuando el denominador es 0
        print("Error: No se puede dividir entre cero")
    except TypeError:  # Captura cuando se pasan tipos incorrectos
        print("Error: Ambos valores deben ser números")
    except Exception as e:
        print(f"Ha ocurrido una excepción: {e}")
    else:
        print(f"El resultado es: {resultado}")

# Ejemplos de uso
dividir(10, 0)  # División entre cero
dividir(10, "2")  # División con tipo de dato incorrecto
# ---------------------------------------------------------------------------------
# Lanzar directamete una excepcion sin crear una clase que herede de exception    ]
# ---------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------
# excepciones disponibles por defecto, 
# así como la clase de la que deriva cada una de ellas entre paréntesis.
# ---------------------------------------------------------------------------------
""" 
BaseException:              Clase de la que heredan todas las excepciones.

Exception (BaseException):           Super clase de todas las excepciones que no sean de salida.
KeyboardInterrupt (BaseException):   El programa fué interrumpido por el usuario.
SystemExit (BaseException):          Petición del intérprete para terminar la ejecución.

StopIteration (Exception):      Se utiliza para indicar el final del iterador.
Warning (Exception):            Clase padre para los avisos.
GeneratorExit (Exception):      Se pide que se salga de un generador.
StandardError (Exception):      Clase base para todas las excepciones que no tengan que ver
                                con salir del intérprete.

ArithmeticError (StandardError):    Clase base para los errores aritméticos.
AssertionError (StandardError):     Falló la condición de un estamento assert.
AttributeError (StandardError):     No se encontró el atributo.
EOFError (StandardError):           Se intentó leer más allá del final de fichero.
EnvironmentError (StandardError):   Clase padre de los errores relacionados con la entrada/salida.
ImportError (StandardError):        No se encuentra el módulo o el elemento del módulo que
                                    se quería importar.

LookupError (StandardError):     Clase padre de los errores de acceso.
MemoryError (StandardError):     No queda memoria suficiente.
NameError (StandardError):       No se encontró ningún elemento con ese nombre.
ReferenceError (StandardError):  El objeto no tiene ninguna referencia fuerte apuntando hacia él.
RuntimeError (StandardError):    Error en tiempo de ejecución no especificado.
SyntaxError (StandardError):     Clase padre para los errores sintácticos.
SystemError (StandardError):     Error interno del intérprete.
TypeError (StandardError):       Tipo de argumento no apropiado.
ValueError (StandardError):      Valor del argumento no apropiado.

FloatingPointError (ArithmeticError):    Error en una operación de coma flotante.
OverflowError (ArithmeticError):         Resultado demasiado grande para poder representarse.
ZeroDivisionError (ArithmeticError):     Lanzada cuando el segundo argumento de una operación de división o módulo era 0.

IOError (EnvironmentError):      Error en una operación de entrada/salida.
OSError (EnvironmentError):      Error en una llamada a sistema.

IndexError (LookupError):        El índice de la secuencia está fuera del rango posible.
KeyError (LookupError):          La clave no existe.


UnicodeDecodeError (UnicodeError):      Error de decodificación unicode.
UnicodeEncodeError (UnicodeError):      Error de codificación unicode.
UnicodeTranslateError (UnicodeError):   Error de traducción unicode.

DeprecationWarning (Warning):        Clase padre para avisos sobre características obsoletas.
ImportWarning (Warning):             Aviso sobre posibles errores a la hora de importar.
PendingDeprecationWarning (Warning): Aviso sobre características que se marcarán como obsoletas en un futuro próximo.
RuntimeWarning (Warning):            Aviso sobre comportmaientos dudosos en tiempo de ejecución.
SyntaxWarning (Warning):             Aviso sobre sintaxis dudosa.
UnicodeWarning (Warning):            Aviso sobre problemas relacionados con Unicode, sobre todo con problemas de conversión.
UserWarning (Warning):               Clase padre para avisos creados por el programador.

WindowsError (OSError):             Error en una llamada a sistema en Windows.
UnboundLocalError (NameError):      El nombre no está asociado a ninguna variable.
NotImplementedError (RuntimeError): Ese método o función no está implementado.
IndentationError (SyntaxError):     Error en la indentación del archivo.
TabError (IndentationError):        Error debido a la mezcla de espacios y tabuladores.
UnicodeError (ValueError):          Clase padre para los errores relacionados con unicode.
"""