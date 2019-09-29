import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from ..main import db
from ..models.user import User
from ..models.topic import Topic
from ..forms.topic import TopicForm

mod = Blueprint('topics', __name__, url_prefix='/')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/', methods=['GET'])
@mod.route('/topics', methods=['GET'])
def list():
	topics = Topic.query.all()
	return render_template('topics/list.html', user=g.user, topics=topics)

@mod.route('/topics/<id>', methods=['DELETE'])
def delete(id):
	topic = Topic.query.get(id)
	db.session().delete(topic)
	db.session().commit()

	return redirect(url_for('topics.list'))

@mod.route('/topics/new', methods=['GET', 'POST'])
def create():
	form = TopicForm(request.form)
	if form.validate_on_submit():
		topic = Topic(title=form.title.data, description=form.description.data)
		db.session().add(topic)
		db.session().commit()

		return redirect(url_for('topics.list'))

	return render_template('topics/create.html', form=form, user=g.user)

@mod.route('/topics/<id>/edit', methods=['GET', 'POST'])
def edit(id):
	topic = Topic.query.get(id)

	form = TopicForm(request.form)
	if form.validate_on_submit():
		topic.title = form.title.data
		topic.description = form.description.data
		db.session().commit()

		return redirect(url_for('topics.list'))

	return render_template('topics/edit.html', form=form, topic=topic, user=g.user)