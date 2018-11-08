import json
from models import db, Book, Author, Publisher

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn

def create_books():
    book = load_json('books.json')

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
        author1 = oneBook['authors']
        for i in author1:
            author = i['name']
        publisher1 = oneBook['publishers']
        for j in publisher1:
            pub = j['name']
        newBook = Book(title = title, google_id = g_id, isbn = idbn_, image_url = img_url, publication_date = pub_date, description = desc, author = author, publisher = pub, val = 0)
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()

def create_authors():
    book = load_json('books.json')

    for oneBook in book['Books']:
        title = oneBook['title']
        id = oneBook['id']
        
        newBook = Book(title = title, id = id)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
        
def create_publishers():
    book = load_json('books.json')

    for oneBook in book['Books']:
        title = oneBook['title']
        id = oneBook['id']
        
        newBook = Book(title = title, id = id)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
        
create_books()
create_authors()
create_publishers()