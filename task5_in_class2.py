class Figure:
    from functools import reduce

    def __init__(self, *args):
        self.sides = list(args)

    def __str__(self):
        return 'I am a {}. My perimeter is {} and my square is {}'.format(type(self), self.perimeter(), self.square())

    def perimeter(self):
        pass

    def square(self):
        pass


class Square(Figure):
    def __init__(self):
        super().__init__(1)

    def perimeter(self):
        return super().reduce(lambda a, b: a + b, self.sides)

    def square(self):
        return super().reduce(lambda a, b: a * b, self.sides)


class Rectange(Square):
    def __init__(self):
        super().__init__(2)


class Triangle(Figure):
    def __init__(self):
        super().__init__(3)

    def square(self):
        p = self.perimeter() / 2
        s = (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
        return s


class FourAngle(Figure):
    def __init__(self):
        super().__init__(4)

    def square(self):
        p = self.perimeter() / 2
        s = (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]) * (p - self.sides[3])) ** 0.5
        return s


class ObjectFactory():
    @staticmethod
    def create_object(*args):
        if len(args) == 1:
            return Square(args)
        elif len(args) == 2:
            return Rectange(args)
        elif len(args) == 3:
            return Triangle(args)
        elif len(args) == 4:
            return FourAngle(args)
        else:
            raise ValueError('Некорректное число аргументов: {}'.format(len(args)))


f1 = ObjectFactory.create_object(2)
f2 = ObjectFactory.create_object(2, 3)
f3 = ObjectFactory.create_object(3, 4, 5)
f4 = ObjectFactory.create_object(4, 8, 4, 5)

print(f1)
print(f2)
print(f3)
print(f4)
