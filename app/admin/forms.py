from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class CentreForm(FlaskForm):
    """
    Form for admin to add or edit a centre
    """

    serviceApprovalNumber = StringField('Service Approval Number', validators = [DataRequired()])
    providerApprovalNumber = StringField('Provider Approval Number', validators = [DataRequired()])
    serviceName = StringField('Service Name', validators = [DataRequired()])
    providerLegalName = StringField('Provider Legal Name', validators = [DataRequired()])
    serviceAddress = StringField('Service Address', validators = [DataRequired()])
    suburb = StringField('Suburb', validators = [DataRequired()])
    state = StringField('State', validators = [DataRequired()])
    postcode = IntegerField('Postcode', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    fax = StringField('Fax', validators = [DataRequired()])
    emailAddress = StringField('Email', validators = [DataRequired()])
    conditionsOnApproval = StringField('Conditions on Approval', validators = [DataRequired()])
    numberOfApprovedPlaces = IntegerField('Number of Approved Places', validators = [DataRequired()])
    overallRating = StringField('Overall Rating', validators = [DataRequired()])
    type = StringField('Type', validators = [DataRequired()])
    submit = SubmitField('Submit')