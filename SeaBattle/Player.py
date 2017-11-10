import json, abc, functools, random
from SeaBattle import Ship

G_MAX_SHIP_SIZE_COUNTS = [
    (4, 1),
    (2, 3),
    (3, 2),
    (1, 4)
]

G_HIT_CODE_MISS = 0
G_HIT_CODE_HIT = 1
G_HIT_CODE_DEAD = 2
G_HIT_CODE_ERROR = 3
G_HIT_CODE = {G_HIT_CODE_MISS: "Miss", G_HIT_CODE_HIT: "Hit", G_HIT_CODE_DEAD: "Dead", G_HIT_CODE_ERROR: "Repeat"}


class UserException(BaseException):
    pass


class AbstractPlayer(abc.ABC):
    def __init__(self, player_name):
        self.player_name = player_name
        self.ships = []
        self.hit_points = []
        self.is_ai = False

    @abc.abstractmethod
    def initialize_player(self):
        pass

    def move(self, point, player):
        if point in self.hit_points:
            return G_HIT_CODE_ERROR, point
        self.hit_points.append(point)
        for ship in player.ships:
            if ship.point_in_range(point):
                ship.damage.append(point)
                if ship.is_alive():
                    return G_HIT_CODE_HIT, point
                return G_HIT_CODE_DEAD, point
        return G_HIT_CODE_MISS, point

    def is_alive(self):
        alive_ships = list(map(lambda ship: ship.is_alive(), self.ships))
        is_alive = functools.reduce(lambda prev, current: prev or current, alive_ships)
        return is_alive

    def __repr__(self):
        fmt = '{name}\n{ships}'
        ships = '\n'.join(list(map(lambda x: x.__repr__(), self.ships)))
        return fmt.format(name=self.player_name, ships=ships)

    def check_ships(self):
        sizes = list(map(lambda s: s.size, self.ships))
        groups = [(s, sizes.count(s)) for s in set(sizes)]
        for g in groups:
            if g[1] > Player.G_MAX_SHIP_SIZE_COUNTS[g[0]]:
                raise UserException()


class Player(AbstractPlayer):
    def initialize_player(self):
        settings_file_name = './SeaBattle/{player_name}.json'.format(player_name=self.player_name)
        try:
            fs = open(settings_file_name)
            try:
                obj = json.load(fs)
                ships = obj['ships']
                self.ships = [Ship.Ship(ship['size'], ship['direction'], ship['location']) for ship in ships]
            except BaseException as e:
                print('Failed to parse player settings', e)
            finally:
                fs.close()
        except IOError as e:
            print('Failed to load player settings', e)


class AIPlayer(AbstractPlayer):
    def __init__(self):
        super().__init__('player2')
        self.rnd = random.randint
        self.prev_hits = []
        self.is_ai = True

    def initialize_player(self):
        self.ships.append(Ship.Ship(4, 'v', (3, 7)))

    def _check_neighbor_cell(self, point_a, point_b):
        pass

    def _get_empty_location(self):
        point = (0, 0)
        while point in self.hit_points:
            point = (self.rnd(0, 8), self.rnd(0, 8))
        return point

    def move(self, point, player):
        point = self._get_empty_location()
        code, point = super().move(point, player)
        if code == G_HIT_CODE_DEAD:
            self.prev_hits = []
        else:
            self.prev_hits.append(point)
        return code, point
