import re

# Задание 1 (простое)


def exec_task1():
    # Вложенная функция. Вопрос задается в цикле, пока не будет дан правильный ответ

    def loop_question_input(question):
        v_answer = input(question['value'])
        while v_answer != question['answer']:
            v_answer = input('Ответ неправильный! Повторите ввод:\n{}: '.format(question['value']))
        print('Правильно!')

    # Массив вопросов
    a_questions = [
        {
            'value': 'В чем смысл жизни?',
            'answer': '42'
        },
        {
            'value': 'Какого числа Гагарин полетел в космос?',
            'answer': '12.04'
        },
        {
            'value': 'Какая версия Python используется в данный момент?',
            'answer': '3.6.2'
        }]
    for q in a_questions:
        loop_question_input(q)
    print('OK')

# Задание 2 (сложное)


def exec_task2():
    CONST_ZERO_DIVISION_EXCEPTION = 'На ноль делить нельзя!'

    CONST_STATE_L_OPERAND = 0
    CONST_STATE_OPERATOR = 1
    CONST_STATE_R_OPERAND = 2

    # Представление арифметических операций в виде функций

    def m_plus(x1, x2):
        return x1 + x2

    def m_minus(x1, x2):
        return x1 - x2

    def m_multiply(x1, x2):
        return x1 * x2

    def m_divide(x1, x2):
        if x2 == 0:
            return CONST_ZERO_DIVISION_EXCEPTION
        return x1 / x2

    # Представляем операторы в виде словаря
    d_operator_func = {'+': m_plus, '-': m_minus, '*': m_multiply, '/': m_divide}
    # Список доступных приглашений для юзера в зависимости от состояния
    d_prompt = {CONST_STATE_L_OPERAND: 'левый операнд',
                CONST_STATE_OPERATOR: 'оператор',
                CONST_STATE_R_OPERAND: 'правый операнд'}
    # Переменные, используемые для выполнения действий
    v_operand_left = None
    v_operand_right = None
    v_operator = None
    v_state = CONST_STATE_L_OPERAND
    while True:
        v_input = input('Введите {}:'.format(d_prompt[v_state]))
        # Парсим ввод с помощью регулярок
        b_is_numeric = bool(re.match('^-?\d+\.?\d*$', v_input))
        b_is_operator = bool(re.match('^[+\-*/]$', v_input))
        b_is_terminator = v_input == '' or v_input is None
        b_is_reset = v_input.upper() == 'C'
        # Нечто вроде машины состояний. Вводим последовательно числа и операторы
        if b_is_terminator:
            break
        if b_is_reset:
            v_state = CONST_STATE_L_OPERAND
            print('0')
            continue
        if not b_is_numeric and not b_is_operator:
            print('Некорректный ввод')
            continue
        if v_state == CONST_STATE_L_OPERAND:
            if b_is_numeric:
                v_operand_left = float(v_input)
                v_state = CONST_STATE_OPERATOR
                continue
            print('Некорректный ввод')
            continue
        if v_state == CONST_STATE_OPERATOR:
            if b_is_operator:
                v_operator = v_input
                v_state = CONST_STATE_R_OPERAND
                continue
            print('Некорректный ввод')
            continue
        if v_state == CONST_STATE_R_OPERAND:
            if b_is_numeric:
                v_operand_right = float(v_input)
            else:
                print('Некорректный ввод')
                continue
        if v_state != CONST_STATE_R_OPERAND:
            print('Что-то пошло не так...')
            continue
        # Вычисляем промежуточный итог и округляем его
        v_intermediate = round(d_operator_func[v_operator](v_operand_left, v_operand_right), 4)
        if v_intermediate == CONST_ZERO_DIVISION_EXCEPTION:
            print(CONST_ZERO_DIVISION_EXCEPTION + '\nПовторите ввод аргументов')
            v_state = CONST_STATE_L_OPERAND
            continue
        print('Промежуточный итог: {}'.format(v_intermediate))
        v_operand_left = v_intermediate
        v_state = CONST_STATE_OPERATOR


# Вызываем оба задания
exec_task1()
exec_task2()
