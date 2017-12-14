from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template

app = Flask(DEBUG=True,
            TEMPLATE_DIR='templates',
            SQLALCHEMY_DATABASE_URI="Data Source=VOSTOK;User Id=izk_rsm;Password=izk_rsm",
            SQLALCHEMY_TRACK_MODIFICATIONS=False)
db = SQLAlchemy(app)


@app.route('/')
def home():
    if request.method == 'POST':
        return 'Home', 200
    return render_template('index.html')


app.run()
