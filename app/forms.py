# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf.file import FileAllowed, FileRequired

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    location = StringField('Location')
    biography = StringField('Biography')
    profile_photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class PostForm(FlaskForm):
    profile_photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    caption = TextAreaField('Caption', validators=[DataRequired()])
