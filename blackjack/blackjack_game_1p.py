import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)


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
    table_cards = []

    def __init__(self, name):
        self.name = name


class Game:
    card_values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10}

    def __init__(self):
        self.game_deck = Deck()
        player_name = input("¿Que nombre tendrá el jugador? ")
        self.player = Player(player_name)

    def decide_winner(self):
        return self.player.points > 21

    def draft_card(self):
        card = self.game_deck.give_random_card()
        self.player.table_cards.append(card)
        return card

    def count_points(self):
        card = self.draft_card()

        if card.number != 1:
            self.player.points += self.card_values[int(card.number)]

        else:
            decision = int(input("¿Quieres 1 punto u once?[1/11]: "))

            if decision == 1:
                self.player.points += 1

            elif decision == 11:
                self.player.points += 11

        if self.player.points == 1:
            print("{} lleva {} punto".format(self.player.name, self.player.points))
        else:
            print("{} lleva {} puntos".format(self.player.name, self.player.points))

    def ask_card(self):
        ask = input("\n¿Quieres seguir pidiendo cartas?[Si/No]: ")
        if ask == "No":
            return False
        else:
            return True

    def start_turn(self):

        keep_playing = True

        while not self.decide_winner() and keep_playing:
            self.count_points()

            if self.decide_winner():
                print("\n\nTe has pasado, perdiste")
                return

            if self.ask_card():
                pass
            else:
                print("Has conseguido {} puntos".format(self.player.points))
                return


Game().start_turn()
