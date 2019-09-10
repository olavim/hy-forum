from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Topic(Base):
	__tablename__ = 'forum.topic'

	title = Column(String(255))

	threads = relationship('thread.Thread')

	def __init__(self, title=None):
		self.title = title

	def __repr__(self):
		return '<Topic %r>' % (self.title)
