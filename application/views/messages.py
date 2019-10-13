import os
import bcrypt
import math
from sqlalchemy_utc.now import utcnow
from flask import Blueprint, request, redirect, url_for, g, render_template, abort
from flask_login import current_user, login_required
from config import page_size
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..models.thread import Thread, ThreadRead
from ..models.message import Message
from ..forms.message import MessageForm, EditMessageForm, DeleteMessageForm

mod = Blueprint('messages', __name__, url_prefix='/topics/<topic_id>/threads/<thread_id>')

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
	topic_id = values.pop('topic_id', None)
	thread_id = values.pop('thread_id', None)
	g.topic = Topic.query.get(topic_id)
	g.thread = Thread.query.get(thread_id)

	if not g.topic or not g.thread:
		abort(404)

@mod.route('/', methods=['GET'])
@mod.route('/messages', methods=['GET'])
def list():
	page = int(request.args.get('page') or '1')

	message_query = Message.query \
		.filter(Message.thread_id == g.thread.id) \
		.order_by(Message.created_at.asc()) \
		.paginate(page, page_size, False)

	messages = message_query.items
	total = message_query.total

	if current_user.is_authenticated:
		thread_read = ThreadRead.query.get((g.thread.id, current_user.id))

		if not thread_read:
			thread_read = ThreadRead(g.thread.id, current_user.id)
			db.session().add(thread_read)
			db.session().commit()

		thread_read.updated_at = utcnow()
		db.session().commit()

	form = DeleteMessageForm(request.form)
	return render_template('messages/list.html', messages=messages, total=total, page=page, form=form)

@mod.route('/messages/new', methods=['GET', 'POST'])
@login_required
def create():
	form = MessageForm(request.form)
	if form.validate_on_submit():
		message = Message(thread_id=g.thread.id, user_id=current_user.id, text=form.text.data)
		db.session().add(message)
		db.session().commit()

		# Redirect user to last page
		total_messages = Message.query.filter(Message.thread_id == g.thread.id).count()
		last_page = int(math.ceil(total_messages / page_size))

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id, page=last_page))

	return render_template('messages/create.html', form=form, messages=g.thread.messages)

@mod.route('/messages/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
	page = int(request.args.get('page') or '1')
	message = Message.query.get(id)

	if not message:
		abort(404)

	if not current_user.has('messages:delete') and message.user.id != current_user.id:
		abort(403)

	db.session().delete(message)
	db.session().commit()

	return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id, page=page))

@mod.route('/messages/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
	page = int(request.args.get('page') or '1')
	message = Message.query.get(id)

	if not message:
		abort(404)

	if not current_user.has('messages:edit') and message.user.id != current_user.id:
		abort(403)

	form = EditMessageForm(request.form)

	if form.validate_on_submit():
		message.text = form.text.data
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=g.thread.id, page=page))

	# Set textarea default value
	form.text.process_data(message.text)
	return render_template('messages/edit.html', form=form, message=message)
