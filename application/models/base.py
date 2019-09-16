from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utc.now import utcnow
from ..main import db
from ..config import database_schema

class Base(db.Model):
	__abstract__ = True
	__table_args__ = {'schema': database_schema}

	id = Column(Integer, primary_key=True, autoincrement=True)
	created_at = Column(DateTime(True), server_default=utcnow())
	updated_at = Column(DateTime(True), server_default=utcnow(), onupdate=utcnow())

	@staticmethod
	def ForeignKey(column):
		ref = '%s.%s' % (database_schema, column) if database_schema else column
		return ForeignKey(ref)
