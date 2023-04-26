"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, url_for, send_from_directory
import os
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Post, Follow, Like
from app.forms import UserForm, LoginForm, PostForm
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/api/v1/register', methods=['POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = request.form['username']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        location = request.form['location']
        biography = request.form['biography']
        profile_photo = request.files['profile_photo']
        
        # check if username or email is already taken
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({"error": "Username already taken"}), 409
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"error": "Email associated with another account"}), 409
        
        # process and save the profile photo
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # create a new User object and save it to the database
        user = User(username=username, password=confirm_password, firstname=firstname, lastname=lastname, email=email, location=location, biography=biography, profile_photo=filename)
        db.session.add(user)
        try:
            db.session.commit()

            response = {
                "message": "User successfully added",
                "username": user.username,
                "email": user.email,
            }
            return jsonify(response), 200
        except  Exception as e:
            return jsonify({"error":"Failed to register"}), 500
    else:
        errors = form_errors(form)
        response = {"errors": errors}
        return jsonify(response), 409

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Get the username and password values from the form.
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username="qq").first()

        if user is None or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        login_user(user)
        return jsonify({'message': 'Login successful'})



@app.route('/api/v1/users/{user_id}/posts', methods=['POST'])
@login_required
def post():
    form =  PostForm()
    if form.validate_on_submit():
        photo = request.files['photo']
        caption = request.form['caption']
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # create a new User object and save it to the database
        post = Post(photo=filename, caption=caption)
        db.session.add(post)
        try:
            db.session.commit()

            response = {
                "message": "Photo successfully posted",
            }
            return jsonify(response), 200
        except  Exception as e:
            return jsonify({"error":"Failed to post photo"}), 500
    else:
        errors = form_errors(form)
        response = {"errors": errors}
        return jsonify(response), 409
