from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text
from flask_login import current_user
from ..main import db
from .base import Base, TimestampBase
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

	def has_new_messages(self):
		if not current_user.is_authenticated:
			return False

		thread_read = ThreadRead.query.get((self.id, current_user.id))
		return not thread_read or self.latest_message().created_at > thread_read.updated_at

class ThreadRead(TimestampBase):
	__tablename__ = 'thread_read'

	thread_id = Column(Integer, ForeignKey('thread.id'), primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

	thread = relationship('Thread', cascade='delete')
	user = relationship('User', cascade='delete')

	def __init__(self, thread_id=None, user_id=None):
		self.thread_id = thread_id
		self.user_id = user_id

	def __repr__(self):
		return '<ThreadRead thread_id=%r user_id=%r>' % (self.thread_id, self.user_id)