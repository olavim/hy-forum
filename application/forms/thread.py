from flask_wtf import FlaskForm
from wtforms import validators, TextField, TextAreaField

class ThreadForm(FlaskForm):
	title = TextField('Title', [validators.required(), validators.length(4, 50)])
	text = TextAreaField('Text', [validators.required()])

class EditThreadForm(FlaskForm):
	title = TextField('Title', [validators.required(), validators.length(4, 50)])
