#!/usr/bin/env python3
from app import app
from models import db, User, Blog, Expert, Community, Message, Comment, Like
from datetime import datetime, timezone

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
    blogs = [
        Blog(
            title="The Rise of Smart Farming in Africa",
            content="How smart farming technologies like IoT and drones are transforming agriculture in Africa.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1576765607926-47a8ee9e3f33?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Sustainable Agriculture: Key to Africa’s Food Security",
            content="A deep dive into sustainable practices that are helping farmers combat climate change and increase yields.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1573497491208-6b1acb260507?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Agroforestry: Merging Conservation with Productivity",
            content="Agroforestry is emerging as a solution to balance ecological conservation with increased agricultural productivity.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Digital Platforms Connecting African Farmers",
            content="How mobile apps and digital platforms are empowering African farmers with market access and knowledge.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1589311051443-1b3f72a15540?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Irrigation Innovation in Dry Regions",
            content="Exploring innovative irrigation systems transforming farming in Africa's arid and semi-arid regions.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1559072133-b5baedf9b7f3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Youth in Agriculture: Changing the Narrative",
            content="How young entrepreneurs in Africa are embracing agriculture as a lucrative career path.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1580910051070-d9f0fbc1dfb3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Organic Farming: The Future of African Agriculture?",
            content="The shift towards organic farming and its potential to meet growing demand for sustainable products.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="The Role of Women in African Agriculture",
            content="Women contribute significantly to Africa's agriculture. Here’s how they are shaping the sector’s future.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1588196722065-879c64c012ce?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="How AI is Revolutionizing Agriculture in Africa",
            content="The impact of AI-driven solutions on crop management, pest control, and forecasting in Africa.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1598514982172-7ba8c78d7aaf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Harnessing Renewable Energy for African Farms",
            content="The use of solar and wind energy in powering agricultural operations in remote areas.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1581091870631-3c8aa564fdb5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="The Rise of Smart Farming in Africa",
            content="How smart farming technologies like IoT and drones are transforming agriculture in Africa.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1576765607926-47a8ee9e3f33?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Sustainable Agriculture: Key to Africa’s Food Security",
            content="A deep dive into sustainable practices that are helping farmers combat climate change and increase yields.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1573497491208-6b1acb260507?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Agroforestry: Merging Conservation with Productivity",
            content="Agroforestry is emerging as a solution to balance ecological conservation with increased agricultural productivity.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Digital Platforms Connecting African Farmers",
            content="How mobile apps and digital platforms are empowering African farmers with market access and knowledge.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1589311051443-1b3f72a15540?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Irrigation Innovation in Dry Regions",
            content="Exploring innovative irrigation systems transforming farming in Africa's arid and semi-arid regions.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1559072133-b5baedf9b7f3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Youth in Agriculture: Changing the Narrative",
            content="How young entrepreneurs in Africa are embracing agriculture as a lucrative career path.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1580910051070-d9f0fbc1dfb3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Organic Farming: The Future of African Agriculture?",
            content="The shift towards organic farming and its potential to meet growing demand for sustainable products.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="The Role of Women in African Agriculture",
            content="Women contribute significantly to Africa's agriculture. Here’s how they are shaping the sector’s future.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1588196722065-879c64c012ce?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="How AI is Revolutionizing Agriculture in Africa",
            content="The impact of AI-driven solutions on crop management, pest control, and forecasting in Africa.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1598514982172-7ba8c78d7aaf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Harnessing Renewable Energy for African Farms",
            content="The use of solar and wind energy in powering agricultural operations in remote areas.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1581091870631-3c8aa564fdb5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        
        Blog(
            title="Crop Diversification for Resilient Farming",
            content="How crop diversification reduces risks and enhances resilience in African agriculture.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1501850305723-0bf5d51d1d43?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Integrating Blockchain in Agriculture",
            content="Blockchain technology and its application in improving supply chain transparency.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1576765607926-47a8ee9e3f33?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="The Benefits of Urban Agriculture",
            content="Urban farming's role in food security and sustainable cities.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1500315331616-db3ef1b6ba22?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Precision Farming Technologies",
            content="A look at how GPS and IoT devices are changing traditional farming methods.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1593626993378-2c5c0ecbff0e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
        Blog(
            title="Climate Adaptation Strategies in Agriculture",
            content="Techniques for farmers to adapt to unpredictable weather patterns.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1588210704700-fb4a3652c9bd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=800"
        ),
    ]

    print("Creating experts...")
    experts = [
        Expert(
            username="john_doe",
            expertise_field="Smart Farming",
            profile_image="https://images.unsplash.com/photo-1542838686-2291dec9e136?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=150",
            user=bob
        ),
        Expert(
            username="jane_doe",
            expertise_field="Sustainable Agriculture",
            profile_image="https://images.unsplash.com/photo-1528758016454-0ec4a9965c69?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=150",
            user=charlie
        )
    ]

    print("Creating communities...")
    communities = [
        Community(
            name="Smart Farming Africa",
            description="A community for sharing innovations and ideas on smart farming.",
            created_at=utc_now,
            user=alice
        ),
        Community(
            name="Youth in Agriculture",
            description="A hub for young African farmers to collaborate and learn.",
            created_at=utc_now,
            user=bob
        ),
    ]

    print("Creating comments...")
    comments = [
        Comment(
            content="This is very insightful! Thanks for sharing.",
            created_at=utc_now,
            user=charlie,
            blog=blogs[0]
        ),
        Comment(
            content="Amazing how digital platforms are helping farmers.",
            created_at=utc_now,
            user=alice,
            blog=blogs[3]
        ),
    ]

    print("Creating likes...")
    likes = [
        Like(user=alice, blog=blogs[0]),
        Like(user=bob, blog=blogs[1]),
        Like(user=charlie, blog=blogs[2]),
    ]

    # Add all data to the session and commit
    db.session.add_all(users)
    db.session.add_all(blogs)
    db.session.add_all(experts)
    db.session.add_all(communities)
    db.session.add_all(comments)
    db.session.add_all(likes)
    db.session.commit()

    print("Seeding done!")
