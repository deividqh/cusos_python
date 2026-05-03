# Ventanas, Formularios, widgets, eventos de widget, formulario...
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# Para enviar parametros al command y bind
from functools import partial
# -----------------------
from .dvdColor import ColorCorp
from .classPrinteX import PrinteX 

from .formPosMov import FormPosMov
from .classCajasDraw import CajasDraw

""" 
?????????????????????????????????????????????????
FALTA
?????????????????????????????????????????????????
1-Validaciones de tipo y en general.... revision
2-try - except - raise

"""
class FrameX():
    contador=0
    def __init__(self, parent, **kwargs):
        self.listaFrameX=[]
        # Inicializa el frame con los argumentos opcionales
        self.frame = tk.Frame(parent, **kwargs)
        FrameX.contador+=1

class WidgetX():
    contador=0
    def __init__(self, parent, **kwargs):
        self.listaWidget=[]
        
        

"""         R E F L E X I O N E S   SOBRE LA TABLA DE RESULTADOS PRINTEX DE GETDATARCSV
======================================================================================= 
-Cuando el level == 3,  coord2,pre-last  se funden en 1 coordenada y queda: coord1-coord2-last
-Cuando el level == 4,  Todas toman su valor: coord1-coord2-pre-last-last => fila(coord1), columna(coord2) dentro de fila + luego, fila(pre-last) x columna(last)
-Cuando el level == 5,  Se pierde un nivel intermedio en la lista de coordenadas, no en el de posiciones.
                        pre-last y last sospecho que son fila y columna relativa(como en todos los casos).

EN TODOS LOS NIVELES, pre-last y last son la fila y columna Relativos


"""

# Obtiene los widgets dentro del Frame
# widgets_en_frame = [frame.nametowidget(child) for child in frame.winfo_children()]

# Configuración de Grid: Ajustamos el weight de cada columna y fila para permitir que los elementos se expandan y se adapten al tamaño de la ventana.

# PACK() = > (se aplica a los WIDGET)
# frame.pack(fill="both", expand=True)
# En este caso, frame ocupará todo el espacio disponible en su contenedor tanto horizontal como verticalmente.

# GRID() => (se aplica a los FRAME) Usa weight con grid para distribuir espacio adicional entre filas y columnas cuando el contenedor cambia de tamaño.
# weight=1: Especifica que esa columna o fila debe crecer o contraerse proporcionalmente 
# cuando la ventana cambia de tamaño. Cuanto mayor sea el weight, más espacio ganará esa 
# fila o columna en comparación con otras que tengan un weight menor.


class Enfileitor():
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """

    """ 
        frame.grid_rowconfigure(i, weight=1)  : configura la fila i del frame con peso 1 en expansion. Se expande con su padre
                                                Pero tb la crea(la fila)!! y deja un espacio contenedor 
                                                para grid(row=fila , column=columna )
        frame.grid_columnconfigure(i, weight=1) : configura la columna i del frame con peso 1 en expansion. Se expande con su padre
                                                Pero tb la crea(la columna)!! y deja un espacio contenedor 
                                                para grid(row=fila , column=columna )
    """        
    

    def __init__(self, 
                objFormPosMov, 
                objMrrwStTK, 
                ):
        self.Ventana    = objFormPosMov
        """ >>> Ventana con un tamaño, una posicion y un movimiento. """
        self.Estructura = objMrrwStTK
        """ >>> Estructura en espejo """
        # ********************************************************************************
        # ======================== OVER ROOT (NIVEL 0)
        # ********************************************************************************
        """ >>> Genera un Contenedor(root) con una fila(0) que se expande con el Contenedor """
        self.Ventana.root.grid_rowconfigure(0, weight=1)
        """ >>> Genera un Contenedor(root) con una columna(0) que se expande con el Contenedor """ 
        self.Ventana.root.grid_columnconfigure(0, weight=1)                

        # ********************************************************************************
        # ============== OVER ROOT/FRAMENIVEL_1  ( N I V E L   1 ) - CONTENEDOR GENERAL
        # ********************************************************************************
        self.frameNivel_1=tk.Frame(master=self.Ventana.root, 
                                    name="frameNivel_1",                #OBLIGATORIO EN LA CLASE PARA BUSCARLO
                                    background=ColorCorp.BlancoX03)                
        """ >>> Frame General de Nivel 1. Obligatorio y cte. El padre de todos a partir de ahora. El Zeus"""
        # __________________________________
        # ====== Configurar La Expansion 
        # ==================================
        # Aqui es donde se tiene que configurar enfileitor o columneitor.        
        self.frameNivel_1.grid_rowconfigure(index=0, weight=1)        
        self.frameNivel_1.grid_columnconfigure(index=0, weight=1)  
        
        # este va así directo en pack y Expansión total, Llenando x é y (both)
        self.frameNivel_1.pack(fill="both", expand=True)

        # ********************************************************************************
        # ========= OVER root/frameNivel_1.../  ( N I V E L   2)  .... - listaEstructura
        # ********************************************************************************
        # self.listaFrameFila_nivel2=self.crearFilas_nivel2(  general=self.frameNivel_1, 
        #                                                     numFilas=self.Estructura.numFilas, 
        #                                                     xpadx=5, 
        #                                                     ypady=5
        #                                                 )
        self.listaFrameFila_nivel2=[]  
        """ >>> Frames de Fila. Obligatorio. Tantas filas como diga la estructura (self.Estructura.numFilas) 
        Es una lista que contiene directamente a los frames creados en el nivel 2!!!  """
        for i in range(int(self.Estructura.numFilas)):
            frameFila=tk.Frame(master=self.frameNivel_1, 
                                name='fila_'+str(i), 
                                background=ColorCorp.BlancoX03
                            )
            frameFila.pack(fill="both", expand=True, padx=5, pady=5)                        

            self.listaFrameFila_nivel2.append (frameFila)

        print('\nLista Nivel2: ')
        print(self.listaFrameFila_nivel2)                        
        
        # *******************************************************************************
        # ========= E N T O R N O   EstrucTK   (NIVEL 3)
        # *******************************************************************************
        
        """ 
        PARA PASAR AL NIVEL 4 HAY QUE CREAR TANTAS COLUMNAS EN CADA FILA COMO ELEMENTOS HAYA 
        EN CADA FILA(SIN ENTRAR EN SUBDIVISIONES)
        """
        # VISUALIZACION DE DATOS>>>>>>>>>>
        print(self.Estructura)        
        self.Estructura.imprDiccDATA()
        # VISUALIZACION DE DATOS]]]]]]]]]]
        
        self.list_numColum_nivel3=[len(self.Estructura.getFila(i)) for i in range(self.Estructura.numFilas) ]
        # print(self.list_numColum_nivel3)
        """ 
        El indice de la lista es el indice de cada la fila de nivel 2.
        El valor de la lista representa el número de columnas que hay que crear de nivel 3 en 
        cada Fila... 
        >>> pejem:  listaNivel_3=[5, 2, 4] 
        >>> Significa que hay 3 FILAS y que la 1ª hay que dividirla en 5, la 2ª en 2 y la 3ª en 4 columnas
        >>> list_numColum_nivel3=[]        
            for i in range(self.Estructura.numFilas):
                list_numColum_nivel3.append(len(self.Estructura.getFila(i)))        
        """ 
        self.listaFrame_nivel3=[]
        """ Recoje los Frames de Nivel 3(Filas)  """
        # ??????????????????????????????????????????????????????????????????????????????????
        # for i in list_numColum_nivel3:
        #     # en la fila 0 el padre es fila0 de listaFrameFila_nivel2
        #     newframe = tk.Frame('XXX',name='frameNivel_3'+str(i) ,bg="gray")
        #     self.listaFrame_nivel3.append(newframe)
        # ??????????????????????????????????????????????????????????????????????????????????
        
        # Preparo la configuracion para el nivel 3 en el nivel 2
        # Tiene que ser en la fila de listaFrameFila_nivel2 pero con el 
        # número de columnas de listraframe_nivel3       
        # ??????????????????????????????????????????????????????????????????????????????????
        # for i, frame_nivel2 in enumerate(self.listaFrameFila_nivel2):
        #     frame_nivel2.grid_columnconfigure(i, weight=1)
        # frame_nivel2.grid_rowconfigure(0, weight=1)
        # ??????????????????????????????????????????????????????????????????????????????????
        print('-Lista Frame Nivel 3:' , end=' ' )
        print(f'{self.listaFrame_nivel3}')
        pass
        
        

        # ??????????????? L O   V I E J O     .... Que Funciona!
        for i in range(self.Estructura.numFilas):
            self.set_nColumnas(frame=self.listaFrameFila_nivel2[i], numColumnas=4)
        # En la filaFrame[0], la divide en 2 filas/frame mas.
        # self.set_nFilas(frame=self.listaFrameFila_nivel2[0], numFilas=2)        
        

        # *******************************************************************************
        # ========= SUBDIVISIONES DENTRO DE LA ESTRUCTURA NIVEL 3     (NIVEL 4)
        # *******************************************************************************
        """ 
        frame.grid_rowconfigure(index=0, weight=1)        
        frame.grid_columnconfigure(index=0, weight=1)
        """
        # *******************************************************************************
        # ========= CREACION DE LOS FRAMES EN LA ESTRUCTURA
        # *******************************************************************************

        # *******************************************************************************
        # ========= S A L I D A
        # *******************************************************************************
        # Mensaje de salida y FIN-INIT
        print('\nE N F I L E I T O R   C R E A D O    ;) \n\n')
        
        
        # *******************************************************************************
        # BORRAR E INSERTAR EN LA INSTANCIA DE ENFILEITOR( OVER _ENFILEITOR() )
        # WIDGETS DEL  FRAME   C L I E N T E          
        # *******************************************************************************
        """ listaWidget={
            "nombreWidget1":[tkObjet, fila, columnaEnFila, xpadx, ypady, sticky, fill, expand] , 
            "nombreWidget2":[tk.Button(), listaFrameFila_nivel2[0], columnaEnFila, ] , 
            "nombreWidget3":[tk.Button(), listaFrameFila_nivel2[0], columnaEnFila, ] 
            } """
        # _________________
        Row_FORM=0        
        # ================           
        """ 
        LISTBOX: Para mostrar los equipos a los que podemos enviar cosas. """
        # print(self.listaFrameFila_nivel2.index(self.listaFrameFila_nivel2[Row_FORM]))

        self.lbxServidores = tk.Listbox(master=self.listaFrameFila_nivel2[Row_FORM], 
                                        name="masterX")
        self.lbxServidores.grid(row=Row_FORM, 
                                column=0,
                                sticky="nsew"   # Y se queda pegado a todos los lados
                                )        
        # ______________________
        # Aqui me falta el evento para que cuando seleccione un PC cambie el lblEquipSelect
        # Enlazar el evento de selección al Listbox
        self.lbxServidores.bind('<<ListboxSelect>>', self.lbxServidoresXaClientMe_on_select)       
        # _________________
        Row_FORM = 1
        # ================   
        """  
        BOTON  Close CNX """
        # print(self.listaFrameFila_nivel2.index(self.listaFrameFila_nivel2[Row_FORM]))
        self.btnCloseCnX = tk.Button(master=self.listaFrameFila_nivel2[Row_FORM], 
                                    text="Boton", 
                                    command=self.closeConection_click)
        self.btnCloseCnX.grid(row=Row_FORM,column=0)
        """  
        LABEL  equipo seleccionado """
        self.lblEquipSelect = tk.Label( master=self.listaFrameFila_nivel2[Row_FORM], 
                                        text="Equipo")
        self.lblEquipSelect.grid(row=Row_FORM, column=1)
        """  
        BOTON  Close CNX """
        self.btn_01 = tk.Button(master=self.listaFrameFila_nivel2[Row_FORM], 
                                text="Cortar Conexión", 
                                command=self.closeConection_click )
        self.btn_01.grid(row=Row_FORM, column=2 )

        """  
        LABEL  estado de la conexión """
        self.lblSTCliente = tk.Label( master=self.listaFrameFila_nivel2[Row_FORM], 
                                        text="Estado", 
                                        borderwidth=1,  
                                        relief="sunken" )
        self.lblSTCliente.grid(row=Row_FORM, column=3)        

        # # ================   
        Row_FORM = 2
        """  
        TEXTBOX  """
        self.txtEnviar = tk.Entry(master=self.listaFrameFila_nivel2[Row_FORM])
        self.txtEnviar.grid(row=Row_FORM, column=0,columnspan=4,  sticky="ew")

    def crearWidget_dinamico(parent, widget_tipo, **kwargs):
        """
        Crea un widget de tkinter dinámicamente y lo asigna al parent especificado.
        
        Argumentos:
        - parent: El widget contenedor, como un frame o ventana.
        - widget_tipo: La clase del widget de tkinter que deseas crear (por ejemplo, tk.Label, tk.Button).
        - kwargs: Argumentos adicionales para el widget.
        
        Retorna:
        - El widget creado.
        """
        widget = widget_tipo(parent, **kwargs)
        widget.pack(padx=5, pady=5)  # Empaca el widget en el parent
        return widget

    def recursivaCrearFrames(self):        
        """ 
        Def:
        """
        for i in range(self.Estructura.numFilas):
            fila=self.Estructura.getFila(indexFila=i)
            SttKFila=CajasDraw(listaEstructura=fila)
            print(SttKFila)
        pass
        
    def crearFilas_nivel2(self, general, numFilas, nombre='fila_',background=ColorCorp.BlancoX03, xpadx=5, ypady=5):
        """
        Crea tantos frames contenedores como numFilas.
        Los frames están disponibles en self.listaFrameFila_nivel2. self.listaFrameFila_nivel2[0] = fila 0
        >>> [general] es el frame contenedor de nivel 1. padre
        >>> contenedor[root][nivel 0] -> contenedor[general][nivel 1] -> listaFrameFila_nivel2[0]....listaFrameFila_nivel2[n]  [nivel 2]filas

        Se hacen pack
        """      
        listaRetorno=[]  
        for i in range(numFilas):
            # ____________
            # Crea un frame, en el frame general
            frameFila=tk.Frame(master=general, name=nombre+str(i), background=background)
            # ____________
            #  lo empackamos(pack) Que llene el espacio y se expanda.
            frameFila.pack(fill="both", expand=True)            
            # ____________
            # Le configuro  padx y pady
            if xpadx:
                frameFila.pack(padx=xpadx)            
            if ypady:
                frameFila.pack(pady=ypady)            
            # ____________
            # Metemos la fila(el frame) en una lista 
            listaRetorno.append (frameFila)

        return listaRetorno
        
    # *************************************************************** 
    # *************************************************************** 
    def set_nColumnas(self, frame, numColumnas=None):
        if not frame: return None
        # frame.grid_rowconfigure(0, weight=1)        
        if numColumnas:
            for i in range(numColumnas):
                frame.grid_columnconfigure(i, weight=1)

    def set_nFilas(self, frame, numFilas=None):
        if not frame: return None
        # frame.grid_rowconfigure(0, weight=1)                
        if numFilas:
            for i in range(numFilas):
                frame.grid_rowconfigure(i, weight=1)
    
    def buscaFrame(self, frameBusca):
        """ 
        Busca un Frame en el arbol desde general hacia abajo.
        Creo que lo mejor es la recursividad.
        """
        # Recorre los widget de un frame. 
        # compara el objeto widget con un frame. 
        # si es el buscado en ese nivel retorna.
        # si no es el buscado en el nivel hay que meterse en cada frame del nivel y buscaar y cuando se agota volver sobre tus pasos para el siguiente.
        if self.esFrame(frameBusca):
            pass
        else:
            self.buscaFrame(frameBusca) 
        
        pass

    def esFrame(self, frame):
        """ 
        tipoFrame es el tipo de objeto.
        """
        if frame==tipoFrame:
            return True
        else:
            return False

    def limpiar_frame(frame):
        # Eliminar todos los widgets dentro del frame
        for widget in frame.winfo_children():
            widget.destroy()

    def eliminar_frame(frame):
        # Elimina el frame y todo su contenido
        frame.destroy()


        # # Crear la ventana principal y una estructura de frames anidados
        # ventana = tk.Tk()
        # ventana.geometry("400x300")
        # frame1 = tk.Frame(ventana, name="frame1", bg="lightblue", width=200, height=100)
        # frame1.pack(fill="both", expand=True, padx=10, pady=10)
        # frame2 = tk.Frame(frame1, name="frame2", bg="lightgreen", width=150, height=75)
        # frame2.pack(fill="both", expand=True, padx=5, pady=5)
        # frame3 = tk.Frame(frame2, name="frame3", bg="lightcoral", width=100, height=50)
        # frame3.pack(fill="both", expand=True, padx=5, pady=5)
        # # Buscar el frame llamado "frame3"
        # frame_buscado = buscaRcrsvFrame_ByName(ventana, "frame3")
        # # Mostrar el resultado de la búsqueda
        # if frame_buscado:
        #     print(f"Frame encontrado: {frame_buscado}")
        #     label = tk.Label(frame_buscado, text="¡Frame encontrado!", bg="yellow")
        #     label.pack()
        # else:
        #     print("Frame no encontrado")
        # ventana.mainloop()
       
    def buscaRcrsvFrame_ByName(framePadreRaiz, nombreFrameBusca):        
        # Si el frame actual tiene el nombre que buscamos, lo retornamos
        if framePadreRaiz.winfo_name() == nombreFrameBusca:
            return framePadreRaiz
        
        # Si no, buscamos en sus hijos de forma recursiva
        for widget in framePadreRaiz.winfo_children():
            if isinstance(widget, tk.Frame):  # Verifica si el hijo es un Frame
                resultado = buscaRcrsvFrame_ByName(widget, nombreFrameBusca)
                if resultado:  # Si encontramos el frame, devolvemos el resultado
                    return resultado
        return None  # Si no se encuentra, devolvemos None

# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????
#  ESTO TIENE QUE SER BORRADO PQ LOS COMMAND DE LOS WIDGET SE DEFINEN EN LA FUNCION QUE INSTANCIA ENFILEITOR
# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????

    # ========================================================    
    # =============== FUNCIONES DIRECTAS DE CLIENTE (Es el emisor de mensajes y archivos)
    # --------------------------
    def enviarMensaje_click(self):        
        messagebox.showinfo("Mensaje", "Enviando mensaje...")
    # --------------------------
    def enviarEmoji_click(self):
        # Lógica para enviar un emoji
        messagebox.showinfo("Emoji", "Enviando emoji...")
    # --------------------------
    def enviarArchivo(self):
        archivo=self.selectFile()
        if archivo:
            messagebox.showinfo("Archivo Seleccionado", f"Has seleccionado: {archivo}")
            pass
        else:
            pass

    # ========================================================    
    # =============== ACCIONES COMUNES A FRAME CLIENTE
    # ========================================================    
    def closeConection_click(self):      
        """     
        Def: Cierra una conexion
        """
        self.lblSTCliente.config(text="Estado: xxxx")
        messagebox.showinfo("Conexión", "Conexión cortada.")

    # --------------------------
    def cargarLboxCliente(self, listServXaClienteMe):
        """ 
        Def: Carga el ListBox de Cliente con los servidores(ip) activos en el puerto.
        [listServXaClienteMe] List de str de servidores escuchando. 
        Esto hay que cambiarlo por un escaneo de la red en el puerto {portCliente} 
        """
        if not isinstance(listServXaClienteMe, list): return 
        for servidor in listServXaClienteMe:
            self.lbxServidores.insert(tk.END, servidor)

    # --------------------------
    def selectFile(self):
        """ 
        Def: Selecciona un Archivo.
        """
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo")
        if archivo:
            return archivo
            # Aquí iría la lógica para enviar el archivo al otherServ From me(client) To other(serv)
        # Función para mostrar una ventana emergente en la esquina superior derecha
    
    # Una misma funcion para gestionar los diferentes eventos
    # Se usa el la librería {functools} el paquete {partial}, 
    # que permite enviar argumentos a un evento command
    def on_button_click(button_name):
        print(f"El botón '{button_name}' ha sido presionado")        
        # =================================
        # FORMA DE LLAMAR A on_button_click
        # =================================
        # button1=tk.Button(root, text="Botón con place()", command=partial(on_button_click, "Btn01"))
        # button1.grid(row=0, column=0 )
        # button2=tk.Button(root, text="Botón2 con place()", command=partial(on_button_click, "Btn02"))
        # button2.grid(row=0, column=1 )

    # _________________________________
    # Función que se ejecuta al seleccionar un elemento en el Listbox
    # =================================
    def lbxServidoresXaClientMe_on_select(self, event):
        # Obtener la selección actual
        seleccion = event.widget.curselection()  # El evento proporciona el widget donde ocurrió
        if seleccion:
            indice = seleccion[0]  # Obtener el primer índice seleccionado
            valor = event.widget.get(indice)  # Obtener el valor del índice
            print(f"Elemento seleccionado: {valor} (Índice {indice})")
            self.lblEquipSelect.config(text=valor)
        else:
            print("Ningún elemento seleccionado.")
    
    # BOTO BUSCAR EQUIPOS
    def buscarEquipos_click(self):
        self.cargarLboxCliente([["localhost","127.0.0.1", "Dvd"],"Equipo 1", "Equipo 2", "Equipo 3"])