from flask import render_template, flash, redirect, request, abort
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
	return 'LOGIN HERE YOU BUM'


