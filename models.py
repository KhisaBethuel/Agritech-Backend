from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    password_hash = db.Column(db.String(255), nullable=False)

    blogs = db.relationship('Blog', back_populates='user')
    experts = db.relationship('Expert', back_populates='user')
    communities = db.relationship('Community', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    likes = db.relationship('Like', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Provided email is not valid"
        return email

    @validates('username')
    def validate_username(self, key, username):
        assert username != '', "Username cannot be empty"
        return username

class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='blogs')
    comments = db.relationship('Comment', back_populates='blog')
    likes = db.relationship('Like', back_populates='blog')

    @validates('title')
    def validate_title(self, key, title):
        assert title != '', "Title cannot be empty"
        return title

class Expert(db.Model, SerializerMixin):
    __tablename__ = 'experts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    expertise_field = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='experts')

    @validates('username', 'expertise_field')
    def validate_fields(self, key, value):
        assert value != '', f"{key} cannot be empty"
        return value

class Community(db.Model, SerializerMixin):
    __tablename__ = 'communities'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='communities')

    @validates('description')
    def validate_description(self, key, description):
        assert description != '', "Description cannot be empty"
        return description

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime)

    @validates('content')
    def validate_content(self, key, content):
        assert content != '', "Content cannot be empty"
        return content

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    created_at = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='comments')
    blog = db.relationship('Blog', back_populates='comments')

    @validates('content')
    def validate_content(self, key, content):
        assert content != '', "Content cannot be empty"
        return content

class Like(db.Model, SerializerMixin):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='likes')
    blog = db.relationship('Blog', back_populates='likes')
