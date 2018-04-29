import random

COSTE_DINO_MINI = 499
RENDIMIENTO_DINO_MINI = 35
COSTE_DINO_INT = 5000
RENDIMIENTO_DINO_INT = 400
COSTE_DINO_MEDIO = 29000
RENDIMIENTO_DINO_MEDIO = 1980


def main():
    dia = 0
    dinos_pequenos = int(input("cuantos dinosaurios pequenos tienes: "))
    cantidad_dino_mini = dinos_pequenos
    cantidad_dino_int = 2
    cantidad_dino_medio = 0
    dinero = 0
    banco = 0
    cantidad_dias = int(input("Dime cuantos dias quieres que calcule: "))
    while dia < cantidad_dias:
        beneficio = (RENDIMIENTO_DINO_MINI * 24 * cantidad_dino_mini) + (
                RENDIMIENTO_DINO_MEDIO * 24 * cantidad_dino_medio) + (
                            RENDIMIENTO_DINO_INT * 24 * cantidad_dino_int)
        dinero += round(beneficio / 100 * 0.7)
        banco += round(beneficio / 100 * 0.3)
        banco += random.randrange(0, 70)
        print("dia {}, dinero {}, banco {}".format(dia, dinero, banco))
        print("{} euros".format(round(banco * 0.0093158494, 2)))
        dia += 1
        if dinero > COSTE_DINO_MINI:
            dinero -= COSTE_DINO_MINI
            cantidad_dino_mini += 1
        elif dinero > COSTE_DINO_MEDIO:
            dinero -= COSTE_DINO_MEDIO
            cantidad_dino_medio += 1


main()
