import tkinter as tk
from tkinter import ttk


class PestanasUpDown(ttk.Frame):
    """Notebook que habilita pestañas de forma secuencial.

    Cada pestaña contiene únicamente un Checkbutton. Al marcarlo se habilita y
    se muestra la pestaña siguiente. Al desmarcarlo se bloquean todas las
    pestañas posteriores.
    """

    def __init__(self, contenedor, titulos_pestanas):
        super().__init__(contenedor)

        if not titulos_pestanas:
            raise ValueError("Debe indicarse al menos un título de pestaña.")

        self.titulos_pestanas = list(titulos_pestanas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.pestanas = []
        self.valores = []
        self.checkbuttons = []

        self._crear_pestanas()
        self._bloquear_pestanas_desde(1)

    def _crear_pestanas(self):
        for indice, titulo in enumerate(self.titulos_pestanas):
            pestana = ttk.Frame(self.notebook)
            valor = tk.BooleanVar(value=False)

            checkbutton = ttk.Checkbutton(
                pestana,
                text="Permitir avanzar a la siguiente pestaña",
                variable=valor,
                command=lambda indice=indice: self._actualizar_pestanas(indice),
            )
            checkbutton.grid(row=0, column=0, sticky="w", padx=10, pady=10)

            self.notebook.add(pestana, text=titulo)
            self.pestanas.append(pestana)
            self.valores.append(valor)
            self.checkbuttons.append(checkbutton)

    def _actualizar_pestanas(self, indice):
        if self.valores[indice].get():
            self._habilitar_siguiente_pestana(indice)
        else:
            self._bloquear_pestanas_desde(indice + 1)

    def _habilitar_siguiente_pestana(self, indice):
        siguiente_indice = indice + 1

        if siguiente_indice >= len(self.pestanas):
            return

        siguiente_pestana = self.pestanas[siguiente_indice]
        self.notebook.tab(siguiente_pestana, state="normal")
        self.notebook.select(siguiente_pestana)

    def _bloquear_pestanas_desde(self, indice_inicial):
        for indice in range(indice_inicial, len(self.pestanas)):
            self.valores[indice].set(False)
            self.notebook.tab(self.pestanas[indice], state="disabled")


def main():
    ventana = tk.Tk()
    ventana.title("Pestañas con avance por booleano")
    ventana.geometry("450x300")

    titulos = ["Datos", "Split", "Algoritmo/Modelo", "Metricas"]
    pestanas = PestanasUpDown(ventana, titulos)
    pestanas.pack(fill="both", expand=True, padx=10, pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
