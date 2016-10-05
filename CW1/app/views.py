from flask import render_template, flash, redirect
from app import app
from .forms import CalculatorForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home Page')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s + %s = %s'%(form.number1.data, form.number2.data, form.number3.data, form.number1.data+form.number2.data+form.number3.data))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)

@app.route('/newtask', methods=['GET','POST'])
def newTask():
    return 'Create a New Task Here'

@app.route('/viewtask')
def viewTask():
    return 'VIEW TASKS'