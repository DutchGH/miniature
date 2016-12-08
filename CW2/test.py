#!flask/bin/python
import os
import unittest
from datetime import datetime, timedelta

from config import basedir
from app import app, db
from app.models import *


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_userCreation(self):
        # create a user and write it to the database
        u = User(user_name='test', email='test@test.com', 
            password = "alpine", first_name = "test", last_name = "mctestyface")
        db.session.add(u)
        db.session.commit()
        user = User.query.filter_by(user_name = 'test').first()
        assert user.user_name == 'test'

    def test_urlCreation(self):
        x = url_table(short_url = "goog", long_url = "http://www.google.co.uk")
        db.session.add(x)
        db.session.commit()
        url = url_table.query.filter_by(short_url = 'goog').first()
        assert url.long_url == "http://www.google.co.uk"

    def test_relationship(self):
        u = User(user_name='test', email='test@test.com', 
            password = "alpine", first_name = "test", last_name = "mctestyface")
        db.session.add(u)
        db.session.commit()
        user = User.query.filter_by(user_name = 'test').first()
        assert user.user_name == 'test'
        x = url_table(short_url = "goog", long_url = "http://www.google.co.uk")
        db.session.add(x)
        db.session.commit()
        url = url_table.query.filter_by(short_url = 'goog').first()
        assert url.long_url == "http://www.google.co.uk"
        user.follow(url)
        assert user.has_generated(url)


if __name__ == '__main__':
    unittest.main()
