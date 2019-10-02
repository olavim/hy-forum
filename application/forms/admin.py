from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SelectField, FieldList, FormField, SubmitField
from ..models.role import Role, Permission
from .validators import alnum, username_available, role_name_available

class SearchUsersForm(FlaskForm):
	search = StringField('Search', [validators.optional()])

class SearchRolesForm(FlaskForm):
	search = StringField('Search', [validators.optional()])

class UserForm(FlaskForm):
	username = StringField('Username', [validators.required(), validators.length(4, 16), alnum, username_available])

class RoleForm(FlaskForm):
	name = StringField('Name', [validators.required(), validators.length(1, 16), alnum, role_name_available])

class DeleteRoleForm(FlaskForm):
	submit = SubmitField('Delete', [validators.required()])

class RolePermissionForm(FlaskForm):
	permission = SelectField('Permission', choices=Permission.choices())

class DeleteRolePermissionForm(FlaskForm):
	submit = SubmitField('Delete', [validators.required()])

class UserRoleForm(FlaskForm):
	role = SelectField('Role', choices=Role.choices())

class DeleteUserRoleForm(FlaskForm):
	submit = SubmitField('Delete', [validators.required()])