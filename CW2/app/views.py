from flask import render_template, flash, redirect, request
from .models import *
from app import app
from .shorty import *
from .forms import *

@app.route('/', methods = ['GET', 'POST'])
def list_all():
	if request.method == 'POST':
		form = shortenerForm(request.form)
		if form.validate_on_submit():
			long_url = form.longURL.data
			short_url = shorty(long_url)
			return render_template('index.html', form=form)
		else:
			return render_template('index.html', form=form)

	else:
		return render_template('index.html', form=shortenerForm())


@app.route('/login', methods = ['GET', 'POST'])
def login():
	return 'LOGIN HERE YOU BUM'