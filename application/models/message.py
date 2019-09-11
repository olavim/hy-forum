from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class Message(Base):
	__tablename__ = 'message'

	text = Column(Text)
	thread_id = Column(Integer, Base.ForeignKey('thread.id'))
	user_id = Column(Integer, Base.ForeignKey('user.id'))

	user = relationship('User')

	def __init__(self, text=None, thread_id=None, user_id=None):
		self.text = text
		self.thread_id = thread_id
		self.user_id = user_id

	def __repr__(self):
		return '<Message>'
