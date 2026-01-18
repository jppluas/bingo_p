# core/lector_txt.py

from core.carton import Carton
from core.datos_prueba import PALABRAS_POR_IDIOMA


def cargar_cartones_lote(ruta, idioma):
    n = PALABRAS_POR_IDIOMA[idioma]
    cartones = []
    errores = []

    try:
        with open(ruta, encoding="utf-8") as archivo:
            for idx, linea in enumerate(archivo):
                linea = linea.strip()

                if not linea:
                    continue

                partes = linea.split()
                identificador = partes[0]
                palabras = partes[1:]

                if len(palabras) != n:
                    errores.append(
                        f"Tabla {idx + 1}: se esperaban {n} palabras y se encontraron {len(palabras)}"
                    )
                    continue  # 🔴 se ignora, NO aborta

                cartones.append(Carton(identificador, palabras))

    except FileNotFoundError:
        errores.append("Archivo no encontrado.")

    except Exception as e:
        errores.append(f"Error inesperado al leer archivo: {str(e)}")

    return cartones, errores
