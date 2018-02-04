"""
Crear un programa que reemplace las letras segun el orden de aparicion
"""

palabra = "aurora boreal"
posicion = 0
numero = 1
frasefinal = ""
while len(palabra) > posicion:
    if palabra[posicion] == "a" or palabra[posicion] == "e" or palabra[posicion] == "i" or palabra[posicion] == "o" or palabra[posicion] == "u":
        frasefinal += str(numero)
        numero += 1
    else:
        frasefinal += palabra[posicion]
    posicion += 1



print(frasefinal)