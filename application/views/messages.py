import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..models.thread import Thread
from ..models.message import Message
from ..forms.message import MessageForm, EditMessageForm, DeleteMessageForm

mod = Blueprint('messages', __name__, url_prefix='/topics/<topic_id>/threads/<thread_id>')

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
	topic_id = values.pop('topic_id', None)
	thread_id = values.pop('thread_id', None)
	g.topic = Topic.query.get(topic_id)
	g.thread = Thread.query.get(thread_id)

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/', methods=['GET'])
@mod.route('/messages', methods=['GET'])
def list():
	form = DeleteMessageForm(request.form)
	return render_template('messages/list.html', topic=g.topic, thread=g.thread, messages=g.thread.messages, user=g.user, form=form)

@mod.route('/messages/new', methods=['GET', 'POST'])
def create():
	form = MessageForm(request.form)
	if form.validate_on_submit():
		message = Message(thread_id=g.thread.id, user_id=g.user.id, text=form.text.data)
		db.session().add(message)
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id))

	return render_template('messages/create.html', form=form, topic=g.topic, thread=g.thread, messages=g.thread.messages, user=g.user)

@mod.route('/messages/<id>/delete', methods=['POST'])
def delete(id):
	message = Message.query.get(id)
	db.session().delete(message)
	db.session().commit()

	return redirect(url_for('messages.list', topic=g.topic, thread=g.thread, user=g.user))

@mod.route('/messages/<id>/edit', methods=['GET', 'POST'])
def edit(id):
	message = Message.query.get(id)

	form = EditMessageForm(request.form)

	# Set textarea default value
	form.text.process_data(message.text)

	if form.validate_on_submit():
		message.text = form.text.data
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id))

	return render_template('messages/edit.html', form=form, topic=g.topic, thread=g.thread, user=g.user, message=message)
