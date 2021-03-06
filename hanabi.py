from random import shuffle


class Game:

    def __init__(self, deck):
        self.bombs = 0
        self.clues = 8
        self.board = {'red': 0, 'blue': 0, 'yellow': 0, 'green': 0} # top card number
        self.discard = []
        self.game_lost = False
        self.game_won = False
        self.players = []
        self.deck = deck
        deck.shuffle()

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        for player in players:
            for i in range(5):
                player.draw_card(self.deck)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.clues = []

    def __str__(self):
        return self.name

    def draw_card(self, deck):
        card = deck.deck[0]
        del deck.deck[0]
        self.hand.append(card)

    def give_clue(self, clue, game):
        clue.player.hand.append(clue)
        game.clues -= 1


    def play_card(self, card_index, game):
        card = self.hand[card_index]
        del self.hand[card_index]

        if card.num == game.board[card.color] + 1:
            game.board[card.color] = card.num
            if all(value == 5 for value in game.board.values()):
                game.game_won = True
        else:
            game.bombs += 1
            game.discard.append(card)
            count = 0

            if card in discard:
                count += 1

            if card.num == 5:
                game.game_lost = True

            if card.num == 4 or card.num == 3 or card.num == 2:
                if count == 2:
                    game.game_lost = True

            if card.num == 1 and count == 3:
                game.game_lost = True



        self.draw_card(game.deck)

    def discard_card(self, card_index, game):
        card = self.hand[card_index]
        del self.hand[card_index]
        game.discard.append(card)
        if game.clues < 8:
            game.clues += 1

        self.draw_card(game.deck)


class Deck:

    def __init__(self):
        self.deck = []
        self.colors = ['red', 'blue', 'yellow', 'green']
        for color in self.colors:

            for i in range(3):
                self.deck.append(Card.Card(color, 1))

            for i in range(2):
                self.deck.append(Card.Card(color, 2))
                self.deck.append(Card.Card(color, 3))
                self.deck.append(Card.Card(color, 4))

            self.deck.append(Card.Card(color, 5))

    def shuffle(self):
        shuffle(self.deck)


class Card:

    def __init__(self, color, num):
        self.num = num
        self.color = color

    def __str__(self):
        return self.color + " " + self.num


class Clue:

    def __init__(self, player, indexes, num=0, color=""):
        self.player = player
        self.num = num
        self.color = color
        self.indexes = indexes

