import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo = True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Sequence

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	name = Column(String(50))
	fullname = Column(String(50))
	password = Column(String(12))

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%'s)>" % (self.name, self.fullname, self.password)
Base.metadata.create_all(engine)
joshke = User(name='Josh', fullname='Josh Ke', password='pubg')
session.add(joshke)
ourUser = session.query(User).filter_by(name='Josh').first()
joshke.password = 'changeup'
session.dirty
