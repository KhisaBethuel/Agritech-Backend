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
            image="https://www.zenadrone.com/wp-content/uploads/2022/10/smart-farming-and-plantation.jpg"
        ),
        Blog(
            title="Sustainable Agriculture: Key to Africa’s Food Security",
            content="A deep dive into sustainable practices that are helping farmers combat climate change and increase yields.",
            created_at=utc_now,
            user=bob,
            image="https://storage.googleapis.com/jm-gcp-bethestory-p-12po-bucket/uploads/2023/09/sustainable-agriculture.jpg"
        ),
        Blog(
            title="Agroforestry: Merging Conservation with Productivity",
            content="Agroforestry is emerging as a solution to balance ecological conservation with increased agricultural productivity.",
            created_at=utc_now,
            user=charlie,
            image="https://media.istockphoto.com/id/1940005387/photo/close-up-on-a-man-selling-carrots-at-a-farmers-market.webp?a=1&b=1&s=612x612&w=0&k=20&c=72Q1Wqtw8pKtZnouskhTBfkjwigSLtDCCPFQynbP_Mo="
        ),
        Blog(
            title="Digital Platforms Connecting African Farmers",
            content="How mobile apps and digital platforms are empowering African farmers with market access and knowledge.",
            created_at=utc_now,
            user=alice,
            image="data:image/png;base64,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"
        ),
        Blog(
            title="Irrigation Innovation in Dry Regions",
            content="Exploring innovative irrigation systems transforming farming in Africa's arid and semi-arid regions.",
            created_at=utc_now,
            user=bob,
            image="https://static6.depositphotos.com/1066611/561/i/450/depositphotos_5619505-stock-photo-freshly-growing-plants-on-acre.jpg"
        ),
        Blog(
            title="Youth in Agriculture: Changing the Narrative",
            content="How young entrepreneurs in Africa are embracing agriculture as a lucrative career path.",
            created_at=utc_now,
            user=charlie,
            image="https://media.gettyimages.com/id/961635070/video/researchers.jpg?s=640x640&k=20&c=Wu327Kxnlmpiq4hDPkJShWXuERLWHdqa3ucY7Nep0l0="
        ),
        Blog(
            title="Organic Farming: The Future of African Agriculture?",
            content="The shift towards organic farming and its potential to meet growing demand for sustainable products.",
            created_at=utc_now,
            user=alice,
            image="https://sheppardrealty.ca/wp-content/uploads/2018/10/SHEPPARD-faming-facts-V2.jpg"
        ),
        Blog(
            title="The Role of Women in African Agriculture",
            content="Women contribute significantly to Africa's agriculture. Here’s how they are shaping the sector’s future.",
            created_at=utc_now,
            user=bob,
            image="https://media.licdn.com/dms/image/C5612AQHJo_XYiL4BPw/article-cover_image-shrink_720_1280/0/1520233567840?e=2147483647&v=beta&t=t8ySk0Qw8A7vAvBqclO330NmrT069_jwq6bt_vcR9lc"
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
            image="https://www.isustainableearth.com/wp-content/uploads/2021/02/Harness-energy.jpeg"
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
            image="data:image/jpeg;base64,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"
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
            image="https://goodineverygrain.ca/wp-content/uploads/2021/11/Farmers-and-climate-change-edu-blog.jpg"
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
            image="https://cdn.wikifarmer.com/wp-content/uploads/2024/07/What-is-Animal-Husbandry-Livestock-Farming.jpg"
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
            image="https://devimpactinstitute.com/wp-content/uploads/2024/03/Agricultural-Policy-Framework-for-Development.png"
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
