# ui/app.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ui.estado import EstadoApp
from ui.panel_idioma import PanelIdioma
from ui.panel_carga import PanelCarga
from ui.panel_ronda import PanelRonda



class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Bingo_P – Asistente del Concursante",
            themename="flatly"
        )

        self.geometry("1000x650")
        self.resizable(False, False)

        self.estado = EstadoApp()

        # -------- ZONA SCROLLEABLE --------
        self.canvas = ttk.Canvas(self)
        self.canvas.pack(side=TOP, fill=BOTH, expand=True)

        self.scroll_y = ttk.Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.frame_principal = ttk.Frame(self.canvas, padding=10)
        self.canvas.create_window((0, 0), window=self.frame_principal, anchor="nw")

        self.frame_principal.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # -------- LOG FIJO --------
        self.frame_log = ttk.Labelframe(self, text="Log del sistema", padding=5)
        self.frame_log.pack(side=BOTTOM, fill=X)

        self.log_text = ttk.Text(self.frame_log, height=6, state="disabled", wrap="word")
        self.log_text.pack(fill=X)

        # -------- PANELES --------
        self.panel_idioma = PanelIdioma(self.frame_principal, self)
        self.panel_idioma.pack(fill=X, pady=10)

        self.panel_carga = PanelCarga(self.frame_principal, self)
        self.panel_carga.pack(fill=X, pady=10)
        self.panel_carga.disable()

        self.panel_ronda = PanelRonda(self.frame_principal, self)
        self.panel_ronda.disable()


        self.log("Aplicación iniciada. Seleccione un idioma.")

    def log(self, mensaje):
        self.log_text.configure(state="normal")
        self.log_text.insert(END, mensaje + "\n")
        self.log_text.see(END)
        self.log_text.configure(state="disabled")

    def limpiar_principal(self):
        for w in self.frame_principal.winfo_children():
            w.destroy()

    def reiniciar_estado(self):
        self.estado.reset()
        self.log("Estado reiniciado.")


if __name__ == "__main__":
    App().mainloop()
