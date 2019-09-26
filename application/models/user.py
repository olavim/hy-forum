from sqlalchemy import Column, String
from .base import Base

class User(Base):
	__tablename__ = 'user'

	username = Column(String(255), unique=True)
	password_hash = Column(String(255))

	def __init__(self, username=None, password_hash=None):
		self.username = username
		self.password_hash = password_hash

	def __repr__(self):
		return '<User id=%r username=%r>' % (self.id, self.username)
