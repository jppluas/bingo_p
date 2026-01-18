# ui/estado.py

import random

IDIOMAS = ["SP", "EN", "DT", "PT"]

class EstadoApp:
    def __init__(self):
        self.cola_idiomas = []
        self.reset()

    def reset(self):
        self.idioma = None
        self.n_palabras = 0
        self.cartones = []
        self.ronda = None
        self.ganadores = []

    def siguiente_idioma(self):
        if not self.cola_idiomas:
            self.cola_idiomas = IDIOMAS.copy()
            random.shuffle(self.cola_idiomas)

        idioma = self.cola_idiomas.pop(0)

        # evitar repetir idioma
        if idioma == self.idioma and self.cola_idiomas:
            self.cola_idiomas.append(idioma)
            idioma = self.cola_idiomas.pop(0)

        self.idioma = idioma
        return idioma
