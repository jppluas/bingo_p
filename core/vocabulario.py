# core/vocabulario.py

from core.normalizador import normalizar

def cargar_vocabulario(ruta_archivo):
    palabras = []

    with open(ruta_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            palabra = linea.strip()
            if palabra:
                palabras.append(normalizar(palabra))

    return palabras
