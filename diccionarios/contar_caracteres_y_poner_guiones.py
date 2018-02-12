"""
Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string
"""

def separar_palabras(string):
    longitud = len(string)
    barras = ""
    for letras in range(0, longitud):
        barras += "-"
    return barras

usuario = input("Dime algo")
print(separar_palabras(usuario))