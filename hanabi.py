from random import shuffle


class Game:

    def __init__(self, deck):
        self.bombs = 0
        self.clues = 8

        # top card of respective color
        self.board = {'red': 0, 'blue': 0, 'yellow': 0, 'green': 0}
        self.deck = deck
        deck.shuffle()
        self.discard = []
        self.game_lost = False
        self.game_won = False


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.clues = []

    def __str__(self):
        return self.name

    def give_clue(self, clue):
        clue.player.hand.append(clue)

    def draw_card(self, deck):
        card = deck.deck[0]
        del deck.deck[0]
        self.hand.append(card)

    def play_card(self, card_index, game):
        card = self.hand[card_index]
        del self.hand[card_index]

        if card.num == game.board[card.color] + 1:
            game.board[card.color] = card.num
        else:
            game.bombs += 1
            game.discard.append(card)

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

    def __init__(self, player, count, num=0, color=""):
        self.player = player
        self.count = count
        self.num = num
        self.color = color

