# Пятнашки
class PyatnashkiGame:
    # PRIVATE:
    def __init__(self):
        self.is_running = True
        self.game_field = list(range(1, 16))

    def __print_game_field__(self):
        r_range = range(0, 4)
        for i in r_range:
            # Распечатываем игровое поле кусками по четыре ячейки
            print(self.game_field[i * 4:(i * 4) + 4])

    def __perform_move__(self, current, delta):
        self.game_field[current] = self.game_field[current - delta]
        self.game_field[current - delta] = None

    def __move__(self, direction=None):
        # Сначала проверка, можно ли двигаться в заданном направлении
        can_move, delta, current = self.__can_move__(direction)
        print('CAN MOVE {}: {}'.format(direction, can_move))
        if not can_move:
            raise ValueError('Такое движение невозможно. Повторите ввод')
        # Если да, то подменяем элементы
        self.__perform_move__(current, delta)

    def __can_move__(self, direction):
        current = self.game_field.index(None)
        if direction == 'left':
            return current - 1 >= 0, 1, current
        elif direction == 'right':
            return current + 1 < len(self.game_field), -1, current
        elif direction == 'up':
            return current - 4 >= 0, 4, current
        elif direction == 'down':
            return current + 4 < len(self.game_field), -4, current
        return False, None

    def __check_win__(self):
        # Условия победы: последний элемент =None И остаток отсортирован
        gf_copy = self.game_field[:-1]
        return gf_copy.count(None) == 0 and tuple(gf_copy) == tuple(sorted(gf_copy))

    def __parse_input__(self):
        command = input('left/right/up/down:')
        try:
            self.__move__(command.lower())
            return True
        except ValueError as e:
            print(e)
            return False

    # PUBLIC:
    def init_game_loop(self):
        while self.is_running:
            self.__print_game_field__()
            if not self.__parse_input__():
                pass
            if self.__check_win__():
                print('Вы победили!')
                self.is_running = False

    def fill_game_field(self):
        import random
        m_range = range(0, 15)
        gf_copy = list(self.game_field)
        for i in m_range:
            if gf_copy[i] is not None:
                gf_copy[i] *= 100
        used_indices = []
        for i in m_range:
            r_cell = int(random.random() * 100) % len(self.game_field)
            while r_cell in used_indices:
                r_cell = int(random.random() * 100) % len(self.game_field)
            gf_copy[i] += self.game_field[r_cell]
            used_indices.append(r_cell)
        for i in m_range:
            if gf_copy[i] is not None:
                gf_copy[i] %= 100
        self.game_field = gf_copy
        self.game_field.append(None)


game = PyatnashkiGame()
game.fill_game_field()
game.init_game_loop()
