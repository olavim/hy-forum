from flask_wtf import FlaskForm
from wtforms import validators, TextField, SubmitField

class TopicForm(FlaskForm):
	title = TextField('Title', [validators.required(), validators.length(4, 50)])
	description = TextField('Description', [validators.required(), validators.length(4, 80)])

class DeleteTopicForm(FlaskForm):
	submit = SubmitField('Delete', [validators.required()])
