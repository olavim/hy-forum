from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from .setup import db

class User(db.Model):
	__tablename__ = 'forum.user'

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(255), unique=True)
	password_hash = Column(String(80))
	created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
	updated_at = Column(TIMESTAMP(timezone=True))

	def __init__(self, username=None, password_hash=None):
		self.username = username
		self.password_hash = password_hash

	def __repr__(self):
		return '<User %r>' % (self.username)
