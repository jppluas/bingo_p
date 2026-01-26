# main.py
"""
Mini Proyecto Final – Bingo_P

Autores:
- Leonel Cabrera
- Juan Pluas
- Steven Lino
- Erick Murillo

Descripción:
Aplicación en Python para la gestión de partidas de bingo con palabras en distintos idiomas 
(Español, Inglés, Portugués y Neerlandes), permitiendo carga manual y masiva de cartones, 
rondas aleatorias por idioma y detección automática de cartones ganadores.

Referencias y apoyos utilizados:
- Uso de librerías estándar de Python
- Apoyo de asistente virtual (ChatGPT) para aclaración de conceptos y estructura del código

Algoritmos o código externo:
- No se utilizaron algoritmos académicos externos completos.
- La lógica de generación aleatoria de rondas y validación de cartones fue diseñada por los autores.

Modificaciones:
- No aplica (código desarrollado desde cero por los integrantes del grupo).
"""

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
