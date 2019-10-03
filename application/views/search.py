import os
import bcrypt
from flask import Blueprint, request, url_for, render_template
from ..main import db
from ..models.thread import Thread
from ..models.message import Message
from ..forms.search import SearchForm

mod = Blueprint('search', __name__, url_prefix='/search')

@mod.route('/', methods=['GET', 'POST'])
def search():
	form = SearchForm()
	results = []

	if form.validate_on_submit():
		like_str = '%{}%'.format(form.query.data)

		if form.search_threads.data:
			threads = Thread.query.filter(Thread.title.like(like_str)).limit(10).all()
			for t in threads:
				results.append(dict(type='thread', result=t.title, topic=t.topic, thread=t, user=t.user, timestamp=t.created_at))

		if form.search_messages.data:
			messages = Message.query.filter(Message.text.like(like_str)).limit(10).all()
			for m in messages:
				results.append(dict(type='message', result=m.text, topic=m.thread.topic, thread=m.thread, user=m.user, timestamp=m.created_at))

	return render_template('search/search.html', form=form, results=results)
