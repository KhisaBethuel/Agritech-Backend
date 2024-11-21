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
            image="https://images.unsplash.com/photo-1611868192475-9c9b1ba2d0ed"
        ),
        Blog(
            title="Sustainable Agriculture: Key to Africa’s Food Security",
            content="A deep dive into sustainable practices that are helping farmers combat climate change and increase yields.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1519892951274-dc6abe9f6e82"
        ),
        Blog(
            title="Agroforestry: Merging Conservation with Productivity",
            content="Agroforestry is emerging as a solution to balance ecological conservation with increased agricultural productivity.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1508887647429-88246f1b0019"
        ),
        Blog(
            title="Digital Platforms Connecting African Farmers",
            content="How mobile apps and digital platforms are empowering African farmers with market access and knowledge.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
        ),
        Blog(
            title="Irrigation Innovation in Dry Regions",
            content="Exploring innovative irrigation systems transforming farming in Africa's arid and semi-arid regions.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1507499241543-3f487d3bdbb6"
        ),
        Blog(
            title="Youth in Agriculture: Changing the Narrative",
            content="How young entrepreneurs in Africa are embracing agriculture as a lucrative career path.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1516261892403-cc6d39f51a7f"
        ),
        Blog(
            title="Organic Farming: The Future of African Agriculture?",
            content="The shift towards organic farming and its potential to meet growing demand for sustainable products.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1546111192-5f0b85d1e68b"
        ),
        Blog(
            title="The Role of Women in African Agriculture",
            content="Women contribute significantly to Africa's agriculture. Here’s how they are shaping the sector’s future.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1556912990-d13e1c774181"
        ),
        Blog(
            title="How AI is Revolutionizing Agriculture in Africa",
            content="The impact of AI-driven solutions on crop management, pest control, and forecasting in Africa.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1537432376769-f87e86b1bdea"
        ),
        Blog(
            title="Harnessing Renewable Energy for African Farms",
            content="The use of solar and wind energy in powering agricultural operations in remote areas.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1504944325015-d8be6837c7e0"
        ),
        Blog(
            title="Crop Diversification for Resilient Farming",
            content="How crop diversification reduces risks and enhances resilience in African agriculture.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1518828460606-fd6b4eb9f972"
        ),
        Blog(
            title="Integrating Blockchain in Agriculture",
            content="Blockchain technology and its application in improving supply chain transparency.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1581091870631-3c8aa564fdb5"
        ),
        Blog(
            title="The Benefits of Urban Agriculture",
            content="Urban farming's role in food security and sustainable cities.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1525130413817-d45c1d7fb6b5"
        ),
        Blog(
            title="Precision Farming Technologies",
            content="A look at how GPS and IoT devices are changing traditional farming methods.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1527596916826-c028c0b51423"
        ),
        Blog(
            title="Climate Adaptation Strategies in Agriculture",
            content="Techniques for farmers to adapt to unpredictable weather patterns.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1516542076529-1ea3854896f2"
        ),
        Blog(
            title="The Power of Agri-Business Startups",
            content="How startups in Africa are driving agricultural transformation.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1598514982172-7ba8c78d7aaf"
        ),
        Blog(
            title="Building Soil Health for Higher Yields",
            content="The importance of soil health and strategies for sustainable farming.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1593529467220-13a7ba2ab24d"
        ),
        Blog(
            title="Digital Inclusion for Smallholder Farmers",
            content="Closing the digital divide for farmers with affordable tools and education.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1587314373795-34b5bd2218c8"
        ),
        Blog(
            title="Animal Husbandry Innovations in Africa",
            content="Modern methods for improving livestock productivity and welfare.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1583941452889-1b6b9d81cd54"
        ),
        Blog(
            title="Affordable Fertilizer Solutions",
            content="New ways to make fertilizers accessible to small-scale farmers.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1556885161-48e68ec66a9e"
        ),
        Blog(
            title="Advancements in Agricultural Drones",
            content="How drones are aiding in precision agriculture for better yields.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1546707013-bb4bbfd1ce42"
        ),
        Blog(
            title="Farm-to-Table Revolution",
            content="The rise of direct farm-to-table supply chains in Africa.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6"
        ),
        Blog(
            title="Eco-Friendly Pest Control Methods",
            content="Exploring natural and sustainable ways to manage pests.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1580910051070-d9f0fbc1dfb3"
        ),
        Blog(
            title="Water Harvesting for Dry Areas",
            content="Techniques for water collection and management in arid regions.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1576765607926-47a8ee9e3f33"
        ),
        Blog(
            title="Agricultural Policy Innovations",
            content="How new policies are shaping the future of farming in Africa.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1578323299339-cbc84a31fdfc"
        ),
    ]

    print("Creating experts...")
    experts = [
        Expert(
            username="john_doe",
            expertise_field="Smart Farming",
            profile_image="https://images.unsplash.com/photo-1542838686-2291dec9e136",
            user=bob
        ),
        Expert(
            username="jane_doe",
            expertise_field="Sustainable Agriculture",
            profile_image="https://images.unsplash.com/photo-1510915228340-29c85a43dcfe",
            user=alice
        )
    ]

    # Add all data to the session and commit
    db.session.add_all(users + blogs + experts)
    db.session.commit()

    print("Seeding done!")
