import Task6_1


def high_ace(cards):
    aces = list(filter(lambda c: c.name == 'Ace', cards))
    return len(aces) == 1


def two_pairs(cards):
    pass
