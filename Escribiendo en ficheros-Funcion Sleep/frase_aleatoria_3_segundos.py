"""
Escribe una frase aleatoria de una lista de strings cada 3 segundos
"""

import random
from time import sleep

def main():
    frases = ["hola que tal","tengo que ir al baño","con hacer un par de ejercicios basta","Insisto, vale?","No me importa abrir otro parte grave","Os falta actitud, no consiento más esto"]
    while True:
        numero = random.randint(0, len(frases)-1)
        print(frases[numero])
        sleep(3)

print(main())