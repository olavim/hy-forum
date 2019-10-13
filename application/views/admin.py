import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, render_template, abort
from flask_login import current_user, login_required
from config import page_size
from ..main import db
from ..models.user import User
from ..models.role import Role, Permission
from ..forms.admin import (
	SearchUsersForm,
	SearchRolesForm,
	UserForm,
	RoleForm,
	DeleteRoleForm,
	RolePermissionForm,
	DeleteRolePermissionForm,
	UserRoleForm,
	DeleteUserRoleForm
)
from ..decorators import require_permission, get_non_admin_user, get_resource, paginated

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.route('/', methods=['GET'])
@mod.route('/users', methods=['GET'])
@paginated
@login_required
@require_permission('roles:manage')
def users(page):
	search_users_form = SearchUsersForm(request.form)
	query = User.query.order_by(User.username)

	# Filter users by username if search parameter was provided
	if request.args.get('search'):
		search = '%{}%'.format(request.args.get('search'))
		query = query.filter(User.username.like(search))

	query = query.paginate(page, page_size, False)
	users = query.items
	total = query.total

	return render_template('admin/users.html', search_users_form=search_users_form, users=users, page=page, total=total)

@mod.route('/roles', methods=['GET'])
@paginated
@login_required
@require_permission('roles:manage')
def roles(page):
	search_roles_form = SearchRolesForm(request.form)
	delete_role_form = DeleteRoleForm(request.form)
	query = Role.query.order_by(Role.name)

	# Filter roles by name if search parameter was provided
	if request.args.get('search'):
		search = '%{}%'.format(request.args.get('search'))
		query = query.filter(Role.name.like(search))

	query = query.paginate(page, page_size, False)
	roles = query.items
	total = query.total

	return render_template('admin/roles.html', search_roles_form=search_roles_form, delete_role_form=delete_role_form, roles=roles, page=page, total=total)

@mod.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@require_permission('roles:manage')
@get_non_admin_user()
def edit_user(user):
	form = UserForm(request.form)
	if form.validate_on_submit():
		user.username = form.username.data
		db.session().commit()

	role_form = UserRoleForm(request.form)

	# Get select field choices dynamically
	role_form.role.choices = Role.choices()

	delete_role_form = DeleteUserRoleForm(request.form)
	return render_template('admin/edit_user.html', user=user, form=form, role_form=role_form, delete_role_form=delete_role_form)

@mod.route('/users/<int:id>/roles/add', methods=['POST'])
@login_required
@require_permission('roles:manage')
@get_non_admin_user()
def add_user_role(user):
	form = UserRoleForm(request.form)

	# Get select field choices dynamically
	form.role.choices = Role.choices()

	if form.validate_on_submit():
		role = Role.query.filter_by(name=form.role.data).first()
		user.roles.append(role)
		db.session().commit()

	return redirect(url_for('admin.edit_user', id=user.id))

@mod.route('/users/<int:id>/roles/<int:role_id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
@get_non_admin_user()
def delete_user_role(user, role_id):
	role = next((r for r in user.roles if r.id == role_id), None)

	if not role:
		abort(404)

	user.roles.remove(role)
	db.session().commit()

	return redirect(url_for('admin.edit_user', id=user.id))

@mod.route('/roles/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@require_permission('roles:manage')
@get_resource(Role)
def edit_role(role):
	form = RoleForm(request.form)
	if form.validate_on_submit():
		role.name = form.name.data
		db.session().commit()

	permission_form = RolePermissionForm(request.form)

	# Get select field choices dynamically
	permission_form.permission.choices = Permission.choices()

	delete_permission_form = DeleteRolePermissionForm(request.form)
	return render_template('admin/edit_role.html', role=role, form=form, permission_form=permission_form, delete_permission_form=delete_permission_form)

@mod.route('/roles/<int:id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
@get_resource(Role)
def delete_role(role):
	db.session().delete(role)
	db.session().commit()
	return redirect(url_for('admin.roles'))

@mod.route('/roles/<int:id>/permissions/add', methods=['POST'])
@login_required
@require_permission('roles:manage')
@get_resource(Role)
def add_role_permission(role):
	form = RolePermissionForm(request.form)

	# Get select field choices dynamically
	form.permission.choices = Permission.choices()

	if form.validate_on_submit():
		permission = Permission.query.filter_by(permission=form.permission.data).first()
		role.permissions.append(permission)
		db.session().commit()

	return redirect(url_for('admin.edit_role', id=id))

@mod.route('/roles/<int:id>/permissions/<int:permission_id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
@get_resource(Role)
def delete_role_permission(role, permission_id):
	permission = next((p for p in role.permissions if p.id == permission_id), None)

	if not permission:
		abort(404)

	role.permissions.remove(permission)
	db.session().commit()
	return redirect(url_for('admin.edit_role', id=role.id))

@mod.route('/roles/new', methods=['GET', 'POST'])
@login_required
@require_permission('roles:manage')
def create_role():
	form = RoleForm(request.form)
	if form.validate_on_submit():
		role = Role(name=form.name.data)
		db.session().add(role)
		db.session().commit()
		return redirect(url_for('admin.edit_role', id=role.id))

	return render_template('admin/create_role.html', form=form)
