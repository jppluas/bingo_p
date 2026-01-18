# ui/panel_resultado.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PanelResultado(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=True)

        self.app = app

    def mostrar(self):
        for w in self.winfo_children():
            w.destroy()

        carton = self.app.ganadores[0]

        ttk.Label(
            self,
            text=f"🎉 BINGO – Cartón {carton.id}",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        grid = ttk.Frame(self)
        grid.pack()

        cols = 4
        for i, palabra in enumerate(carton.palabras_originales):
            r = i // cols
            c = i % cols

            color = "success" if palabra.lower() in carton.marcadas else "secondary"

            ttk.Label(
                grid,
                text=palabra,
                bootstyle=color,
                padding=5
            ).grid(row=r, column=c, padx=5, pady=5)
