"""
Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés
"""

colores = {"rojo": "red", "azul": "blue", "verde": "green", "lila": "violet", "amarillo": "yellow"}

preguntar = True
while preguntar:
    print("Esto es un diccionario, si me escribes un color en español te digo la traducción en ingles")
    accion = input("Quieres saber la traducción de un color o salir?[traduccion(t)/salir(s)]: ")
    if accion == "t":
        color = input("¿Que color quieres saber? ")
        if color in colores:
            print(colores[color])
        else:
            print("El color {} no lo conozco".format(color))

    if accion == "s":
        preguntar = False
