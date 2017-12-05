from flask import Flask, request, render_template
from Task10_in_class_flask import SomeForm
from flask_wtf import csrf


def get_application():
    app = Flask(__name__)
    app.secret_key = 'xtdD41Ccacdrc'
    csrf.CSRFProtect(app)

    @app.route('/', methods=['GET'])
    def home_get():
        return render_template('view.html')

    @app.route('/', methods=['POST'])
    def home_post():
        mvt_form = SomeForm.SomeForm(request.form)
        return render_template('view.html', mvt_form.name, mvt_form.age, mvt_form.job, app.secret_key)

    return app
