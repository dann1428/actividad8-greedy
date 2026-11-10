"""
Cobertura de casas con la menor cantidad de antenas (algoritmo voraz).

Idea central: siempre se atiende la casa que quedó más a la izquierda sin señal,
y la antena se coloca lo más lejos posible hacia la derecha sin perder esa casa.
Así cada antena alcanza el mayor número de casas nuevas.

Ejecución:
    python cobertura_antenas.py          -> pide los datos por teclado
    python cobertura_antenas.py --demo   -> corre los dos ejemplos de la guía
"""
import sys


def colocar_antenas(casas, R):
    """
    casas : posiciones enteras de las casas (en cualquier orden, con repetidas).
    R     : alcance de cada antena (>= 0); una antena en x cubre [x-R, x+R].

    Devuelve la lista con las posiciones elegidas para las antenas.
    """
    if R < 0:
        raise ValueError("El alcance R no puede ser negativo.")

    posiciones = sorted(set(casas))   # orden creciente, sin duplicados: O(n log n)
    antenas = []
    cubierto_hasta = None             # extremo derecho de la última cobertura

    for casa in posiciones:           # un solo recorrido: O(n)
        # Si la casa ya cae dentro de la cobertura anterior, no hace falta nada.
        if cubierto_hasta is not None and casa <= cubierto_hasta:
            continue
        # Casa sin señal: la antena va en casa + R (máximo desplazamiento a la derecha).
        centro = casa + R
        antenas.append(centro)
        cubierto_hasta = centro + R

    return antenas


def imprimir_resultado(casas, R):
    antenas = colocar_antenas(casas, R)
    print(f"Casas: {casas}")
    print(f"Cobertura: {R}")
    print("Antenas colocadas en:")
    for posicion in antenas:
        print(f"  {posicion}")
    print(f"Cantidad total: {len(antenas)}")


def ejemplos_guia():
    print("=== Ejemplo 1 ===")
    imprimir_resultado([1, 2, 7, 11, 20, 21, 30], 5)
    print("\n=== Ejemplo 2 ===")
    imprimir_resultado([2, 4, 8, 15, 18, 22], 3)


def pedir_datos():
    casas = [int(x) for x in input("Posiciones de las casas (separadas por espacio): ").split()]
    R = int(input("Cobertura R: "))
    print()
    imprimir_resultado(casas, R)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        ejemplos_guia()
    else:
        pedir_datos()
