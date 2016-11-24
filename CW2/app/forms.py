from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.validators import url


class shortenerForm(FlaskForm):
	longURL = URLField('url', validators = [url()])

# class loginForm(FlaskForm):
# 	user_name
# 	password