class form_biblioteca(Formulario_Ninja):
    """ 
    >>> Def: Define un formulario Tkinter con funcion de gestión de una clase Biblioteca y otra Libro.
    Hereda de Formulario_Ninja, que a su vez hereda de tk.Tk. 
    El formulario tiene un diseño con varios frames organizados en filas y columnas, 
    y contiene widgets como Checkbutton, Button, Label, Entry y Listbox para interactuar con la 
    biblioteca de libros. 
    """
    def __init__(self, 
                root, 
                title="Formulario", 
                ancho=300, 
                alto=450, 
                posY=None):

        # ====== Llamada al PADRE
        super().__init__(root=root, ancho=ancho, alto=alto, posY=posY)

        """ Familias de objetos para realizar acciones en masa (validar, vaciar, cargar, etc)
        van a tener sus propios metodos dedicados """
        self.family_txtbx = []            # los objetos texto que tienen que ser validados en grupo.
        self.family_bttn_crud = []        # los objetos boton add / del / updt 
        
        self.memo_inf=InfApp()
        """ >>>  """

        self.archivo = ''
        """ >>> Nombre de la ruta al archivo que queremos cargar. """

        self.biblioteca = Biblioteca()
        """ >>> Instancia de Biblioteca """

        self.libro_select_lstbx=[]
        """ >>> lista que guardará una copia de los valores del elemento seleccionado en el self.lbx_babel """

        # ________________________________________
        # ====== NIVEL ZERO (root) 
        # ########################################
        self.root.title(title)        
        """ Configurar Que el contenido(grid) de la fila 0 se expaandirá con la ventana(root)
        Como en root se va a meter un contenedor general (frame_nivel1), solo va a haber una fila y columna(=0) """
        self.root.grid_rowconfigure(0, weight=1,)        
        self.root.grid_columnconfigure(0, weight=1)  
        pass
        # ________________________________________
        # ====== from NIVEL ZERO  to  NIVEL 1( Contenedor General: self.frame_nivel1 )
        # ########################################
        self.frame_nivel1=tk.Frame(master=self.root, name="frame_nivel1", background=ColorCorp.Canela )     
        self.frame_nivel1.pack(fill="both", expand=True)
        # Configurar La Expansion 
        self.frame_nivel1.grid_rowconfigure(0, weight=1)        
        self.frame_nivel1.grid_columnconfigure(0, weight=1) 
        pass
        # ________________________________________
        # ====== FROM NIVEL 1   to   NIVEL 2  ( F I L A S  )
        # ########################################
        Row_FORM = 0    #  F I L A 0
        # ================
        self.frm_nivel2_0 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.Canela   )
        self.frm_nivel2_0.pack(fill="both", padx=5, pady=5)
        """ >>> Empaqueta el frame con expansion vertical y horizontal.
        """
        self.frm_nivel2_0.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_0.grid_columnconfigure(i, weight=1)
        """ >>> CONFIGURA 5 COLUMNAS EN EL FRAME:
        grid_columnconfigure(i, weight=1) establece el peso de cada columna. 
        Cuando el weight es 1, indica que todas las columnas se expandirán uniformemente cuando el Frame cambie de tamaño.
        Ahora, al usar .grid(row=..., column=...) para ubicar los widgets en el Frame, 
        tienes 5 columnas disponibles y puedes colocarlos sabiendo de antemano cómo se dividirá el espacio.        """
        #__________________________________
        # CHECK-BUTTON  de Conexion/Desconexion
        self.chkBttnServer_valor = tk.IntVar()  # 0 = desmarcado, 1 = marcado
        """ >>> Crear una variable de control(chkBttnServer_valor) para almacenar el estado del Checkbutton 
        """
        self.chkBttnServer = tk.Checkbutton(master=self.frm_nivel2_0, 
                                            text="Cargar Babel", 
                                            background=ColorCorp.Canela  ,
                                            variable=self.chkBttnServer_valor, 
                                            command=self.chkbttn_click
                                            )                                            
        """ >>> Crear el Checkbutton y enlazar la función chkbttn_click() al evento de cambio
        """
        # Situo con grid.
        self.chkBttnServer.grid(row=Row_FORM, column=0, sticky="ew", padx=3 )
        """  
        BUTTON  """
        self.bttn_loadfile = tk.Button(  master=self.frm_nivel2_0, text="Load File", command=self.bttn_loadfile_click )
        self.bttn_loadfile.grid(row=Row_FORM, column=4, sticky="ew" )   

        # ======================================================================
        Row_FORM = 1            # L A B E L   R U T A   A B R E V I A D A    A R C H I V O 
        # ================
        self.frm_nivel2_1 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX02 )
        self.frm_nivel2_1.pack(fill="x", padx=5, pady=5)
        # ________________
        self.frm_nivel2_1.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_1.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        LABEL   """
        self.lbl_archivo=tk.Label( master=self.frm_nivel2_1, text="-", background=ColorCorp.BlancoX01)
        self.lbl_archivo.grid( row=Row_FORM, column=0, rowspan=1,columnspan=5 , sticky="we")

        # ======================================================================
        Row_FORM = 2        # L I S T B O X   B A B E L 
        # ================
        self.frm_nivel2_1 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX01)
        self.frm_nivel2_1.pack(fill="both", expand=True, padx=5, pady=5)        
        # ____________________________________        
        self.frm_nivel2_1.grid_rowconfigure(0, weight=1)        
        self.frm_nivel2_1.grid_columnconfigure(0, weight=1)   
        # __________
        # LISTBOX 
        """ >>> LISTBOX de MENSAJES RECIBIDOS. Aquí no cofiguro columnas. Meto el list e PACK(), para que ocupe el frame entero
        # for i in range(5):
        #     self.frm_nivel2_1.grid_columnconfigure(i, weight=1, minsize=50)  
        """        
        self.lbx_babel = tk.Listbox(master=self.frm_nivel2_1, background=ColorCorp.BlancoX04)
        self.lbx_babel.pack(fill="both", expand=True, padx=5, pady=5 ) 
        self.lbx_babel.bind("<<ListboxSelect>>", self.lbx_on_select)
        # ======================================================================
        # Row_FORM = 3            # L A B E L   I N F O 
        # ================
        self.frm_nivel2_2 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX02 )
        self.frm_nivel2_2.pack(fill="x", padx=5, pady=5)
        # ________________
        self.frm_nivel2_2.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_2.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        LABEL   """
        self.lbl_info=tk.Label( master=self.frm_nivel2_2, text="Info:", background=ColorCorp.AzulX01 )
        self.lbl_info.grid( row=Row_FORM, column=0, rowspan=1,columnspan=3 , sticky="we")
        """  
        LABEL   """
        self.lbl_subinfo=tk.Label( master=self.frm_nivel2_2, text="sub-info:", background=ColorCorp.AzulX02 )
        self.lbl_subinfo.grid( row=Row_FORM, column=3 , rowspan=1,columnspan=2, sticky="we")
        # ======================================================================
        Row_FORM = 4        # BOTONES  A D D  -  D E L  -  U P D T 
        # ================        
        self.frm_nivel2_3 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX03)
        self.frm_nivel2_3.pack(fill="x", padx=5, pady=5)        
        # ________________
        self.frm_nivel2_3.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_3.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        BUTTON  """
        self.bttn_add = tk.Button(  master=self.frm_nivel2_3, text="Add", command=self.bttn_add_click, background=ColorCorp.BlancoX05)
        self.bttn_add.grid(row=Row_FORM, column=0, rowspan=1,columnspan=2, sticky="ew" )
        # self.bttn_add.bind("<Button-1>", self.bttn_add_click)
        """  
        BUTTON  """
        self.bttn_updt = tk.Button(  master=self.frm_nivel2_3, text="Updt", background=ColorCorp.BlancoX05)
        self.bttn_updt.grid(row=Row_FORM, column=2, rowspan=1,columnspan=2, sticky="ew")        #Los convierte elastico derecha-izquierda
        self.bttn_updt.bind("<Button-1>", self.bttn_updt_click)
        """  
        BUTTON  """
        self.bttn_del=tk.Button(  master=self.frm_nivel2_3, text="Del", background=ColorCorp.BlancoX05)
        self.bttn_del.grid(row=Row_FORM, column=4, rowspan=1,columnspan=1, sticky="ew" )        
        self.bttn_del.bind("<Button-1>", self.bttn_del_click)
        # ======================================================================      
        Row_FORM = 5        # T E X T    T I T U L O
        # ================       
        self.frm_nivel2_4 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX03)
        self.frm_nivel2_4.pack(fill="x", padx=5)        
        # ________________
        self.frm_nivel2_4.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_4.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        LABEL   """
        self.lbl_xxx=tk.Label( master=self.frm_nivel2_4, text="Titulo:", background=ColorCorp.BlancoX05 )
        self.lbl_xxx.grid( row=Row_FORM, column=0,rowspan=1,columnspan=2,sticky="we" )
        """  
        TEXTBOX  """
        self.txt_titulo = tk.Entry(master=self.frm_nivel2_4, name='titulo')
        self.txt_titulo.grid(row=Row_FORM, column=2,rowspan=1,columnspan=3,sticky="we")
        # ======================================================================
        Row_FORM = 6        # T E X T    A U T O R
        # ================        
        self.frm_nivel2_5 = tk.Frame( master=self.frame_nivel1, background=ColorCorp.BlancoX03 )
        self.frm_nivel2_5.pack(fill="x", padx=5)        
        # ________________
        self.frm_nivel2_5.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_5.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        LABEL   """
        self.lbl_xxx=tk.Label( master=self.frm_nivel2_5, name='autor', text="Autor:" , background=ColorCorp.BlancoX05)
        self.lbl_xxx.grid( row=Row_FORM, column=0,rowspan=1,columnspan=2, sticky="we" )        
        """  
        TEXTBOX  """
        self.txt_autor = tk.Entry(master=self.frm_nivel2_5)
        self.txt_autor.grid(row=Row_FORM, column=2,rowspan=1,columnspan=3, sticky="we")
        # ======================================================================        
        Row_FORM = 7        # T E X T    N U M  P A G 
        # ================        
        self.frm_nivel2_6 = tk.Frame( master=self.frame_nivel1, name='numpag', background=ColorCorp.BlancoX03 )
        self.frm_nivel2_6.pack(fill="x" , padx=5 , pady=(0, 10) )        
        # ________________
        self.frm_nivel2_6.grid_rowconfigure(0, weight=1)        
        for i in range(5):
            self.frm_nivel2_6.grid_columnconfigure(i, weight=1, minsize=50)  # Primera columna más pequeña
        """  
        LABEL   """
        self.lbl_numpag=tk.Label( master=self.frm_nivel2_6, text="Numero Pag:", background=ColorCorp.BlancoX05)
        self.lbl_numpag.grid( row=Row_FORM, column=0,rowspan=1,columnspan=2, sticky="we", pady=3)
        """  
        TEXTBOX  """
        self.txt_numpag = tk.Entry(master=self.frm_nivel2_6)
        self.txt_numpag.grid(row=Row_FORM, column=2,rowspan=1,columnspan=3, sticky="we", pady=3)

        # ***********************************************************
        # GRUPOS (Para realizar acciones en masa - Familias objetos)
        # ***********************************************************
        self.family_txtbx.append(self.txt_titulo)
        self.family_txtbx.append(self.txt_autor)
        self.family_txtbx.append(self.txt_numpag)

        self.family_bttn_crud.append(self.bttn_add)
        self.family_bttn_crud.append(self.bttn_del)
        self.family_bttn_crud.append(self.bttn_updt)
