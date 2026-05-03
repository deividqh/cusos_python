# Ventanas, Formularios, widgets, eventos de widget, formulario...
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# Para enviar parametros al command y bind
from functools import partial
# -----------------------
from .dvdColor import ColorCorp

from .formPosMov import FormPosMov


class FormularioClienteChatAvanza(FormPosMov):
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """
    def __init__(self, 
                root, 
                title="Formulario Cliente Chat", 
                ancho=300, alto=150, 
                posY=None
                ):
        # ====== cacho el AnchoxAlto Inicial
        self.anchoIni=ancho
        self.altoIni=alto
        # _________________________
        # ====== Llamada al PADRE        
        super().__init__(root=root,ancho=self.anchoIni, alto=self.altoIni, posY=posY)
        # ====== Titulo de la Ventana
        self.root.title(title)
        # Configurar que el Frame se expanda con la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        
        self.frameCliente=tk.Frame(master=root, 
                                    name="framecliente", 
                                    background=ColorCorp.BlancoX03)                
        # Configurar el peso de las columnas y filas para permitir expansión
        # self.frameCliente.grid_columnconfigure( 0, weight=1)
        # self.frameCliente.grid_rowconfigure(0, weight=1)
        # Expansion del frame
        self.frameCliente.pack(fill="both", expand=True)

        # __________________________________
        # ====== Configurar La Expansion 
        # ==================================        
        self.frameCliente.grid_rowconfigure(0, weight=1)        
        self.frameCliente.grid_columnconfigure(0, weight=1)  # Primera columna más pequeña

        # *******************************************
        # ----- WIDGETS DEL  FRAME   C L I E N T E 
        # *******************************************

        # _________________
        Row_FORM=0        
        # ================           
        self.frameFila0 = tk.Frame(master=self.frameCliente, 
                            background=ColorCorp.BlancoX03)
        self.frameFila0.pack(fill="both", expand=True, padx=3, pady=3)        
        # _________________
        # CONFIGURA 5 COLUMNAS EN EL FRAME        
        self.frameFila0.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frameFila0.grid_columnconfigure(i, weight=1)
        # _________________
        # CONFIGURA 2 FILAS EN EL FRAME        
        for i in range(2):
            self.frameFila0.grid_rowconfigure(i, weight=1)
        
        """ 
        LISTBOX: Para mostrar los equipos a los que podemos enviar cosas. """
        self.lbxServidores = tk.Listbox(master=self.frameFila0)
        self.lbxServidores.grid(row=0,          
                                column=0, 
                                rowspan=2,      # ocupa 2 FILAS
                                columnspan=3 ,  # ocupa 2 COLUMNAS
                                sticky="nsew"   # Y se queda pegado a todos los lados
                                )        

        # ______________________
        # Aqui me falta el evento para que cuando seleccione un PC cambie el lblEquipSelect
        # Enlazar el evento de selección al Listbox
        self.lbxServidores.bind('<<ListboxSelect>>', self.lbxServidoresXaClientMe_on_select)       
        """  
        BOTON  Close CNX """
        self.btnCloseCnX = tk.Button(master=self.frameFila0, 
                                    text="Cortar Conexión", 
                                    command=self.closeConection_click)
        self.btnCloseCnX.grid(row=0, 
                            column=4)
        """  
        BOTON  Buscar Equipos ----- infoSocket.checkRedLocalFromTo(1,255) """
        self.btnBuscarEquipos = tk.Button(master=self.frameFila0, 
                                        text="Load Pc's", 
                                        command=self.buscarEquipos_click)
        self.btnBuscarEquipos.grid(row=1, 
                                    column=4)
        # _________________
        Row_FORM = 1     
        # ================   
        self.frameFila1 = tk.Frame(  master=self.frameCliente, 
                                background=ColorCorp.BlancoX03)
        self.frameFila1.pack(padx=10, pady=10)
        """  
        LABEL  equipo seleccionado """
        self.lblEquipSelect = tk.Label( master=self.frameFila1, 
                                        text="Equipo: Ninguno")
        # self.lblEquipSelect.grid(row=Row_FORM, column=0, padx=2, pady=2)
        self.lblEquipSelect.grid(row=Row_FORM, column=0)
        """  
        LABEL  estado de la conexión """
        self.lblSTCliente = tk.Label(master=self.frameFila1, 
                                     text="Estado: Desconectado")
        self.lblSTCliente.grid(row=Row_FORM, column=1)        
        # _________________
        Row_FORM = 2
        # ================   
        self.frameFila2 = tk.Frame(  master=self.frameCliente, 
                                background=ColorCorp.BlancoX03)
        self.frameFila2.pack(padx=10, pady=10)
        """  
        TEXTBOX  """
        self.txtEnviar = tk.Entry(master=self.frameFila2)
        self.txtEnviar.grid(row=Row_FORM, column=0,columnspan=4,  sticky="ew")
        # _________________
        Row_FORM = 3
        # ================   
        self.frameFila3 = tk.Frame(  master=self.frameCliente, 
                                background=ColorCorp.BlancoX03)
        self.frameFila3.pack(padx=10, pady=10)
        # ----- Boton Enviar Texto.
        """  
        BOTON  """
        self.btnEnviarMsg = tk.Button(  master=self.frameFila3, 
                                        text="Enviar", 
                                        command=self.enviarMensaje_click)
        self.btnEnviarMsg.grid(row=Row_FORM, column=0)

        # ----- Boton Eviar Archivo
        """  
        BOTON  """
        self.btnEnviarArchivo = tk.Button(  master=self.frameFila3, 
                                            text="Enviar Archivo", 
                                            command=self.selectFile)
        self.btnEnviarArchivo.grid(row=Row_FORM, column=1)

        # ----- Boton Eviar Emoji
        # aqui necesito eventos para seleccionar el emoji
        """  
        BOTON  """
        self.btnEnviarEmoji = tk.Button(master=self.frameFila3,  
                                        text="Enviar Emoji", 
                                        command=self.enviarEmoji_click)
        self.btnEnviarEmoji.grid(row=Row_FORM, column=2)
        
        # ----- Rellenaar el listBox -> Lista de equipos(Cachar equipos de Red)
        # self.cargarLboxCliente([["localhost","127.0.0.1", "Dvd"],"Equipo 1", "Equipo 2", "Equipo 3"])
        
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
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo", )
        if archivo:
            return archivo
            # Aquí iría la lógica para enviar el archivo al otherServ From me(client) To other(serv)
        # Función para mostrar una ventana emergente en la esquina superior derecha

    def OpenVentanaUpRight(self, mensaje):
        ventana = tk.Tk()
        ventana.title("Nuevo Mensaje")
        ventana.geometry(f"200x100+{ventana.winfo_screenwidth() - 210}+10")  # Posicionar en la esquina superior derecha
        
        label = tk.Label(ventana, text=mensaje)
        label.pack(padx=20, pady=20)
        
        # Configura para que la ventana se cierre automáticamente después de 3 segundos
        ventana.after(3000, ventana.destroy)
        ventana.mainloop()

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