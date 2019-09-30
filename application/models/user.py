from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import AnonymousUserMixin, UserMixin
from .base import Base
from ..main import login_manager

class User(UserMixin, Base):
	__tablename__ = 'user'

	username = Column(String(255), unique=True)
	password_hash = Column(String(255))

	roles = relationship('Role', secondary='role_membership')

	def __init__(self, username=None, password_hash=None):
		self.username = username
		self.password_hash = password_hash

	def __repr__(self):
		return '<User id=%r username=%r>' % (self.id, self.username)

	def has_role(self, role):
		return any(role for role in self.roles if role.name == role)

	def has(self, permission):
		return self.has_role('admin') \
			or any(p for role in self.roles for p in role.permissions if p.permission == permission)

class AnonymousUser(AnonymousUserMixin):
	def has_role(self, role):
		return False

	def has(self, permission):
		return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)
