# core/flujo_ronda.py

from core.ronda_bingo import RondaBingo
from core.datos_prueba import PALABRAS_GANADORAS
from core.normalizador import normalizar


def ejecutar_ronda(cartones, idioma):
    ronda = RondaBingo(
        idioma,
        cartones,
        PALABRAS_GANADORAS[idioma]
    )

    print(f"\n🟢 Ronda iniciada en idioma {idioma}")
    print("Ingrese palabras anunciadas (escriba salir() para terminar)\n")

    while True:
        palabra = input("").strip()

        if not palabra:
            print("Entrada vacía, intente nuevamente.")
            continue

        if palabra.lower() == "salir()":
            print("Ronda finalizada sin bingo.")
            return

        palabra = normalizar(palabra)
        ganadores = ronda.anunciar_palabra(palabra)

        if ganadores:
            print("\n🎉 BINGO DETECTADO 🎉")
            for g in ganadores:
                print(f"Cartón ganador: {g.id}")
            return
