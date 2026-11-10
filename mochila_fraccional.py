"""
Mochila fraccional resuelta con un algoritmo voraz.

Idea central: lo más rentable es llenar la mochila primero con los objetos que
dan más valor por cada unidad de peso. Si el siguiente objeto ya no entra
entero, se corta la parte que sí cabe y se termina.

Ejecución:
    python mochila_fraccional.py          -> pide los datos por teclado
    python mochila_fraccional.py --demo   -> corre los dos ejemplos de la guía
"""
import sys
from fractions import Fraction


def valor_por_peso(objeto):
    """Devuelve cuánto valor aporta el objeto por unidad de peso."""
    _, valor, peso = objeto
    return Fraction(valor) / Fraction(peso)


def resolver_mochila(capacidad, objetos):
    """
    capacidad : peso máximo que soporta la mochila (>= 0).
    objetos   : lista de tuplas (nombre, valor, peso).

    Devuelve (elegidos, total):
      elegidos -> lista de (nombre, parte_tomada, peso_usado)
      total    -> valor acumulado (Fraction)
    """
    if capacidad < 0:
        raise ValueError("La capacidad no puede ser negativa.")
    for nombre, valor, peso in objetos:
        if peso <= 0 or valor < 0:
            raise ValueError(f"Objeto {nombre}: peso debe ser > 0 y valor >= 0.")

    # Paso 1: de mayor a menor rentabilidad (costo O(n log n)).
    por_rentabilidad = sorted(objetos, key=valor_por_peso, reverse=True)

    libre = Fraction(capacidad)   # espacio que aún queda en la mochila
    total = Fraction(0)
    elegidos = []

    # Paso 2: una sola pasada, llenando el espacio libre (costo O(n)).
    for nombre, valor, peso in por_rentabilidad:
        if libre == 0:
            break
        peso = Fraction(peso)
        # Si cabe entero se toma 1 (todo); si no, solo la proporción libre/peso.
        parte = Fraction(1) if peso <= libre else libre / peso
        usado = parte * peso
        elegidos.append((nombre, parte, usado))
        total += parte * Fraction(valor)
        libre -= usado

    return elegidos, total


def imprimir_resultado(capacidad, objetos):
    elegidos, total = resolver_mochila(capacidad, objetos)
    peso_de = {nombre: peso for nombre, _, peso in objetos}

    print(f"Capacidad máxima: {capacidad}")
    print("Objetos seleccionados:")
    if not elegidos:
        print("  (ninguno)")
    for nombre, parte, usado in elegidos:
        if parte == 1:
            print(f"  {nombre} completo")
        else:
            print(f"  {usado}/{peso_de[nombre]} Parte del objeto {nombre}")
    print(f"Valor total obtenido: {float(total):g}")


def ejemplos_guia():
    print("=== Ejemplo 1 ===")
    imprimir_resultado(50, [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)])
    print("\n=== Ejemplo 2 ===")
    imprimir_resultado(25, [("A", 80, 20), ("B", 100, 10), ("C", 120, 30)])


def pedir_datos():
    capacidad = float(input("Capacidad máxima: "))
    cantidad = int(input("Cantidad de objetos: "))
    objetos = []
    for i in range(cantidad):
        nombre = input(f"Nombre del objeto {i + 1}: ")
        valor = float(input("  Valor: "))
        peso = float(input("  Peso: "))
        objetos.append((nombre, valor, peso))
    print()
    imprimir_resultado(capacidad, objetos)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        ejemplos_guia()
    else:
        pedir_datos()
