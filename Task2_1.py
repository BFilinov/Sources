# Константы ключей словаря
CONST_KEY_VALUE = 'value'
CONST_KEY_ANSWER = 'answer'
CONST_KEY_MODE = 'mode'

# Константы варианта вопроса
CONST_MODE_ALL = 'all'  # Все ответы либо единственный ответ должны совпасть
CONST_MODE_ANY = 'any'  # Любое количество верных ответов


# Выдает пересекающиеся в двух коллекциях элементы
def intersect(p_array1, p_array2):
    a_result = []
    for i in p_array1:
        if str(i).strip(' ') in p_array2:
            a_result.append(i)
    return a_result


# Вложенная функция.  Вопрос задается в цикле, пока не будет даны
# правильные
# ответы.  Ответы вводятся через точку с запятой
def loop_question_input(question):
    v_answers = str(input(question[CONST_KEY_VALUE])).split(';')
    v_intersect = intersect(v_answers, question[CONST_KEY_ANSWER])
    if question[CONST_KEY_MODE] == CONST_MODE_ALL:
        return len(question[CONST_KEY_ANSWER]) == len(v_intersect)
    elif question[CONST_KEY_MODE] == CONST_MODE_ANY:
        return len(v_answers) > 0
    else:
        return False


# Запускающая функция
def exec_task1():
    # Массив вопросов.  Правильные ответы перечислены кортежами
    a_questions = [{
            CONST_KEY_VALUE: 'В чем смысл жизни?',
            CONST_KEY_ANSWER: ('42','Будда', '0'),
            CONST_KEY_MODE: CONST_MODE_ALL
        },
        {
            CONST_KEY_VALUE: 'Какого числа Гагарин полетел в космос?',
            CONST_KEY_ANSWER: ('12.04', ),
            CONST_KEY_MODE : CONST_MODE_ALL
        },
        {
            CONST_KEY_VALUE: 'Перечислите известные Вам реализации Python',
            CONST_KEY_ANSWER: ('CPython', 'PyPy', 'IronPython', 'Jython'),
            CONST_KEY_MODE : CONST_MODE_ANY
        }]
    for q in a_questions:
        b_correct = loop_question_input(q)
        while not b_correct:
            print('Ответ неправильный! Повторите ввод')
            b_correct = loop_question_input(q)
        print('Правильно!')

exec_task1()