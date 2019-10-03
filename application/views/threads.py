import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, g, render_template, abort
from flask_login import current_user, login_required
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..models.thread import Thread
from ..models.message import Message
from ..forms.thread import ThreadForm, EditThreadForm, DeleteThreadForm
from ..decorators.auth import require_permission

mod = Blueprint('threads', __name__, url_prefix='/topics/<topic_id>/threads')

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
	topic_id = values.pop('topic_id', None)
	g.topic = Topic.query.get(topic_id)

	if not g.topic:
		abort(404)

@mod.route('/', methods=['GET'])
def list():
	delete_form = DeleteThreadForm(request.form)
	return render_template('threads/list.html', topic=g.topic, threads=g.topic.threads, delete_form=delete_form)

@mod.route('/<int:id>/delete', methods=['POST'])
@login_required
@require_permission('threads:delete')
def delete(id):
	Thread.query.filter(Thread.id == id).delete()
	db.session().commit()
	return redirect(url_for('threads.list', topic_id=g.topic.id))

@mod.route('/new', methods=['GET', 'POST'])
@login_required
def create():
	form = ThreadForm(request.form)

	if form.validate_on_submit():
		thread = Thread(title=form.title.data, topic_id=g.topic.id, user_id=current_user.id)
		db.session().add(thread)
		db.session().flush()

		message = Message(text=form.text.data, thread_id=thread.id, user_id=current_user.id)
		db.session().add(message)
		db.session().commit()

		return redirect(url_for('messages.list', topic_id=g.topic.id, thread_id=thread.id))

	return render_template('threads/create.html', form=form, topic=g.topic)

@mod.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@require_permission('threads:edit')
def edit(id):
	thread = Thread.query.get(id)

	if not thread:
		abort(404)

	form = EditThreadForm(request.form)

	if form.validate_on_submit():
		thread.title = form.title.data
		db.session().commit()

		return redirect(url_for('threads.list', topic_id=g.topic.id))

	return render_template('threads/edit.html', form=form, topic=g.topic, thread=thread)