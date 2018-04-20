POKEMON_LIST = ["Charmander", "Bulbasur", "Squirtle"]
from time import sleep

class Pokemon:
    vida_base = 100
    ataque = 10

    def __init__(self):
        self.vida = self.vida_base

    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)

    def recibir_dano(self, dano):
        self.vida -= dano


class Charmander(Pokemon):
    nombre = "Charmander"
    vida_base = 90
    ataque = 14


class Bulbasur(Pokemon):
    nombre = "Bulbasur"
    vida_base = 100
    ataque = 11


class Squirtle(Pokemon):
    nombre = "Squirtle"
    vida_base = 110
    ataque = 8


def ask_pokemon(pokemons):
    selected = False
    print("Selecciona tu pokemon:")
    for i in pokemons:
        print("- {}".format(i))

    user_choice = ""

    while user_choice not in pokemons:
        user_choice = input("¿Cual quieres?: ")
        if user_choice == "Charmander":
            return Charmander()
            selected = True

        elif user_choice == "Bulbasur":
            return Bulbasur()
            selected = True

        elif user_choice == "Squirtle":
            return Squirtle()
            selected = True

def combat(pokemon1, pokemon2):
    print("Comienza el combate")
    while pokemon1.vida > 0 and pokemon2.vida > 0:
        pokemon1.atacar(pokemon2)
        print("{} ha atacado a {}, le quedan {} puntos de vida".format(pokemon1.nombre, pokemon2.nombre, pokemon2.vida))
        sleep(2)
        pokemon2.atacar(pokemon1)
        print("{} ha atacado a {}, le quedan {} puntos de vida".format(pokemon2.nombre, pokemon1.nombre, pokemon1.vida))
        sleep(2)
        if pokemon1.vida < 1:
            print("\nAcabó el combate, ha ganado {}".format(pokemon2.nombre))
        if pokemon2.vida < 1:
            print("\nAcabó el combate, ha ganado {}".format(pokemon1.nombre))


def main():
    user1_pokemon = ask_pokemon(POKEMON_LIST)
    user2_pokemon = ask_pokemon(POKEMON_LIST)
    combat(user1_pokemon, user2_pokemon)


if __name__ == '__main__':
    main()