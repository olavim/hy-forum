from sqlalchemy import Column, Integer, TIMESTAMP, func
from ..main import db

class Base(db.Model):
	__abstract__ = True

	id = Column(Integer, primary_key=True, autoincrement=True)
	created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
	updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())