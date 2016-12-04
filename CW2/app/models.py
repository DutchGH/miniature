from datetime import datetime
from app import db

class url_table(db.Model):
    __tablename__ = "url"
    id = db.Column('id', db.Integer, primary_key=True)
    short_url = db.Column('url', db.String(100))
    long_url = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url


class user(db.Model):
	__tablename__ = "user"
	id = db.Column('id', db.Integer, primary_key = True)
	user_name = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(500), index = True, unique = True)
	password = db.Column(db.String(500))
	first_name = db.Column(db.String(500))
	last_name = db.Column(db.String(500))

	def __repr__(self):
		return '<User %r>' % (self.user_name)

   