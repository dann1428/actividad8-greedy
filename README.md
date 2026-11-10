# Actividad 8: Algoritmos Voraces (Greedy)

Soluciones en Python 3 a dos problemas de optimización, usando la técnica voraz. No necesitan instalar librerías.

## Contenido

- `mochila_fraccional.py`: llena una mochila maximizando el valor, pudiendo cortar objetos.
- `cobertura_antenas.py`: coloca el mínimo de antenas para dar señal a todas las casas de una carretera.

## Requisitos

Tener instalado Python 3.8 o más reciente.

## Cómo correrlos

Para ver los ejemplos de la guía:

```bash
python mochila_fraccional.py --demo
python cobertura_antenas.py --demo
```

Para probar con tus propios datos, ejecuta el programa sin argumentos y responde lo que pregunta:

```bash
python mochila_fraccional.py
# Capacidad máxima, cantidad de objetos, y luego nombre, valor y peso de cada uno

python cobertura_antenas.py
# Posiciones de las casas separadas por espacios, y después el valor de R
```

## Resumen de las estrategias

- **Mochila:** se prioriza lo que más valor da por unidad de peso. Se meten objetos enteros hasta que el siguiente no cabe, y de ese se toma solo la porción que rellena el espacio. Costo: O(n log n).
- **Antenas:** se recorre de izquierda a derecha; ante la primera casa sin señal se instala una antena a distancia R hacia la derecha de esa casa, y se continúa después del último punto cubierto. Costo: O(n log n).

Los detalles, el análisis de complejidad y las ejecuciones están en el informe PDF.
