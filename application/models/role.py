from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampBase

class Role(Base):
	__tablename__ = 'role'

	name = Column(String(255), unique=True)

	users = relationship('User', secondary='role_membership')
	permissions = relationship('Permission', secondary='role_permission')

	def __init__(self, name=None):
		self.name = name

	def __repr__(self):
		return '<Role id=%r name=%r>' % (self.id, self.name)

	@classmethod
	def choices(cls):
		roles = Role.query.all()
		return [(r.name, r.name) for r in roles if r.name != 'admin']

class Permission(Base):
	__tablename__ = 'permission'

	permission = Column(String(255), unique=True)

	def __init__(self, permission=None):
		self.permission = permission

	def __repr__(self):
		return '<Permission id=%r permission=%r>' % (self.id, self.permission)

	@classmethod
	def choices(cls):
		permissions = Permission.query.all()
		return [(p.permission, p.permission) for p in permissions]

class RoleMembership(TimestampBase):
	__tablename__ = 'role_membership'

	role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

	user = relationship('User', cascade='delete')
	role = relationship('Role', cascade='delete')

	def __init__(self, role_id=None, user_id=None):
		self.role_id = role_id
		self.user_id = user_id

	def __repr__(self):
		return '<RoleMembership id=%r role_id=%r user_id=%r>' % (self.id, self.role_id, self.user_id)

class RolePermission(TimestampBase):
	__tablename__ = 'role_permission'

	role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
	permission_id = Column(Integer, ForeignKey('permission.id'), primary_key=True)

	role = relationship('Role', cascade='delete')
	permission = relationship('Permission', cascade='delete')

	def __init__(self, role_id=None, permission_id=None):
		self.role_id = role_id
		self.permission_id = permission_id

	def __repr__(self):
		return '<RolePermission id=%r role_id=%r permission_id=%r>' % (self.id, self.role_id, self.permission_id)
