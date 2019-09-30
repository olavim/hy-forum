import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user, login_required
from ..main import db
from ..models.user import User
from ..models.role import Role, Permission
from ..forms.admin import SearchUsersForm

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.route('/', methods=['GET'])
@mod.route('/users', methods=['GET'])
@login_required
def users():
	search_users_form = SearchUsersForm(request.form)
	query = User.query.order_by(User.username)

	if request.args.get('search'):
		search = '%{}%'.format(request.args.get('search'))
		query = query.filter(User.username.like(search))

	users = query.all()

	return render_template('admin/users.html', search_users_form=search_users_form, users=users)

@mod.route('/users/<id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
	return render_template('admin/edit_user.html')
