"""
2 – Define una clase que corresponda con tu animal favorito y crea algunas instancias dentro de una lista
"""


class Dog:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed


def main():
    dog1 = Dog("Bobby", "gris", "labrador")
    dog2 = Dog("Canelo", "marron", "perro de agua")
    dog3 = Dog("Jack", "negro y blanco", "golden retriever")
    my_dogs = [dog1, dog2, dog3]
    print("Tengo {} perros".format(len(my_dogs)))
    for i in my_dogs:
        print("- {}".format(i.name))


if __name__ == '__main__':
    main()
