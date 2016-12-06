from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views
from .models import User

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()

