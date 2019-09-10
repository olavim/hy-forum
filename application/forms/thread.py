from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class ThreadForm(FlaskForm):
	title = TextField('Title', [Required()])
