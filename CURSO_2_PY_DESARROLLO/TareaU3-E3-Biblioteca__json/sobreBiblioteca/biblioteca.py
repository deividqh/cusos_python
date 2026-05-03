from .libro import Libro
import json

class Biblioteca():
    def __init__(self):
        self.libros_biblioteca = []
        
    # _______________________
    # ADD 
    def agregar_libro(self, new_libro):
        """ 
        Def: Agrega un libro a la lista self.libros
        [new_libro]: objeto libro
        >>> if biblio.agregar_libro(libro_quijote): pass        """  
        if self.get_index_libro(libroBusca=new_libro)==None:
            self.libros_biblioteca.append(new_libro)
            return True
        else:
            return False

    # _______________________
    # UPDT    
    def updt_libro(self, libro):
        """         """
    # _______________________
    # DEL    
    def del_libro(self, libroDel):
        """ Def: Borra un libro, de la lista de libros, que se pasa como argumento         """
        index=self.get_index_libro(libroBusca=libroDel)
        if index:
            # return self.libros_biblioteca.pop(libroDel)
            return self.libros_biblioteca.pop(index)
    
    def get_index(self, libro):

        pass
    # _______________________
    # SEARCH
    def get_index_libro(self, libroBusca):
        """
        Def: Busca un libro por el título que le entra o por el libro que le entra.
        [libroBusca]: str, el nombre del libro a buscar 
        Instancia de libro. Esto vale para cuando se quiere crear un libro nuevo y se introduce una instancia.
        Retorno: objeto Libro encontrado o None si no lo encuentra.
        >>> libro_quijote=biblio.get_index_libro("Don Quijote de la Mancha")
        >>> libro_quijote=biblio.get_index_libro( Libro('La Nausea', 'Sartre', 200) )
        """
        if isinstance(libroBusca, str):
            for index, libro_biblioteca in enumerate(self.libros_biblioteca):
                if str(libro_biblioteca.titulo).strip().lower() == str(libroBusca).strip().lower():
                    return index
        elif isinstance(libroBusca, Libro):
            for index, libro_biblioteca in enumerate(self.libros_biblioteca):
                
                titulo_babel=str(libro_biblioteca.titulo).strip().lower()
                autor_babel=str(libro_biblioteca.autor).strip().lower()

                titulo_busca=str(libroBusca.titulo).strip().lower()
                autor_busca=str(libroBusca.autor).strip().lower()

                # Hacen Match? 
                if titulo_babel==titulo_busca and autor_babel==autor_busca:
                    return index
        return None

    def total_paginas(self):
        """ 
        Def: Retorna el total de paginas de todos los libros de la biblioteca.
        llamada desde Imprime All
        """
        paginas = 0
        for libro in self.libros_biblioteca:
            try:
                paginas += int(libro.numpag)
            except:
                continue
        return paginas

    def imprime_All(self):
        """
        >>> Def: Imprime todos los libros. Ejemplo: bibilio.imprime_All()
        """
        print(f'\n{'='*20}\nBiblioteca\n{'='*20}')
        for libro in self.libros_biblioteca:
            print(libro)
                
        print(f'\n\n{'='*20}\nFin Biblioteca\n{'='*20}')

    # _______________________
    # ARCHIVO-JSON to BIBLIOTECA No la uso, pero la dejo.
    def a_json_to_biblioteca(self, nombre_archivo):
        """ >>> Lee el archivo json y agrega libros a  la biblioteca. """
        if nombre_archivo:
            with open(file=nombre_archivo, mode="r") as archivo:
                datos_json = json.load(archivo)
            
            # print(datos_json)
            # ________________________
            # Pongo a cero los libros para cargar la lista de libros de la biblioteca.
            self.libros_biblioteca=[]

            for item in datos_json:
                libro = Libro(titulo=item['titulo'], autor=item['autor'], numpag=item['numpag'])
                # self.agregar_libro(libro)
                if self.get_index_libro(libroBusca=new_libro)==None:
                    self.libros_biblioteca.append(new_libro)

    # _______________________
    # LISTA BIBLIOTECA to ARCHIVO-JSON 
    def from_biblioteca_to_json(self, ruta_archivo=None):
        """ >>> Def: Convierte los atributos del objeto en un diccionario 
        [ruta_archivo]: El path del archivo json sobre el que escribir.
        """
        try:
            # Convierto en formato json para escribir en el archivo.
            retorno=[ libro.to_dicc_json(libro) for libro in self.libros_biblioteca ]
        except Exception as e:
            print(e)
            return None
        else:
            try:
                with open(ruta_archivo, "w") as archivo:
                    json.dump(retorno, archivo, indent=4)
            except Exception as e:
                print(e)
                return None
            else:       
                return retorno





