# core/normalizador.py

import unicodedata

def normalizar(palabra):
    """
    Convierte a minúsculas y elimina tildes.
    """
    palabra = palabra.lower()
    palabra = unicodedata.normalize("NFD", palabra)
    palabra = "".join(
        c for c in palabra if unicodedata.category(c) != "Mn"
    )
    return palabra
