import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, g, render_template, abort
from flask_login import current_user, login_required
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

@mod.route('/', methods=['GET'])
@mod.route('/messages', methods=['GET'])
def list():
	form = DeleteMessageForm(request.form)
	return render_template('messages/list.html', topic=g.topic, thread=g.thread, messages=g.thread.messages, form=form)

@mod.route('/messages/new', methods=['GET', 'POST'])
@login_required
def create():
	form = MessageForm(request.form)
	if form.validate_on_submit():
		message = Message(thread_id=g.thread.id, user_id=current_user.id, text=form.text.data)
		db.session().add(message)
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id))

	return render_template('messages/create.html', form=form, topic=g.topic, thread=g.thread, messages=g.thread.messages)

@mod.route('/messages/<id>/delete', methods=['POST'])
@login_required
def delete(id):
	message = Message.query.get(id)

	if message.user.id != current_user.id:
		abort(403)

	db.session().delete(message)
	db.session().commit()

	return redirect(url_for('messages.list', topic=g.topic, thread=g.thread))

@mod.route('/messages/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
	message = Message.query.get(id)

	if message.user.id != current_user.id:
		abort(403)

	form = EditMessageForm(request.form)

	# Set textarea default value
	form.text.process_data(message.text)

	if form.validate_on_submit():
		message.text = form.text.data
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id))

	return render_template('messages/edit.html', form=form, topic=g.topic, thread=g.thread, message=message)
