from flask import render_template, redirect, url_for, request
from flask_login import login_required

from . import home

import requests

base_url = 'http://localhost:8080'

@home.route('/')
def homepage():
	return render_template('home/index.html', title = 'Welcome')

@home.route('/search')
def search():
	"""
	Search a Childcare Centre
	"""
	url = base_url+'/centres'
	centres = requests.get(url).json()

	return render_template('home/search.html', centres = centres, title="Search")
