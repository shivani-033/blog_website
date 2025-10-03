from flask_wtf import FlaskForm
from wtforms import TextAreaField , SubmitField ,PasswordField
from wtforms.validators import DataRequired , Length

class RegistrationForm(FlaskForm):
    username = TextAreaField('enter username',  validators=[DataRequired() , Length(5)])
    password = PasswordField('enter password',  validators=[DataRequired() , Length( min=5)])
    submit = SubmitField('sign up')
    
class LoginForm(FlaskForm):
    password = PasswordField('enter password',  validators=[DataRequired() , Length( min=5)])
    submit = SubmitField('login')