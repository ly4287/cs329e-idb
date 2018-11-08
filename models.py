# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# from sqlalchemy.orm import relationship,sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine

import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','postgres://postgres:patrick@localhost:5432/books')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    google_id = Column(Integer, primary_key = True)
    title = Column(String, unique=True)
    publication_date = Column(String)
    image_url = Column(String)
    description = Column(String)

class Author(Base):
    __tablename__ = 'author'
    born = Column(String)
    name = Column(String, primary_key = True, nullable = False)
    education = Column(String)
    nationality = Column(String)
    description = Column(String)
    alma_mater = Column(String)
    wikipedia_url = Column(String)
    died = Column(String, nullable = True)
    image_url = Column(String)
    def __repr__(self):
        return self.name

class Publisher(Base):
    __tablename__ = 'publisher'
    wikipedia_url = Column(String)
    name = Column(String, primary_key = True, nullable = False)
    description = Column(String)
    owner = Column(String)
    image_url = Column(String)
    website = Column(String)
    def __repr__(self):
        return self.name

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
