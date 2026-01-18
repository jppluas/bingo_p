import random
import os

from core.datos_prueba import PALABRAS_POR_IDIOMA

VOCAB_DIR = "data/vocabularios"
OUTPUT_DIR = "tests/cartones_prueba"


def cargar_vocabulario(idioma):
    ruta = os.path.join(VOCAB_DIR, f"{idioma.lower()}.txt")
    palabras = []

    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            palabra = linea.strip()
            if palabra:
                palabras.append(palabra)

    return palabras


def generar_carton(vocabulario, n):
    """
    Genera un cartón con n palabras que NO sea ganador
    """
    while True:
        palabras = random.sample(vocabulario, n)
        return palabras


def generar_archivo_prueba(idioma, total_cartones):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    n = PALABRAS_POR_IDIOMA[idioma]
    vocabulario = cargar_vocabulario(idioma)

    ruta_salida = os.path.join(
        OUTPUT_DIR, f"{idioma.lower()}{total_cartones}.txt"
    )

    with open(ruta_salida, "w", encoding="utf-8") as f:
        for i in range(total_cartones):
            identificador = f"{idioma}{str(i + 1).zfill(6)}"

            palabras = generar_carton(
                vocabulario, n
            )

            linea = identificador + " " + " ".join(palabras)
            f.write(linea + "\n")

    print(f"✔ Archivo generado: {ruta_salida}")


def main():
    """
    Ejemplos de generación:
    """
    generar_archivo_prueba("SP", 20)
    generar_archivo_prueba("SP", 50)
    generar_archivo_prueba("SP", 100)
    generar_archivo_prueba("SP", 200)

    generar_archivo_prueba("EN", 20)
    generar_archivo_prueba("EN", 50)
    generar_archivo_prueba("EN", 100)
    generar_archivo_prueba("EN", 200)

    generar_archivo_prueba("PT", 20)
    generar_archivo_prueba("PT", 50)
    generar_archivo_prueba("PT", 100)
    generar_archivo_prueba("PT", 200)

    generar_archivo_prueba("DT", 20)
    generar_archivo_prueba("DT", 50)
    generar_archivo_prueba("DT", 100)
    generar_archivo_prueba("DT", 200)


if __name__ == "__main__":
    main()
