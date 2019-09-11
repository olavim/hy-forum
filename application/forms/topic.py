from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class TopicForm(FlaskForm):
	title = TextField('Title', [Required()])
