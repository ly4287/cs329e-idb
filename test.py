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

    def test_db_1(self):
        r = db.session.query(Books).filter_by(google_id = 'wrOQLV6xB-wC').one()
        self.assertEqual(str(r.google_id), 'wrOQLV6xB-wC')
    def test_db_2(self):
        r = db.session.query(Books).filter_by(google_id = 'kPpeTrfXpKsC').first()
        self.assertEqual(str(r.google_id), 'kPpeTrfXpKsC')
    def test_db_3(self):
        r = db.session.query(Books).filter_by(isbn = '1101486406').first()
        self.assertEqual(str(r.isbn), '1101486406')
    def test_db_4(self):
        r = db.session.query(Books).filter_by(title = 'Royal Assassin').first()
        self.assertEqual(str(r.Books), 'Royal Assassin')
    def test_db_5(self):
        r = db.session.query(Authors).filter_by(name = 'Terry Goodkind').first()
        self.assertEqual(str(r.name), 'Terry Goodkind')
    def test_db_6(self):
        r = db.session.query(Authors).filter_by(name = 'Stephen King').first()
        self.assertEqual(str(r.name), 'Stephen King')
    def test_db_7(self):
        r = db.session.query(Authors).filter_by(education = 'Dana Hall School, 1928').first()
        self.assertEqual(str(r.education), 'Dana Hall School, 1928')
    def test_db_8(self):
        r = db.session.query(Authors).filter_by(alma_mater = 'Princeton University').first()
        self.assertEqual(str(r.alma_mater), 'Princeton University')
    def test_db_9(self):
        r = db.session.query(Publishers).filter_by(name = 'Del Rey Books').first()
        self.assertEqual(str(r.name), 'Del Rey Books')
    def test_db_10(self):
        r = db.session.query(Publishers).filter_by(owner = 'Scholastic Corporation').first()
        self.assertEqual(str(r.owner), 'Scholastic Corporation')
    def test_db_11(self):
        r = db.session.query(Publishers).filter_by(owner = 'Penguin Random House').first()
        self.assertEqual(str(r.owner), 'Penguin Random House')
    def test_db_12(self):
        r = db.session.query(Publishers).filter_by(name = 'Palgrave Macmillan').first()
        self.assertEqual(str(r.name), 'Palgrave Macmillan')
if __name__ == '__main__':
	unittest.main()