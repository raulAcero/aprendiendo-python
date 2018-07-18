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

    n_players = 2

    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.table_cards = []

    def ask_player_name(self, player_n):
        return input("¿Cual es el nombre del {}?: ".format(player_n))

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        return card

    def count_table_cards(self):
        total = 0

        for card in self.table_cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total += 1
            else:
                total += self.card_values[card.number]

        return total

    def player_wants_to_continue(self):
        response = input("¿Quieres otra carta[Y/N]?")
        return response == "Y"

    def start_turn(self, player):
        self.table_cards = []
        self.deck = Deck()
        print("\nTurno de {}\n".format(player.name))

    def play(self):

        for i in range(self.n_players):
            self.players.append(Player(self.ask_player_name(i + 1)))

        user_continue = True
        winner_score = 0
        winner = None

        for player in self.players:
            self.start_turn(player)

            while not self.count_table_cards() > 21 and user_continue:
                self.draft_card()
                user_continue = self.player_wants_to_continue()

            player.points = self.count_table_cards()
            print("Tu puntuación es : {}".format(player.points))

            if player.points > 21:
                print("Perdiste")
            elif player.points > winner_score:
                winner_score = player.points
                winner = player

        print("El ganador es {} con {} puntos".format(winner.name, winner_score))


if __name__ == "__main__":
    blackjack = Game()
    blackjack.play()
