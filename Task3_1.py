# 1. Проверка строк с помощью фильтров
import re

# Словари и регулярки
r_en = range(ord('a'), ord('z'))
r_ru = range(ord('а'), ord('я'))
ex_en = '[A-z]+'
ex_ru = '[А-я]+'


# Функция, проверяющая, является ли строка панграммой (все символы из одного алфавита)
def is_full_alphabet_match(s_input):
    return bool(re.match(ex_en, s_input)) or bool(re.match(ex_ru,s_input))


# Преобразует строку в отсортированный массив символов по коду
def get_sorted_set_map(s_input):
    return sorted(set(map(lambda c: ord(c), s_input.lower())))


# Обратная операция: преобразует массив чисел в массив символов
def get_sorted_char_map(l_input):
    return sorted(map(lambda i: chr(i), l_input))


# Высчитывает количество символов, необходимых до полного включения всех букв из алфавита
def get_alphabet_count(s_input = ''):
    a_chars = get_sorted_set_map(s_input)
    if bool(re.match(ex_en, s_input)):
        r_target_range = r_en
    elif bool(re.match(ex_ru,s_input)):
        r_target_range = r_ru
    else:
        return None
    a_filtered = filter(lambda c: c not in a_chars, r_target_range)
    return list(get_sorted_char_map(a_filtered))


x1 = 'The quick brown fox jumped over the lazy dog' # => 's'
x2 = 'Съешь же ещё этих мягких французских булок да выпей чаю' # => []
x3 = 'Lorem ipsum dolor sit amet' # => ['b', 'c', 'f', 'g', 'h', 'j', 'k', 'n', 'q', 'v', 'w', 'x', 'y']
x4 = 'Hello World' # => ['a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'u', 'v', 'x', 'y']

print(is_full_alphabet_match(x1))
print(is_full_alphabet_match(x2))
print(is_full_alphabet_match(x3))
print(is_full_alphabet_match(x4))

print(get_alphabet_count(x1))
print(get_alphabet_count(x2))
print(get_alphabet_count(x3))
print(get_alphabet_count(x4))
