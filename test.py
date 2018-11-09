import os
import psycopg2
import unittest
from models import db, Book, Author, Publisher

conn = psycopg2.connect(host="localhost", database="bookdb", user="patrick", password="sqlRAGTAG", port="5432")
cursor = conn.cursor()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Book(id='5000', title = 'TESTONE')
        db.session.add(s)
        db.session.commit()

	cursor.execute("SELECT id, title FROM Book")
	rows = cursor.fetchall()
	swag = ''
	for row in rows:
		if(row[1] == 'TESTONE'):
			swag = row[1]
			break
	self.assertEqual(swag, 'TESTONE')

        db.session.delete(s)
        db.session.commit()
		



if __name__ == '__main__':
	unittest.main()
