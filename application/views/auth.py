import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from flask_login import current_user, login_required, login_user, logout_user
from ..main import db
from ..models.user import User
from ..forms.auth import RegisterForm, LoginForm

mod = Blueprint('auth', __name__, url_prefix='/')

@mod.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()

		if user and bcrypt.checkpw(form.password.data.encode('utf8'), user.password_hash.encode('utf8')):
			login_user(user)
			return redirect(url_for('topics.list'))

		flash('Wrong username or password', 'error-message')

	return render_template('auth/login.html', form=form)

@mod.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		password_hash = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt())
		user = User(form.username.data, password_hash.decode('utf8'))
		db.session().add(user)
		db.session().commit()

		login_user(user)
		return redirect(url_for('topics.list'))

	return render_template('auth/register.html', form=form)

@mod.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('topics.list'))
