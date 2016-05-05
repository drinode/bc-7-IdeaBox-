
# Basic models for demonstration

import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

 
Base = declarative_base()

engine = create_engine('sqlite:///db/sample.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Idea(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	description = Column(Text)
	date_time = Column(DateTime, default=datetime.datetime.utcnow)
	comment = relationship('Comment', backref='title', lazy='dynamic')

	def save(self):
		session.add(self)
		session.commit()

	def get_comment(self):
		return Comment.query.filter_by(post_id=post.id)



class Comment(Base):
	__tablename__ = 'comment'
	id = Column(Integer, primary_key=True)
	descriprtion = Column(Text)
	date_time = Column(DateTime, default=datetime.datetime.utcnow)
	post_id = Column(Integer, ForeignKey('post.id'))

	def save(self):
		session.add(self)
		session.commit()
	


# to run migrations (sort of)
if __name__ == '__main__':
	Base.metadata.create_all(engine)
	print "migrations successful"


