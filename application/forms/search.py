from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, BooleanField, HiddenField

class SearchForm(FlaskForm):
	query = StringField('Query', [validators.required()])
	search_threads = BooleanField('Threads', default='checked')
	search_messages = BooleanField('Messages', default='checked')
	submit = SubmitField('Search', [validators.optional()])

class QuickSearchForm(FlaskForm):
	query = StringField('Query', [validators.required()])
	search_threads = HiddenField('Threads', default='checked')
	search_messages = HiddenField('Messages', default='checked')
	submit = SubmitField('Search', [validators.optional()])
