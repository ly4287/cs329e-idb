import psycopg2
import json, logging 
from sqlalchemy.orm import sessionmaker
from models import db, Book, Author

#from models import Base, Book, Author, Publisher, engine
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine)
#session = DBSession()

conn = psycopg2.connect(host="localhost", database="bookdb", user="patrick", password="sqlRAGTAG", port="5432")
cursor = conn.cursor()

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn

def create_books():
    book = load_json('books.json')
    counter = 0
    dupe = False
    for oneBook in book:
        title = oneBook['title']
        g_id = oneBook['google_id']
        try:
            isbn_ = oneBook['isbn']
        except:
            isbn_ = "None"
        try:
            img_url = oneBook['image_url']
        except:
            img_url = "None"
        try:
            pub_date = oneBook['publication_date']
        except:
            pub_date = "None"
        try:
            desc = oneBook['description']
        except:
            desc = "None"
        publishers_attribute = oneBook['publishers']
        for i in publishers_attribute:
            publisher = i['name']
        authors_attribute = oneBook['authors']
        for j in authors_attribute:
            author = j['name']
        newBook = Book(title = title, google_id = g_id, isbn = isbn_, image_url = img_url, publication_date = pub_date, description = desc, author = author, publisher = publisher)
	cursor.execute("SELECT google_id FROM book")
	rows = cursor.fetchall()
	for row in rows:
		if g_id in row:
			dupe = True
			continue
	if(not dupe):
        	# After I create the book, I can then add it to my session. 
        	db.session.add(newBook)
        	# commit the session to my DB.
        	db.session.commit()
        	counter += 1
		print("we added a book into the DB! it was: "+title)
	else:
		print("there was a dupe!")

def create_authors():
    book = load_json('books.json')
    counter = 0
    dupe = False
    for oneBook in book:
        title = oneBook['title']
        publishers_attribute = oneBook['publishers']
        for i in publishers_attribute:
            publisher = i['name']
        authors_attribute = oneBook['authors']
        for j in authors_attribute:
            author = j['name']
            try:
                born = j['born']
            except:
                born = "None"
            try:
                education = j['education']
            except:
                education = "None"
            try:
                nationality = j['nationality']
            except:
                nationality = "None"
            try:
                desc = j['description']
            except:
                desc = "None"
            try:
                alma = j['alma_mater']
            except:
                alma = "None"
            try:
                wiki = j['wikipedia_url']
            except:
                wiki = "None"
            try: 
                died = j['died']
            except:
                died = "None"
            try:
                img_url = j['image_url']
            except:
                img_url = "None"
        newAuthor =  Author(name = author, born = born, education = education, nationality = nationality, description = desc, alma_mater = alma, wikipedia_url = wiki, image_url = img_url, publisher = publisher)
	cursor.execute("SELECT name FROM author")
	rows = cursor.fetchall()
	for row in rows:
		if author in row:
			dupe = True
			continue
	if(not dupe):
		db.session.add(newAuthor)
		db.session.commit()
		counter += 1
		print("we added an author into the DB! it was: "+author)
	else:
		print("there was a dupe!")
'''
        if session.query(Authors).filter(Authors.name == newAuthor.name).count() == 0: 
            db.session.add(newAuthor)
            db.session.commit()
            counter += 1
'''

'''        
def create_publishers():
    book = load_json('books.json')
    counter = 0
    for oneBook in book:
        title = oneBook['title']
        publishers_attribute = oneBook['publishers'] 
        for i in publishers_attribute:
            publisher = i['name']
            try:
                wiki = i['wikipedia_url']
            except:
                wiki = "None"
            try:
                desc = i['description']
            except:
                desc = "None"
            try:
                owner = i['owner']
            except:
                owner = "None"
            try:
                img_url = i['image_url']
            except:
                img_url = "None"
            try:
                website = i['website']
            except:
                website = "None"
        authors_attribute = oneBook['authors']
        for j in authors_attribute:
            author = j['name']
        newPublisher = Publishers(title= title, author = author, name = publisher, wiki_url = wiki, description = desc, owner = owner, image_url = img_url, website = website, id = counter)
        if session.query(Publishers).filter(Publishers.name == newPublisher.name).count() == 0: 
            session.add(newPublisher)
            session.commit()
            counter += 1
'''
create_books()
create_authors()

cursor.close()
#create_publishers()
