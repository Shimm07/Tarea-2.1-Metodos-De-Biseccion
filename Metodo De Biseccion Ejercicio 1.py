# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B8oTQS6dLf-8loQT9bq1RASCPpDjYDjU
"""

#   Implementación del Método de Bisección
#   para encontrar la raíz de la ecuación f(x) = x^3 - 4x - 9 = 0
#
#   Autor: Angel Gabriel Chim Vera
#   Contacto: angchimvera@gmail.com
#   Versión 1.1 : 12/02/2025
#

import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) dada en el enunciado
def f(x):
    return x**3 - 4*x - 9

# Algoritmo del Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    """
    Método de bisección para encontrar una raíz de f(x) en el intervalo [a, b].

    Retorna:
    iteraciones -> Lista con los valores intermedios de c en cada iteración.
    errores_abs -> Lista con los errores absolutos en cada iteración.
    errores_rel -> Lista con los errores relativos en cada iteración.
    errores_cuad -> Lista con los errores cuadráticos en cada iteración.
    """
    if f(a) * f(b) >= 0:
        print("Error: El método de bisección no es aplicable en el intervalo dado.")
        return None

    iteraciones, errores_abs, errores_rel, errores_cuad = [], [], [], []
    c_old = a

    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error Absoluto     |   Error Relativo   |  Error Cuadrático ")
    print("-" * 120)

    for i in range(max_iter):
        c = (a + b) / 2  # Punto medio
        iteraciones.append(c)

        error_abs = abs(c - c_old)  # Error absoluto
        error_rel = abs((c - c_old) / c) if c != 0 else 0  # Error relativo
        error_cuad = error_abs**2  # Error cuadrático

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cuad:.8e}")

        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Intervalo de búsqueda
a, b = 2, 3
iteraciones, errores_abs, errores_rel, errores_cuad = biseccion(a, b)

# Gráfica de la función y la convergencia de iteraciones
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# Puntos para graficar f(x)
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

# Gráfica de la función y las iteraciones
ax[0].plot(x, y, label=r'$f(x) = x^3 - 4x - 9$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica del error absoluto
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, marker='o', linestyle='-', color='r')
ax[1].set_yscale("log")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error Absoluto")
ax[1].set_title("Error Absoluto en cada Iteración")
ax[1].grid()

# Gráfica del error relativo y cuadrático
ax[2].plot(range(1, len(errores_rel)+1), errores_rel, marker='s', linestyle='-', color='g', label='Error Relativo')
ax[2].plot(range(1, len(errores_cuad)+1), errores_cuad, marker='^', linestyle='-', color='m', label='Error Cuadrático')
ax[2].set_yscale("log")
ax[2].set_xlabel("Iteración")
ax[2].set_ylabel("Error")
ax[2].set_title("Errores Relativo y Cuadrático")
ax[2].legend()
ax[2].grid()

# Guardar la figura
plt.savefig("biseccion_errores.png", dpi=300)
plt.show()