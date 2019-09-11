from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class MessageForm(FlaskForm):
	text = TextField('Text', [Required()])
