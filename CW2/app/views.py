from flask import render_template, flash, redirect, request, abort, g, Markup
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

@app.route('/createprofile', methods = ['GET', 'POST'])
def create():
	form = RegistrationForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			first =  form.first_name.data
			last = form.last_name.data
			username = form.username.data
			email = form.email.data
			password = form.password.data
			confirm = form.confirm.data
			data = User(user_name = username, email = email, password = password, first_name = first, last_name = last)
			db.session.add(data)
			db.session.commit()
			return redirect ('/')
		else:
			return render_template('signup.html', form = form)
	return render_template('signup.html', form = form)


@app.route('/profile/<nickname>')
@login_required
def profile(nickname):
	user = User.query.filter_by(user_name = nickname).first()
	posts = g.user.generated_links()
	if user == None:
		flash('User %s not found.' % nickname)
		return redirect(url_for('index'))
	return render_template('profile.html', user = user, posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user.is_authenticated:
		flash('You are already logged in. Please logout to login')
		return redirect('/')
	
	error = None
	form = loginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			username = User.query.filter_by(user_name = request.form['username']).first()
			if username is not None and (username.password == request.form['password']):
				login_user(username)
				#session['logged_in'] = True
				flash(Markup('You were logged in. Wrong User? <a href = "/logout">Click Here<a>'))
				return redirect('/')
			else:
				error = 'Invalid Credentials'
	return render_template('login.html', form = form, error = error)

@app.route('/editprofile/<id>', methods = ['GET', 'POST'])
@login_required
def editprofile(id):
    #Get the ID of the database entry and alter it's is done var - refresh page
    x = ToDo.query.get(id)
    if x.is_done == False:
        x.is_done = True
        db.session.commit()
        return redirect('/')



@app.route('/logout')
def logout():
	logout_user()
	flash('You were logged out.')
	return redirect('/')




