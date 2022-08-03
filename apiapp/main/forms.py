from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Regexp, Length

class MyForm(FlaskForm):
    server_id = StringField('Server ID', validators=[DataRequired(),
                Regexp(regex=r'^[0-9]*$', message='Numbers only'),
                Length(min=17, max=20, message="Server IDs are usually 18-19 digits.")
                ])
