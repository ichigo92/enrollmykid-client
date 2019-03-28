from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import CentreForm

import requests

base_url = 'http://localhost:8080'


@admin.route('/dashboard', methods = ['GET', 'POST'])
# @login_required
def dashboard():
	"""
	Dashboard view
	"""
	url = base_url+'/centres'
	centres = requests.get(url).json()

	return render_template('admin/dashboard.html', centres = centres, title="Dashboard")

@admin.route('/dashboard/add', methods = ['GET', 'POST'])
#@login_required
def add_centre():
	"""
	Add Centre
	"""

	add_centre = True

	url = base_url+'/centres'

	form = CentreForm()
	if form.validate_on_submit():
		service_approval_number = form.serviceApprovalNumber.data
		provider_approval_number = form.providerApprovalNumber.data
		service_name = form.serviceName.data
		provider_legal_name = form.providerLegalName.data
		service_address = form.serviceAddress.data
		suburb = form.suburb.data
		state = form.state.data
		postcode = form.postcode.data
		phone = form.phone.data
		fax = form.fax.data
		email_address = form.emailAddress.data
		conditions_on_approval = form.conditionsOnApproval.data
		number_of_approved_places = form.numberOfApprovedPlaces.data
		overall_rating = form.overallRating.data
		type = form.type.data

		try:
			requests.post(url, data = {'centres':centres})
		except:
			flash('Service name already exists')
		return redirect(url_for('admin.dashboard'))

	return render_template('admin/centre.html', action = 'Add', add_centre = add_centre, form = form, title="Add Centre")



@admin.route('/dashboard/edit/<int:id>', methods = ['GET', 'POST'])
#@login_required
def edit_centre(id):
	"""
	Edit Centre
	"""

	add_centre=False

	url = base_url+'/centres/{id}'
	url = url.format(id = id)

	centre = requests.get(url).json()
	print(centre)
	print(centre['service_approval_number'])

	form = CentreForm(obj=centre)
	if form.validate_on_submit():
		centre['service_approval_number'] = form.serviceApprovalNumber.data
		centre['provider_approval_number'] = form.providerApprovalNumber.data
		centre['service_name'] = form.serviceName.data
		centre['provider_legal_name'] = form.providerLegalName.data
		centre['service_address'] = form.serviceAddress.data
		centre['suburb'] = form.suburb.data
		centre['state'] = form.state.data
		centre['postcode'] = form.postcode.data
		centre['phone'] = form.phone.data
		centre['fax'] = form.fax.data
		centre['email_address'] = form.emailAddress.data
		centre['conditions_on_approval'] = form.conditionsOnApproval.data
		centre['number_of_approved_places'] = form.numberOfApprovedPlaces.data
		centre['overall_rating'] = form.overallRating.data
		centre['type'] = form.type.data
		requests.put(url, data = {'centre': centre})
		flash('You have successfully edited the centre')

		return redirect(url_for('admin.dashboard'))

	return render_template('admin/centre.html', action='Edit', add_centre=add_centre, form = form, centre = centre, title='Edit Centre')

@admin.route('/dashboard/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
def delete_centre(id):
	"""
	Delete Centre
	"""

	url = base_url+'/centres/{id}'
	url = url.format(id = id)

	centre = requests.delete(url).json()

	flash('You have successfully deleted the centre')

	return redirect(url_for('admin.dashboard'))

@admin.route('/dashboard/save/<int:id>', methods=['GET', 'POST'])
def save_centre(id):
	url = base_url+'/save/{id}'
	url = url.format(id = id)
	requests.get(url)