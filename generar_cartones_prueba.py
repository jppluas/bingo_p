import random
import os

from core.datos_prueba import PALABRAS_POR_IDIOMA, PALABRAS_GANADORAS


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


def generar_carton_no_ganador(vocabulario, palabras_ganadoras, n):
    """
    Genera un cartón con n palabras que NO sea ganador
    """
    while True:
        palabras = random.sample(vocabulario, n)
        if set(palabras) != set(palabras_ganadoras):
            return palabras


def generar_archivo_prueba(idioma, total_cartones, indices_ganadores):
    """
    indices_ganadores: lista de índices (0-based) donde irá un cartón ganador
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    n = PALABRAS_POR_IDIOMA[idioma]
    palabras_ganadoras = PALABRAS_GANADORAS[idioma]
    vocabulario = cargar_vocabulario(idioma)

    ruta_salida = os.path.join(
        OUTPUT_DIR, f"{idioma.lower()}{total_cartones}.txt"
    )

    with open(ruta_salida, "w", encoding="utf-8") as f:
        for i in range(total_cartones):
            identificador = f"{idioma}{str(i + 1).zfill(6)}"

            if i in indices_ganadores:
                palabras = palabras_ganadoras
            else:
                palabras = generar_carton_no_ganador(
                    vocabulario, palabras_ganadoras, n
                )

            linea = identificador + " " + " ".join(palabras)
            f.write(linea + "\n")

    print(f"✔ Archivo generado: {ruta_salida}")


def main():
    """
    Ejemplos de generación:
    """
    generar_archivo_prueba("SP", 20, [6])
    generar_archivo_prueba("SP", 50, [11, 36])
    generar_archivo_prueba("SP", 100, [24, 62])
    generar_archivo_prueba("SP", 200, [49, 119, 198])

    generar_archivo_prueba("EN", 20, [10])
    generar_archivo_prueba("EN", 50, [25, 40, 15])
    generar_archivo_prueba("EN", 100, [5, 55, 75])
    generar_archivo_prueba("EN", 200, [33, 66, 99, 150])

    generar_archivo_prueba("PT", 20, [20])
    generar_archivo_prueba("PT", 50, [10, 30])
    generar_archivo_prueba("PT", 100, [25, 50, 75])
    generar_archivo_prueba("PT", 200, [40, 80, 120, 160])

    generar_archivo_prueba("DT", 20, [5])
    generar_archivo_prueba("DT", 50, [15, 35])
    generar_archivo_prueba("DT", 100, [20, 40, 60])
    generar_archivo_prueba("DT", 200, [25, 50, 75, 100])


if __name__ == "__main__":
    main()
