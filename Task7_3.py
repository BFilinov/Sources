def check(**kwargs):
    def func_wrapper(func):
        def params_wrapper(**kwargs_inner):
            for p_key, p_value in kwargs_inner.items():
                p_type = kwargs.get(p_key)
                if p_type is None:
                    continue
                if not isinstance(p_value, p_type):
                    raise ValueError('ValueOf={} is supposed to be OfType={}'.format(p_key, p_type))
            func(**kwargs_inner)

        return params_wrapper

    return func_wrapper


@check(param3=(type(None), str, int, tuple))
def test_function(**kwargs):
    print(kwargs)


test_function(param1='ABC', param2="""Lorem ipsum""", param3=None)
test_function(param1=1253123, param2="123512", param3="Hello")
test_function(param2=0xff, param3=3.0)
