
import enum as ENUM
from enum import Enum as MASTER_INDEX
class Config(MASTER_INDEX):
    MASTER=0
    INDEX=1
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
class MenuDvd():
    """ 
    Def: Define las partes esenciales de un menu Simple:
    Titulo(lst_str) ....  opcional
    opt(enumerate)... obligatorio
    Cuerpo(lst_str). obligatorio.
    FinTitulo(bool)   opcional 

    necesito el igualador de listas     para igualar lista titulo con listaCuerpo.
    necesito a validator                para validar fechas y numeros y str.
    necesito a KeyBDicc                 para las opciones de update_byTcld.
    """
    def __init__(self, 
                titulo, 
                lst_menu, 
                lst_func,  
                msgIntroData='Opt.... ',
                num_char = 40,
                char_1 ='-' , char_2='-' , char_3='-'):        
        pass
        self.titulo=titulo
        self.lst_menu=lst_menu
        self.lst_func=lst_func        
        self.msgIntroData=msgIntroData
        self.num_char=num_char
        self.char_1=char_1
        self.char_2=char_2
        self.char_3=char_3

        self.salir=["SALIR"]
        self.cabecera, self.pie , self.lst_numeracion = self.formar_entorno()
        # _____________________________
        # Generacion del diccionario

        lst_valor_dicc = tuple(zip(self.lst_menu, self.lst_func))            
        """ >>> Creo una tupla con el par lst_menu, lst_func """
        self.dicc_menu={i+1:valor_dicc  for i, valor_dicc in enumerate(lst_valor_dicc)}                                          
        """ >>> Creo el diccionario num_n: (menu_n, func) """
        # print(self.dicc_menu)
        print('dicc_menu cargado ok: ')

    def __str__(self):        
        self.Impr()
    
    def formar_entorno(self):
        cabecera=f'\n{ self.char_1 * self.num_char }\n{ self.titulo }\n{ self.char_2 * self.num_char }'        
        lst_numeracion=[i+1 for i in range(len(self.lst_menu))]
        pie=f'{self.char_3*self.num_char}'
        return cabecera, pie, lst_numeracion

    def Impr(self):
        # _________
        # Cabecera
        print(self.cabecera)
        # _________
        # Menu
        for menu in self.cuerpo:
            print (f'{menu}')
        # _________
        # Fin
        print (self.pie)            
       
    # estatica    
    def MDicc(dicc_menu, tituloMenu):
        if not isinstance(dicc_menu,dict): return -1
        salir={"SALIR": 0}
        # Asi puedes adjuntar por el principio (y recibir en una funcion) un diccionario(**), una lista se envia así(*)
        menuSalir={**salir, **dicc_menu}
        # al pasar dicc_menu por referencia, cambia en la funcion que lo llama tb. 
        # y no lo retorno sino que lo cambio aqui.
        dicc_menu=menuSalir
        # print(menuSalir)
        # while (True):
            # Imprime dicc_menu:
        
        # Estas cossa de python son la pera
        print ('\n'+'-'*9,tituloMenu,'-'*9)    
        for index,tit in enumerate(menuSalir):
            print (f'{index}....{tit}')
        print ('-'*22)
        
        # Selecciona Opcion:
        i=input("Intro opcion... ")
        if i.isdigit():
            i=abs(int(i))
        else:
            return -1

        return i
    # _________________________________
    # ESTATICA PARA CREAR MENUS RAPIDOS DE UNA LINEA PADRE
    # =================================    
    def MList(lst_menu, tituloMenu="M E N U", 
                msgItem='Intro Opcion...', 
                num_char=40,
                char_1='-', char_2='-', char_3='-'):
        """ 
        Devuelve un lst_menu. Añade la opcion de salir.
        [lst_menu]: lista de str con los textos del lst_menu.

        """
        salir=["SALIR"]
        lst_menu=salir+lst_menu    
        # Imprime lst_menu:
        # print('\n'+char_1*40+'\n'+tituloMenu+'\n'+char_2*40)
        print(f'\n{char_1*num_char}\n{tituloMenu}\n{char_2*num_char}')
        for index,opc in enumerate(lst_menu):
            print (f'{index}....{opc}')
        print (f'{char_3*num_char}')    
        
        while(True):
            # Selecciona Opcion:        
            i=input(f"{msgItem}")    
            # Si todo lo introducido en la cadena son digitos = True
            try:
                if i.isdigit():
                    i=abs(int(i))
                    if i==0: return None
                    if i>len(lst_menu): 
                        continue
                    else:                
                        return i
                else:
                    continue
            except Exception:
                continue


# ============================================================================================
# ============================================================================================
import threading
# ============================================================================================
# ============================================================================================
class XindiceX(MenuDvd):
    """ 
    Def: Gestiona una lista de menus y sub menus y los muestra por Terminal.
    """
    def __init__(self, thread=None):
        """ >>> Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        """        
        if thread==None:
            """ Auto Gestion de Hilos """
            self.thread = None
            # self.thread = threading.Thread(target=self.func)
        else:
            """ El hilo lo gestiona el main """
            self.thread = thread


        """ >>>  """
        self.lst_menuXX=[]
        """ >>> Lista de objetos MenuDvd que mantiene un lst_menu,  dicc_menu(num_n:[strMenu_n, func_n])  """

        self.lst_titulos=[]
        """ >>> Lista de titulos introducidos. Me permite validar rapido  """

        self.dicc_xindicex={}
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """


    def iniciar_hilo(self):
        """Inicia el hilo si no está activo."""
        if self.thread and not self.thread.is_alive():
            self.thread.start()

    def verificar_hilo(self):
        """Verifica si el hilo está activo."""
        return self.thread.is_alive() if self.thread else False

    def reiniciar_hilo(self):
        """Reinicia el hilo si está terminado y se proporciona una función."""
        if self.thread and not self.thread.is_alive() and self.func:
            self.thread = threading.Thread(target=self.func)
            self.thread.start()
    # _________________________
    # AÑADE UN MENU AL GESTOR 
    def add(self, titulo, lst_menu, lst_func, msgIntroData='Opt.... ', num_char = 40, char_1 ='-' , char_2='-' , char_3='-'):
        """  """
        if titulo in self.lst_titulos: 
            return False
        new_menu=MenuDvd(titulo=titulo, lst_menu=lst_menu, lst_func=lst_func, 
                        msgIntroData=msgIntroData, 
                        num_char = num_char, char_1 =char_1 , char_2=char_2 , char_3=char_3)

        self.lst_titulos.append(titulo)
        self.lst_menuXX.append(new_menu)

        print(f'Load Menu {titulo} Ok ;)')
        return True
    
    # ___________________________________________________
    # CONFIGURA LA RELACION PADRE HIJO(INDICE) DEL MENU
    def config(self, titulo, master=None, indexInMaster=None): 
        """ >>> Configura la relacion de los menus. """
        if not titulo in self.lst_titulos:
            return False
        if master == None:
            """ NO MASTER """
            pass
        else:
            """ MASTER """
            if indexInMaster==None:
                indexInMaster=self.busca_index_free(titulo_busca=titulo, master_busca=master)
                if not indexInMaster: indexInMaster=0
                if indexInMaster == self.dicc_xindicex[titulo][Config.INDEX.value]:
                    pass
                else:
                    self.dicc_xindicex[titulo]=[master, indexInMaster]
            else:
                self.dicc_xindicex[titulo]=[master, indexInMaster]

    # _________________________________________________
    # BUSCA INDEX FREE.
    def busca_index_free(self, titulo_busca, master_busca):
        """ >>> Busca en el diccionario de configuracion dicc_xindicex, un index libre(el siguiente). 
        Retorna: None si Error | indice para insertar si todo OK """
        lst_indexes=[]
        for tit_dicc, master_idx in self.dicc_xindicex.items():
            if tit_dicc==titulo_busca:
                if master_idx[Config.MASTER.value]==master_busca:
                    lst_indexes.append(master_idx[Config.INDEX.value])
        
        # Cuando sale del bucle espero tener una lista de los index del master.
        print(lst_indexes)
        try:
            max_index=lst_indexes.max()
            new_index=max_index+1
            return new_index
        except Exception as e:
            print(f'Error: {e} ')
            return None


    
    def lst_sin_repetidos(self, lst_to):
        """  """
        

        
    # _________________________________________________
    # EJECUTA UN MENU AQUÍ ES DONDE SE GENERA EL HILO.
    def start(self, tituloMenu, withConfig=True, bTomaControl=True):
        """ >>> Def: Comienza un menu.
        [tituloMenu]: str, el menu que se quiere visualizar...
        [withConfig]: Si lanza el menu Tal cual o quiere dependencia index.
        [bTomaCotrol]: bool; True, si es un menú cerrado y se auto-gestiona.
        False, si lanza hilos por cada funcion que ejecuta.

        """
        while True:
            
            respuesta=TheMen.MList(lst_menu=lst_menu_ppal, tituloMenu=tituloMenu)

            if respuesta==None:                
                    break
            if 1 <= respuesta < len(lst_menu_ppal):            
                """ >>> Ejec Funcion del menu. """
                if lst_func_ppal[respuesta]:
                    lst_func_ppal[respuesta]()
            else:
                continue        
            pass    
            print('\n\nS A L I E N D O ......\n\n')


# ============================================================================================
# ============================================================================================
import time
# ============================================================================================
# ============================================================================================
class X_Men:
    def __init__(self, thread=None):
        """
        Inicializa la clase con un hilo opcional.
        - thread: Puede ser proporcionado o inicializado más tarde.
        """
        self.thread = thread
        self.func = None  # Función asociada al hilo
        self.running = False

    def add(self, func):
        """
        Asigna una función al hilo.
        - func: La función que ejecutará el hilo.
        """
        self.func = func

    def start(self, delay=0.3, is_form=False, config_others=True):
        """
        Inicia el hilo con las configuraciones especificadas.
        - delay: Tiempo de espera entre ejecuciones (predeterminado 0.3s).
        - is_form: Indica si es un formulario tkinter.
        - config_others: Si es un formulario, indica si debe configurar otros formularios.
        """
        if self.func is None:
            raise ValueError("No se ha asignado una función al hilo.")

        if self.thread and self.thread.is_alive():
            print("El hilo ya está activo.")
            return

        # Crear y asignar el hilo
        self.thread = threading.Thread(target=self._run_task, args=(delay, is_form, config_others))
        self.running = True
        self.thread.start()

    def _run_task(self, delay, is_form, config_others):
        """
        Lógica interna para ejecutar la tarea.
        - Si es un formulario, controla su inicialización.
        - Si no, ejecuta la función con control de tiempos.
        """
        if is_form:
            if config_others:
                print("Configurando otros formularios...")
            print("Iniciando formulario...")
            self.func()  # Ejecuta el formulario directamente (mainloop)
        else:
            print("Ejecutando función inmediata...")
            while self.running:
                self.func()
                time.sleep(delay)

    def stop(self):
        """
        Detiene el hilo si está en ejecución.
        """
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def is_running(self):
        """
        Verifica si el hilo está activo.
        """
        return self.thread.is_alive() if self.thread else False