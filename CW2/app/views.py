from flask import render_template, flash, redirect, request
from .models import *
from app import app
from .forms import *

@app.route('/', methods = ['GET', 'POST'])
def list_all():
    return render_template(
        'list.html',
        todos=ToDo.query.filter_by(is_done = False).all() ,
        title = "ToDo - Tasks To Complete"
    )


@app.route('/newTask', methods=['GET', 'POST'])
def new():
    form = ToDoList()

    if form.validate_on_submit():
        todo = ToDo(name=form.name.data ,description= form.description.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            'new-task.html',
            page='new-task',
            form = form,
            title = "ToDo - Create New Task"
        )

@app.route('/edit_db/<id>')
def editDB(id):
    x = ToDo.query.get(id)
    if x.is_done == False:
        x.is_done = True
        db.session.commit()
        return redirect('/')
    else:
        x.is_done = False
        db.session.commit()
        return redirect('/')

@app.route('/delete_db/<id>')
def deleteDB(id):
    x = ToDo.query.get(id)
    db.session.delete(x)
    db.session.commit()
    return redirect('/viewcomplete')


@app.route('/viewcomplete')
def viewTask():
        return render_template(
        'list.html',
        todos=ToDo.query.filter_by(is_done = True).all(), #primaryJoin(Priority).order_by(Priority.value.desc())
        title = "ToDo - Completed Tasks"
    )