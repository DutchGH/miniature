from flask import render_template, flash, redirect
from app import app
from .forms import CalculatorForm

@app.route('/')
@app.route('/index')
def index():
    return 'Hello Jake!'

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s  = %s'%(form.number1.data, form.number2.data, form.number1.data+form.number2.data))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)