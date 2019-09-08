from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from ..main import db

class Base(db.Model):
	__abstract__ = True

	id = Column(Integer, primary_key=True, autoincrement=True)
	created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
	updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

class User(Base):
	__tablename__ = 'forum.user'

	username = Column(String(255), unique=True)
	password_hash = Column(String(80))

	def __init__(self, username=None, password_hash=None):
		self.username = username
		self.password_hash = password_hash

	def __repr__(self):
		return '<User %r>' % (self.username)
