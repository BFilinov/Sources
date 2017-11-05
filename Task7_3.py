def check(**kwargs):
    def func_wrapper(func):
        def params_wrapper(**kwargs_inner):
            for p_key, p_value in kwargs_inner.items():
                p_type = kwargs.get(p_key)
                if p_type is None:
                    continue
                if not isinstance(p_value, p_type):
                    raise ValueError('ValueOf={} is supposed to be OfType={}'.format(p_key, p_type))
            ret = func(**kwargs_inner)
            ret_type = kwargs.get('hresult')
            if not isinstance(ret, ret_type):
                raise ValueError('FuncResult={} is supposed to be OfType={}'.format(ret, ret_type))
            return ret

        return params_wrapper

    return func_wrapper


@check(param3=(type(None), str, int, tuple), hresult=int)
def test_function(**kwargs):
    print(kwargs)
    return 0


test_function(param1='ABC', param2="""Lorem ipsum""", param3=None)
test_function(param1=1253123, param2="123512", param3="Hello")
test_function(param2=0xff, param3=3.0)
