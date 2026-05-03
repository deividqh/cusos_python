
import os
import tkinter as tk
import json
# Para enviar parametros al command y bind
from functools import partial
from tkinter import filedialog, messagebox, ttk
from enum import Enum as SMFR
# ___________________
from .formPosMov import Formulario_Ninja
from .dvdColor import ColorCorp

from sobreBiblioteca.libro import Libro
from sobreBiblioteca.biblioteca import Biblioteca


class Semaforo_bttn(SMFR):
    ADD=0
    UPT=1
    DEL=2
class InfApp():
    def __init__(self, last_msg='', last_index=0):
        self.last_msg=last_msg
        self.last_index=last_index


class form_biblioteca(Formulario_Ninja):
    """ 
    >>> Def: Define un formulario Tkinter con funcion de gestión de una clase Biblioteca y otra Libro.    
    """
    # coorX=0
    # coorY=0
    # esExpandido=False
    def __init__(self, 
                root, 
                title="Formulario", 
                ancho=300, 
                alto=450, 
                posY=None):

        # ====== Llamada al PADRE
        super().__init__(root=root,ancho=ancho, alto=alto, posY=posY)

        self.family_txtbx=[]            # los objetos texto que tienen que ser validados en grupo.
        self.family_bttn_crud=[]        # los objetos boton add / del / updt 
        
        self.memo_inf=InfApp()

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
    # ==============================================================================================================

    # **************************************************************************************************************
    #    A C C I O N E S   D I R E C T A S     ( BOTONES ADD, DEL, UPDT, LOADFILE - CHECKBUTTON - SELECT-LISTBOX )
    # **************************************************************************************************************
    
    # ____________________
    def bttn_add_click(self):      
        """     
        >>> Def: Add Registro   """
        # self.semaforo_botones(boton=event.widget, bIni=False)
        if self.validar_texto() == False:
            self.informarApp('Error Datos Text...', 'Failed :(')
            return                
        # _________________
        # Creo un libro
        titulo=str(self.txt_titulo.get())
        autor=str(self.txt_autor.get())
        numpag=str(self.txt_numpag.get())  

        un_libro=Libro(titulo=titulo, autor=autor, numpag=numpag)
        """ >>> Instancia de la clase libro """        
        if not un_libro:
            return None
        try:
            if self.biblioteca.agregar_libro(new_libro=un_libro)==False: 
                self.informarApp('Error de Libro. Op. Anulada ',':(')
                return
            # ____________________________
            # Escribe en el archivo desde self.biblioteca.libros
            formato_json=self.biblioteca.from_biblioteca_to_json(ruta_archivo=self.archivo)
            # ____________________________
            self.vaciar_listbox()
            # ____________________________
            self.from_archivo_to_biblioteca()
            # ____________________________
            self.from_archivo_to_lbx_babel()

            self.vaciar_textbox()

        except Exception as e:
            self.informarApp('Error al Añadir Registro', ':(')
            print(f"Error: {e}")
        else:
            self.informarApp('Registro Add!!', 'OK ;)')        
            # messagebox.Message(title='Añadir Registro', message=f'Titulo: {unlibro.titulo}\nAutor: {unlibro.autor} \nNumero de Páginas: {unlibro.numpag} \nadd OK!! ;)')
    # ____________________        
    def bttn_updt_click(self, event):      
        """     
        >>> Def: Upt Registro  """
        # self.biblioteca.a_json_to_biblioteca(nombre_archivo=self.archivo)        
        if self.validar_texto() == False:
            self.informarApp('Error UPDT Data Text...', 'Failed :(')
            return
        seleccion = self.lbx_babel.curselection() 
        if seleccion:
            libro = self.crea_libro_from_txtbox()
            copy_libro = self.crea_libro_from_txtbox()

            if self.biblioteca.get_index_libro(libroBusca=libro):
                self.informarApp('Updt No Posible....',':(')
                return None
            else:
                self.biblioteca.del_libro(libroDel=self.libro_select_lstbx)
                self.bttn_add_click()
                self.vaciar_textbox()
        else:
            pass
        
        self.informarApp('Registro Updt', 'OK ;')
    # ____________________
    def bttn_del_click(self, event):      
        """     
        >>> Def: Del Registro  """
        if self.validar_texto() == False:
            self.informarApp('Error DEL Data Text...', 'Failed :(')
            return
        seleccion = self.lbx_babel.curselection() 
        if seleccion:
            libro = self.crea_libro_from_txtbox()
            if not self.biblioteca.get_index_libro(libroBusca=libro):
                self.informarApp('Libro no Encontrado',':(')
                return None
            else:
                """  """
                self.biblioteca.del_libro(libroDel=libro)
                self.biblioteca.from_biblioteca_to_json(self.archivo)
                # self.from_archivo_to_biblioteca()
                self.vaciar_listbox()
                self.from_archivo_to_lbx_babel()
                self.vaciar_textbox()
                self.informarApp('Registro DEL', 'OK ;)')
    
    # ____________________
    # B O T O N  Para FILEDIALOG       Del Fichero seleccionado  a lbl_archivo y self.archivo
    def bttn_loadfile_click(self):      
        """     
        >>> Def: Load Fichero  """
        self.archivo = self.selectFile()
        if self.archivo:
            # messagebox.showinfo(title="Load File:", message=f"Fichero cargado {archivo} ")
            # Nombre y path
            nombre_archivo = os.path.basename(p=self.archivo)
            ruta_archivo = os.path.dirname(p=self.archivo)
            ruta_abrevd = form_biblioteca.ruta_abrevd(ruta_archivo)
            # print(ruta_abrevd)
            self.lbl_archivo.config(text=ruta_abrevd+'//'+nombre_archivo)
            self.informarApp('Load File', 'OK ;)')
            
        else:
            messagebox.showinfo(title="Load File:", message=f"No se ha cargado ningún archivo ")
            self.informarApp('Load File', 'Failed :(')
            # Salir y no hacer nada
    # ____________________
    # C H E C K   B U T T O N   Del Fichero al ListBox 
    def chkbttn_click(self):
        if self.chkBttnServer_valor.get() == 1:  # Si el Checkbutton está marcado
            # messagebox.showinfo(title="Empezamos!!:", message=f"Bienvenido a Babel :)")
            # print(f"Bienvenido a Babel :)")      
            self.informarApp("Bienvenido a Babel :)", "Empezamos!!")

            if self.archivo:
                try:
                    self.quitar_duplicados_json(archivo=self.archivo)
                except Exception as e:
                    print(e); pass
                self.from_archivo_to_biblioteca()
                self.from_archivo_to_lbx_babel()                    
            else:
                self.lbl_archivo.config(text='-')
                self.informarApp('Archivo no existe', 'Load File')
                pass

        elif self.chkBttnServer_valor.get() == 0:
            try:
                self.quitar_duplicados_json(archivo=self.archivo)
            except:
                pass
            # print(f'Salimos de Babel :(')
            self.informarApp("Salimos de Babel :(", "Chaoo!!")
            self.vaciar_listbox()
            self.vaciar_textbox()
            os.system('cls')
            print('Has salido de  B A B E L,  Biblioteca Central..... Tuyo es el camino')
    # ___________________
    # S E L E C T  EN  L I S T B O X  Del ListBox a los Text del Formulario 
    def lbx_on_select(self, event):
        seleccion = event.widget.curselection() 
        if seleccion:
            indice = seleccion[0]            
            """ >>> Obtener el primer índice seleccionado
            """
            valor_lstbx = event.widget.get(indice)  
            """ >>> Obtener el valor del índice de un ListBox
            """
            
            # print(f"Elemento seleccionado: {valor} (Índice {indice})")
            self.informarApp(txt_info=valor_lstbx, txt_subinfo=f'{indice} de {len(self.biblioteca.libros_biblioteca)}')
            listaValor=str(valor_lstbx).split('-')
            listaValor=[str(item).strip().title() for item in listaValor]

            self.vaciar_textbox()
            self.llenar_txtbx_from_lbx(listaValor)
            
            # _________________________
            # GUARDO UNA COPIA del libro SELECT para el  UPDATE ;)
            self.libro_select_lstbx = self.crea_libro_from_txtbox()            

        else:
            print("Ningún elemento seleccionado.")
    
    # **************************************************************************************************************
    #    A C C I O N E S    C O M U N E S  (NO DIRECTAS)
    # **************************************************************************************************************    
    
    # ================================================================================= TEXTBOX    
    # ____________________
    # V A L I D A C I O N  T E X T O S  V A C I O S
    def validar_texto(self):
        """ 
        >>> Def: Valida que haya contenido en los 3 textBox o saca un msgBox de alerta."""
        # for txtBox in txtEntry:
        for txtBox in self.family_txtbx:
            valor_txtEntry = txtBox.get()
            if valor_txtEntry.strip() == '':
                txtBox.focus()
                return False
        return True    
    # ____________________
    # CARGA LOS TEXTBOX CON LA LISTA PASADA DE LISTBOX.............Llamada desde self.lbx_on_select()
    def llenar_txtbx_from_lbx(self, lst_fila_lbx):
        for i,txtbx in enumerate(self.family_txtbx):
            txtbx.insert(0, string=str(lst_fila_lbx[i]).strip())
    # ____________________
    # PONE   sP   EN  T E X T B O X
    def vaciar_textbox(self):
        """ >>> Def: Vacia el listbox por completo
        """
        for textbox in self.family_txtbx:
            textbox.delete(0, tk.END)
    # ____________________
    # SEMAFORO DE BOTONES: 'normal' - 'disabled'
    def semaforo_botones(self, index=SMFR):
        """ 
        Def: actua sobre los botones. Crea un semaforo de accion. 
        [boton]= objeto boton. Si no se pasa como argumento opera sobre todos los botones poniendolos a normal
        Si se pasa como argumento un boton, este lo pone normal y el resto los pone disabled."""
        for boton in self.family_bttn_crud:
            boton.config(state='disabled')

        self.family_bttn_crud[index].config(state='normal')
    # ____________________
    # NO USADO
    def get_bttn_normal(self):
        for boton in self.family_bttn_crud:
            estado = boton.cget('state')  # Obtener el estado actual del botón
            if estado == 'normal':
                return boton
    # ================================================================================= LISTBOX    
    # ____________________
    # LIMPIA EL   L I S T B O X 
    def vaciar_listbox(self):
        """ >>> Def: Vacia el listbox por completo
        """
        self.lbx_babel.delete(0, tk.END)
    # ================================================================================= FICHEROS
    # ____________________
    # F I L E D I A L O G . Retorna self.archivo
    def selectFile(self):
        """ 
        Def: Selecciona un Archivo con fileDialog y devuelve el resultado.
        """
        # Obtiene el directorio del archivo de Python actual
        carpeta_inicial = os.path.dirname(os.path.abspath(__file__))
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo", 
                                            initialdir=carpeta_inicial ,
                                            filetypes=[ ("Archivos JSON", "*.json"), 
                                                        ("Archivos CSV", "*.csv"), 
                                                        ("Archivos de texto", "*.txt")])
        
        return archivo if archivo else None
    # ____________________
    # L E E  F I C H E R O    AL INICIAR SOLAMENTE.(NO USADA)
    def lectura_inicial(self, archivo_json=''):
        """ 
        Def: si existe el archivo lo lee y devuelve en formato json
        """
        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as archivo:
                datos = json.load(archivo)
        else:
            datos = []  # Crear una lista nueva si el archivo no existe
        return datos
    # ____________________
    # f r o m   A R C H I V O  (self.archivo)   t o    L I S T B O X
    def from_archivo_to_lbx_babel(self):
        if not self.archivo: return None
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        with open(self.archivo, 'r') as file:
            data = file.read()  
            if data.strip():        # Valida que no esté vacío
                try:
                    json_data = json.loads(data)
                    """ >>> Devuelve una lista de diccionario libro """
                    print('J S O N   L E I D O :')
                    # print(json_data)

                    # Extraer los datos del JSON 
                    for libro_json in json_data:                        

                        self.lbx_babel.insert(tk.END, f"{libro_json['titulo']} - {libro_json['autor']} - {libro_json['numpag']}" )
                    
                    self.informarApp("Carga de Biblioteca Realizada", ";)")

                except json.JSONDecodeError as e:
                    self.informarApp('Error al decodificar JSON', e)
                    # print("Error al decodificar JSON:", e)
            else:
                self.informarApp('El archivo está vacío' , ':(')
    # f r o m   A R C H I V O  (self.archivo)   t o    self.libros_biblioteca ( L I S T )
    def from_archivo_to_biblioteca(self):
        if not self.archivo: return None
        with open(self.archivo, 'r') as file:
            data = file.read()  
            if data.strip():        # Valida que no esté vacío
                try:
                    json_data = json.loads(data)
                    """ >>> Devuelve en una lista los datos del archivo en una estructura definida en el archivo json (el que tenga) """
                    print('J S O N   C A R G A D O :')

                    for libro_json in json_data:                        
                        self.biblioteca.agregar_libro(Libro(titulo=libro_json['titulo'], autor=libro_json['autor'], numpag=libro_json['numpag']))

                    self.informarApp("Carga de Biblioteca Realizada", ";)")
                except json.JSONDecodeError as e:
                    self.informarApp('Error al decodificar JSON', e)
            else:
                self.informarApp('El archivo está vacío' , ':(')
    # ____________________
    # B U S C A    UN VALOR EN UN ARCHIVO JSON. EN UN DICCIONARIO JSON
    def buscar_en_json(archivo_json, clave, valor_buscado):
        # Cargar el JSON en una lista de diccionarios
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)

        # Recorrer la lista y buscar el valor
        resultados = []
        for elemento in datos:
            if clave in elemento:
                if elemento[clave] == valor_buscado:
                    resultados.append(elemento)

        # Mostrar resultados
        if resultados:
            # print(f"Encontrado(s) {len(resultados)} resultado(s):")
            for resultado in resultados:
                # Me lo muestra en una cadena rapidamente                
                print(json.dumps(resultado, indent=4))
        # else:
            # print("No se encontraron coincidencias.")
    # ================================================================================= OTROS/AS
    # ____________________
    # A B R E V I A   LA RUTA       Para ver en  self.lbl_archivo
    def ruta_abrevd(ruta, numpartes=2):
        """ >>> Def: Divide la ruta en partes new_ruta=self.ruta_abrevd(ruta)"""
        partes = str(ruta).split('/')

        # Toma solo las dos últimas carpetas y añade '...'
        if len(partes) > numpartes:            
            return os.path.join("...", partes[-2], partes[-1])
        else:
            # Si hay menos de dos carpetas, muestra la ruta tal cual
            return ruta
    # ____________________
    # M E N S A J E S   DE LA APP
    def informarApp(self, txt_info='', txt_subinfo=''):
        self.lbl_info.config(text=txt_info)
        self.lbl_subinfo.config(text=txt_subinfo)

        if self.memo_inf.last_msg == self.lbl_info.cget("text"):
            self.memo_inf.last_index += 1
            self.lbl_subinfo.config(text=self.memo_inf.last_index)
        else:
            self.memo_inf.last_index = 0        
        
        self.memo_inf.last_msg=self.lbl_info.cget("text")

    # _______________________
    # CREA UNA INSTANCIA DE LIBRO A PARTIR DE LOS TEXTBOX
    def crea_libro_from_txtbox(self):
        """ >>> Crear un libro desde los textbox python es la pera limonera!!!  """        
        data_libro=[str(txtbx.get()).strip() for txtbx in self.family_txtbx]
        libro=Libro(*data_libro)
        return libro
    # _______________________
    # ELIMINA LOS DUPLICADOS DEL ARCHIVO JSON
    def quitar_duplicados_json(self, archivo):
        # abrir el archivo json para leer.(with open)
        # Recuperar los datos en un json_data_list (load)
        with open(archivo, 'r') as file:
            data = file.read()  
            if data.strip():        # Valida que no esté vacío
                try:
                    json_data_list = json.loads(data)                    
                except json.JSONDecodeError as e:
                    self.informarApp('Error al decodificar JSON', e)
                
        # Usar la lista para crear una lista sin duplicados
        retorno = [frozenset(dicc.items()) for dicc in json_data_list]                                                
        # print(retorno)
        retorno_sin_duplicados = set(retorno)
        retorno_sin_duplicados = [dict(item) for item in retorno_sin_duplicados]
        # print(retorno_sin_duplicados)

        try:
            with open(archivo, "w") as archivo:
                json.dump(retorno_sin_duplicados, archivo, indent=4)
        except Exception as e:
            print(e)
            return None
        else:       
            return retorno
        # Retornar true