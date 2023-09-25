from flask_wtf import FlaskForm # The WTF is a built-in module of the flask which provides an alternative way of designing forms in the flask web applications. Importing FlaskForm argument.
from wtforms import StringField, IntegerField, BooleanField, SubmitField # Importing the types of fields that will be used in the form.
from wtforms.validators import DataRequired, Email # Validators: Prevent users from skipping or putting incorrect into a field.


class SignUpForm(FlaskForm): # Create a class function for the field
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(message="not a valid email")])
    mobile = IntegerField()
    country = StringField(validators=[DataRequired()])
    newsletter = BooleanField('Weekly Digest')
    submit = SubmitField()

