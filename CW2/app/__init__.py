from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import LoginManager, login_required
app = Flask(__name__)
#set up flask-login here
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

#pipe through bootstrap
Bootstrap(app)
app.config.from_object('config')

#set up ORM
db = SQLAlchemy(app)

from app import views
from .models import User




