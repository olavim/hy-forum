import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from ..main import db
from ..models.user import User
from ..forms.auth import RegisterForm, LoginForm

mod = Blueprint('auth', __name__, url_prefix='/')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.checkpw(form.password.data.encode('utf8'), user.password_hash.encode('utf8')):
			session['user_id'] = user.id
			return redirect(url_for('topics.list'))
		flash('Wrong username or password', 'error-message')

	return render_template("auth/login.html", form=form)

@mod.route('/logout', methods=['GET', 'POST'])
def logout():
	session.clear()
	return redirect(url_for('topics.list'))

@mod.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		password_hash = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt())
		user = User(form.username.data, password_hash)
		db.session().add(user)
		db.session().commit()

		session['user_id'] = user.id
		flash('Thanks for registering')
		return redirect(url_for('topics.list'))

	return render_template("auth/register.html", form=form)
