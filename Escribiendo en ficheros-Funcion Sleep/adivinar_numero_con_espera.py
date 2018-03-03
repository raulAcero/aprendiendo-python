"""
Crea un programa que pregunte al usuario que adivine un numero del 1 al 10, pero ese numero se va a generar aleatoriamente. Hacer esperar al usuario 3 segundos antes de dar la respuesta
"""

import random
from time import sleep

def main():
    print("Vamos a ver si puedes adivinar el número que estoy pensando")
    num_usuario = int(input("¿Que numero crees que es?: "))
    num_a_adivinar = random.randint(1,10)
    while num_usuario < 1 or num_usuario > 10:
        num_usuario = int(input("Ese número no vale, dime otro entre 1 y 10: "))

    if num_usuario == num_a_adivinar:
        sleep(3)
        print("Ganaste")
    else:
        sleep(3)
        print("Perdiste, el numero era {}".format(num_a_adivinar))

print(main())