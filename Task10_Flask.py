# READY

import flask
import io

app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'index'


@app.route('/about')
def about():
    return str(flask.request.args)


@app.route('/<int:p1>/<int:p2>')
def home_with_param(p1, p2):
    return 'sum of {} and {} is {}'.format(p1, p2, p1 + p2)


@app.route('/<string:str1>/<string:str2>')
def home_concat(str1, str2):
    return 'concat is {}'.format(str1 + str2)


@app.route('/str/<string:s1>/<string:s2>')
def home_strlen(s1, s2):
    return s1 if len(s1) > len(s2) else s2


@app.route('/path/<path:path_param>')
def test_path(path_param):
    try:
        stream = io.open(path_param, 'read')
        stream.close()
        return 'File {} exists'.format(path_param)
    except Exception:
        return 'File not exists'


app.run(host='localhost', port=8080)
