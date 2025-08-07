from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
  name = StringField('Name', validators=[
    DataRequired(message="Name is required."), 
    Length(min=3, max=100, message="Name must be between 3 and 100 characters.")
  ])
  email = EmailField('Email', validators=[
    DataRequired(message="Email is required."), 
    Email(message="Invalid email format.")
  ])
  message = TextAreaField('Message', validators=[
    DataRequired(message='Message is required.'), 
    Length(min=10, max=500, message="Message must be between 10 and 500 characters.")])
  submit = SubmitField('Send')