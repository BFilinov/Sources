from SeaBattle import Player
from ast import literal_eval


class Game(object):
    def __init__(self):
        self.use_ai = False
        self.player_1 = None
        self.player_2 = None
        self.next_move_player = None
        self.loop_count = 0

    def enable_ai(self):
        self.use_ai = True

    def start(self):
        self.player_1 = Player.Player(player_name="player1")
        self.player_2 = Player.AIPlayer() if self.use_ai else Player.Player("player2")
        self.player_1.initialize_player()
        self.player_2.initialize_player()
        while self.player_1.is_alive() and self.player_2.is_alive():
            self._game_loop()
        print('Game complete on {} loops'.format(self.loop_count))

    def _game_loop(self):
        if self.next_move_player is None:
            self.next_move_player = self.player_1
        target = self.player_2 if self.player_1 == self.next_move_player else self.player_1
        if not self.next_move_player.is_ai:
            point = literal_eval(input('Ход игрок ' + self.next_move_player.player_name))
        else:
            point = None
        move_code, out_point = self.next_move_player.move(point, target)
        print(out_point)
        move_code_str = Player.G_HIT_CODE[move_code]
        print(move_code_str)
        if move_code == Player.G_HIT_CODE_MISS:
            self.next_move_player = target
        self.loop_count += 1
