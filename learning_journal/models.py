from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
	Unicode,
	DateTime,
	UnicodeText,
    )
	
import datetime
	
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now())
    edited = Column(DateTime, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
	
    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        session.query(cls).all()
	
    @classmethod
    def by_id(cls, entry_id, session=None):
        if session is None:
            session = DBSession
        session.query(cls).filter_by(id=entry_id)
