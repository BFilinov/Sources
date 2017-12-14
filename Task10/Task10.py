from flask import Flask, session, request, redirect, url_for
from flask_session import Session
import random, time

app = Flask(__name__)
app.config.update(DEBUG=True,
                  SECRET_KEY='A859h',
                  WTF_CSRF_ENABLED=False,
                  SESSION_TYPE='filesystem')
Session(app)
G_KEY_NAME = 'KeyNumber'


def measure_exec_time(func):
    def wrapper(*args):
        t_start = time.time()
        func_value = func(*args)
        t_end = time.time()
        delta = round((t_end - t_start) * 1000)
        print('{} was executed for: {} sec'.format(func, delta))
        return func_value

    return wrapper


def suppress_exceptions(func):
    def wrapper(*args):
        func_value, code = '', 200
        try:
            func_value = func(*args)
        except BaseException as be:
            print('Исключение при выполнении {}: {}'.format(func.__name__, be))
            code = 500
        finally:
            return func_value, code

    return wrapper


@app.route('/', methods=['GET', 'POST'])
def home():
    @measure_exec_time
    def wrapper():
        if session.get(G_KEY_NAME) is None:
            session[G_KEY_NAME] = random.randint(1, 1000)
        response = 'Число загадано'
        if app.debug:
            response += ': %s' % session[G_KEY_NAME]
        return response

    return wrapper()


@app.route('/guess/<number>', methods=['POST'])
def guess(number):
    @suppress_exceptions
    @measure_exec_time
    def wrapper():
        session_number = session.get(G_KEY_NAME)
        if session_number is None:
            return 'Число не было загадано'
        num_number = int(number)
        if num_number == session_number:
            return 'Угадал!'
        elif num_number < session_number:
            return 'Мое число больше'
        else:
            return 'Мое число меньше'

    return wrapper()


@app.route('/restart', methods=['GET', 'POST'])
def restart():
    @measure_exec_time
    def wrapper():
        session[G_KEY_NAME] = None
        if request.method == 'POST':
            return 'Число сброшено'
        elif request.method == 'GET':
            return redirect(url_for('home'), 302)
        else:
            return 'Некорректный метод', 401

    return wrapper()


app.run()
