from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, FieldList, FormField, SubmitField
from wtforms.validators import Required, EqualTo
from ..models.role import Role, Permission

class SearchUsersForm(FlaskForm):
	search = TextField('Search')

class SearchRolesForm(FlaskForm):
	search = TextField('Search')

class UserForm(FlaskForm):
	username = TextField('Username', [Required()])

class RoleForm(FlaskForm):
	name = TextField('Name', [Required()])

class DeleteRoleForm(FlaskForm):
	submit = SubmitField('Delete', [Required()])

class RolePermissionForm(FlaskForm):
	permission = SelectField('Permission', choices=Permission.choices())

class DeleteRolePermissionForm(FlaskForm):
	submit = SubmitField('Delete', [Required()])

class UserRoleForm(FlaskForm):
	role = SelectField('Role', choices=Role.choices())

class DeleteUserRoleForm(FlaskForm):
	submit = SubmitField('Delete', [Required()])