import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..models.thread import Thread
from ..models.message import Message
from ..forms.thread import ThreadForm

mod = Blueprint('threads', __name__, url_prefix='/topics/<topic_id>/threads')

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
	topic_id = values.pop('topic_id', None)
	g.topic = Topic.query.get(topic_id)

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/', methods=['GET'])
def list():
	return render_template('threads/list.html', topic=g.topic, threads=g.topic.threads, user=g.user)

@mod.route('/<id>', methods=['DELETE'])
def delete(id):
	thread = Thread.query.get(id)
	db.session().delete(thread)
	db.session().commit()

	return redirect(url_for('threads.list', topic_id=g.topic.id))

@mod.route('/new', methods=['GET', 'POST'])
def create():
	form = ThreadForm(request.form)
	if form.validate_on_submit():
		thread = Thread(title=form.title.data, topic_id=g.topic.id, user_id=g.user.id)
		db.session().add(thread)
		db.session().flush()

		message = Message(text=form.text.data, thread_id=thread.id, user_id=g.user.id)
		db.session().add(message)
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=thread.id))

	return render_template('threads/create.html', form=form, user=g.user, topic=g.topic)