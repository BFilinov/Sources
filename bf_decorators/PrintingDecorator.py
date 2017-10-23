from bf_decorators import DecoratorBase
import time


class PrintingDecorator(DecoratorBase):
    def __on_before__(self, *args, **kwargs):
        print('I am called before the target method' + super()._method)

    def __on_after__(self, *args, **kwargs):
        print('I am called after the target method: ' + super()._method)

    def __init__(self):
        super().__init__(self.__on_before__, self.__on_after__)


class TimerDecorator(DecoratorBase):
    def __init__(self):
        super().__init__(self.__on_before__, self.__on_after__)
        self.elapsed = None

    def __on_before__(self):
        self.time_start = time.time()

    def __on_after__(self):
        self.elapsed = time.time() - self.time_start
