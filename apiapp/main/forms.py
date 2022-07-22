from flask_wtf import FlaskForm
from wtfforms import StringField
from wtfforms.validators import DataRequired

class MyForm(FlaskForm):
    server_id = StringField('server_id', validators=[DataRequired()])
