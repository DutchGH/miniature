import random
import string

from app import db
from app.models import url
from flask import requests
from urllib.request import HTTPError, Request, urlopen 

def random_string(size):
	random_string = ''.join(random.choce(string.ascii_letters + string.digits) 
		for x in range(size))
	return random_string


def shorty(long_url)
	longurl_query = url.query.filter_by(long_url = long_url).first()
	if longurl_query is None:
		for x in range(6,11):
			short_url = random_string(x)
			shorturl_query = url.query.filter_by(short_url=short_url).first()
			if short_url is None:
				data = url(short_url, long_url)
				db.session.add(data)
				db.session.commit()
				return request.url_root + short_url
	else:
		return request.url_root + longurl_query.short_url