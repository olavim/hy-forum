from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo

class SearchUsersForm(FlaskForm):
	search = TextField('Search')
