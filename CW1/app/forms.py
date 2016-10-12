from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField ('number1', validators= [InputRequired()])
    number2 = IntegerField ('number2', validators=[InputRequired()])
    number3 = IntegerField ('number3', validators=[InputRequired()])

class ToDoList(FlaskForm):
    description =  StringField ('description', validators= [InputRequired()])
    is_done = BooleanField ('is_done')