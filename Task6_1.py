import random


class Card(object):
    G_CARD_VALUES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, value=None, suit=None):
        self.numeric_value = value
        string = Card.G_CARD_VALUES.get(value)
        self.value = str(value) if string is None else string
        self.suit = suit

    def __str__(self):
        if self.value is not None:
            return '{} of {}'.format(self.value, self.suit)
        return 'Joker'

    def __hash__(self):
        return '{}_{}'.format(self.suit, self.value)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def convert_to_text(numeric):
        string = Card.G_CARD_VALUES.get(numeric)
        return string if string is not None else str(numeric)


# Колода
class Deck(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if Deck.instance is None:
            Deck.instance = object.__new__(Deck)
        return Deck.instance

    def __init__(self):
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.cards = [Card(val, suit) for val in range(2, 15) for suit in suits]
        random.shuffle(self.cards)

    def __str__(self):
        return '\n'.join(list(map(lambda c: c.__str__(), self.cards)))

    def give_cards(self, hand=None, size=1):
        popped = [self.cards.pop() for i in range(0, size)]
        if hand is not None:
            hand.append_cards(popped)
        return popped


# Набор карт игрока
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

    def __repr__(self):
        return self.name

    def __add__(self, other):
        new_hand = Hand('TMP_' + self.name)
        new_hand.cards_in_hand = self.cards_in_hand + other.cards_in_hand
        return new_hand

    def get_numeric_values(self):
        card_map = map(lambda card: card.numeric_value, self.cards_in_hand)
        return list(card_map)

    def get_suits(self):
        suits = dict()
        for card in self.cards_in_hand:
            val = suits.get(card.suit)
            if val is None:
                val = [1, card.numeric_value]
            else:
                val[0] += 1
                val[1] = max([val[1], card.numeric_value])
            suits[card.suit] = val
        return suits


class Combo(object):
    G_COMBO_KEY_RF = "Royal Flush"
    G_COMBO_KEY_FOK = "Four-of-a-Kind"
    G_COMBO_KEY_SF = "Straight Flush"
    G_COMBO_KEY_FH = "Full House"
    G_COMBO_KEY_S = "Straight"
    G_COMBO_KEY_F = "Flush"
    G_COMBO_KEY_TOK = "Three-of-a-Kind"
    G_COMBO_KEY_TP = "Two Pairs"
    G_COMBO_KEY_NONE = None

    G_COMBO_PRIORITY = {
        G_COMBO_KEY_RF: 999999,
        G_COMBO_KEY_FOK: 100400,
        G_COMBO_KEY_SF: 100300,
        G_COMBO_KEY_FH: 100200,
        G_COMBO_KEY_S: 100100,
        G_COMBO_KEY_F: 100000,
        G_COMBO_KEY_TOK: 900,
        G_COMBO_KEY_TP: 599
    }

    def __init__(self, hand: Hand):
        self.hand = hand

    def get_straight(self, wildcards=0):

        """Checks for a five card straight

        Inputs: list of non-wildcards plus wildcard count
            2,3,4, ... 10, 11 for Jack, 12 for Queen,
            13 for King, 14 for Ace
            Hand can be any length (i.e. it works for seven card games).

        Outputs:  highest card in a five card straight
                  or 0 if not a straight.
            Original list is not mutated.
            Ace can also be a low card (i.e. A2345).

        >>> is_straight([14,2,3,4,5])
        5
        >>> is_straight([14,2,3,4,6])
        0
        >>> is_straight([10,11,12,13,14])
        14
        >>> is_straight([2,3,5], 2)
        6
        >>> is_straight([], 5)
        14
        >>> is_straight([2,4,6,8,10], 3)
        12
        >>> is_straight([2,4,4,5,5], 2)
        6
        """
        set_hand = set(self.hand.get_numeric_values())
        if 14 in set_hand:
            set_hand.add(1)
        for low in (10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
            needed = set(range(low, low + 5))
            if len(needed - set_hand) <= wildcards:
                return low + 4
        return 0

    def get_groups(self, wildcards=0):

        """Checks for pairs, threes-of-a-kind, fours-of-a-kind,
           and fives-of-a-kind

        Inputs: list of non-wildcards plus wildcard count
            2,3,4, ... 10, 11 for Jack, 12 for Queen,
            13 for King, 14 for Ace
            Hand can be any length (i.e. it works for seven card games)
        Output: tuple with counts for each value (high cards first)
            for example (3, 14), (2, 11)  full-house Aces over Jacks
            for example (2, 9), (2, 7)    two-pair Nines and Sevens
        Maximum count is limited to five (there is no seven of a kind).
        Original list is not mutated.

        >>> groups([11,14,11,14,14])
        [(3, 14), (2, 11)]
        >>> groups([7, 9, 10, 9, 7])
        [(2, 9), (2, 7)]
        >>> groups([11,14,11,14], 1)
        [(3, 14), (2, 11)]
        >>> groups([9,9,9,9,8], 2)
        [(5, 9), (2, 8)]
        >>> groups([], 7)
        [(5, 14), (2, 13)]
        """
        result = []
        nums = self.hand.get_numeric_values()
        counts = [(nums.count(v), v) for v in range(2, 15)]
        for c, v in sorted(counts, reverse=True):
            newcount = min(5, c + wildcards)  # Add wildcards upto five
            wildcards -= newcount - c  # Wildcards remaining
            if newcount > 1:
                result.append((newcount, v))
        return result

    # Возвращает масть
    def get_flushes(self):
        flush_groups = self.hand.get_suits()
        for k, v in flush_groups.items():
            if v[0] >= 5:
                return k, v
        return None

    def check_combo_in_hand(self):
        fmt = '{} of {}'
        # Royal flush
        key, suit = self._royal_flush()
        if key != Combo.G_COMBO_KEY_NONE:
            return fmt.format(key, suit), Combo.G_COMBO_PRIORITY[key]
        # Four-of-a-kind
        key, value = self._four_of_a_kind()
        if key != Combo.G_COMBO_KEY_NONE:
            convo = Card.convert_to_text(value)
            return fmt.format(key, convo), Combo.G_COMBO_PRIORITY[key] + value
        # Straight flush
        key, value, suit = self._straight_flush()
        if key != Combo.G_COMBO_KEY_NONE:
            text = ' from ' + Card.convert_to_text(value)
            return fmt.format(key, suit) + text, Combo.G_COMBO_PRIORITY[key] + value
        # Full House
        key, value_pair, value_three = self._full_house()
        if key != Combo.G_COMBO_KEY_NONE:
            text = '{} and {}'.format(Card.convert_to_text(value_three), Card.convert_to_text(value_pair))
            num_priority = value_three + value_pair
            return fmt.format(key, text), Combo.G_COMBO_PRIORITY[key] + num_priority
        # Three of a kind
        key, value = self._three_of_a_kind()
        if key != Combo.G_COMBO_KEY_NONE:
            value_string = Card.convert_to_text(value)
            return fmt.format(key, value_string), Combo.G_COMBO_PRIORITY[key] + value
        # Flush
        key, value, suit = self._flush()
        if key != Combo.G_COMBO_KEY_NONE:
            value_string = Card.convert_to_text(value)
            text = ' from ' + value_string
            return fmt.format(key, suit) + text, Combo.G_COMBO_PRIORITY[key] + value
        # Two pairs
        key, value1, value2 = self._two_pairs()
        if key != Combo.G_COMBO_KEY_NONE:
            text = '{} and {}'.format(Card.convert_to_text(value1), Card.convert_to_text(value2))
            return fmt.format(key, text), Combo.G_COMBO_PRIORITY[key] + value1 + value2

        return None

    def _royal_flush(self):
        sf = self._straight_flush()
        if sf[0] != Combo.G_COMBO_KEY_NONE and sf[2] == 14:
            return Combo.G_COMBO_KEY_RF, 14
        return Combo.G_COMBO_KEY_NONE, None

    def _four_of_a_kind(self):
        groups = self.get_groups()
        for i in groups:
            if i[0] == 4:
                return Combo.G_COMBO_KEY_FOK, i[1]
        return Combo.G_COMBO_KEY_NONE, None

    # Возвращает ключ, значение, масть
    def _straight_flush(self):
        straight = self.get_straight()
        if straight == 0:
            return Combo.G_COMBO_KEY_NONE, None, None
        suits = self.hand.get_suits()
        for k, v in suits.items():
            if v[0] >= 5:
                return Combo.G_COMBO_KEY_RF, k, straight
        return Combo.G_COMBO_KEY_NONE, None, None

    def _three_of_a_kind(self):
        groups = self.get_groups()
        for i in groups:
            if i[0] == 3:
                return Combo.G_COMBO_KEY_TOK, i[1]
        return Combo.G_COMBO_KEY_NONE, None

    def _full_house(self):
        three = self._three_of_a_kind()
        if three[0] == Combo.G_COMBO_KEY_NONE:
            return Combo.G_COMBO_KEY_NONE, None, None
        groups = self.get_groups()
        for i in groups:
            if i[0] == 2:
                return Combo.G_COMBO_KEY_FH, i[1], three[1]
        return Combo.G_COMBO_KEY_NONE, None, None

    def _flush(self):
        flush = self.get_flushes()
        if flush is None:
            return Combo.G_COMBO_KEY_NONE, None, None
        return Combo.G_COMBO_KEY_F, flush[1][1], flush[0]

    def _two_pairs(self):
        groups = self.get_groups()
        ls_pairs = list(filter(lambda k: k[0] == 2, groups))
        if len(ls_pairs) == 2:
            return Combo.G_COMBO_KEY_TP, ls_pairs[0][1], ls_pairs[1][1]
        return Combo.G_COMBO_KEY_NONE, None, None


# Игра в техасский холдем
class PokerGame(object):
    G_MAX_MOVES = 3

    def __init__(self):
        self.deck = Deck()
        self.is_running = True
        self.player_1 = None
        self.player_2 = None
        self.display_cards = None
        self.winner = None
        self.move_count = 0

    def run(self):
        p1_name = input('Введите имя первого игрока:')
        p2_name = input('Введите имя второго игрока:')
        self.player_1 = Hand(p1_name)
        self.player_2 = Hand(p2_name)
        self.display_cards = Hand(None)
        while self.is_running:
            self.__game_loop()
        print(self.winner)

    def __game_loop(self):
        if self.move_count >= PokerGame.G_MAX_MOVES:
            p1_cards_with_table = self.player_1 + self.display_cards
            p2_cards_with_table = self.player_2 + self.display_cards
            combo_checker = Combo(p1_cards_with_table)
            result1 = combo_checker.check_combo_in_hand()
            combo_checker = Combo(p2_cards_with_table)
            result2 = combo_checker.check_combo_in_hand()
            if result1 is None and result2 is None:
                self.winner = None, "Draw"
            elif result1 is not None and result2 is None or result1[1] > result2[1]:
                self.winner = self.player_1, result1[0]
            elif result1 is None and result2 is not None or result2[1] > result1[1]:
                self.winner = self.player_2, result2[0]
            self.is_running = False
            return None
        if self.move_count == 0:
            self.deck.give_cards(self.player_1, 2)
            self.deck.give_cards(self.player_2, 2)
            self.__add_new_card_to_table(3)
        elif self.move_count < PokerGame.G_MAX_MOVES:
            self.__add_new_card_to_table()

        print('Ход', self.move_count + 1)
        print(self.display_cards)
        print(self.player_1)
        print(self.player_2)
        self.move_count += 1

    def __add_new_card_to_table(self, count=1):
        # По правилам берем из колоды две карты, одну откладываем в сторону, вторую кладем на стол
        for i in range(0, count):
            self.deck.give_cards()
            self.deck.give_cards(self.display_cards)


game = PokerGame()
game.run()
