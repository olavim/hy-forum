import re
from wtforms import ValidationError
from ..models.user import User
from ..models.role import Role

def alnum(form, field):
	if not re.match('^[a-zA-Z0-9-_]+$', field.data):
		raise ValidationError('Spaces and special characters other than - _ not allowed')

def username_available(form, field):
	user = User.query.filter_by(username=field.data).first()
	if user:
		raise ValidationError('Username taken')

def role_name_available(form, field):
	role = Role.query.filter_by(name=field.data).first()
	if role:
		raise ValidationError('Role with that name already exists')