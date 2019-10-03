from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text
from ..main import db
from .base import Base
from .message import Message

class Thread(Base):
	__tablename__ = 'thread'

	title = Column(String(255))
	topic_id = Column(Integer, ForeignKey('topic.id'))
	user_id = Column(Integer, ForeignKey('user.id'))

	user = relationship('User')
	messages = relationship('Message', backref='thread')

	def __init__(self, title=None, topic_id=None, user_id=None):
		self.title = title
		self.topic_id = topic_id
		self.user_id = user_id

	def __repr__(self):
		return '<Thread id=%r title=%r topic_id=%r user_id=%r>' \
			% (self.id, self.title, self.topic_id, self.user_id)

	def total_messages(self):
		stmt = text('SELECT COUNT(message.id) '
								'FROM thread '
								'LEFT JOIN message ON message.thread_id = thread.id '
								'WHERE thread.id = :id').params(id=self.id)
		res = db.engine.execute(stmt).fetchone()
		return res[0]

	def latest_message(self):
		message = Message.query \
			.filter(Message.thread_id == self.id) \
			.order_by(Message.created_at.desc()) \
			.first()
		return message
