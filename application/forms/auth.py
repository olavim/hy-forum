from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo

class LoginForm(FlaskForm):
	username = TextField('Username', [Required()])
	password = PasswordField('Password', [Required()])

class RegisterForm(FlaskForm):
	username = TextField('Username', [Required()])
	password = PasswordField('Password', [Required()])
	confirm = PasswordField('Repeat Password', [
		Required(),
		EqualTo('password', message='Passwords must match')
	])