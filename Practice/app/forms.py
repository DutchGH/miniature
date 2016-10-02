from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField ('number1', validators= [DataRequired()])
    number2 = IntegerField ('number2', validators=[DataRequired()])
    number3 = IntegerField ('number3', validators=[DataRequired()])