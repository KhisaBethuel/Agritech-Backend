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
            content="Smart farming is revolutionizing agriculture across Africa by leveraging cutting-edge technologies like the Internet of Things (IoT), drones, and data analytics to optimize farming practices. In many African countries, farmers are adopting smart farming techniques to increase yields and reduce waste. IoT sensors, for example, allow farmers to monitor soil conditions and weather patterns in real-time, enabling more efficient use of water and fertilizers. Drones equipped with cameras and sensors help farmers conduct aerial surveys of their crops, providing detailed information about crop health and identifying areas that need attention. The widespread adoption of these technologies has the potential to transform the agricultural landscape in Africa, helping farmers face challenges like climate change and food security.Despite these advances, digital inclusion remains a challenge.Many smallholder farmers lack access to smartphones or stable internet connections, limiting their ability to benefit from these innovations. Addressing this digital divide requires investment in rural connectivity and affordable technology.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://www.zenadrone.com/wp-content/uploads/2022/10/smart-farming-and-plantation.jpg"
        ),
        Blog(
            title="Sustainable Agriculture: Key to Africa’s Food Security",
            content="Sustainable agriculture is increasingly recognized as a key solution to Africa’s food security challenges. As the population continues to grow, the demand for food increases, putting pressure on existing farming practices. Sustainable farming practices focus on increasing productivity while conserving natural resources, such as soil and water. Techniques like crop rotation, agroecology, and organic farming help to reduce the environmental impact of agriculture and promote long-term food security. By embracing sustainable farming, African farmers can improve their livelihoods, enhance biodiversity, and contribute to the global fight against climate change. Moreover, these practices can increase the resilience of African agriculture to extreme weather events and other climate-related challenges.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=bob,
            image="https://storage.googleapis.com/jm-gcp-bethestory-p-12po-bucket/uploads/2023/09/sustainable-agriculture.jpg"
        ),
        Blog(
            title="Agroforestry: Merging Conservation with Productivity",
            content="Agroforestry is an innovative agricultural system that combines trees with crops or livestock to create mutually beneficial interactions between the environment and farming practices. In Africa, where land degradation is a growing concern, agroforestry provides a sustainable way to enhance productivity while conserving natural resources. Trees improve soil fertility, prevent erosion, and provide shade, all of which can lead to increased yields and better water retention. Agroforestry also offers farmers additional income from timber, fruit, and other forest products. By integrating conservation into their farming practices, African farmers can boost productivity and help mitigate the effects of climate change.However, challenges such as limited access to land, capital, and mentorship often hinder young people from entering the agricultural sector. Governments and development organizations must address these barriers by providing training programs, financial support, and platforms for networking.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=charlie,
            image="https://media.istockphoto.com/id/1940005387/photo/close-up-on-a-man-selling-carrots-at-a-farmers-market.webp?a=1&b=1&s=612x612&w=0&k=20&c=72Q1Wqtw8pKtZnouskhTBfkjwigSLtDCCPFQynbP_Mo="
        ),
        Blog(
            title="Digital Platforms Connecting African Farmers",
            content="In recent years, digital platforms have emerged as powerful tools for connecting farmers across Africa with markets, resources, and educational content. Mobile apps and websites are enabling farmers to access real-time weather updates, market prices, and best agricultural practices. These platforms help farmers make informed decisions about planting, irrigation, and harvesting, improving their productivity and profitability. Additionally, digital platforms are creating new opportunities for farmers to access financial services like microloans and insurance, helping them cope with risks like droughts or crop failure. By fostering collaboration and knowledge-sharing, digital platforms are empowering African farmers to thrive in an increasingly digital world.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://www.newaginternational.com/wp-content/uploads/2023/12/P370e_Image1_-xarvio_and_CNH.jpg"
        ),
        Blog(
            title="Irrigation Innovation in Dry Regions",
            content="Water scarcity is one of the most significant challenges faced by farmers in Africa’s arid and semi-arid regions. Traditional irrigation systems often waste large amounts of water, exacerbating the problem. However, innovative irrigation technologies are helping to conserve water while improving crop yields. Drip irrigation, for example, delivers water directly to plant roots, reducing evaporation and runoff. Other systems, like solar-powered pumps and smart irrigation controllers, enable farmers to manage water resources more efficiently. These innovations are crucial for ensuring that African farmers can continue to produce food in increasingly dry regions, where climate change is making traditional farming methods less viable.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=bob,
            image="https://static6.depositphotos.com/1066611/561/i/450/depositphotos_5619505-stock-photo-freshly-growing-plants-on-acre.jpg"
        ),
        Blog(
            title="Youth in Agriculture: Changing the Narrative",
            content="Africa's youth are increasingly recognizing the potential of agriculture as a viable and lucrative career path. Traditionally seen as a sector for older generations, agriculture is now attracting young entrepreneurs who are eager to innovate and drive change. From tech startups creating farming apps to young farmers adopting modern techniques like precision farming, the youth are bringing fresh ideas and enthusiasm to the industry. Governments and NGOs are also investing in youth-led agricultural projects, providing training, funding, and mentorship to help young farmers succeed. This shift is transforming the agricultural landscape, creating new opportunities and helping to ensure the future of food security on the continent.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=charlie,
            image="https://media.gettyimages.com/id/961635070/video/researchers.jpg?s=640x640&k=20&c=Wu327Kxnlmpiq4hDPkJShWXuERLWHdqa3ucY7Nep0l0="
        ),
        Blog(
            title="Organic Farming: The Future of African Agriculture?",
            content="The demand for organic produce is growing around the world, and African farmers are beginning to tap into this lucrative market. Organic farming practices, which avoid synthetic chemicals and focus on building healthy, biodiverse ecosystems, are seen as more sustainable and environmentally friendly. In Africa, organic farming can help improve soil health, reduce the risk of pests and diseases, and offer higher market prices for produce. As consumers become more conscious about the environmental impact of their food choices, organic farming has the potential to become a major sector in African agriculture. However, challenges such as certification processes and access to organic inputs remain obstacles that need to be addressed for organic farming to reach its full potential.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://sheppardrealty.ca/wp-content/uploads/2018/10/SHEPPARD-faming-facts-V2.jpg"
        ),
        Blog(
            title="The Role of Women in African Agriculture",
            content="Women play a crucial role in Africa’s agricultural sector, contributing to everything from planting and harvesting to managing farm finances. Despite their significant contributions, women often face challenges like limited access to land, credit, and training. Empowering women in agriculture can have a transformative effect on the entire sector, leading to improved productivity, income, and food security. By supporting women with the resources, education, and opportunities they need, African countries can unlock the full potential of their agricultural sector. Numerous initiatives across Africa are already helping to bridge the gender gap, from training programs to microloans tailored for women farmers.However, challenges such as limited access to land, capital, and mentorship often hinder young people from entering the agricultural sector. Governments and development organizations must address these barriers by providing training programs, financial support, and platforms for networking.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.",
            created_at=utc_now,
            user=bob,
            image="https://media.licdn.com/dms/image/C5612AQHJo_XYiL4BPw/article-cover_image-shrink_720_1280/0/1520233567840?e=2147483647&v=beta&t=t8ySk0Qw8A7vAvBqclO330NmrT069_jwq6bt_vcR9lc"
        ),
        Blog(
            title="How AI is Revolutionizing Agriculture in Africa",
            content="Artificial Intelligence (AI) is poised to revolutionize agriculture in Africa, offering farmers innovative solutions for managing crops, pests, and resources. AI-powered technologies like crop management software, pest detection systems, and predictive analytics can help farmers optimize their operations, reduce waste, and improve yields. In particular, AI can help with precision farming, where decisions about irrigation, planting, and fertilization are based on data rather than guesswork. By analyzing vast amounts of data from sensors and drones, AI systems can identify patterns and trends that help farmers make smarter, more informed decisions. This technology has the potential to significantly improve food security across Africa, especially as the continent faces the dual challenges of climate change and population growth.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            user=charlie,
            image="https://images.unsplash.com/photo-1537432376769-f87e86b1bdea"
        ),
        Blog(
            title="Harnessing Renewable Energy for African Farms",
            content="Water scarcity is one of the most significant challenges faced by farmers in Africa’s arid and semi-arid regions. Traditional irrigation systems often waste large amounts of water, exacerbating the problem. However, innovative irrigation technologies are helping to conserve water while improving crop yields. Drip irrigation, for example, delivers water directly to plant roots, reducing evaporation and runoff. Other systems, like solar-powered pumps and smart irrigation controllers, enable farmers to manage water resources more efficiently. These innovations are crucial for ensuring that African farmers can continue to produce food in increasingly dry regions, where climate change is making traditional farming methods less viable.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://www.isustainableearth.com/wp-content/uploads/2021/02/Harness-energy.jpeg"
        ),
        Blog(
            title="Crop Diversification for Resilient Farming",
            content="Smart farming is revolutionizing agriculture across Africa by leveraging cutting-edge technologies like the Internet of Things (IoT), drones, and data analytics to optimize farming practices. In many African countries, farmers are adopting smart farming techniques to increase yields and reduce waste. IoT sensors, for example, allow farmers to monitor soil conditions and weather patterns in real-time, enabling more efficient use of water and fertilizers. Drones equipped with cameras and sensors help farmers conduct aerial surveys of their crops, providing detailed information about crop health and identifying areas that need attention. The widespread adoption of these technologies has the potential to transform the agricultural landscape in Africa, helping farmers face challenges like climate change and food security.Key strategies in sustainable agriculture include crop rotation, agroforestry, organic farming, and conservation tillage. These practices help preserve soil fertility, reduce erosion, and promote biodiversity. For example, integrating trees into farmland not only provides shade and wind protection but also enhances soil nutrients and water retention.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1518828460606-fd6b4eb9f972"
        ),
        Blog(
            title="Integrating Blockchain in Agriculture",
            content="Sustainable agriculture is increasingly recognized as a key solution to Africa’s food security challenges. As the population continues to grow, the demand for food increases, putting pressure on existing farming practices. Sustainable farming practices focus on increasing productivity while conserving natural resources, such as soil and water. Techniques like crop rotation, agroecology, and organic farming help to reduce the environmental impact of agriculture and promote long-term food security. By embracing sustainable farming, African farmers can improve their livelihoods, enhance biodiversity, and contribute to the global fight against climate change. Moreover, these practices can increase the resilience of African agriculture to extreme weather events and other climate-related challenges.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1581091870631-3c8aa564fdb5"
        ),
        Blog(
            title="The Benefits of Urban Agriculture",
            content="The demand for organic produce is growing around the world, and African farmers are beginning to tap into this lucrative market. Organic farming practices, which avoid synthetic chemicals and focus on building healthy, biodiverse ecosystems, are seen as more sustainable and environmentally friendly. In Africa, organic farming can help improve soil health, reduce the risk of pests and diseases, and offer higher market prices for produce. As consumers become more conscious about the environmental impact of their food choices, organic farming has the potential to become a major sector in African agriculture. However, challenges such as certification processes and access to organic inputs remain obstacles that need to be addressed for organic farming to reach its full potential.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://friedmanrealestate.com/wp-content/uploads/2019/06/URBANFARMING.jpg"
        ),
        Blog(
            title="Precision Farming Technologies",
            content="Water scarcity is one of the most significant challenges faced by farmers in Africa’s arid and semi-arid regions. Traditional irrigation systems often waste large amounts of water, exacerbating the problem. However, innovative irrigation technologies are helping to conserve water while improving crop yields. Drip irrigation, for example, delivers water directly to plant roots, reducing evaporation and runoff. Other systems, like solar-powered pumps and smart irrigation controllers, enable farmers to manage water resources more efficiently. These innovations are crucial for ensuring that African farmers can continue to produce food in increasingly dry regions, where climate change is making traditional farming methods less viable.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1527596916826-c028c0b51423"
        ),
        Blog(
            title="Climate Adaptation Strategies in Agriculture",
            content="Africa's youth are increasingly recognizing the potential of agriculture as a viable and lucrative career path. Traditionally seen as a sector for older generations, agriculture is now attracting young entrepreneurs who are eager to innovate and drive change. From tech startups creating farming apps to young farmers adopting modern techniques like precision farming, the youth are bringing fresh ideas and enthusiasm to the industry. Governments and NGOs are also investing in youth-led agricultural projects, providing training, funding, and mentorship to help young farmers succeed. This shift is transforming the agricultural landscape, creating new opportunities and helping to ensure the future of food security on the continent.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1516542076529-1ea3854896f2"
        ),
        Blog(
            title="The Power of Agri-Business Startups",
            content="The demand for organic produce is growing around the world, and African farmers are beginning to tap into this lucrative market. Organic farming practices, which avoid synthetic chemicals and focus on building healthy, biodiverse ecosystems, are seen as more sustainable and environmentally friendly. In Africa, organic farming can help improve soil health, reduce the risk of pests and diseases, and offer higher market prices for produce. As consumers become more conscious about the environmental impact of their food choices, organic farming has the potential to become a major sector in African agriculture. However, challenges such as certification processes and access to organic inputs remain obstacles that need to be addressed for organic farming to reach its full potential.",
            created_at=utc_now,
            user=alice,
            image="https://goodineverygrain.ca/wp-content/uploads/2021/11/Farmers-and-climate-change-edu-blog.jpg"
        ),
        Blog(
            title="Building Soil Health for Higher Yields",
            content="The importance of soil health and strategies for sustainable farming.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1593529467220-13a7ba2ab24d"
        ),
        Blog(
            title="Digital Inclusion for Smallholder Farmers",
            content="Artificial Intelligence (AI) is poised to revolutionize agriculture in Africa, offering farmers innovative solutions for managing crops, pests, and resources. AI-powered technologies like crop management software, pest detection systems, and predictive analytics can help farmers optimize their operations, reduce waste, and improve yields. In particular, AI can help with precision farming, where decisions about irrigation, planting, and fertilization are based on data rather than guesswork. By analyzing vast amounts of data from sensors and drones, AI systems can identify patterns and trends that help farmers make smarter, more informed decisions. This technology has the potential to significantly improve food security across Africa, especially as the continent faces the dual challenges of climate change and population growth.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1587314373795-34b5bd2218c8"
        ),
        Blog(
            title="Animal Husbandry Innovations in Africa",
            content="Women play a crucial role in Africa’s agricultural sector, contributing to everything from planting and harvesting to managing farm finances. Despite their significant contributions, women often face challenges like limited access to land, credit, and training. Empowering women in agriculture can have a transformative effect on the entire sector, leading to improved productivity, income, and food security. By supporting women with the resources, education, and opportunities they need, African countries can unlock the full potential of their agricultural sector. Numerous initiatives across Africa are already helping to bridge the gender gap, from training programs to microloans tailored for women farmers.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://cdn.wikifarmer.com/wp-content/uploads/2024/07/What-is-Animal-Husbandry-Livestock-Farming.jpg"
        ),
        Blog(
            title="Affordable Fertilizer Solutions",
            content="Africa's youth are increasingly recognizing the potential of agriculture as a viable and lucrative career path. Traditionally seen as a sector for older generations, agriculture is now attracting young entrepreneurs who are eager to innovate and drive change. From tech startups creating farming apps to young farmers adopting modern techniques like precision farming, the youth are bringing fresh ideas and enthusiasm to the industry. Governments and NGOs are also investing in youth-led agricultural projects, providing training, funding, and mentorship to help young farmers succeed. This shift is transforming the agricultural landscape, creating new opportunities and helping to ensure the future of food security on the continent.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1556885161-48e68ec66a9e"
        ),
        Blog(
            title="Advancements in Agricultural Drones",
            content="Water scarcity is one of the most significant challenges faced by farmers in Africa’s arid and semi-arid regions. Traditional irrigation systems often waste large amounts of water, exacerbating the problem. However, innovative irrigation technologies are helping to conserve water while improving crop yields. Drip irrigation, for example, delivers water directly to plant roots, reducing evaporation and runoff. Other systems, like solar-powered pumps and smart irrigation controllers, enable farmers to manage water resources more efficiently. These innovations are crucial for ensuring that African farmers can continue to produce food in increasingly dry regions, where climate change is making traditional farming methods less viable.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1546707013-bb4bbfd1ce42"
        ),
        Blog(
            title="Farm-to-Table Revolution",
            content="In recent years, digital platforms have emerged as powerful tools for connecting farmers across Africa with markets, resources, and educational content. Mobile apps and websites are enabling farmers to access real-time weather updates, market prices, and best agricultural practices. These platforms help farmers make informed decisions about planting, irrigation, and harvesting, improving their productivity and profitability. Additionally, digital platforms are creating new opportunities for farmers to access financial services like microloans and insurance, helping them cope with risks like droughts or crop failure. By fostering collaboration and knowledge-sharing, digital platforms are empowering African farmers to thrive in an increasingly digital world.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=alice,
            image="https://images.unsplash.com/photo-1501004318641-b39e6451bec6"
        ),
        Blog(
            title="Eco-Friendly Pest Control Methods",
            content="Exploring natural and sustainable ways to manage pests.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.In regions prone to drought, agroforestry systems help retain soil moisture and provide shade, reducing heat stress on crops. Trees also act as natural windbreaks, protecting crops from strong winds and erosion. Economically, farmers can harvest fruits, nuts, and timber alongside their regular crops, creating a steady income stream.",
            created_at=utc_now,
            user=bob,
            image="https://images.unsplash.com/photo-1580910051070-d9f0fbc1dfb3"
        ),
        Blog(
            title="Water Harvesting for Dry Areas",
            content="Agroforestry is an innovative agricultural system that combines trees with crops or livestock to create mutually beneficial interactions between the environment and farming practices. In Africa, where land degradation is a growing concern, agroforestry provides a sustainable way to enhance productivity while conserving natural resources. Trees improve soil fertility, prevent erosion, and provide shade, all of which can lead to increased yields and better water retention. Agroforestry also offers farmers additional income from timber, fruit, and other forest products. By integrating conservation into their farming practices, African farmers can boost productivity and help mitigate the effects of climate change.",
            created_at=utc_now,
            user=charlie,
            image="https://images.unsplash.com/photo-1576765607926-47a8ee9e3f33"
        ),
        Blog(
            title="Agricultural Policy Innovations",
            content="Sustainable agriculture is increasingly recognized as a key solution to Africa’s food security challenges. As the population continues to grow, the demand for food increases, putting pressure on existing farming practices. Sustainable farming practices focus on increasing productivity while conserving natural resources, such as soil and water. Techniques like crop rotation, agroecology, and organic farming help to reduce the environmental impact of agriculture and promote long-term food security. By embracing sustainable farming, African farmers can improve their livelihoods, enhance biodiversity, and contribute to the global fight against climate change. Moreover, these practices can increase the resilience of African agriculture to extreme weather events and other climate-related challenges.",
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