"""
Crear un programa que sustituya valores de una lista cuando:
    sea divisible entre 3 por fizz
    sea divisible entre 5 por buzz
    sea divisible entre 3 y 5 por bazinga
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 50, 100, 123, 120, 201]

for posicion in range(len(numeros)):
    numero = numeros[posicion]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[posicion] = ""

        if numero % 3 == 0:
            numeros[posicion] = "fizz"

        if numero % 5 == 0:
            numeros[posicion] = "buzz"

        if numero % 3 == 0 and numero % 5 == 0:
            numeros[posicion] = "bazinga"

print(numeros)
