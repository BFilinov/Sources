from Task14_Filinach import app

db = app.db


class Post(db.Model):
    __tablename__ = 'blog_post'

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    image = db.Column('IMAGE', db.LargeBinary)
    title = db.Column('TITLE', db.String(1000))
    body = db.Column('BODY', db.String(4000))

    def __init__(self):
        self.image_base64 = str(self.image)
