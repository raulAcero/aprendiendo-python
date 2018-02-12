"""
Crea un programa que cuente el número de veces que aparece una palabra en una string
"""

palabras = dict()

frase = input("dime una frase: ")

palabra = ""
indice = 0

for letra in frase:
    if letra != " ":
        palabra += letra
        if indice == len(frase) - 1:
            if palabra in palabras:
                palabras[palabra] += 1
            else:
                palabras[palabra] = 1
    else:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
        palabra = ""
    indice +=1

print(palabras)