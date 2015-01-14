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
import sqlalchemy as sa
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
    def all(cls):
    #return a query with all of the entries in the database ordered by creation date
        return DBSession.query(cls).order_by(sa.desc(cls.created)).all()
    
    @classmethod
    def by_id(cls, id):
    #return a query with the specified entry by id
        return DBSession.query(cls).get(id)