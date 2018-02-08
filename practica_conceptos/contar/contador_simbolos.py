"""
Programa contador de simbolos
"""

frase_usuario = input("Introduzca la frase a contar: ")

espacio = " "
coma = ","
punto = "."

n_espacio = 0
n_comas = 0
n_puntos = 0

for simbolo in frase_usuario:
    if simbolo == espacio:
        n_espacio += 1
    elif simbolo == coma:
        n_comas += 1
    elif simbolo == punto:
        n_puntos += 1

print("Ha escrito {} espacios, {} puntos y {} comas.".format(n_espacio, n_puntos, n_comas))


