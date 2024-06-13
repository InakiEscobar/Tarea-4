# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:16:27 2024

@author: HBKfdo
"""

def promedio():
    """Función que interactúa con el usuario para obtener y calcular el promedio de notas."""
    print("Programa para calcular el promedio de notas")

    # Pedir el número de notas
    while True:
        try:
            num_notas = int(input("¿Cuántas notas deseas ingresar? "))
            if num_notas <= 0:
                raise ValueError("El número de notas debe ser positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, ingresa un número entero positivo.")

    # Pedir las notas una por una
    notas = []
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if nota < 0 or nota > 10:
                    raise ValueError("La nota debe estar entre 0 y 10.")
                notas.append(nota)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, ingresa un número válido.")

    # Calcular y mostrar el promedio
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las {num_notas} notas es:")
    return promedio