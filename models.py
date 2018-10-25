from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

db = SQLAlchemy()

class Books(Base):
    __tablename__ = 'books'
    google_id = db.Column(db.String(), primary_key = True)
    title = db.Column(db.String(), unique=True)
    publication_date = db.Column(db.String())
    image_url = db.Column(db.String())
    description = db.Column(db.String())

class Authors(Base):
    __tablename__ = 'authors'
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

class Publishers(Base):
    __tablename__ = 'publishers'
    wikipedia_url = db.Column(db.String())
    name = db.Column(db.String(), primary_key = True, nullable = False)
    description = db.Column(db.String())
    owner = db.Column(db.String())
    image_url = db.Column(db.String())
    website = db.Column(db.String())
    def __repr__(self):
        return self.name
