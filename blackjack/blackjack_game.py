import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class Deck:
    suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        position = random.randint(1, len(self.cards))
        random_card = self.cards.pop(position)
        try:
            print("{} of {}".format(random_card.number, random_card.suit))
            return random_card
        except IndexError:
            print("Se acabó")


class Player:
    points = 0

    def __init__(self, name):
        self.name = name


class Game:

    def __init__(self):
        self.game_deck = Deck()
        player_name = input("¿Que nombre tendrá el jugador 1?")
        self.player = Player(player_name)

    def decide_winner(self):
        return self.player.points > 21

    def start_turn(self):
        while not self.decide_winner():
            random_card = self.game_deck.give_random_card()
            if 2 <= random_card.number <= 10:
                print("Te ha salido el {} de {}".format(random_card.number, random_card.suit))
                self.player.points += int(random_card.number)
            elif 11 <= random_card.number <= 13:
                print("Te ha salido el {} de {}".format(random_card.number, random_card.suit))
                self.player.points += 10
            elif random_card.number == 1:
                print("Te ha salido el AS de {}".format(random_card.suit))
                one_or_eleven = input("¿Quieres 1 punto u once?[1/11]: ")
                if int(one_or_eleven) == 1:
                    self.player.points += 1
                if int(one_or_eleven) == 11:
                    self.player.points += 11

            if self.decide_winner():
                print("\n\nTe has pasado, perdiste")

            if self.player.points == 1:
                print("{} lleva {} punto".format(self.player.name, self.player.points))
            else:
                print("{} lleva {} puntos".format(self.player.name, self.player.points))
            ask_card = input("\n¿Quieres seguir pidiendo cartas?[Si/No]: ")
            if ask_card == "Si":
                pass
            elif ask_card == "No":
                return

prueba = Game().start_turn()