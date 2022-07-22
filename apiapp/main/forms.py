from flask_wtf import FlaskForm
from wtforms.fields import IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    server_id = IntegerField('Server ID', validators=[DataRequired()])
