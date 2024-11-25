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
            image="https://www.newaginternational.com/wp-content/uploads/2023/12/P370e_Image1_-xarvio_and_CNH.jpg"
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
            image="https://friedmanrealestate.com/wp-content/uploads/2019/06/URBANFARMING.jpg"
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
