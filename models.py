from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5432/bookdb')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#

class Book(Base):
    __tablename__ = 'book'
    google_id = db.Column(db.String(), primary_key = True)
    title = db.Column(db.String(), unique=True)
    publication_date = db.Column(db.String())
    image_url = db.Column(db.String())
    description = db.Column(db.String())

class Author(Base):
    __tablename__ = 'author'
    born = db.Column(db.String())
    name = db.Column(db.String(), primary_key = True, nullable = False)
    education = db.Column(db.String())
    nationality = db.Column(db.String())
    description = db.Column(db.String())
    alma_mater = db.Column(db.String())
    wikipedia_url = db.Column(db.String())
    died = db.Column(db.String(), nullable = True)
    image_url = db.Column(db.String())
    def __repr__(self):
        return self.name

class Publisher(Base):
    __tablename__ = 'publisher'
    wikipedia_url = db.Column(db.String())
    name = db.Column(db.String(), primary_key = True, nullable = False)
    description = db.Column(db.String())
    owner = db.Columndb.String())
    image_url = db.Column(db.String())
    website = db.Column(db.String())
    def __repr__(self):
        return self.name

db.drop_all()
db.create_all()
