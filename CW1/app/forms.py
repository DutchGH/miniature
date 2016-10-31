from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired

#Form for data entry - used to process data for Db
class ToDoList(FlaskForm):
	name = StringField ('name', validators = [InputRequired()])
	description = StringField ('description', validators= [InputRequired()])
	is_done = BooleanField ('is_done')