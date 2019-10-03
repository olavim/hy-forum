from flask_wtf import FlaskForm
from wtforms import validators, TextAreaField, SubmitField

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.required()])
	submit = SubmitField("Submit")

class EditMessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.required()])
	submit = SubmitField("Save")

class DeleteMessageForm(FlaskForm):
	submit = SubmitField("Delete")
