class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        return f'{str(self.titulo).title()}\n\tAutor: {str(self.autor).title()}\n\tNum-Pag: {self.num_paginas}'
