"""
Calcular media de varios numeros
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
suma_numeros = sum(lista)
media = suma_numeros / len(lista)
print("La media es {}".format(media))