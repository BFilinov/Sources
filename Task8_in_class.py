import random


def gen_random():
    while True:
        yield random.randint()


def gen_range(start=0, size=1):
    current = start
    while current < size:
        yield current
        current += 1


def gen_map(expr, collection):
    index = 0
    while index < len(collection):
        current = collection[index]
        yield expr(current)
        index += 1


def gen_enumerate(collection, start=0):
    index = start
    while index < len(collection):
        yield index, collection[index]
        index += 1


def gen_zip(collection1, collection2, start=0):
    index = start
    while index < len(collection1) and index < len(collection2):
        yield (collection1[index], collection2[index])
        index += 1
