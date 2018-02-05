"""
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""
print("Dime 3 numeros y te diré cual es el más grande")
primer = int(input("Primer número"))
segundo = int(input("Segundo número"))
tercero = int(input("Tercer número"))

def numero_grande(primer, segundo, tercero):
    if primer > segundo:
        num_grande = primer
    else:
        num_grande = segundo

    if num_grande < tercero:
        num_grande = tercero
    return num_grande

print(numero_grande(primer, segundo, tercero))