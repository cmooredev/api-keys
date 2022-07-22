from flask_wtf import FlaskForm
from wtforms.fields import IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    server_id = IntegerField('Server ID', validators=[DataRequired(),
                Regexp('^([\s\d]+)$', message='Numbers only')
                ])

    def validate_server(form, field):
        if len(field.data) < 18:
            raise ValidationError("Server ID too short")
        if len(field.data) > 17:
            raise ValidationError("Server ID too long")
