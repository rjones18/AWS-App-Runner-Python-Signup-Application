from flask import render_template, redirect, url_for, flash 
from app import application # Importing the application module.
from app.forms import SignUpForm # Importing the SignUpForm class function from the forms.py file 
import boto3 # The AWS SDK for Python.

# dynamodb
db = boto3.resource('dynamodb', region_name='us-east-2')
table = db.Table('nameofyourtable')

# sns
notification = boto3.client('sns', region_name='us-east-2')
topic_arn = 'arn:aws:sns:us-east-2:XXXXXXXX'


@application.route('/')
@application.route('/home') # Routing the default page and home page to the home.html file.
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST']) # Routing the signup page based off users actions. When first going to the page it does a GET request and returns the signup.html page but if the user puts in the information on this page is successfully POST it then it return the pop-up and rediect them to the home page.
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit(): # If the data entered by the user passes all the validations we defined in the 
        table.put_item(
            Item={
                'name': form.name.data, 'email': form.email.data,
                'mobile': form.mobile.data, 'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        ) # Putting the users information into the dynamo db table
        msg = 'Congratulations !!! {} is now a Premium Member !'.format(form.name.data)
        flash(msg) # Creates a pop-up message when the form is successfully saved
        # Email is sent to me that a user signed up
        email_message = '\nname: {} ' \
                        '\nmobile: {} ' \
                        '\nemail: {} ' \
                        '\ncountry: {}'.format(form.name.data, form.mobile.data, form.email.data, form.country.data)
        notification.publish(Message=email_message, TopicArn=topic_arn, Subject="You've Got A Mail")
        return redirect(url_for('home_page')) # Redirect user to the home page
    return render_template('signup.html', form=form) # Return the signup.html page

