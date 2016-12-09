from flask import render_template, flash, redirect, request, abort, g, Markup, url_for
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
			flash('Profile Created')
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
		return redirect('/')
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
				flash('Invalid Credentials. Please Try Again')
	return render_template('login.html', form = form, error = error)

@app.route('/editprofile', methods = ['GET', 'POST'])
@login_required
def editprofile():
    #Get the ID of the database entry and alter it's is done var - refresh page
    x = User.query.get(g.user.id)
    form = editForm()
    if request.method == 'POST':
    	if form.validate_on_submit():
		    new_first = form.new_first_name.data
		    new_last = form.new_last_name.data
		    old_password = form.old_password.data
		    new_password = form.password.data
		    confirm = form.confirm.data
		    if new_first is not '':
		    	x.first_name = new_first
		    if new_last is not '':
		    	x.last_name = new_last
		    if new_password is not None and new_password == confirm and old_password == x.password:
		    	x.password = new_password
		    db.session.commit()
		    flash("Your Profile Has Been Updated")
		    return redirect(url_for('profile', nickname = g.user.user_name))
	    flash("There was a problem updating your credentials. Try again.")
    return render_template('edit.html', form = form)
    



@app.route('/logout')
def logout():
	logout_user()
	flash('You were logged out.')
	return redirect('/')




