from flask import render_template, flash, redirect
from app import app
from .forms import CalculatorForm

# index view function suppresed

@app.route('/')
def index():
    return 'HELLO WORLD'


@app.route('/calculator', methods=['GET', 'POST'])
def login():
    def calculator():
        form = CalculatorForm()
        if form.validate_on_submit():
            flash('Succesfully received form data. %s + %s  = %s' % (
                form.number1.data, form.number2.data, form.number1.data + form.number2.data))
        return render_template('calculator.html',
                               title='Calculator',
                               form=form)
