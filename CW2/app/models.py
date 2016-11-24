from datetime import datetime
from app import db

class url(db.Model):
    __tablename__ = "url"
    id = db.Column('id', db.Integer, primary_key=True)
    short_url = db.Column('url', db.String(100))
    long_url = db.Column(db.Text)

    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url
   