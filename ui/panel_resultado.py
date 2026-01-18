# ui/panel_resultado.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PanelResultado(ttk.Labelframe):
    def __init__(self, parent, app, carton):
        super().__init__(parent, text="Resultado de la ronda", padding=10)

        self.app = app
        self.carton = carton

        ttk.Label(
            self,
            text=f"🎉 BINGO – Cartón {carton.id}",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        # -------- GRID DE PALABRAS DEL CARTÓN --------
        grid = ttk.Frame(self)
        grid.pack(pady=10)

        palabras = carton.palabras_originales
        marcadas = carton.marcadas

        cols = 4
        for i, palabra in enumerate(palabras):
            fila = i // cols
            col = i % cols

            estilo = SUCCESS if palabra.lower() in marcadas else SECONDARY

            ttk.Label(
                grid,
                text=palabra,
                bootstyle=estilo,
                padding=5
            ).grid(row=fila, column=col, padx=5, pady=5)