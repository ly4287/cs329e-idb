from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

db = SQLAlchemy()

class Books(Base):
	__tablename__ = 'books'
	google_id = db.Column(db.String(), primary_key = true, nullable = False)
	title = db.Column(db.String(), unique=True, nullable = False)
	publication_date = db.Column(db.String(), nullable = False)
	image_url = db.Column(db.String(), nullable = False)
	description = db.Column(db.String(), nullable = False)
	digest = db.Column(db.String(), nullable = False)

class Authors(db.Model):
    __tablename__ = 'authors'
    born = db.Column(db.String(), nullable = False)
    name = db.Colunn(db.String(), primary_key = true, nullable = False)
    education = db.Column(db.String(), nullable = False)
    nationality = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    alma_mater = db.Column(db.String(), nullable = False)
    wikipedia_url = db.Column(db.String(), nullable = False)
    image_url = db.Column(db.String(), nullable = False)
    def __repr__(self):
        return self.name

class Publishers(Base):
	__tablename__ = 'publishers'
	name = db.Column(db.String(), primary_key = true, nullable = False)
	wikipedia_url = db.Column(db.String(), nullable = False)
	description = db.Column(db.String(), nullable = False)
	owner = db.Column(db.String(), nullable = False)
	founded = db.Column(db.String(), nullable = False)
	location = db.Column(db.String(), nullable = False)
	image_url = db.Column(db.String(), nullable = False)
	website = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return self.name
