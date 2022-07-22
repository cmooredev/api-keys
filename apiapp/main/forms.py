from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Regexp, Length

class MyForm(FlaskForm):
    server_id = StringField('Server ID', validators=[DataRequired(),
                Regexp(regex=r'^[0-9]*$', message='Numbers only'),
                Length(min=18, max=18, message="Server IDs are usually 18 digits.")
                ])
