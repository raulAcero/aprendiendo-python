"""
Escribe un programa que imprima por pantalla una frase aleatoria cada segundo. La lista de frases de la que se seleccionará la frase aleatoria será distinta según el segundo en el que estemos:
"""
from time import sleep
import random
import datetime

frases_alegres = ["Que bonita es la vida", "La accion más pequeña es más que la intención más grande", "Aquello que te hace SONREÍR, es por lo que VALE la PENA VIVIR", "Piensa en POSTIVO y atraerás cosas POSITIVAS a tu VIDA"]
muebles = ["cajonera", "armario", "sofá", "Sillón", "Silla"]
bebidas = ["freeway", "pepsi", "limonada", "nestea", "cerveza"]
frases_odio = ["Odiar a alguien es otorgarle demasiada importancia", "No honres con tu odio a quien no podrías honrar con tu amor", "Ira de hermanos, ira de diablos", "Pasión más viva que la amistad es el odio"]
comida = ["pizza", "durum", "atún", "chuletas asadas", "costillas de ternera"]
frases_absurdas = ["El profesor de matemáticas se ha suicidado, tenía demasiados PROBLEMAS", "Cambio lindo perro DOBERMAN por mano ortopedica", "¿Cómo se llama un boomerang que no vuelve? PALO", "Cada MUJER es un MUNDO... ¡Haz turismo!"]
animales = ["koala", "gallina", "avestruz", "rinoceronte", "ornitorrinco"]
frases_motivadoras = ["Los sueños se realizan cuando mantienes el compromiso con ellos", "La felicidad no es una estación de llegada, sino un modo de viajar", "Detrás de los sueños siempre hay esfuerzos que la gente no ve", "Mis sueños son mentiras que algún día dejarán de serlo"]
sonidos_animales = ["beee", "oink", "muuuuu", "guau", "miau"]
frases_tristes = ["Los grandes no mueren, sólo se ausentan para ser recordados", "Sólo en la agonía de despedirnos somos capaces de comprender la profundidad de nuestro amor", "A menudo el sepulcro encierra sin saberlo, dos corazones en un mismo ataúd"]

frases = [frases_alegres, muebles, bebidas, frases_odio, comida, frases_absurdas, animales, frases_motivadoras, sonidos_animales, frases_tristes]

hora_actual = datetime.datetime.now()

def segundo_actual(hora):
    segundo = str(hora.second)
    return int(segundo[-1])

def sacar_frase():
    while True:
        hora_actual = datetime.datetime.now()
        seg_actual = segundo_actual(hora_actual)
        numero = random.randint(0, len(frases[seg_actual]) - 1)
        print(frases[seg_actual][numero])
        sleep(1)

print(sacar_frase())