"""
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
"""

print("Introduce numeros y te dire los pares, cuando quieras parar escribe 'FIN'")
lista = []
input_usuario = ""
while input_usuario != "FIN":
    input_usuario = input("Dime un numero: ")
    if input_usuario.isdigit() == True:
        lista.append(int(input_usuario))
    else:
        print("Eso que has escrito no vale, tiene que ser un número")

def devolver_pares(numeros):
    pares = []
    posicion = 0
    for numero in lista:
        if numero % 2 == 0:
            pares.append(lista[posicion])
        posicion += 1
    return pares

print(devolver_pares(lista))