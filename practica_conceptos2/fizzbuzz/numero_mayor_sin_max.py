"""
Crea un programa que te diga el mayor número sin la función max
"""

lista_numeros = [3, 5, 4, 8, 90, 12, 15, 34, 11, 16]
numero_grande = 0

for numero in lista_numeros:
    if numero_grande < numero:
        numero_grande = numero

print(numero_grande)