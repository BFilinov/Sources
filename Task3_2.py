# 2. Поле чудес
CONST_CHAR_PLACEHOLDER = '_ '
d_word_chars = {}


# Конвертирует строку в структуру хранения {Индекс: [Символ, Символ угадан]}
def convert_string_to_char_dict(p_str):
    i = 0
    d = {}
    for c in p_str:
        d[i] = [c, False]
        i += 1
    return d


# Обновляет статус угаданности символа
def update_char_status(p_char):
    for k, v in d_word_chars.items():
        if v[0].lower() == p_char.lower():
            v[1] = True


# Собирает отображаемую на экране угаданную строку: p y t _ _ n
def get_guessed_string():
    s_result = ''
    for k, v in d_word_chars.items():
        if v[1]:
            s_result += v[0] + ' '
        else:
            s_result += CONST_CHAR_PLACEHOLDER
    return s_result


# Признак того, что все символы угаданы
def is_finished():
    a_filtered = [k for k, v in d_word_chars.items() if v[1]]
    return len(a_filtered) == len(d_word_chars)


w_target_word = input('Введите слово, которое будете отгадывать:').lower()
i_word_length = len(w_target_word)
# Структура такая: {Индекс: [Символ, Угадали или нет]}
d_word_chars = convert_string_to_char_dict(w_target_word)
while not is_finished():
    v_input = input('Введите букву:').lower()
    if len(v_input) != 1:
        print('Разрешается вводить не более одной буквы')
        pass
    if v_input in w_target_word:
        print('Правильно!')
        update_char_status(v_input)
        print(get_guessed_string())

print(get_guessed_string)
