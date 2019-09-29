from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [Required()])
	submit = SubmitField("Create")

class EditMessageForm(FlaskForm):
	text = TextAreaField('Text', [Required()])
	submit = SubmitField("Edit")

class DeleteMessageForm(FlaskForm):
	submit = SubmitField("Delete")
