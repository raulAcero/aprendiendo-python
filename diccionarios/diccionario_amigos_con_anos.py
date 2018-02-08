"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.
"""

salir = False
amigos = dict()

while not salir:
    print("Este programa sirve para tener una lista de tus amigos junto a sus años de nacimiento")
    eleccion = input("¿Que quieres hacer?(Añadir amigo{a}/Ver amigo{v}/Salir{s})")

    if eleccion == "a":
        nombre = input("Dime su nombre: ")
        ano_nacimiento = input("Dime su año de nacimiento: ")
        amigos[nombre] = ano_nacimiento

    if eleccion == "v":
        nombre = input("Dime el nombre de la persona que quieres consultar: ")
        print(amigos[nombre])

    if eleccion == "s":
        salir = True