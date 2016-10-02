from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class CalculatorForm(Form):
    number1 = IntegerField ('number1', validators= [DataRequired()])
    number2 = IntegerField ('number2', validators=[DataRequired()])