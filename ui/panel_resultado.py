# ui/panel_resultado.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PanelResultado(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

    def mostrar(self):
        self.pack(fill=BOTH, expand=True)

        ttk.Label(
            self,
            text="🎉 BINGO 🎉",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ttk.Button(
            self,
            text="Otra ronda",
            bootstyle=SUCCESS,
            command=self.app.iniciar_ronda   # ✅ ahora sí existe
        ).pack(pady=10)
