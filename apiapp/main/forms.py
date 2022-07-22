from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    server_id = StringField('server_id', validators=[DataRequired()])
