from app import db

class toDoList(db.Model):
    id = db.Column (db.Integer, primary_key =  True)
    taskDesc = db.Column (db.String[500], index = True)
    taskComplete = db.Column (db.Boolean)
