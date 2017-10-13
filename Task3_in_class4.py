

# 4
def multiply(p_list):
    v_result = 1
    for i in p_list:
        try:
            v_result *= float(i)
        except BaseException as e:
            return 'Невозможно перемножить: {}\nТекущий результат: {}'.format(e.args,v_result)
    return v_result


l = [10, 20, 0xff, 'ZZZ', 23, -1, '123']
ml = multiply(l)
print(ml)