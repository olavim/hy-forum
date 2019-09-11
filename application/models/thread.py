from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Thread(Base):
	__tablename__ = 'thread'

	title = Column(String(255))
	topic_id = Column(Integer, Base.ForeignKey('topic.id'))
	user_id = Column(Integer, Base.ForeignKey('user.id'))

	user = relationship('User')
	messages = relationship('Message')

	def __init__(self, title=None, topic_id=None, user_id=None):
		self.title = title
		self.topic_id = topic_id
		self.user_id = user_id

	def __repr__(self):
		return '<Thread %r>' % (self.title)