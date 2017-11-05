# Кэширующий декоратор
class Cache:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Cache._instance is None:
            Cache._instance = object.__new__(cls)
            Cache._instance._storage = {}
        return Cache._instance

    def __str__(self):
        return str(self._storage)

    def __repr__(self):
        return """Count: {}\nContents:{}""".format(len(self._storage), self._storage)

    def append(self, key, value):
        self._storage[key] = value

    def get_value(self, key):
        get = self._storage.get(key)
        return get

    def merge_storage(self, **kwargs):
        for k, v in kwargs.items():
            get = self.get_value(k)
            if get:
                self._storage[k] = [get, v]
            else:
                self._storage[k] = v


def cached():
    def func_wrapper(func):
        def param_wrapper(*args):
            cache = Cache()
            precached = cache.get_value(args)
            if precached is not None:
                return precached + ' from cache'
            ret = func(*args)
            cache.append(args, ret)
            return ret

        return param_wrapper

    return func_wrapper


@cached()
def test_function(*args):
    agg = ""
    for arg in args:
        agg += str(arg)
    return agg


t1 = test_function('a', 'h', 25, 'gasdg', 'FORM', 'DDAA')
t2 = test_function(1, 2)
t3 = test_function(1, 2)
t4 = test_function(2, 3)
print(t1)
print(t2)
print(t3)
print(t4)
