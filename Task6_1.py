import random


class Card(object):
    def __init__(self, value=None, sign=None):
        self.value = value
        self.sign = sign

    def __str__(self):
        if self.value is not None:
            return '{} of {}'.format(self.value, self.sign)
        return 'Joker'

    def __hash__(self):
        return '{}_{}'.format(self.sign, self.value)


class Deck(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if Deck.instance is None:
            Deck.instance = object.__new__(Deck)
        return Deck.instance

    def __init__(self):
        signs = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.cards = [Card(val, sign) for val in range(2, 11) for sign in signs]
        self.cards += [Card(val, sign) for val in {'Jack', 'Queen', 'King', 'Ace'} for sign in signs]
        # Раскомментировать, если играть с джокерами
        # self.cards.append(Card())
        # self.cards.append(Card())
        random.shuffle(self.cards)

    def __str__(self):
        return '\n'.join(list(map(lambda c: c.__str__(), self.cards)))

    def give_cards(self, hand=None, size=1):
        popped = [self.cards.pop() for i in range(0, size)]
        if hand is not None:
            hand.append_cards(popped)
        return popped


class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []

    def append_cards(self, cards):
        for card in cards:
            self.cards_in_hand.append(card)

    def __str__(self):
        cards = list(map(lambda c: c.__str__(), self.cards_in_hand))
        cards_str = ', '.join(cards)
        if self.name is not None:
            return 'Player {} has: {}'.format(self.name, cards_str)
        return '{} are on the table'.format(cards_str)


# Игра в техасский холдем
class PokerGame(object):
    G_MAX_FLUSH_COUNT = 3

    G_COMBOS = [
        ('High Ace', lambda cards: None),
        ('Two Pairs', lambda cards: None),
        ('Three of a Kind', lambda cards: None),
        ('Flush', lambda cards: None),
        ('Straight', lambda cards: None),
        ('Straight Flush', lambda cards: None),
        ('Four of a Kind', lambda cards: None),
        ('Royal Flush', lambda cards: None),
        # Раскомментить, если играть с джокерами
        # ('Poker', lambda cards:None)
    ]

    def __init__(self):
        self.deck = Deck()
        self.is_running = True
        self.player_1 = None
        self.player_2 = None
        self.display_cards = None
        self.winner = None
        self.flush_count = 0

    def run(self):
        p1_name = input('Введите имя первого игрока:')
        p2_name = input('Введите имя второго игрока:')
        self.player_1 = Hand(p1_name)
        self.player_2 = Hand(p2_name)
        self.display_cards = Hand(None)
        while self.is_running:
            self.__game_loop()
        print('Выиграл игрок', self.winner)

    def __game_loop(self):
        if self.flush_count >= PokerGame.G_MAX_FLUSH_COUNT:
            # Check combos
            # Determine the winner
            self.winner = ''
            self.is_running = False
            return None
        if self.flush_count == 0:
            self.deck.give_cards(self.player_1, 2)
            self.deck.give_cards(self.player_2, 2)
            self.__add_new_card_to_table(3)
        elif self.flush_count < PokerGame.G_MAX_FLUSH_COUNT:
            self.__add_new_card_to_table()

        print('Ход', self.flush_count + 1)
        print(self.display_cards)
        print(self.player_1)
        print(self.player_2)
        self.flush_count += 1

    def __add_new_card_to_table(self, count=1):
        # По правилам берем из колоды две карты, одну откладываем в сторону, вторую кладем на стол
        for i in range(0, count):
            self.deck.give_cards()
            self.deck.give_cards(self.display_cards)


game = PokerGame()
game.run()
