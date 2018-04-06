"""
Escribe la función para averiguar la edad de un contacto sabiendo tan solo el año de nacimiento (utiliza datetime y
strptime, no está relacionado directamente con clases)
"""

import datetime


class persona:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        today = datetime.datetime.now()
        age_number = today - self.birthday
        print("{} tiene {} años".format(self.name, int(age_number.days / 365)))


def main():
    birthday = datetime.datetime.strptime(input("Dime tu fecha de cumpleaños[dd/mm/yyyy]"), "%d/%m/%Y")
    raul = persona("raul", birthday)
    print(raul.age())


if __name__ == '__main__':
    main()
