# ui/estado.py

class EstadoApp:
    def __init__(self):
        self.reset()

    def reset(self):
        self.idioma = None
        self.n_palabras = 0
        self.cartones = []
        self.ronda = None
