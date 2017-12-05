from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from Task14_Filinach import config, filinach_model, view

app = Flask(__name__, template_folder='./templates')
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home():
    data = filinach_model.Post.query.all()
    return render_template('index.html', posts=data)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'GET':
        return render_template('createPost.html')
    form = view.BlogForm(request.form)
    post = filinach_model.Post(title=form.title, body=form.body, image=form.image)
    db.session.add(post)
    db.session.commit()
    return home()


if __name__ == '__main__':
    db.create_all()
    app.run()
