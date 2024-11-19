#!/usr/bin/env python3
from app import app
from models import db, User, Blog, Expert, Community, Message, Comment, Like
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash

utc_now = datetime.now(timezone.utc)

with app.app_context():
    # Delete existing data to prevent duplicates
    print("Deleting data...")
    Like.query.delete()
    Comment.query.delete()
    Message.query.delete()
    Community.query.delete()
    Expert.query.delete()
    Blog.query.delete()
    User.query.delete()

    print("Creating users...")
    alice = User(username="alice", email="alice@example.com")
    alice.set_password("password123")
    bob = User(username="bob", email="bob@example.com")
    bob.set_password("password123")
    charlie = User(username="charlie", email="charlie@example.com")
    charlie.set_password("password123")
    users = [alice, bob, charlie]

    print("Creating blogs...")
    blog1 = Blog(title="Tech Trends in 2024", content="The latest trends in technology...", created_at=utc_now, user=alice)
    blog2 = Blog(title="AI for Healthcare", content="How AI is transforming healthcare...", created_at=utc_now, user=bob)
    blogs = [blog1, blog2]

    print("Creating experts...")
    expert1 = Expert(username="john_doe", expertise_field="AI", profile_image="expert1.jpg", user=bob)
    expert2 = Expert(username="jane_doe", expertise_field="Cybersecurity", profile_image="expert2.jpg", user=charlie)
    experts = [expert1, expert2]

    print("Creating communities...")
    community1 = Community(name= "Techies group", description="Tech Enthusiasts", created_at=utc_now, user=alice)
    community2 = Community(name= "Ai experts", description="AI Experts", created_at=utc_now, user=bob)
    communities = [community1, community2]

    print("Creating comments...")
    comment1 = Comment(content="Great post, thanks for sharing!", created_at=utc_now, user=charlie, blog=blog1)
    comment2 = Comment(content="Very informative, I agree with your points!", created_at=utc_now, user=alice, blog=blog2)
    comments = [comment1, comment2]

    print("Creating likes...")
    like1 = Like(user=alice, blog=blog1)
    like2 = Like(user=bob, blog=blog2)
    likes = [like1, like2]

    # Add all data to the session and commit
    db.session.add_all(users)
    db.session.add_all(blogs)
    db.session.add_all(experts)
    db.session.add_all(communities)
    db.session.add_all(comments)
    db.session.add_all(likes)
    db.session.commit()

    print("Seeding done!")
