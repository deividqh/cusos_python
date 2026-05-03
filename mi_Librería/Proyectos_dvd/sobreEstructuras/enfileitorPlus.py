# Ventanas, Formularios, widgets, eventos de widget, formulario...
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# Para enviar parametros al command y bind
from functools import partial
# -----------------------
from .dvdColor import ColorCorp

from .formPosMov import FormPosMov

class FrameContext:
    contador=0
    def __init__(self, parent, **kwargs):
        # Inicializa el frame con los argumentos opcionales
        self.frame = tk.Frame(parent, **kwargs)
        FrameContext.contador+=1


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


class Enfileitor(FormPosMov):
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
    # listaBordes = list("solid", "raised", "sunken", "groove", "ridge")

    def __init__(self, 
                root, 
                title="Form Cliente Chat", 
                ancho=300, 
                alto=150, 
                posY=None, 
                numFilas=1
                ):
        self.listaFilas=[]
        # ====== cacho el AnchoxAlto Inicial
        self.anchoIni = ancho
        self.altoIni  = alto
        self.numFilas=numFilas
        
        # _________________________
        # ====== Llamada al PADRE                
        super().__init__(root=root,ancho=self.anchoIni, alto=self.altoIni, posY=posY)
        # 

        # ********************************************************************************
        # ======================== OVER ROOT (NIVEL 0)
        # ********************************************************************************
        # Titulo de la Ventana
        self.root.title(title)
        # ==================
        """ 
        Genera un Contenedor(root) con una fila(0) que se expande con el Contenedor
        Genera un Contenedor(root) con una columna(0) que se expande con el Contenedor 

        Genera una Celda que se expande       
        """        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)                

        # ********************************************************************************
        # ======================== OVER ROOT/FRAMENIVEL_1  (NIVEL 1) - CONTENEDOR GENERAL
        # ********************************************************************************
        self.frameNivel_1=tk.Frame(master=root, 
                                    name="frameNivel_1",                #OBLIGATORIO EN LA CLASE PARA BUSCARLO
                                    background=ColorCorp.BlancoX03)                
        # __________________________________
        # ====== Configurar La Expansion 
        # ==================================
        # Aqui es donde se tiene que configurar enfileitor o columneitor.        
        self.frameNivel_1.grid_rowconfigure(index=0, weight=1)        
        self.frameNivel_1.grid_columnconfigure(index=0, weight=1)  
        
        # este va así directo en pack y es el (NIVEL 1) ó  G E N E R A L
        self.frameNivel_1.pack(fill="both", expand=True)

        # ********************************************************************************
        # ======================== OVER ROOT/FRAMENIVEL_1/.... - LISTAESTRUCTURA
        # ********************************************************************************
        self.listaFilas=self.crearFilas_nivel2(general=self.frameNivel_1, numFilas=self.numFilas, xpadx=5, ypady=5)
        # print(self.listaFilas)                        

        # Crea 5 Columnas sobre cada fila.
        for i in range(self.numFilas):
            self.set_nColumnas(frame=self.listaFilas[i], numColumnas=5)
        
        # En la filaFrame[0], la divide en 2 filas/frame mas.
        self.set_nFilas(frame=self.listaFilas[0], numFilas=2)        

        """ listaWidget={
            "nombreWidget1":[tkObjet, fila, columnaEnFila, xpadx, ypady, sticky, fill, expand] , 
            "nombreWidget2":[tk.Button(), listaFilas[0], columnaEnFila, ] , 
            "nombreWidget3":[tk.Button(), listaFilas[0], columnaEnFila, ] 
            } """
        
        
        # *******************************************
        # ----- WIDGETS DEL  FRAME   C L I E N T E 
        # *******************************************
        # _________________
        Row_FORM=0        
        # ================           
        """ 
        LISTBOX: Para mostrar los equipos a los que podemos enviar cosas. """
        print(self.listaFilas.index(self.listaFilas[0]))

        self.lbxServidores = tk.Listbox(master=self.listaFilas[0], name="masterX:1")
        self.lbxServidores.grid(row=Row_FORM, 
                                column=0,                                 
                                sticky="nsew"   # Y se queda pegado a todos los lados
                                )        
        # ______________________
        # Aqui me falta el evento para que cuando seleccione un PC cambie el lblEquipSelect
        # Enlazar el evento de selección al Listbox
        self.lbxServidores.bind('<<ListboxSelect>>', self.lbxServidoresXaClientMe_on_select)       
        # _________________
        Row_FORM = 2     
        # ================   
        """  
        BOTON  Close CNX """
        print(self.listaFilas.index(self.listaFilas[2]))
        self.btnCloseCnX = tk.Button(master=self.listaFilas[2], 
                                    text="Boton", 
                                    command=self.closeConection_click)
        self.btnCloseCnX.grid(row=Row_FORM, column=0)
        """  
        LABEL  equipo seleccionado """
        self.lblEquipSelect = tk.Label( master=self.listaFilas[2], text="Equipo")
        self.lblEquipSelect.grid(row=Row_FORM, column=1)
        """  
        BOTON  Close CNX """
        self.btn_01 = tk.Button(master=self.listaFilas[2], text="Cortar\nConexión", command=self.closeConection_click )
        self.btn_01.grid( row=0, column=4 )
        """  
        LABEL  estado de la conexión """
        self.lblSTCliente = tk.Label( master=self.listaFilas[2], text="Estado", borderwidth=1,  relief="sunken" )
        self.lblSTCliente.grid(row=Row_FORM, column=3)        

        Row_FORM = 3
        # ================   
        """  
        TEXTBOX  """
        self.txtEnviar = tk.Entry(master=self.listaFilas[2])
        self.txtEnviar.grid(row=Row_FORM, column=0,columnspan=4,  sticky="ew")

        Row_FORM = 4
        # ================   
        """  
        BOTON  """
        self.btnEnviarMsg = tk.Button(  master=self.listaFilas[3], text="Enviar", command=self.enviarMensaje_click)
        self.btnEnviarMsg.grid(row=Row_FORM, column=0)

        """  
        BOTON  Eviar Archivo """
        self.btnEnviarArchivo = tk.Button(master=self.listaFilas[3], text="Enviar Archivo", command=self.selectFile)
        self.btnEnviarArchivo.grid(row=Row_FORM, column=1)

        """  
        BOTON  Emoji """
        self.btnEnviarEmoji = tk.Button(master=self.listaFilas[3], text="Enviar Emoji", command=self.enviarEmoji_click)
        self.btnEnviarEmoji.grid(row=Row_FORM, column=2)
    
    # def crearFrame(self, numFilas)
        
        
    def crearFilas_nivel2(self, general, numFilas, background=ColorCorp.BlancoX03, xpadx=5, ypady=5):
        """
        Crea tantos frames contenedores como numFilas.
        Los frames están disponibles en self.listaFilas. self.listaFilas[0] = fila 0
        >>> [general] es el frame contenedor de nivel 1. 
        >>> contenedor[root][nivel 0] -> contenedor[general][nivel 1] -> listaFilas[0]....listaFilas[n]  [nivel 2]filas
        """        
        for i in range(numFilas):
            # Crea un frame, en el frame general
            frameFila=tk.Frame(master=general, name="fila_"+str(i), background=background)
            # _________________________
            # Metemos la fila(el frame) en una lista y lo empackamos(pack)
            self.listaFilas.append (frameFila)

            frameFila.pack()
            if xpadx:
                frameFila.pack(padx=xpadx)            
            if ypady:
                frameFila.pack(pady=ypady)
            
        return self.listaFilas
        
    # *************************************************************** 
    # *************************************************************** 
    def set_nColumnas(self, frame, numColumnas=None):
        if not frame: return None
        frame.grid_rowconfigure(0, weight=1)        
        if numColumnas:
            for i in range(numColumnas):
                frame.grid_columnconfigure(i, weight=1)

    def set_nFilas(self, frame, numFilas=None):
        if not frame: return None
        # frame.grid_rowconfigure(0, weight=1)                
        if numFilas:
            for i in range(numFilas):
                frame.grid_rowconfigure(i, weight=1)

    # Crea un nivel (division filas y columnas) en una Fila/Frame
    # def crearNivelFila(self, filaFrame, numFilas=-1, numColumns=-1):
    #     if numColumns !=-1:
    #         self.set_nColumnas(frame=filaFrame, numColumnas=numColumns)
    #     if numFilas !=-1:
    #         self.set_nFilas(frame=filaFrame, numFilas=numFilas)

    
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



    # =======================    
    # FUNCIONES DIRECTAS DE CLIENTE (Es el emisor de mensajes y archivos)
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
    # =============== ACCIONES COMUNES
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
    
    def buscarEquipos_click(self):
        self.cargarLboxCliente([["localhost","127.0.0.1", "Dvd"],"Equipo 1", "Equipo 2", "Equipo 3"])