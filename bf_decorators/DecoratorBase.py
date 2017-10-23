import functools, time


class DecoratorBase:
    def __init__(self, on_before=None, on_after=None, enabled=True):
        self.on_before = on_before
        self.on_after = on_after
        self.enabled = enabled

    def __call__(self, f_target):
        self._method = f_target.__name__
        if not self.enabled:
            pass

        @functools.wraps(f_target)
        def wrapper(*args, **kwargs):
            start = time.time()
            if self.on_before is not None:
                self.on_before(*args, **kwargs)
            f_target(args, kwargs)
            if self.on_before is not None:
                self.on_after(*args, **kwargs)
            end = time.time()
            print('Elapsed: %d' % end - start)

        return wrapper
