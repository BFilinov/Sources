import time


# 1
def is_palindrome(s):
    from functools import reduce
    s_trim = list(filter(lambda char: char != ' ', s))
    checksum = [ord(s_trim[i]) - ord(s_trim[-i]) for i in range(len(s_trim) // 2)]
    return reduce(lambda x, y: x + y, checksum) == 0


# 2
def func_working_time(func):
    def func_inner(string):
        stamp1 = time.time()
        ret = func(string)
        stamp2 = time.time()
        exec_time = stamp2 - stamp1
        print('Execution complete: {}'.format(exec_time))
        print('Value={}'.format(ret))
        return ret

    return func_inner


# 3
def switch(enabled=True):
    def func_inner_1(func):
        def func_inner_2(string):
            if not enabled:
                return func(string)
            stamp1 = time.time()
            ret = func(string)
            stamp2 = time.time()
            exec_time = stamp2 - stamp1
            print('Execution complete: {}'.format(exec_time))
            print('Value={}'.format(ret))
            return ret

        return func_inner_2

    return func_inner_1


# 4 name decorator
def name_decorator(name):
    def inner(func):
        def wrapper(params):
            print(name)
            func(params)

        return wrapper

    return inner


@name_decorator('S1')
@name_decorator('S2')
@name_decorator('S3')
def test_function(string):
    if len(string) > 5:
        print('Hey I am banana')
    print("And that's all folks")


# decorated = func_working_time(is_palindrome)
# decorated('а роза упала на лапу азора')
# decorated('not a palindrome')
test_function('YoloSwagg')
test_function('Nope')
