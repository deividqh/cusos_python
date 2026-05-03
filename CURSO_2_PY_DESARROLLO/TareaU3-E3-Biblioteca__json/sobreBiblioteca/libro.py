from enum import Enum as ENUM
class registros(ENUM):
    TIT='titulo'
    AUT='autor'
    PAG='numpag'

class Libro():
    def __init__(self, titulo, autor, numpag):
        self.titulo = titulo
        self.autor = autor
        try:
            self.numpag = int(numpag)
        except Exception as e:
            print(e)
            return None

    def __str__(self):
        return f'{str(self.titulo).title()}\n\tAutor: {str(self.autor).title()}\n\tNum-Pag: {self.numpag}'
    
    def to_dicc_json(self, un_libro):
        """ >>> Def: Recibe un libro y lo convierte en un diccionario.... para formato j_son        """
        try:
            return {
                registros.TIT.value: un_libro.titulo,
                registros.AUT.value: un_libro.autor,
                registros.PAG.value: un_libro.numpag
            }
        except Exception as e:
            print(e)
            return None
