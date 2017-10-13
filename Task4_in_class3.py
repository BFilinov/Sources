# Крестики-нолики
# Человек начинает, играет крестиками
# Компьютер отвечает ноликами
import re
import random


def game():
    game_field = [[None, None, None], [None, None, None], [None, None, None]]
    const_field_range = range(0, 3)

    def apply_move(value, index=(0, 0)):
        game_field[index[0]][index[1]] = value

    def cell_is_empty(index=(0, 0)):
        return game_field[index[0]][index[1]] is None

    def is_field_complete():
        for i in const_field_range:
            for j in const_field_range:
                if game_field[i][j] is None:
                    return False
        return True

    def print_game_field():
        for i in game_field:
            print(i)

    def is_win(value='X'):
        # Горизонтальный обход
        b_win = False
        for i in const_field_range:
            for j in const_field_range:
                b_win &= game_field[i][j] == value
            if b_win:
                return True
            b_win = False
        # Вертикальный обход
        for cell in const_field_range:
            for i in game_field:
                b_win &= i[cell] == value
            if b_win:
                return True
            b_win = False
        # Диагональный обход
        if range_is_win(const_field_range, value) or range_is_win(reversed(const_field_range), value):
            return True
        return False

    def parse_input():
        m_c = re.findall('[0-2]', input('Введите пару координат от 0 до 2:'))
        m_tup = tuple(map(lambda c: int(c), m_c))
        return m_tup

    def range_is_win(p_range, value):
        for i in p_range:
            for j in p_range:
                if game_field[i][j] != value:
                    return False
        return True

    while not is_field_complete():
        c_tup = parse_input()
        while not (cell_is_empty(c_tup)):
            print('Клетка уже занята')
            c_tup = parse_input()
        apply_move('X', c_tup)
        print('Ход компьютера:')
        c_tup = (int(random.random() * 100) % 3, int(random.random() * 10 + 1) % 3)
        while not (cell_is_empty(c_tup)):
            c_tup = (int(random.random() * 100) % 3, int(random.random() * 10 + 1) % 3)
        apply_move('O', c_tup)
        print_game_field()

    if is_win('X'):
        print('Вы выиграли!')
    elif is_win('O'):
        print('Вы проиграли')
    if input('Сыграть еще раз? (Нажмите z)') == 'z':
        game()


game()
