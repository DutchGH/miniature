from flask import render_template, flash, redirect, request
from .models import *
from app import app
from .forms import *

@app.route('/', methods = ['GET', 'POST'])
def list_all():
    return render_template(
        'index.html',
         title = "JAPHABYTES - MAIN")