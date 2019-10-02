from flask_wtf import FlaskForm
from wtforms import validators, TextAreaField, SubmitField

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.required()])
	submit = SubmitField("Create")

class EditMessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.required()])
	submit = SubmitField("Edit")

class DeleteMessageForm(FlaskForm):
	submit = SubmitField("Delete")
