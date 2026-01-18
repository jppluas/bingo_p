# ui/panel_idioma.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from core.datos_prueba import PALABRAS_POR_IDIOMA
from ui.panel_carga import PanelCarga


class PanelIdioma(ttk.Labelframe):
    def __init__(self, parent, app):
        super().__init__(parent, text="1. Selección de idioma", padding=10)
        self.app = app

        idiomas = [
            ("Español", "SP"),
            ("English", "EN"),
            ("Portuguese", "PT"),
            ("Dutch", "DT")
        ]

        for texto, codigo in idiomas:
            ttk.Button(
                self,
                text=texto,
                width=15,
                command=lambda c=codigo: self.seleccionar(c)
            ).pack(side=LEFT, padx=5)

    def seleccionar(self, idioma):
        if self.app.estado.idioma is not None:
            confirmar = messagebox.askyesno(
                "Cambiar idioma",
                "Cambiar el idioma reiniciará la partida.\n¿Desea continuar?"
            )
            if not confirmar:
                return

            self.app.limpiar_principal()
            self.app.reiniciar_estado()

            self.app.panel_idioma = PanelIdioma(self.app.frame_principal, self.app)
            self.app.panel_idioma.pack(fill=X, pady=10)

            self.app.panel_carga = PanelCarga(self.app.frame_principal, self.app)
            self.app.panel_carga.pack(fill=X, pady=10)
            self.app.panel_carga.disable()

        self.app.estado.idioma = idioma
        self.app.estado.n_palabras = PALABRAS_POR_IDIOMA[idioma]

        self.app.log(f"✔ Idioma seleccionado: {idioma}")
        self.app.log(f"✔ Palabras por cartón: {self.app.estado.n_palabras}")

        self.app.panel_carga.enable()
