import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, g, render_template, abort
from ..decorators import require_permission, get_resource
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..forms.topic import TopicForm, EditTopicForm, DeleteTopicForm

mod = Blueprint('topics', __name__, url_prefix='/')

@mod.route('/', methods=['GET'])
@mod.route('/topics', methods=['GET'])
def list():
	topics = Topic.query.all()
	delete_form = DeleteTopicForm(request.form)
	return render_template('topics/list.html', topics=topics, delete_form=delete_form)

@mod.route('/topics/<int:id>/delete', methods=['POST'])
@require_permission('topics:delete')
@get_resource(Topic)
def delete(topic):
	Topic.query.filter(Topic.id == topic.id).delete()
	db.session().commit()
	return redirect(url_for('topics.list'))

@mod.route('/topics/new', methods=['GET', 'POST'])
@require_permission('topics:create')
def create():
	form = TopicForm(request.form)
	if form.validate_on_submit():
		topic = Topic(title=form.title.data, description=form.description.data)
		db.session().add(topic)
		db.session().commit()

		return redirect(url_for('topics.list'))

	return render_template('topics/create.html', form=form)

@mod.route('/topics/<int:id>/edit', methods=['GET', 'POST'])
@require_permission('topics:edit')
@get_resource(Topic)
def edit(topic):
	form = EditTopicForm(request.form)
	if form.validate_on_submit():
		topic.title = form.title.data
		topic.description = form.description.data
		db.session().commit()

		return redirect(url_for('topics.list'))

	return render_template('topics/edit.html', form=form, topic=topic)