from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, FloatField
from wtforms.validators import InputRequired, Email, Length



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class Settings(FlaskForm):
	power = BooleanField('On/Off')
	speed = FloatField('Captures based on time in seconds')
	
