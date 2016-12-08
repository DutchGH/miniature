from datetime import datetime
from app import db
from sqlalchemy.orm import relationship



#Association, so that a generated URL can have owenership by multiple users (being the 'children' of the URL)
gens = db.Table('gens',
	db.Column('generator_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('url_id', db.Integer, db.ForeignKey('url.id')),
	)

# class Association(db.Model):
# 	__tablename__ = 'association'
# 	url_id = db.Column(db.Integer, db.ForeignKey('url.id'), primary_key = True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
# 	child = relationship("url_table")


#Table to store the shortened URLS and its corresponding parent URLS
class url_table(db.Model):
    __tablename__ = "url"
    id = db.Column('id', db.Integer, primary_key=True)
    short_url = db.Column('url', db.String(100))
    long_url = db.Column(db.Text)

    # usergens = db.relationship('User', secondary=gens, 
    # 	backref = db.backref('generated', lazy = 'dynamic'))


    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url


#User model, will be implemented with Flask-Login and Flask-Security
class User(db.Model):
	__tablename__ = "user"
	id = db.Column('id', db.Integer, primary_key = True)
	user_name = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(500), index = True, unique = True)
	password = db.Column(db.String(500))
	first_name = db.Column(db.String(500))
	last_name = db.Column(db.String(500))

	generated = db.relationship('url_table',
		secondary = gens,
		primaryjoin = (gens.c.generator_id == id),
		secondaryjoin = (gens.c.url_id == url_table.id),
		backref = db.backref('gens', lazy='dynamic'), lazy='dynamic')

	def has_generated(self, genURL):
		return self.generated.filter(
			gens.c.url_id == genURL.id).count() > 0

	def follow(self, genURL):
		if not self.has_generated(genURL):
			self.generated.append(genURL)
			return self





	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.user_name)



# # create parent, append a child via association
# p = Parent()
# a = Association(extra_data="some data")
# a.child = Child()
# p.children.append(a)

# # iterate through child objects via association, including association
# # attributes
# for assoc in p.children:
#     print(assoc.extra_data)
#     print(assoc.child)


   