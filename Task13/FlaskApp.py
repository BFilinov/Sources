from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request


class FlaskAlchemyApp(Flask):
    def __init__(self, name, **kwargs):
        super().__init__(import_name=name)
        super().config.update(**kwargs)
        self.db_context = SQLAlchemy(self)
        self.add_url_rule('/', "local", self._home_get)

    # def home_get(self):
    def _home_get(self):
        return 'HELLO WORLD'


app = FlaskAlchemyApp(DEBUG=True,
                      SQLALCHEMY_DATABASE_URI="Data Source=VOSTOK;User Id=izk_rsm;Password=izk_rsm",
                      SQLALCHEMY_TRACK_MODIFICATIONS=False)
app.run()
