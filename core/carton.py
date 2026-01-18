# core/carton.py

from core.normalizador import normalizar

class Carton:
    def __init__(self, identificador, palabras):
        self.id = identificador
        self.idioma = identificador[:2]

        # 🔴 Normalizamos TODAS las palabras al cargar el cartón
        self.palabras = set(normalizar(p) for p in palabras)

        self.marcadas = set()
        self.pendientes = len(self.palabras)

    def marcar_palabra(self, palabra):
        palabra = normalizar(palabra)  # 🔴 normalizamos entrada

        if palabra in self.palabras and palabra not in self.marcadas:
            self.marcadas.add(palabra)
            self.pendientes -= 1

    def es_ganador(self):
        return self.pendientes == 0
