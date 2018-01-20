"""
Encontrar el numero más pequeño
"""

numeros_usuario = []
input_usuario = ""
while len(numeros_usuario) < 6:
    input_usuario = input("Dime un numero: ")
    if input_usuario.isdigit() == True:
        numeros_usuario.append(int(input_usuario))
    else:
        print("Eso que has escrito no vale, tiene que ser un número")
# print("Hemos acabado, has escrito {}".format(numeros_usuario))
numero_pequeno = numeros_usuario[0]
for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El número mas pequeño es {}".format(numero_pequeno))
