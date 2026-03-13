from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    file = FileField(
        'File Upload',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], "Only .jpg, .jpeg, or .png files are allowed.")
        ],
        render_kw={"accept": "image/*"},
        description="Upload an image file."
    )
