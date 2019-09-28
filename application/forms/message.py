from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Required

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [Required()])

class EditMessageForm(FlaskForm):
	text = TextAreaField('Text', [Required()])
