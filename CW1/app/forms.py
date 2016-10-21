from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired


class ToDoList(FlaskForm):
	name = StringField ('name', validators = [InputRequired()])
	description = StringField ('description', validators= [InputRequired()])
	is_done = BooleanField ('is_done')