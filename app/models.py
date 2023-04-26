# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, caption, photo, user_id):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id

class Like(db.Model):

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

class Follow(db.Model):

    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id


class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120))
    biography = db.Column(db.String(255))
    profile_photo = db.Column(db.String(255))
    joined_on = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, username, password, email, firstname, lastname, location, biography, profile_photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username