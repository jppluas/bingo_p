# ui/panel_carga.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox

from core.lector_txt import cargar_cartones_lote
from core.carton import Carton


class PanelCarga(ttk.Labelframe):
    def __init__(self, parent, app):
        super().__init__(parent, text="2. Carga de cartones", padding=10)
        self.app = app
        self.entries = []

        self.frame_modos = ttk.Frame(self)
        self.frame_modos.pack(fill=X, pady=5)

        ttk.Button(self.frame_modos, text="Archivo TXT", command=self.cargar_archivo).pack(side=LEFT, padx=5)
        ttk.Button(self.frame_modos, text="Ingreso manual", command=self.modo_manual).pack(side=LEFT, padx=5)

        self.frame_dinamico = ttk.Frame(self)
        self.frame_dinamico.pack(fill=X, pady=10)

    def disable(self):
        for w in self.frame_modos.winfo_children():
            w.state(["disabled"])
        self.limpiar_dinamico()

    def enable(self):
        for w in self.frame_modos.winfo_children():
            w.state(["!disabled"])

    def limpiar_dinamico(self):
        for w in self.frame_dinamico.winfo_children():
            w.destroy()
        self.entries.clear()

    def cargar_archivo(self):
        self.limpiar_dinamico()

        ruta = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if not ruta:
            return

        cartones, errores = cargar_cartones_lote(ruta, self.app.estado.idioma)

        self.app.log(f"✔ Archivo seleccionado: {ruta}")
        self.app.log(f"✔ Tablas procesadas: {len(cartones) + len(errores)}")
        self.app.log(f"✔ Tablas válidas: {len(cartones)}")

        if errores:
            self.app.log(f"⚠ Tablas inválidas: {len(errores)}")
            for e in errores:
                self.app.log(f"  - {e}")

        if not cartones:
            messagebox.showerror("Error", "No hay cartones válidos.")
            return

        self.app.estado.cartones = cartones
        messagebox.showinfo("Carga exitosa", "Cartones listos para la ronda")
        
        # Ocultar carga y mostrar ronda
        self.pack_forget()
        self.app.panel_ronda.enable()


    def modo_manual(self):
        self.limpiar_dinamico()
        n = self.app.estado.n_palabras

        grid = ttk.Frame(self.frame_dinamico)
        grid.pack()

        for i in range(n):
            e = ttk.Entry(grid, width=18)
            e.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            self.entries.append(e)

        ttk.Button(self.frame_dinamico, text="Cargar cartón", bootstyle=SUCCESS,
                   command=self.cargar_manual).pack(pady=10)

    def cargar_manual(self):
        palabras = [e.get().strip() for e in self.entries]
        if any(not p for p in palabras):
            messagebox.showwarning("Error", "Debe completar todas las palabras.")
            return

        self.app.estado.cartones = [
            Carton(f"{self.app.estado.idioma}000001", palabras)
        ]

        self.app.log("✔ Ingreso manual completado")
        self.app.log(f"✔ Palabras procesadas: {len(palabras)} / {len(palabras)}")

        messagebox.showinfo("Carga exitosa", "Cartón listo para la ronda")

        # Ocultar carga y mostrar ronda
        self.pack_forget()
        self.app.panel_ronda.enable()

