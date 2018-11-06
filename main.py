#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------



from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# create a flask object (flask needs an object to represent the application)

app = Flask(__name__)



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
    return render_template('books.html')

@app.route('/authors/')
def authors():
    return render_template('authors.html')

@app.route('/publishers/')
def publishers():
    return render_template('publishers.html')

@app.route('/book/<title>/')
def some_book(title = "Harry Potter",google_id="alskdfj",isbn="alskdjf",publication_date="laskjdf",description="laskdjf",image_url="https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500",author="alskdjf",publisher="alskdfj"):
    return render_template('some_book.html',title = title,google_id=google_id,isbn=isbn,publication_date=publication_date,description=description,image=image)

@app.route('/authors/<name>/')
def some_author(name="JK Rowling",born = None, education = "alskdjfla",nationality="alskdf",alma_mater="laksd",description="laksd",wikipedia_url="llaskdjf",image_url="slkdjf"):
    return render_template('some_author.html',name=name, born=born,education=education,nationality=nationality,alma_mater=alma_mater,description=description,wikipedia_url=wikipedia_url,image_url=image_url)

@app.route('/publishers/<name>')
def some_publisher(name="Pottermore",owner="laskdjf",description="laskdjf",wikipedia_url="alskdjf",image_url="laskdfj",website="alskdfj"):
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


# if main.py is run directly, i.e., as the main module, it will be assigned the value main
# and if it's main go ahead and run the application.
# if this application is imported, then the __name__ is no longer __main__ and
# the code, app.run(), will not be executed

if __name__ == "__main__":
    app.debug = True

    #leave this line so lydia can run the website on her UTCS machine thanks
    app.run(host='128.83.139.95')

    #app.run('104.248.122.33', '80')
#----------------------------------------
# end of main.py
#----------------------------------------
