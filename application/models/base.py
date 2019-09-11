from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from ..main import db
from ..config import database_schema

class Base(db.Model):
	__abstract__ = True
	__table_args__ = {'schema': database_schema}

	id = Column(Integer, primary_key=True, autoincrement=True)
	created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
	updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

	@staticmethod
	def ForeignKey(column):
		ref = '%s.%s' % (database_schema, column) if database_schema else column
		return ForeignKey(ref)
