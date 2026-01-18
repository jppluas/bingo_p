# main.py

from core.carga_cartones import cargar_cartones
from core.flujo_ronda import ejecutar_ronda


def seleccionar_idioma():
    opciones = {
        "1": "SP",
        "2": "EN",
        "3": "PT",
        "4": "DT"
    }

    print("Seleccione idioma de la ronda:")
    print("1. Español (SP)")
    print("2. English (EN)")
    print("3. Portuguese (PT)")
    print("4. Dutch (DT)")

    while True:
        opcion = input("Opción: ").strip()
        if opcion in opciones:
            return opciones[opcion]
        print("Opción inválida. Ingrese 1, 2, 3 o 4.\n")


def main():
    print("=== Bingo_P – Asistente del Concursante ===\n")

    idioma = seleccionar_idioma()
    cartones, errores = cargar_cartones(idioma)

    if errores:
        print("\n⚠️ Advertencias durante la carga de cartones:")
        for e in errores:
            print("-", e)

    print(f"\n✔️ {len(cartones)} cartón(es) listos para la ronda.")

    while True:
        iniciar = input("\n¿Desea iniciar la ronda? (s/n): ").lower()
        if iniciar == "s":
            ejecutar_ronda(cartones, idioma)
            return
        if iniciar == "n":
            print("Programa finalizado.")
            return
        print("Entrada inválida. Escriba 's' o 'n'.")


if __name__ == "__main__":
    main()
