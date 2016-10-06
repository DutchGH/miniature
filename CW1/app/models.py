from app import db

class ToDo(db.Model):
    __tablename__ = "todo"
    id = db.Column('id', db.Integer, primary_key=True)
    priority_id = db.Column('priority_id', db.Integer, db.ForeignKey('priority.id'))
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date)
    is_done = db.Column('is_done', db.Boolean, default= False)

    priority = db.relationship('Priority', foreign_keys = priority_id,
                               backref = "todos")


class Priority(db.Model):
    __tablename__ = "priority"
    id = db.Column('id', db.Integer, primary_key= True)
    name = db.Column('name', db.Unicode)
    value = db.Column('value', db.Integer)


