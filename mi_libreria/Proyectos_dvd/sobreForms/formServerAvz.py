import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from .formPosMov import FormPosMov
from .dvdColor import ColorCorp
# _____________________
# Para enviar parametros al command y bind
# from functools import partial
# -----------------------
# class FormularioServerAvanza():
class FormularioServerAvanza(FormPosMov):
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """
    # coorX=0
    # coorY=0
    # esExpandido=False
    def __init__(self, root, 
                title="FormServ Chat", 
                ancho=300, 
                alto=150, 
                posY=None):

        # ====== Llamada al PADRE
        super().__init__(root=root,ancho=ancho, alto=alto, posY=posY)
        
        # ====== cacho el AnchoxAlto Inicial
        self.anchoIni=ancho
        self.altoIni=alto
        # ====== Titulo de la Ventana
        self.root.title(title)        
        
        # ==================================
        # ====== Configurar Que el contenido(grid) de la fila 0 se expaandirá con la ventana(root)
        # ====== Como en root se va a meter un contenedor general (frameServidor), solo va a haber una fila y columna(=0)
        # ==================================
        self.root.grid_rowconfigure(0, weight=1,)        
        self.root.grid_columnconfigure(0, weight=1)  

        # ****************************************
        # ====== WIDGETS DEL FRAME SERVIDOR 
        # ****************************************
        self.frameServidor=tk.Frame(master=self.root,
                                    name="frameservidor", 
                                    background=ColorCorp.Canela                                    
                                    )     
        self.frameServidor.pack(fill="both", expand=True)
        # ==================================
        # ====== Configurar La Expansion 
        # ==================================        
        self.frameServidor.grid_rowconfigure(0, weight=1)        
        self.frameServidor.grid_columnconfigure(0, weight=1)  # Primera columna más pequeña
        pass

        # ________________
        Row_FORM = 0
        # ================
        self.frameFila0 = tk.Frame( master=self.frameServidor, 
                                    background=ColorCorp.BlancoX03
                                    )
        self.frameFila0.pack(fill="both", padx=5, pady=5)

        # CONFIGURA 5 COLUMNAS EN EL FRAME
        # grid_columnconfigure(i, weight=1) establece el peso de cada columna. 
        #   Cuando el weight es 1, indica que todas las columnas se expandirán uniformemente cuando el Frame cambie de tamaño.
        #   Ahora, al usar .grid(row=..., column=...) para ubicar los widgets en el Frame, 
        #   tienes 4 columnas disponibles y puedes colocarlos sabiendo de antemano cómo se dividirá el espacio.       
        self.frameFila0.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frameFila0.grid_columnconfigure(i, weight=1)

        """  
        CHECK-BUTTON  de Conexion/Desconexion """
        # Crear una variable de control(chkBttnServer_valor) para almacenar el estado del Checkbutton
        self.chkBttnServer_valor = tk.IntVar()  # 0 = desmarcado, 1 = marcado
        # Crear el Checkbutton y enlazar la función chkBttnServer_Check() al evento de cambio
        self.chkBttnServer = tk.Checkbutton(master=self.frameFila0, 
                                            text="Servidor\n Activo", 
                                            variable=self.chkBttnServer_valor, 
                                            command=self.chkBttnServer_Check
                                            )                                            
        self.chkBttnServer.grid(row=Row_FORM, 
                                column=0, 
                                sticky="ew",    #Los convierte elastico derecha-izquierda
                                padx=3          
                                )
        # Botón Toggle Desplegar
        """  
        BOTÓN TOGGLE Desplegar """
        self.btnToggle = tk.Button(master=self.frameFila0, 
                                   text="DPleg", 
                                   command=self.toggle_expand)
        self.btnToggle.grid(row=Row_FORM, 
                            column=1,
                            sticky="ew"
                            )
        """  
        BUTTON  """
        self.btnSetPuerto = tk.Button(  master=self.frameFila0, 
                                        text="Alfa", 
                                        command=self.setPuerto_click
                                    )
        self.btnSetPuerto.grid(row=Row_FORM, 
                                column=2, 
                                sticky="ew"     #Los convierte elastico derecha-izquierda
                                )
        """  
        BUTTON  """
        self.btnSetPuerto = tk.Button(  master=self.frameFila0, 
                                        text="Port", 
                                        command=self.setPuerto_click
                                    )
        self.btnSetPuerto.grid(row=Row_FORM, 
                                column=3, 
                                sticky="ew")        #Los convierte elastico derecha-izquierda
        """  
        BUTTON  """
        self.btnSetPuerto = tk.Button(  master=self.frameFila0, 
                                        text="Open", 
                                        command=self.setPuerto_click
                                    )
        self.btnSetPuerto.grid(row=Row_FORM, 
                                column=4,
                                sticky="ew"         #Los convierte elastico derecha-izquierda
                                )


        # ________________
        Row_FORM = 1
        # ================
        self.frameFila1 = tk.Frame( master=self.frameServidor, 
                                    background=ColorCorp.BlancoX01)
        self.frameFila1.pack(fill="both", 
                            expand=True, 
                            padx=5, pady=5)
        
        # CONFIGURA 5 COLUMNAS EN EL FRAME
        self.frameFila1.grid_rowconfigure(0, weight=1)        
        self.frameFila1.grid_columnconfigure(0, weight=1)        
        # for i in range(5):
        #     self.frameFila1.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña

        """  
        LISTBOX de MENSAJES RECIBIDOS. 
        Aquí no cofiguro columnas. Meto el list e PACK(), para que ocupe el frame entero"""
        self.lbxMensajesRecibidos=tk.Listbox(master=self.frameFila1, 
                                            background=ColorCorp.BlancoX04)
        self.lbxMensajesRecibidos.pack(fill="both", 
                                        expand=True, 
                                        padx=5, 
                                        pady=5
                                    )  # Ocupa todo el ancho disponible
        # ________________
        Row_FORM = 2
        # ================
        self.frameFila2 = tk.Frame( master=self.frameServidor, 
                                    background=ColorCorp.BlancoX02
                                    )
        self.frameFila2.pack(fill="x", padx=5, pady=5)
        # CONFIGURA 5 COLUMNAS EN EL FRAME
        self.frameFila2.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frameFila2.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña

        """  
        LABEL  Equipo """
        self.lblPcCnx=tk.Label( master=self.frameFila2, 
                                text="Equipo X"
                                )
        self.lblPcCnx.grid( row=Row_FORM, 
                            column=0
                            )
        """  
        LABEL   """
        self.lblPcCnx=tk.Label( master=self.frameFila2, 
                                text="Lbl 1"
                                )
        self.lblPcCnx.grid( row=Row_FORM, 
                            column=1
                            )
        """  
        LABEL   """
        self.lblPcCnx=tk.Label( master=self.frameFila2, 
                                text="Lbl 2"
                                )
        self.lblPcCnx.grid( row=Row_FORM, 
                            column=3
                            )
        """          
        LABEL  Estado """
        self.lblStCnxServ=tk.Label( master=self.frameFila2, 
                                    text="Estado X"
                                    )
        self.lblStCnxServ.grid(row=Row_FORM, 
                                column=4 )        
        # ________________
        Row_FORM = 3
        # ================
        
        self.frameFila3 = tk.Frame( master=self.frameServidor, 
                                    background=ColorCorp.BlancoX03
                                )
        self.frameFila3.pack(fill="x", padx=5, pady=5)
        
        # CONFIGURA 5 COLUMNAS EN EL FRAME
        self.frameFila3.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frameFila3.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña

        """  
        BUTTON  """
        self.btnSetPuerto = tk.Button(  master=self.frameFila3, 
                                        text="Puerto", 
                                        command=self.setPuerto_click
                                    )
        self.btnSetPuerto.grid(row=Row_FORM, 
                                column=0,
                                sticky="ew"
                                )
        """  
        TEXTBOX  """
        self.txtEnviar = tk.Entry(master=self.frameFila3)
        self.txtEnviar.grid(row=Row_FORM, 
                            column=1,
                            columnspan=1,  
                            sticky="we")
        

    # ==========================================================================    
    # METODOS FUNDAMENTALES DE SERVIDOR (Es el receptor de mensajes y archivos)
    # ----------------------------------
    def recibirMsg():
        messagebox.showinfo("Recibir Msg")
        pass
    def recibirArchivo():
        messagebox.showinfo("Recibir Archivo\nMostrar nombreArchivo\n1-BtnGuardar Archivo\n2-BtnVer Archivo en RAM")
        pass
    def recibirEmoji():
        messagebox.showinfo("Archivo Seleccionado", f"Has seleccionado: {archivo}")
        pass
    # ____________________
    # Función que manejará el evento de cambio en el Checkbutton
    # Tiene que poner el Servidor en escucha
    def chkBttnServer_Check(self):
        if self.chkBttnServer_valor.get() == 1:  # Si el Checkbutton está marcado
            print("""1- Aqui tengo que crear un hilo Xa el socketServidor Xa Independizar el servidor del Formulario
2- Tengo que ponerlo en escucha.
3- Notificarlo en el Formulario con un semaforo Canvas(este me gusta)
                     """)
        else:
            print("""1- Notificar al cliente que corto la Conexion
2- Cortar la Conexion o Matar el hilo del socket.
3- Notificar en el Formulario con un Semaforo.
                """)
    
    # =======================    
    # ACCIONES COMUNES
    # ------------------------
    # ___________________
    # Al hacer doble clic, expandir o contraer la ventana
    # def formRoot_dblClick(self, event):
    #     if FormularioServerAvanza.esExpandido:
    #         self.desplazaFormRoot(mostrar_completa=False)
    #     else:
    #         self.desplazaFormRoot(mostrar_completa=True)
    # # ____________________
    # # Mueve la ventana con el metodo de root after
    # def desplazaFormRoot(self, mostrar_completa=True):
    #     # global coorX, esExpandido
    #     if mostrar_completa:
    #         # Expande la ventana hacia el centro de la pantalla
    #         if FormularioServerAvanza.coorX > self.screenWidth - self.formWidth - 10:
    #             FormularioServerAvanza.coorX -= 10
    #             self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormularioServerAvanza.coorX}+{FormularioServerAvanza.coorY}')
    #             self.root.after(20, self.desplazaFormRoot)
    #         else:
    #             FormularioServerAvanza.esExpandido = True  # Indica que la ventana está completamente expandida
    #     else:
    #         # Contrae la ventana de nuevo hacia los 40 píxeles visibles
    #         if FormularioServerAvanza.coorX < self.screenWidth - 40:
    #             FormularioServerAvanza.coorX += 10
    #             self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormularioServerAvanza.coorX}+{FormularioServerAvanza.coorY}')
    #             self.root.after(20, self.desplazaFormRoot, False)
    #         else:
    #             FormularioServerAvanza.esExpandido = False  # Indica que la ventana está contraída


    def closeConection_click(self):      
        """     
        Def: Cierra una conexion
        """
        messagebox.showinfo("Conexión", "Conexión cortada.")
    # --------------------------

    

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

    def setPuerto_click(self):        
        messagebox.showinfo(title="set Puerto",message="Cambiando el puerto")