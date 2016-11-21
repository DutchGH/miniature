from flask import render_template, flash, redirect, request
from .models import *
from app import app
from .forms import *

#Home Page - Display all Pending Tasks by filtering DB
@app.route('/', methods = ['GET', 'POST'])
def list_all():
    return render_template(
        'list.html',
        todos=ToDo.query.filter_by(is_done = False).all() ,
        title = "ToDo - Tasks To Complete"
    )

#Page for creating new task
@app.route('/newTask', methods=['GET', 'POST'])
def new():
    form = ToDoList()

    #If the user submits data, grab the data from the fields, create a new DB entry with it
    if form.validate_on_submit():
        todo = ToDo(name=form.name.data ,description= form.description.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        #If request is GET - then load the webpage 
        return render_template(
            'new-task.html',
            page='new-task',
            form = form,
            title = "ToDo - Create New Task"
        )

#Used for editing the is_done var in the DB
@app.route('/edit_db/<id>')
def editDB(id):
    #Get the ID of the database entry and alter it's is done var - refresh page
    x = ToDo.query.get(id)
    if x.is_done == False:
        x.is_done = True
        db.session.commit()
        return redirect('/')
    else:
        x.is_done = False
        db.session.commit()
        return redirect('/')

#DELETE ENTRY FROM DB
@app.route('/delete_db/<id>')
def deleteDB(id):
    x = ToDo.query.get(id)
    db.session.delete(x)
    db.session.commit()
    return redirect('/viewcomplete')

#Filter and display Complete tasks only 
@app.route('/viewcomplete')
def viewTask():
        return render_template(
        'list.html',
        todos=ToDo.query.filter_by(is_done = True).all(), #primaryJoin(Priority).order_by(Priority.value.desc())
        title = "ToDo - Completed Tasks"
    )