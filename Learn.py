st.set_page_config(page_title="Learn", page_icon="📘")

import streamlit as st

# Set up page
st.set_page_config(page_title="Learn About Trees", layout="wide")
st.title("📘 Learn: Trees, Climate & CO₂")

# Sidebar navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/learn.py", label="📘 Learn")

# Search
search = st.text_input("🔍 Search a topic...", "").lower()

# Educational Topics
topics = {
    "CO₂ Topics": {
        "How do trees absorb CO₂?": """
Trees absorb CO₂ from the air using their leaves during photosynthesis.
The CO₂ is stored in their roots, trunk, and branches as biomass.
""",
        "What is CO₂ sequestration?": """
It means capturing and storing carbon dioxide from the air.
Trees, plants, and soil all help in natural carbon sequestration.
""",
        "Why is CO₂ a greenhouse gas?": """
CO₂ traps heat in the atmosphere, warming the planet.
Human activities like burning fossil fuels increase CO₂ levels rapidly.
""",
        "CO₂ Absorption Formula": """
Formula: CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor  
Example: 10 × 25 × 0.9 × 1.1 = 247.5 kg CO₂
""",
        "Why reducing CO₂ matters": """
Excess CO₂ causes global warming and ocean acidification.
Reducing CO₂ improves air quality and climate stability.
""",
        "How much CO₂ does one tree absorb?": """
On average, a mature tree can absorb 20–30 kg CO₂ per year.
The amount varies by species, location, and age.
""",
        "Why is CO₂ harmful to the planet?": """
CO₂ traps heat in the Earth’s atmosphere, causing global warming.
Too much CO₂ from burning fossil fuels and deforestation leads to climate disruption.
""",

        "Difference between carbon footprint and carbon sequestration": """
A carbon footprint measures how much CO₂ a person or activity releases.
Carbon sequestration refers to removing CO₂ from the atmosphere — often by trees.
""",

        "How much CO₂ does a person emit per year?": """
The average person globally emits about 4 to 5 tonnes of CO₂ per year.
In urban areas, emissions can be higher due to vehicles, electricity, and construction.
""",

        "Formula to calculate CO₂ sequestration by trees": """
CO₂ absorbed = (CO₂_per_year × tree_age × survival_rate × growth_factor)
This helps estimate carbon capture by species over time.
""",

    },

    "Climate Topics": {
        "How do trees fight climate change?": """
They remove CO₂, cool the air, and improve water cycles.
Forests reduce heat and protect against extreme weather.
""",
        "What is afforestation?": """
Afforestation means planting trees in a place where there were no previous forests.
It helps increase green cover and reduce carbon levels.
""",
        "What is reforestation?": """
It is the process of replanting trees in a deforested area.
This helps restore ecosystems and biodiversity.
""",
        "What is a carbon sink?": """
A carbon sink absorbs more carbon than it releases.
Forests are natural carbon sinks that help fight climate change.
""",
        "Why is biodiversity important?": """
More species means better balance in nature.
Forests with more biodiversity are more resilient to climate changes.
""",
        "What is the greenhouse effect?": """
The greenhouse effect keeps the Earth warm by trapping heat using gases like CO₂ and methane.
Without it, Earth would be too cold — but excess gases cause global warming.
""",

        "How do forests cool cities?": """
Trees provide shade and release water vapor through transpiration.
This cools the surrounding air and reduces urban heat island effects.
""",

        "What are climate-resilient trees?": """
These are tree species that survive extreme weather like drought or floods.
Examples include Neem, Pongamia, and Indian Almond.
""",

    },

    "Forest Fires": {
        "Why do forest fires occur?": """
They can start naturally from lightning or human causes like campfires or discarded cigarettes.
Dry weather and strong winds can quickly spread fires.
""",
        "Impact of forest fires on CO₂": """
Fires release stored CO₂ back into the air, harming the climate.
They also destroy carbon sinks and affect air quality.
""",
        "How to prevent forest fires?": """
Avoid open fires in dry seasons and clear dry leaves.
Planting fire-resistant species and awareness can help.
""",
        "What are fire-resistant trees?": """
Some trees like Neem, Tamarind resist burning due to thick bark or moisture.
Using such trees can limit fire damage in sensitive zones.
""",
        "How to prevent forest fires?": """
Avoid burning dry waste or leaves near forest areas.
Creating firebreaks and planting fire-resistant species can reduce risk.
""",

        "What trees are resistant to fire?": """
Some species like Banyan and Teak have thicker bark and higher moisture content.
These trees survive better in fire-prone areas.
""",

    },

    "Tree Planting Tips": {
        "Where should I plant a tree?": """
Plant in places with sunlight, space, and access to water.
Avoid areas with cement or pollution where roots can't grow.
""",
        "When is the best time to plant trees?": """
The rainy season (June–August) is best for planting in India.
It helps trees get established with natural moisture.
""",
        "Why choose native species?": """
Native trees are adapted to local soil and climate.
They need less care and help protect local biodiversity.
""",
        "How to take care of young trees?": """
Water regularly, protect with guards, and weed the base.
The first two years are critical for tree survival.
""",
        "When is the best time to plant a tree?": """
The ideal season is during or just before the monsoon.
This gives the young sapling time to grow roots with enough water.
""",

        "How to care for saplings in the first year?": """
Water the saplings regularly and protect them from grazing animals.
Use mulching to retain soil moisture and prevent weeds.
""",

        "Should I plant one species or mixed trees?": """
Planting a mix of native species improves biodiversity and reduces disease risk.
It also ensures different CO₂ absorption patterns and ecosystem roles.
""",

    },

    "Growth & Survival": {
        "What is survival rate in afforestation?": """
It's the percentage of trees that survive after planting.
High survival means better success of the plantation.
""",
        "What is a tree’s growth factor?": """
It shows how well a tree grows in its environment.
Higher growth factor means more CO₂ is absorbed over time.
""",
        "Which trees grow faster?": """
Species like Casuarina, Pongamia, and Subabul grow quickly.
Fast-growing trees absorb more CO₂ in less time.
""",
        "What reduces tree survival?": """
Lack of water, grazing by animals, and poor soil lower survival.
Regular care improves outcomes dramatically.
""",
        "Why do some trees grow faster than others?": """
Growth speed depends on genetics, water availability, sunlight, and soil quality.
Fast-growing trees like Subabul absorb CO₂ quickly but may need more care.
""",

        "How to increase tree survival rate?": """
Choose native species, plant in the right season, and protect saplings from stress.
Adding compost and regular watering in the first 2 years improves survival.
""",

    },

    "Soil & Locations": {
        "What is sandy loam soil?": """
It's a mix of sand and silt, drains well, and is great for Neem or Amla trees.
Common in many Indian villages and coastal areas.
""",
        "Best trees for red soil?": """
Red soil suits Tamarind, Pongamia, and Indian Almond.
These trees grow well in warm, dry climates.
""",
        "Which soil is best for Teak?": """
Teak prefers deep, well-drained black or red soil.
It requires warm weather and good spacing.
""",
        "Planting near coasts": """
Use salt-tolerant species like Casuarina and Indian Almond.
They protect coastal land and are wind-resistant.
""",
        "What is soil pH and why does it matter?": """
Soil pH affects how nutrients are absorbed by trees.
Most trees grow best in slightly acidic to neutral pH (6.0–7.5).
""",

        "How to test soil before planting?": """
You can test soil manually or with a soil test kit.
Knowing if it's clayey, sandy, or loamy helps match the right tree species.
""",
        "Which plant requires which soil type?": """
Different plants thrive in different soil types based on their root structure and nutrient needs.  
For example, Neem grows well in sandy or loamy soil, while Banyan prefers well-drained fertile soil.  
Peepal does well in alluvial or clayey soil, and Indian Almond prefers moist, well-drained soil.  
Always choose tree species that match your local soil type for best survival and CO₂ absorption.  
Using local species adapted to your soil improves plantation success.
""",

    }
}

# Display topics that match search
for section, items in topics.items():
    filtered = {q: a for q, a in items.items() if search in q.lower() or search in a.lower()}
    if filtered:
        st.header(section)
        for question, answer in filtered.items():
            with st.expander(question):
                st.markdown(answer)

# Visual learning resources
st.markdown("### 📹 Learn with Visuals")
st.markdown("""
- [🌿 How trees help with CO₂](https://www.youtube.com/watch?v=3pD68uxRLkM)
- [🌱 Afforestation explained simply](https://www.youtube.com/watch?v=FtQjGPfkEe8)
- [🔥 Causes of Forest Fires](https://www.youtube.com/watch?v=ZCVmAo5s3Xw)
""")
