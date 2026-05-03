
class Biblioteca():
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """ 
        Def: Agrega un libro a la lista self.libros
        [libro]: objeto libro
        >>> if biblio.agregar_libro(libro_quijote):
               pass
        """        
        libroBuscado=self.buscar_libro(libro.titulo)
        
        if not libroBuscado:
            self.libros.append(libro)
            return True
        else:
            return False

    def buscar_libro(self, titulo):
        """
        Def: Busca un libro por el título que le entra 
        [titulo]: str, el nombre del libro a buscar.
        Retorno: objeto Libro encontrado o None si no lo encuentra.
        >>> libro_quijote=biblio.buscar_libro("Don Quijote de la Mancha")
        """
        for libro in self.libros:
            if str(libro.titulo).lower() == str(titulo).lower():
                return libro
        return None  

    def total_paginas(self):
        """ 
        Def: Retorna el total de paginas de todos los libros de la biblioteca.
        llamada desde Imprime All
        """
        paginas = 0
        for libro in self.libros:
            paginas += int(libro.num_paginas)
        return paginas

    def imprime_All(self):
        """
        >>> Def: Imprime todos los libros. Ejemplo: bibilio.imprime_All()
        """
        print(f'\n{'='*20}\nBiblioteca\n{'='*20}')
        for libro in self.libros:
            print(libro)
        
        print(f'\n{'~'*20}\nTotal Paginas: {self.total_paginas()}')
        print(f'\n{'='*20}\nFin Biblioteca\n{'='*20}')
