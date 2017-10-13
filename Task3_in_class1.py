# 1
import random


def throw_random_exception():
    v_random = round(random.random()*100 % 3)
    print(v_random)
    d_exceptions = [NameError, RuntimeError, TypeError]
    try:
        raise d_exceptions[v_random]('Throw exception')
    except NameError:
        print('Ошибка имени')
    except RuntimeError:
        print('Рантайм полетел')
    except TypeError:
        print('Type mismatch')
    finally:
        print('Stream.Close()')

throw_random_exception()

