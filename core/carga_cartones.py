# core/carga_cartones.py

from core.carton import Carton
from core.lector_txt import cargar_cartones_lote
from core.datos_prueba import PALABRAS_POR_IDIOMA


def cargar_carton_individual(idioma):
    n = PALABRAS_POR_IDIOMA[idioma]
    palabras = []

    print(f"\nIngrese {n} palabras (una por una):")

    for i in range(n):
        while True:
            palabra = input(f"Palabra {i + 1}: ").strip()
            if palabra:
                palabras.append(palabra)
                break
            print("Entrada inválida, intente nuevamente.")

    identificador = idioma + "000001"
    return [Carton(identificador, palabras)], []


def cargar_cartones(idioma):
    while True:
        print("\n¿Cómo desea cargar los cartones?")
        print("1. Ingreso individual")
        print("2. Carga por lote (TXT)")

        opcion = input("Opción: ").strip()

        # ---------- INGRESO INDIVIDUAL ----------
        if opcion == "1":
            return cargar_carton_individual(idioma)

        # ---------- CARGA POR LOTE ----------
        if opcion == "2":
            while True:
                ruta = input("Ruta del archivo TXT: ").strip()
                cartones, errores = cargar_cartones_lote(ruta, idioma)

                if errores:
                    print("\n⚠️ Se detectaron errores:")
                    for e in errores:
                        print("-", e)

                if cartones:
                    print(f"\n✔️ {len(cartones)} cartón(es) cargados correctamente.")
                    return cartones, errores

                print("\n❌ El archivo no contiene cartones válidos.")
                print("Ingrese otro archivo.\n")

        print("Opción inválida, intente nuevamente.\n")
