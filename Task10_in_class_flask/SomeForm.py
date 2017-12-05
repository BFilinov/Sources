from flask_wtf import FlaskForm
from wtforms import *


class SomeForm(FlaskForm):
    name = StringField(label='Name',
                       validators=[validators.Length(min=1, max=100), validators.required()])
    age = IntegerField(label='Age', validators=[validators.required(), validators.NumberRange(min=18)])
    job = SelectField(label='Job', choices=['it', 'bank', 'hr'])
    csrf_token = HiddenField()
