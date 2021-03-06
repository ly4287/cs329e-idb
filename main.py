#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------



from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from models import app, db, Book, Author, Publisher


#book_data = json.load(open('books.json'))


# create a flask object (flask needs an object to represent the application)

#app = Flask(__name__)
# we move this to models.py


# The route decorator '@app.route()' maps a function to a route on your website.
# decorators are used to map a function, index(), to a web page, / or
# i.e., when someone types in the home address of the web site,
# flask will run the function index()
# summary: type in a URL, flask check the URL, finds the associate function with it, runs the function, collect responses, and send back the results to the browser.

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/books/')
def books():
    books = db.session.query(Book).all()
    return render_template('books.html', books = books)

@app.route('/books/<int:book_id>')
def singlebook(book_id):
	single_book = db.session.query(Book).get(book_id)
	return render_template('singlebook.html', book_id = book_id, book = single_book)

@app.route('/authors/')
def authors():
    authors = db.session.query(Author).all()
    return render_template('authors.html', authors = authors)

@app.route('/authors/<int:author_id>')
def singleauthor(author_id):
	single_author = db.session.query(Author).get(author_id)
	return render_template('singleauthor.html', author_id = author_id, author = single_author)

@app.route('/publishers/')
def publishers():
    publishers = db.session.query(Publisher).all()
    return render_template('publishers.html', publishers = publishers)

@app.route('/publishers/<int:pub_id>')
def singlepublisher(pub_id):
	single_publisher = db.session.query(Publisher).get(pub_id)
	return render_template('singlepublisher.html', pub_id = pub_id, publisher = single_publisher)
	
@app.route('/test/')
def test():
	p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			stdin=subprocess.PIPE)
	out, err = p.communicate()
	output=err+out
	output = output.decode("utf-8") #convert from byte type to string type
	
	return render_template('test.html', output = "<br/>".join(output.split("\n")))

'''
@app.route('/book/<title>/')
def some_book(title):
	for i in book_data:
		if i["title"] == title:
			title = i["title"]
			google_id=i["google_id"]
			isbn=i["isbn"]
			publication_date=i["publication_date"]
			image_url=i["image_url"]
			description=i["description"]
	return render_template('some_book.html',title = title,google_id=google_id,isbn=isbn,publication_date=publication_date,description=description,image_url=image_url)

@app.route('/authors/<name>/')
def some_author(name):
	for i in book_data:
		for j in range(len(i["authors"])):
			if i["authors"][j]["name"] == name:
				name = i["authors"][j]["name"]
				born = i["authors"][j]["born"]
				education = i["authors"][j]["education"]
				nationality=i["authors"][j]["nationality"]
				alma_mater=i["authors"][j]["alma_mater"]
				wikipedia_url=i["authors"][j]["wikipedia_url"]
				description = i["authors"][j]["description"]
				image_url = i["authors"][j]["image_url"]
	return render_template('some_author.html',name=name, born=born,education=education,nationality=nationality,alma_mater=alma_mater,description=description,wikipedia_url=wikipedia_url,image_url=image_url)

@app.route('/publishers/<name>')
def some_publisher(name):
	for i in book_data:
		for j in range(len(i["publishers"])):
			if i["publishers"][j]["name"] == name:
				name = i["publishers"][j]["name"]
				owner = i["publishers"][j]["owner"]
				website = i["publishers"][j]["website"]
				wikipedia_url=i["publishers"][j]["wikipedia_url"]
				description = i["publishers"][j]["description"]
				image_url = i["publishers"][j]["image_url"]
	return render_template('some_publisher.html',name=name,owner=owner,description=description,wikipedia_url=wikipedia_url,image_url=image_url,website=website)







@app.route('/harrypotter/')
def harrypotter():
    return render_template('harrypotter.html')

@app.route('/eggs/')
def eggs():
    return render_template('eggs.html')

@app.route('/romeo/')
def romeo():
    return render_template('romeo.html')

@app.route('/jkrowling/')
def jkrowling():
    return render_template('jkrowling.html')

@app.route('/seuss/')
def seuss():
    return render_template('seuss.html')

@app.route('/shakespeare/')
def shakespeare():
    return render_template('shakespeare.html')

@app.route('/pottermore/')
def pottermore():
    return render_template('pottermore.html')

@app.route('/randomhouse/')
def randomhouse():
    return render_template('randomhouse.html')

@app.route('/barrons/')
def barrons():
    return render_template('barrons.html')
'''

# if main.py is run directly, i.e., as the main module, it will be assigned the value main
# and if it's main go ahead and run the application.
# if this application is imported, then the __name__ is no longer __main__ and
# the code, app.run(), will not be executed

if __name__ == "__main__":
    app.debug = True

    #leave this line so lydia can run the website on her UTCS machine thanks
    #app.run(host='128.83.139.95')

    app.run('104.248.122.33', '80')
#----------------------------------------
# end of main.py
#----------------------------------------
