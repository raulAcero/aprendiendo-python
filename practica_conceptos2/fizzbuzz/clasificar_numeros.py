"""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una
lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.
"""

numeros = []
numeros_usuario = ""

while numeros_usuario != "FIN":
    numeros_usuario = input("Dime numeros y cuando hayas terminado escribe 'FIN': ")

    if numeros_usuario.isdigit() == True:
        numeros.append(int(numeros_usuario))
    elif numeros_usuario == "FIN":
        print("Ya hemos terminado")
    else:
        print("Repite, eso no era un número")

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []


for digitos in numeros:
    if digitos % 2 == 0:
        multiplos_dos.append(digitos)

    if digitos % 3 == 0:
        multiplos_tres.append(digitos)

    if digitos % 5 == 0:
        multiplos_cinco.append(digitos)

    if digitos % 7 == 0:
        multiplos_siete.append(digitos)

print("Estos son los numeros : {}".format(numeros))
print("Los multiplos de 2 son: {}".format(multiplos_dos))
print("Los multiplos de 3 son: {}".format(multiplos_tres))
print("Los multiplos de 5 son: {}".format(multiplos_cinco))
print("Los multiplos de 7 son: {}".format(multiplos_siete))