from datetime import datetime
from app import db

class ToDo(db.Model):
    __tablename__ = "todo"
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)
    is_done = db.Column('is_done', db.Boolean, default= False)