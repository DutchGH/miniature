from flask import render_template, flash, redirect, request, abort, g 
from flask_login import login_user, current_user, logout_user, login_required
from .models import *
from app import app, lm
from .shorty import *
from .forms import *

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))


@app.before_request
def before_request():
	g.user = current_user 


@app.route('/', methods = ['GET', 'POST'])
def index():
	user = g.user
	form = shortenerForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			long_url = form.longURL.data
			short_url = shorty(long_url)
			if g.user is not None and g.user.is_authenticated:
				return render_template('index.html', form=form, short_url = short_url, user = user)
			else:
				return render_template('index.html', form=form, short_url = short_url)
		else:
			if g.user is not None and g.user.is_authenticated:
				return render_template('index.html', form = form, user = user)
			else:
				return render_template('index.html', form = form)
	else:
		if g.user is not None and g.user.is_authenticated:
			return render_template('index.html', form=form, user = user)
		else:
			return render_template('index.html', form = form)



@app.route('/<string:short_url>')
def moveToURL(short_url):
	shorturl_query = url_table.query.filter_by(short_url=short_url).first()
	if shorturl_query is None:
		abort(404)
	else:
		return redirect(shorturl_query.long_url)

@app.route('/profile/<nickname>')
@login_required
def profile(nickname):
	user = User.query.filter_by(user_name = nickname).first()
	if user == None:
		flash('User %s not found.' % nickname)
		return redirect(url_for('index'))
	return user.user_name


@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	form = loginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = User.query.filter_by(user_name = request.form['username']).first()
			if username is not None and (username.password == request.form['password']):
				login_user(username)
				#session['logged_in'] = True
				flash('You were logged in.')
				return redirect('/')
			else:
				error = 'Invalid Credentials'
	return render_template('login.html', form = form, error = error)


@app.route('/logout')
def logout():
	logout_user()
	flash('You were logged out.')
	return redirect('/')




