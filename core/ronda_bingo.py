# core/ronda_bingo.py
from core.normalizador import normalizar

class RondaBingo:
    def __init__(self, idioma, cartones, vocabulario):
        self.idioma = idioma
        self.vocabulario = set(normalizar(p) for p in vocabulario)

        # Divide y vencerás:
        # Solo cartones del idioma de la ronda
        self.cartones = [
            carton for carton in cartones
            if carton.idioma == idioma
        ]

        self.ganadores = []

    def anunciar_palabra(self, palabra):
        """
        Turno del juego (estrategia voraz)
        """
        if palabra not in self.vocabulario:
            return []  # palabra inválida para este idioma

        for carton in self.cartones:
            carton.marcar_palabra(palabra)

            if carton.es_ganador():
                self.ganadores.append(carton)

        return self.ganadores
