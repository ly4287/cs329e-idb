# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# from sqlalchemy.orm import relationship,sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
#from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.ext.declarative import declarative_base 
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING", 'postgres://patrick:sqlRAGTAG@localhost:5432/bookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','postgres://patrick:password@localhost:5432/books')
#engine = create_engine(SQLALCHEMY_DATABASE_URI)

#Base = declarative_base()

class Book(db.Model):
    __tablename__ = 'book'
    google_id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, unique=True)
    isbn = db.Column(db.String)
    publication_date = db.Column(db.String)
    image_url = db.Column(db.String)
    description = db.Column(db.String)
    publisher = db.Column(db.String)
    author = db.Column(db.String)

class Author(db.Model):
    __tablename__ = 'author'
    born = db.Column(db.String)
    name = db.Column(db.String, primary_key = True, nullable = False)
    education = db.Column(db.String)
    nationality = db.Column(db.String)
    description = db.Column(db.String)
    alma_mater = db.Column(db.String)
    wikipedia_url = db.Column(db.String)
    died = db.Column(db.String, nullable = True)
    image_url = db.Column(db.String)
    publisher = db.Column(db.String)
    def __repr__(self):
        return self.name

class Publisher(db.Model):
    __tablename__ = 'publisher'
    wikipedia_url = db.Column(db.String)
    name = db.Column(db.String, primary_key = True, nullable = False)
    description = db.Column(db.String)
    owner = db.Column(db.String)
    image_url = db.Column(db.String)
    website = db.Column(db.String)
    author = db.Column(db.String)
    def __repr__(self):
        return self.name

db.drop_all()
db.create_all()

#db.drop_all()
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)
