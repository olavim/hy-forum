import os
import bcrypt
from flask import Blueprint, request, redirect, url_for, render_template, abort
from flask_login import current_user, login_required
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
from ..decorators.auth import require_permission

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.route('/', methods=['GET'])
@mod.route('/users', methods=['GET'])
@login_required
@require_permission('roles:manage')
def users():
	search_users_form = SearchUsersForm(request.form)
	query = User.query.order_by(User.username)

	if request.args.get('search'):
		search = '%{}%'.format(request.args.get('search'))
		query = query.filter(User.username.like(search))

	users = query.all()

	return render_template('admin/users.html', search_users_form=search_users_form, users=users)

@mod.route('/roles', methods=['GET'])
@login_required
@require_permission('roles:manage')
def roles():
	search_roles_form = SearchRolesForm(request.form)
	delete_role_form = DeleteRoleForm(request.form)

	query = Role.query.order_by(Role.name)

	if request.args.get('search'):
		search = '%{}%'.format(request.args.get('search'))
		query = query.filter(Role.name.like(search))

	roles = query.all()

	return render_template('admin/roles.html', search_roles_form=search_roles_form, delete_role_form=delete_role_form, roles=roles)

@mod.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@require_permission('roles:manage')
def edit_user(id):
	user = User.query.get(id)

	if not user:
		abort(404)

	if user.has_role('admin'):
		abort(403)

	form = UserForm(request.form)

	if form.validate_on_submit():
		user.username = form.username.data
		db.session().commit()

	role_form = UserRoleForm(request.form)
	delete_role_form = DeleteUserRoleForm(request.form)
	return render_template('admin/edit_user.html', user=user, form=form, role_form=role_form, delete_role_form=delete_role_form)

@mod.route('/users/<int:id>/roles/add', methods=['POST'])
@login_required
@require_permission('roles:manage')
def add_user_role(id):
	user = User.query.get(id)

	if not user:
		abort(404)

	if user.has_role('admin'):
		abort(403)

	form = UserRoleForm(request.form)

	if form.validate_on_submit():
		role = Role.query.filter_by(name=form.role.data).first()

		if role.name == 'admin':
			abort(403)

		user.roles.append(role)
		db.session().commit()

	return redirect(url_for('admin.edit_user', id=id))

@mod.route('/users/<int:id>/roles/<int:role_id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
def delete_user_role(id, role_id):
	user = User.query.get(id)
	role = next((r for r in user.roles if r.id == role_id), None)

	if not user or not role:
		abort(404)

	if user.has_role('admin') or role.name == 'admin':
		abort(403)

	user.roles.remove(role)
	db.session().commit()

	return redirect(url_for('admin.edit_user', id=id))

@mod.route('/roles/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@require_permission('roles:manage')
def edit_role(id):
	role = Role.query.get(id)

	if not role:
		abort(404)

	if role.name == 'admin':
		abort(403)

	form = RoleForm(request.form)

	if form.validate_on_submit():
		role.name = form.name.data
		db.session().commit()

	permission_form = RolePermissionForm(request.form)
	delete_permission_form = DeleteRolePermissionForm(request.form)
	return render_template('admin/edit_role.html', role=role, form=form, permission_form=permission_form, delete_permission_form=delete_permission_form)

@mod.route('/roles/<int:id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
def delete_role(id):
	role = Role.query.get(id)

	if not role:
		abort(404)

	if role.name == 'admin':
		abort(403)

	db.session().delete(role)
	db.session().commit()

	return redirect(url_for('admin.roles'))

@mod.route('/roles/<int:id>/permissions/add', methods=['POST'])
@login_required
@require_permission('roles:manage')
def add_role_permission(id):
	role = Role.query.get(id)

	if not role:
		abort(404)

	if role.name == 'admin':
		abort(403)

	form = RolePermissionForm(request.form)

	if form.validate_on_submit():
		permission = Permission.query.filter_by(permission=form.permission.data).first()
		role.permissions.append(permission)
		db.session().commit()

	return redirect(url_for('admin.edit_role', id=id))

@mod.route('/roles/<int:id>/permissions/<int:permission_id>/delete', methods=['POST'])
@login_required
@require_permission('roles:manage')
def delete_role_permission(id, permission_id):
	role = Role.query.get(id)
	permission = next((p for p in role.permissions if p.id == permission_id), None)

	if not role or not permission:
		abort(404)

	if role.name == 'admin':
		abort(403)

	role.permissions.remove(permission)
	db.session().commit()

	return redirect(url_for('admin.edit_role', id=id))

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
