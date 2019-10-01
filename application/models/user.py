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

	@property
	def is_admin(self):
		return self.username == 'admin'

	def has_role(self, role_name):
		return any(role for role in self.roles if role.name == role_name)

	def has(self, permission):
		return (
			self.is_admin or
			any(p for role in self.roles for p in role.permissions if p.permission == permission)
		)

class AnonymousUser(AnonymousUserMixin):
	@property
	def is_admin(self):
		return False

	def has_role(self, role):
		return False

	def has(self, permission):
		return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)
