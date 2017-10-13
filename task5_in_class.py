class BagBase:
    def __init__(self):
        self.items = []
        self.product_type = None

    def __str__(self):
        return 'I am {} and I hold {} of {}'.format(str(type(self)), len(self.items), self.product_type)

    def put_item(self, item):
        if item.item_type == self.product_type:
            self.items.append(item)
        else:
            print('You can only append items of type {}'.format(self.product_type))

    def put_items(self, items=[]):
        for i in items:
            self.put_item(i)


class Basket(BagBase):
    def __init__(self):
        super().__init__()
        self.product_type = 'apple'


class Avoska(BagBase):
    def __init__(self):
        super().__init__()
        self.product_type = 'orange'


class BigBlackCase(BagBase):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'I AM IRON MAN!!! AND I HOLD {} OBJECTS OF ANY TYPE!!!'.format(len(self.items))

    def put_item(self, item):
        self.items.append(item)


class SomeProduct:
    def __init__(self):
        self.item_type = 'Something'


class Apple(SomeProduct):
    def __init__(self):
        self.item_type = 'apple'


class Orange(SomeProduct):
    def __init__(self):
        self.item_type = 'orange'


bag = Basket()
apple = Apple()
orange = Orange()
bag.put_item(apple)
print(bag)
bag.put_item(orange)

avoska = Avoska()
avoska.put_items([orange, Orange(), Orange(), ])
print(avoska)

black_case = BigBlackCase()
black_case.put_item(apple)
black_case.put_items(avoska.items)
print(black_case)
