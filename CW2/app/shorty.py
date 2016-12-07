import random
import string

from app import db
from app.models import *
from flask import request, g
from urllib.request import HTTPError, Request, urlopen 

def random_string(size):
	random_string = ''.join(random.choice(string.ascii_letters + string.digits) 
		for x in range(size))
	return random_string


def shorty(long_url):
	user = g.user
	longurl_query = url_table.query.filter_by(long_url = long_url).first()
	if longurl_query is None:
		for x in range(6,11):
			short_url = random_string(x)
			shorturl_query = url_table.query.filter_by(short_url=short_url).first()
			if shorturl_query is None:
				data = url_table(short_url, long_url)
				if user is not None and user.is_authenticated:
					db.session.add(data)
					db.session.commit()
					return request.url_root + short_url

				db.session.add(data)
				db.session.commit()
				return request.url_root + short_url
	else:
		return request.url_root + longurl_query.short_url