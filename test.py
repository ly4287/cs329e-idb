import os
import psycopg2
import unittest
from models import db, Book, Author, Publisher

conn = psycopg2.connect(host="localhost", database="bookdb", user="patrick", password="sqlRAGTAG", port="5432")
cursor = conn.cursor()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Book(id='5000', title = 'josh')
        db.session.add(s)
        db.session.commit()

        cursor.execute("SELECT id, title FROM Book")
        rows = cursor.fetchall()
        swag = ''
        for row in rows:
            if(row[1] == 'josh'):
                swag = row[1]
                break
        self.assertEqual(swag, 'josh')

        db.session.delete(s)
        db.session.commit()

    def test_source_insert_2(self):
        s = Book(id='5001', title = 'paul')
        db.session.add(s)
        db.session.commit()

        cursor.execute("SELECT id, title FROM Book")
        rows = cursor.fetchall()
        swag = ''
        for row in rows:
            if(row[1] == 'paul'):
                swag = row[1]
                break
        self.assertEqual(swag, 'paul')

        db.session.delete(s)
        db.session.commit()

    def test_source_insert_3(self):
	s = Author(id='6969', name = 'bam')
	db.session.add(s)
	db.session.commit()
	
	cursor.execute("SELECT id, name FROM Author")
	rows = cursor.fetchall()
	swag = ''
	for row in rows:
		if(row[1] == 'bam'):
			swag = row[1]
			break
	self.assertEqual(swag, 'bam')

	db.session.delete(s)
	db.session.commit()

    def test_source_insert_4(self):
	s = Publisher(id='99100', name = 'bum')
	db.session.add(s)
	db.session.commit()

	cursor.execute("SELECT id, name FROM Publisher")
	rows = cursor.fetchall()
	swag = ''
	for row in rows:
		if(row[1] == 'bum'):
			swag = row[1]
			break
	self.assertEqual(swag, 'bum')

	db.session.delete(s)
	db.session.commit()
	

if __name__ == '__main__':
	unittest.main()
