class Ship(object):
    class LocationException(Exception):
        pass

    def __init__(self, size=1, direction='', location=(0, 0)):
        self.size = size
        self.direction = direction
        self.location = location
        self.damage = []

    def __repr__(self):
        fmt = 'Ship of size={size} located at {location} {direction} is {alive}'
        direction = 'vertically' if self.direction == 'v' else 'horizontally'
        alive = 'alive' if self.is_alive() else 'dead'
        return fmt.format(size=self.size, location=self.location, direction=direction, alive=alive)

    def __str__(self):
        return self.__repr__()

    def __and__(self, other):
        return self.is_alive() and other

    def __rand__(self, other):
        return self.__and__(other)

    def __hash__(self):
        return self.size * ord(self.direction[0]) + self.location[0] + self.location[1]

    def is_alive(self):
        return len(self.damage) < self.size

    def point_in_range(self, point):
        m_range = list(self.get_range())
        return point in m_range

    def get_range(self):
        index = 0
        while index < self.size:
            if self.direction == 'v':
                yield (self.location[0], self.location[1] + index)
            elif self.direction == 'h':
                yield (self.location[0] + index, self.location[1])
            else:
                raise Ship.LocationException('Unconfirmed direction of ship {}'.format(self.__repr__()))
            index += 1
