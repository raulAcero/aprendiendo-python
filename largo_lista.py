"""
Contar parametros sin len()
"""
print("Introduce numeros y te dire cuantos han sido, cuando quieras parar escribe 'FIN'")
lista = []
input_usuario = ""
while input_usuario != "FIN":
    input_usuario = input("Dime un numero: ")
    if input_usuario.isdigit() == True:
        lista.append(int(input_usuario))
    else:
        print("Eso que has escrito no vale, tiene que ser un número")
largo_lista = 0
for numero in lista:
    largo_lista += 1

print("La lista mide {}".format(largo_lista))


print("La lista contiene {}".format(lista))