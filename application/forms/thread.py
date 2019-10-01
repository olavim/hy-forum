from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField
from wtforms.validators import Required

class ThreadForm(FlaskForm):
	title = TextField('Title', [Required()])
	text = TextAreaField('Text', [Required()])

class EditThreadForm(FlaskForm):
	title = TextField('Title', [Required()])
