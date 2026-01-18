# ui/panel_ronda.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import os

from core.ronda_bingo import RondaBingo
from core.datos_prueba import PALABRAS_GANADORAS
from core.vocabulario import cargar_vocabulario
from core.normalizador import normalizar


class PanelRonda(ttk.Labelframe):
    def __init__(self, parent, app):
        super().__init__(parent, text="3. Ronda", padding=10)

        self.app = app
        self.ronda = None
        self.vocabulario = []

        # ---------- INPUT ----------
        input_frame = ttk.Frame(self)
        input_frame.pack(fill=X, pady=5)

        self.entry = ttk.Entry(input_frame)
        self.entry.pack(side=LEFT, fill=X, expand=True, padx=5)

        self.btn = ttk.Button(
            input_frame,
            text="Anunciar",
            bootstyle=PRIMARY,
            command=self.anunciar
        )
        self.btn.pack(side=LEFT, padx=5)

        self.entry.bind("<Return>", lambda e: self.anunciar())

        # ---------- LISTA SUGERENCIAS ----------
        self.lista = tk.Listbox(self, height=6)
        self.lista.pack(fill=X, pady=5)

        self.lista.bind("<<ListboxSelect>>", self.autocompletar)
        self.entry.bind("<KeyRelease>", self.actualizar_sugerencias)

    # ---------- ACTIVAR PANEL ----------
    def enable(self):
        self.pack(fill=X, pady=10)

        # Crear ronda
        self.ronda = RondaBingo(
            self.app.estado.idioma,
            self.app.estado.cartones
        )


        # Cargar vocabulario REAL del idioma
        ruta_vocab = os.path.join(
            "data",
            "vocabularios",
            f"{self.app.estado.idioma.lower()}.txt"
        )

        self.vocabulario = cargar_vocabulario(ruta_vocab)

        self.entry.focus()
        self.app.log("✔ Ronda iniciada")
        self.app.log("✔ Vocabulario cargado para sugerencias")

    def disable(self):
        self.pack_forget()

    # ---------- AUTOCOMPLETADO ----------
    def actualizar_sugerencias(self, event=None):
        texto = normalizar(self.entry.get())
        self.lista.delete(0, END)

        if not texto:
            return

        for palabra in self.vocabulario:
            if palabra.startswith(texto):
                self.lista.insert(END, palabra)

    def autocompletar(self, event):
        if not self.lista.curselection():
            return

        palabra = self.lista.get(self.lista.curselection()[0])
        self.entry.delete(0, END)
        self.entry.insert(0, palabra)
        self.lista.delete(0, END)

    # ---------- ANUNCIAR ----------
    def anunciar(self):
        palabra = self.entry.get().strip()
        if not palabra:
            return

        self.entry.delete(0, END)
        self.lista.delete(0, END)

        self.app.log(f"▶ Palabra anunciada: {palabra}")

        ganadores = self.ronda.anunciar_palabra(palabra)

        if ganadores:
            self.app.log("🎉 BINGO DETECTADO")

            # Ocultar panel de ronda
            self.pack_forget()

            from ui.panel_resultado import PanelResultado
            ganador = ganadores[0]

            self.app.panel_resultado = PanelResultado(
                self.master,
                self.app,
                ganador
            )
            self.app.panel_resultado.pack(fill=X, pady=10)



