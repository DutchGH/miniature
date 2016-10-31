from datetime import datetime
from app import db

#Database model represented as a class in python
class ToDo(db.Model):
    __tablename__ = "todo"
    id = db.Column('id', db.Integer, primary_key=True) #ID of task - hidden from user 
    name = db.Column('name', db.Unicode) #Name of Task
    description = db.Column('description', db.Unicode) #Description of Task
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow) #Defaults to current date
    is_done = db.Column('is_done', db.Boolean, default= False) #Used for marking process as done