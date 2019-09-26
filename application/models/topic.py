from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from ..main import db
from .base import Base
from .message import Message
from .thread import Thread

class Topic(Base):
	__tablename__ = 'topic'

	title = Column(String(255))
	description = Column(String(255))

	threads = relationship('Thread')

	def __init__(self, title=None, description=None):
		self.title = title
		self.description = description

	def __repr__(self):
		return '<Topic id=%r title=%r description=%r>' % (self.id, self.title, self.description)

	def total_threads(self):
		stmt = text('SELECT COUNT(thread.id) '
								'FROM topic '
								'LEFT JOIN thread ON thread.topic_id = topic.id '
								'WHERE topic.id = :id')

		res = db.engine.execute(stmt, id=self.id).fetchone()
		return res[0]

	def total_messages(self):
		stmt = text('SELECT COUNT(message.id) '
								'FROM topic '
								'LEFT JOIN thread ON thread.topic_id = topic.id '
								'LEFT JOIN message ON message.thread_id = thread.id '
								'WHERE topic.id = :id')

		res = db.engine.execute(stmt, id=self.id).fetchone()
		return res[0]

	def latest_message(self):
		message = Message.query \
			.join(Message.thread) \
			.filter(Thread.topic_id == self.id) \
			.order_by(Message.created_at.desc()) \
			.first()
		return message