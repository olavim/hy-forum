from flask_wtf import FlaskForm
from wtforms import validators, TextField

class TopicForm(FlaskForm):
	title = TextField('Title', [validators.required(), validators.length(4, 50)])
	description = TextField('Description', [validators.required(), validators.length(4, 80)])
