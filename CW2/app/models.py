from datetime import datetime
from app import db

class url(db.Model):
    __tablename__ = "url"
    id = db.Column('id', db.Integer, primary_key=True)
    url = db.Column('name', db.String(100))
    long_url = db.Column(db.Text)
   