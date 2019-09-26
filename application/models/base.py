from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utc.now import utcnow
from ..main import db

class Base(db.Model):
	__abstract__ = True

	id = Column(Integer, primary_key=True, autoincrement=True)
	created_at = Column(DateTime, server_default=utcnow())
	updated_at = Column(DateTime, server_default=utcnow(), onupdate=utcnow())
