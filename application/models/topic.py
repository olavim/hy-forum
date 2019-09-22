from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Topic(Base):
	__tablename__ = 'topic'

	title = Column(String(255))
	description = Column(String(255))

	threads = relationship('Thread')

	def __init__(self, title=None, description=None):
		self.title = title
		self.description = description

	def __repr__(self):
		return '<Topic %r %r>' % (self.title)
