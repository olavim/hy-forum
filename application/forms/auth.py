from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField
from .validators import alnum, username_available, role_name_available

class LoginForm(FlaskForm):
	username = StringField('Username', [validators.required()])
	password = PasswordField('Password', [validators.required()])

class RegisterForm(FlaskForm):
	username = StringField('Username', [validators.required(), validators.length(4, 16), alnum, username_available])
	password = PasswordField('Password', [validators.required(), validators.length(4)])
	confirm = PasswordField('Repeat Password', [
		validators.required(),
		validators.equal_to('password', message='Passwords must match')
	])