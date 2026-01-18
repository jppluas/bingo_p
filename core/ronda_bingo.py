# core/ronda_bingo.py

from core.normalizador import normalizar


class RondaBingo:
    def __init__(self, idioma, cartones):
        self.idioma = idioma
        self.cartones = cartones
        self.anunciadas = set()

    def anunciar_palabra(self, palabra):
        palabra_norm = normalizar(palabra)
        self.anunciadas.add(palabra_norm)

        ganadores = []

        for carton in self.cartones:
            carton.marcar_palabra(palabra_norm)
            if carton.es_ganador():
                ganadores.append(carton)

        return ganadores
