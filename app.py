# ui/app.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ui.estado import EstadoApp
from ui.panel_carga import PanelCarga
from ui.panel_ronda import PanelRonda
from core.datos_prueba import PALABRAS_POR_IDIOMA


class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Bingo_P – Asistente del Concursante",
            themename="flatly"
        )

        self.geometry("1100x650")
        self.resizable(False, False)

        # ================= ESTADO =================
        self.estado = EstadoApp()

        # ================= CONTENEDOR GENERAL =================
        self.container = ttk.Frame(self)
        self.container.pack(fill=BOTH, expand=True)

        # ================= TÍTULO =================
        titulo_frame = ttk.Frame(self.container)
        titulo_frame.pack(side=TOP, fill=X, pady=5)

        self.titulo = ttk.Label(
            titulo_frame,
            font=("Arial", 20, "bold")
        )
        self.titulo.pack(side=LEFT, padx=10)

        ttk.Button(
            titulo_frame,
            text="⏭ Siguiente ronda",
            bootstyle=SUCCESS,
            command=self.iniciar_ronda
        ).pack(side=RIGHT, padx=10)


        # ================= ZONA DINÁMICA (ARRIBA) =================
        self.frame_principal = ttk.Frame(self.container, padding=10)
        self.frame_principal.pack(side=TOP, fill=BOTH, expand=True)

        # ================= LOG FIJO (ABAJO) =================
        self.frame_log = ttk.Labelframe(
            self.container,
            text="Log del sistema",
            padding=5
        )
        self.frame_log.pack(side=BOTTOM, fill=X)

        self.log_text = ttk.Text(
            self.frame_log,
            height=6,
            state="disabled",
            wrap="word"
        )
        self.log_text.pack(fill=X)

        # ================= INICIO =================
        self.iniciar_ronda()

    # ================= LOG =================
    def log(self, mensaje):
        self.log_text.configure(state="normal")
        self.log_text.insert(END, mensaje + "\n")
        self.log_text.see(END)
        self.log_text.configure(state="disabled")

    # ================= LIMPIAR ZONA DINÁMICA =================
    def limpiar_principal(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    # ================= NUEVA RONDA =================
    def iniciar_ronda(self):
        # Ocultar panel de resultado si existe
        if hasattr(self, "panel_resultado"):
            self.panel_resultado.pack_forget()
            del self.panel_resultado

        # Limpiar UI dinámica
        self.limpiar_principal()

        # Reiniciar estado de la ronda (no la cola de idiomas)
        self.estado.cartones = []
        self.estado.ronda = None
        self.estado.ganadores = []

        # Selección automática de idioma
        idioma = self.estado.siguiente_idioma()
        self.estado.idioma = idioma
        self.estado.n_palabras = PALABRAS_POR_IDIOMA[idioma]

        # Título
        self.titulo.config(text=f"Ronda – Idioma: {idioma}")

        # Log de estado
        self.log("────────────────────────────────")
        self.log("🔁 Nueva ronda iniciada")
        self.log(f"✔ Idioma seleccionado automáticamente: {idioma}")
        self.log(f"✔ Palabras por cartón: {self.estado.n_palabras}")

        # Panel de carga
        self.panel_carga = PanelCarga(self.frame_principal, self)
        self.panel_carga.pack(fill=X, pady=10)

        # Panel de ronda (oculto hasta que se carguen cartones)
        self.panel_ronda = PanelRonda(self.frame_principal, self)
        self.panel_ronda.disable()


if __name__ == "__main__":
    App().mainloop()
