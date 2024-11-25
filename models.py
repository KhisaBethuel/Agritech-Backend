from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class UserCommunity(db.Model):
    __tablename__ = 'user_community'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'), primary_key=True)

    user = db.relationship('User', back_populates='communities_joined')
    community = db.relationship('Community', back_populates='members')

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    password_hash  = db.Column(db.String(255), nullable=False)

    blogs = db.relationship('Blog', back_populates='user')
    experts = db.relationship('Expert', back_populates='user')
    communities = db.relationship('Community', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    likes = db.relationship('Like', back_populates='user')
    communities_joined = db.relationship('UserCommunity', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if not email or '@' not in email:
            raise ValueError("Provided email is not valid")
        return email

    @validates('username')
    def validate_username(self, key, username):
        if not username.strip():
            raise ValueError("Username cannot be empty")
        return username

class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), nullable=True)

    user = db.relationship('User', back_populates='blogs')
    comments = db.relationship('Comment', back_populates='blog')
    likes = db.relationship('Like', back_populates='blog')
    expert = db.relationship('Expert', back_populates='blogs')

    @validates('title')
    def validate_title(self, key, title):
        assert title != '', "Title cannot be empty"
        return title
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "image": self.image,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "expert_id": self.expert_id,
            "comments": [comment.to_dict() for comment in self.comments],
            "likes": len(self.likes)
        }

class Expert(db.Model, SerializerMixin):
    __tablename__ = 'experts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    expertise_field = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='experts')
    blogs = db.relationship('Blog', back_populates='expert', cascade="all, delete-orphan")

    @validates('username', 'expertise_field')
    def validate_fields(self, key, value):
        assert value != '', f"{key} cannot be empty"
        return value
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "expertise_field": self.expertise_field,
            "profile_image": self.profile_image,
            "user_id": self.user_id,
            "blogs": [blog.to_dict() for blog in self.blogs]
        }

class Community(db.Model, SerializerMixin):
    __tablename__ = 'communities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates='communities')
    members = db.relationship('UserCommunity', back_populates='community')

    @validates('description')
    def validate_description(self, key, description):
        assert description != '', "Description cannot be empty"
        return description
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "image": self.image,
            "user_id": self.user_id,
            "username": self.user.username if self.user else None,
            "members": [user_community.user.username for user_community in self.members]
        }

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages')

    serialize_rules = ('-sender.sent_messages', '-recipient.received_messages')

    @validates('content')
    def validate_content(self, key, content):
        assert content != '', "Content cannot be empty"
        return content

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "created_at": self.created_at.isoformat(),
            "sender": {
                "id": self.sender.id,
                "username": self.sender.username,
            } if self.sender else None,
            "recipient": {
                "id": self.recipient.id,
                "username": self.recipient.username,
            } if self.recipient else None,
        }


class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 

    user = db.relationship('User', back_populates='comments')
    blog = db.relationship('Blog', back_populates='comments')

    @validates('content')
    def validate_content(self, key, content):
        assert content != '', "Content cannot be empty"
        return content

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_at": self.created_at,
            "user": {
                "id": self.user.id,
                "username": self.user.username
            },
            "blog": {
                "id": self.blog.id,
                "title": self.blog.title
            }
        }

class Like(db.Model, SerializerMixin):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='likes')
    blog = db.relationship('Blog', back_populates='likes')
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_at": self.created_at,
            "user": {"id": self.user.id, "username": self.user.username},
            "blog": {"id": self.blog.id, "title": self.blog.title}
        }


class UserFollow(db.Model):
    __tablename__ = 'user_follows'

    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    follower = db.relationship('User', foreign_keys=[follower_id], backref='following')
    followed = db.relationship('User', foreign_keys=[followed_id], backref='followers')

    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id


class ExpertFollow(db.Model):
    __tablename__ = 'expert_follows'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    expert_id = db.Column(db.Integer, db.ForeignKey('experts.id'), primary_key=True)

    user = db.relationship('User', backref='expert_following')
    expert = db.relationship('Expert', backref='followers')

    def __init__(self, user_id, expert_id):
        self.user_id = user_id
        self.expert_id = expert_id
