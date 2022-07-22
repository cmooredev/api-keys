from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Regexp, Length

class MyForm(FlaskForm):
    server_id = StringField('Server ID', validators=[DataRequired(),
                Regexp('^([\s\d]+)$', message='Numbers only', Length(min=5, message="Server IDs are usually 18 digits."))
                ])

    def validate_server(form, field):
        if len(field.data) < 18:
            raise ValidationError("Server ID too short")
        if len(field.data) > 17:
            raise ValidationError("Server ID too long")
