from flask import Flask
from flask_material import Material
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
Material(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views

