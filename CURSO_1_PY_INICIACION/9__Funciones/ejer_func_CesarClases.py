# Ejercicios Funciones II ............... Cesar

import re       #Para usar expresiones Regulares
import os       #Para Limpiar la terminal con os.system('cls')
import string   #Para crear el str abcdario y ABCDARIO 


class clssCesar:
    codeByDef=2                #Desplazamiento por defecto
    codigoD = codeByDef
    # --------------------------------- Constructor
    def __init__(self, fraseToEncript, codigoD):
        try:
            if self.__esValidCode(codigoD) == True:
                clssCesar.codigoD=codigoD
            else:
                clssCesar.codigoD = codeByDef
        except:
            print(f"Error en Desplazamiento: {codigoD} ... codigo asigado por defecto: {clssCesar.codeByDef}")
            clssCesar.codigoD = codeByDef
        else:
            print(f"desplazamiento {clssCesar.codigoD} ;)")
        # ---------------- ahora con la frase
        try:
            if self.__esValidFrase(fraseToEncript)==True:
                self.__fraseToEncript = fraseToEncript 
            else:
                self.__fraseToEncript = ''
        except:
            print("Error en Frase")
            self.__fraseToEncript = ''
            print("Cesar sin Frase")
        else:
            print("Objeto Cesar Creado") 

            print("Cesar Esperando instrucciones.....")
            self.__fraseCripted = self.cifrar(  fraseToEncript=self.__fraseToEncript, 
                                                codigoD=clssCesar.codigoD, 
                                                bPrint=False)
        finally:
            None

        # ------------------ Llamo a cifrar para obtener ya un resultado, pero con false para no imprimirlo
    # -----------------------------------GETTERS AND SETTERS BY @property >
    # -----------------------------------GETTERS AND SETTERS BY @property >
    def codigoD(self):
        return self.__nombre   
    # Setters de la variable  estatica codigoD por @property
    def codigoD(self, codigoD):
        if self.__esValidCode(codeDigit)==True:
            clssCesar.codigoD=int(codeDigit)        
        else:
            clssCesar.codigoD=clssCesar.codeByDef        
 
    def fraseToEncript(self):
        return self.__fraseToEncript   
    def fraseToEncript(self, fraseToEncript):
        if self.__esValidFrase(fraseToEncript)==True:
            self.__fraseToEncript = fraseToEncript
        else:
            self.__fraseToEncript = ''
    # -----------------------------------GETTERS AND SETTERS BY @property ]

    # -----------------------------
    def __setStrCursor(self, abcdario):    
        """ 
        Def: Dependiedo del signo del desplazamiento colocamos el cursor en una posicion u otra.
        Args: [abcdario] = 'abcdefghijklmnopqrstuvxyz' o 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        """
        if int(clssCesar.codigoD)>=0:
            return (abcdario + abcdario) , 0
        else:
            return (abcdario*2) , len(abcdario)

    # -----------------------------
    # funcion de re, por lo que recibe un solo argumento(match)
    def __funcDesplaza(self, match):
        """ 
        Def:    Entra un caracter y devuelve su equivalente desplazado(desplazamiento +-).
        Args: [match] es una funcion re(Regular Exp). Se recoge el dato con group.
              el dato significa tantas coincidencias con el patron estén establecidas
              En este caso viene de .
        Retorno: el caracter desplazado segun el valor de self.codigoD
        """
        abc=string.ascii_lowercase  # 'abcdefg....'
        ABC=string.ascii_uppercase  # 'ABCDEFG....'
    
        char = match.group()
        if char in abc:                
            strMatch, cursor = self.__setStrCursor(abc)
        elif char in ABC:
            strMatch, cursor = self.__setStrCursor(ABC)
        else:       
            return char                        # Si es otra cosa lo dejo tal cual Sp o _ incluido.
        pos=strMatch.find(char, cursor)        # calculo la posicion en el texto de strMatch    
        return strMatch[pos+clssCesar.codigoD]                 # Devuelvo el nuevo caracter

    # -----------------------------
    def __esValidFrase(self, texto):        
        """     
        Def:    Valida la Entrada segun expresion la Regular: r'^[da-zA-Z]+$' 
                Si [texto] no se ajusta al patron => ha introducido un char no valido($ pej)

                ^          => Inicio de la cadena
                [da-zA-Z]  => [char] | d=>un digito | a-z => From a To z | A-Z => from A to Z
                + =>  cualquier numero de veces. Si no se pone sólo valdría para un sólo char
                $          => Fin de la cadena
        Args:   [texto] = str() no Validado.
        
        Return: (True/False)
                None, si texto==''
        """        
        if not isinstance(texto, str):  return False
        if texto.strip=='': return None
        texto=texto.strip()
        patron=r'^[da-zA-Z]+$'
        if re.search(patron, texto)==None:
            return True
        else:
            return False
    # -----------------------------
    def __esValidCode(self, codeDigit):
        """ 
        Def: Valida si el codeDigit pasado como argumento es un número entero.
             No incluye _ , . (decimal)
             si entra en el patron True / si no entra, False 
        """
        # .... Se lee: en toda la cadena [ From Ini(^); to Fin ($) ]
        #              Buscamos:  guion(-) opcional(?) y/o  0-9(\d)   ,  n veces(+)(solo el digito) 
        patronInt=r'^-?\d+$'
        num=re.match(patronInt, str(codeDigit))        
        return (True if num else False)
    # -----------------------------
    # def cifrar(self, fraseToEncript='', bPrint=False):        
    def cifrar(self, fraseToEncript='', codigoD=2, bPrint=False):        
        """ 
        Def:    Funcion que tiene el algoritmo de cifrado de una Cadena 
                por el método Cesar. Devuelve un str con la frase Encriptada.                
        Args:   [bPrint] ==> Booleano = True si quieres que haga Print 
                del str Encript
        """
        # Valida frase de entrada        
        esfraseOk=self.__esValidFrase(fraseToEncript)
        if esfraseOk==False: 
            return ':('
        elif esfraseOk==None:
            if self.__fraseToEncript=='': 
                return ''
            else:
                fraseToEncript=self.__fraseToEncript
        fraseToEncript=fraseToEncript.strip()
        
        # Valida codigo D Desplazamiento
        if self.__esValidCode(codigoD)==False:             
            return ':( Error en codigo'
            clssCesar.codigoD=codeByDef
        else:
            clssCesar.codigoD=codigoD
        
        # Working Procedure
        try:
            wd_spRE=r'[\w\s]'    # letra-digit-guionBajo o(inclusivo) Sp
            listResultado=[ re.sub(wd_spRE, self.__funcDesplaza, n) for n in fraseToEncript ]
        except:
            pass
        else:    
            self.fraseToEncript = fraseToEncript
            self.__fraseCripted = ''.join(listResultado)
            if bPrint==True: print(self.__fraseCripted)

        return self.__fraseCripted

    # -----------------------------
    def descifrar(self, bPrint=True):
        # Valido datos
        if self.__fraseToEncript=='': return ''
        if self.__esValidFrase(self.__fraseToEncript)==False: return ''     
        if self.__esValidCode(clssCesar.codigoD)==False: return ''     
        # if clssCesar.codigoD==0: return self.__fraseToEncript 
        # Guardo el codigo de desplazamiento original        
        codeAux = clssCesar.codigoD         
        # Le cambio el signo al desplazamiento para que haga el opuesto al cifrado.
        clssCesar.codigoD = ( - clssCesar.codigoD)
        
        strDescifrada = self.cifrar(self.__fraseCripted,clssCesar.codigoD , bPrint )        
 
        # Re Asigno el codigo de Desplazamiento al original
        clssCesar.codigoD = codeAux

        if bPrint==True: print(self.__fraseCripted)
        return strDescifrada


    # -----------------------------
    # Crea un menu donde tienes que introducir una cadena valida y un desplazamiento
    # para la encriptacion
    def initMenuCesar(self):
        os.system('cls')
        print("ENCRIPTACION CESAR:")
        while(True):
            desp=input(f"Actual Desplazamiendo( {clssCesar.codigoD} )\nIntro nuevo Desplazamiento o cualquier tecla Xa aceptar {clssCesar.codigoD}.... ")    
            if self.__esValidCode(desp):
                self.codigoD=int(desp)
            else:
                self.codigoD = clssCesar.codeByDef

            introFrase=input(f"Actual Desplazamiendo( {self.codigoD} )\nEsperando Frase Para Cifrado.... ")
            if self.__esValidFrase(introFrase.strip()):
                self.fraseToEncript=introFrase
                break
            print(f'< {introFrase} >\nFrase con caracteres no Válidos')

        self.cifrar(True)

    def __addToDict(self):
        pass

# Creando un objeto de la clase Perro
os.system('cls')
cesar = clssCesar("el PerZo", 2)
cifrado = cesar.cifrar(True)
descifrado = cesar.descifrar(True)
# cesar.initMenuCesar()
cifrado=cesar.cifrar("eZ PerZO", 2, True)
cesar.fraseToEncript("el Perro de Zan Roque")
cesar.cifrar("", 2, True)