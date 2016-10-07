from flask import render_template, flash, redirect, request
from .models import *
from app import app
from .forms import *



@app.route('/', methods = ['GET', 'POST'])
def list_all():
    return render_template(
        'list.html',
        todos=ToDo.query.all() #primaryJoin(Priority).order_by(Priority.value.desc())
    )


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s + %s = %s'%(form.number1.data, form.number2.data, form.number3.data, form.number1.data+form.number2.data+form.number3.data))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)

@app.route('/newTask', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        todo = ToDo(description=request.form['description'])
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            'new-task.html',
            page='new-task',
        )

@app.route('/mark-done/<int:todo_id>', methods=['POST'])
def mark_done(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        todo.is_done = True
        db.session.commit()
        return redirect('/')


@app.route('/viewcomplete')
def viewTask():
    return 'VIEW TASKS'