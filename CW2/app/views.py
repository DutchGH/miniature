from flask import render_template, flash, redirect, request, abort
from flask.ext.login import login_user
from .models import *
from app import app
from .shorty import *
from .forms import *

@app.route('/', methods = ['GET', 'POST'])
def list_all():
	if request.method == 'GET':
		return render_template('index.html', form=shortenerForm())
	else:
		form = shortenerForm()
		if form.validate_on_submit():
			long_url = form.longURL.data
			short_url = shorty(long_url)
			return render_template('index.html', form=form, short_url = short_url)
		else:
			return render_template('index.html', form=form)



@app.route('/<string:short_url>')
def moveToURL(short_url):
	shorturl_query = url_table.query.filter_by(short_url=short_url).first()
	if shorturl_query is None:
		abort(404)
	else:
		return redirect(shorturl_query.long_url)



@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	form = loginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = User.query.filter_by(user_name = request.form['username']).first()
			if User is not None and User.password == request.form['password']:
				login_user(user)
				flash('You were logged in.')
				return redirect('/')
			else:
				error = 'Invalid Credentials'
	return render_template('login.html', form = form, error = error)


@app.route('/logout')
def logout():
	return 'GET OUT'


