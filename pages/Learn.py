import streamlit as st

# ✅ First Streamlit command
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")

# ✅ Title
st.title("📘 Learn: Trees, Climate & CO₂")

# ✅ Sidebar navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/Learn.py", label="📘 Learn")

# ✅ Search box
search = st.text_input("🔍 Search a topic...", "").lower()

# ✅ Banner image (add your own image or use free URLs)
st.image("https://images.unsplash.com/photo-1558944351-dae09f7d82e9", caption="🌳 Forests are Earth’s lungs", use_column_width=True)

# ✅ Topics grouped by category with emojis
topics = {
    "🌿 CO₂ Topics": {
        "🌱 How do trees absorb CO₂?": """
Trees absorb CO₂ from the air using leaves during photosynthesis.  
That CO₂ gets stored in their roots, trunks, and branches as biomass.
""",
        "🌀 What is CO₂ sequestration?": """
CO₂ sequestration means capturing and storing carbon dioxide from the air.  
Trees, plants, and soil all help in this natural process.
""",
        "🌡️ Why is CO₂ a greenhouse gas?": """
CO₂ traps heat in the atmosphere, causing Earth to warm.  
Fossil fuels and deforestation increase CO₂ levels rapidly.
""",
        "🧮 CO₂ Absorption Formula": """
**Formula**: CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor  
**Example**: 10 × 25 × 0.9 × 1.1 = 247.5 kg CO₂
""",
        "🚨 Why reducing CO₂ matters": """
Too much CO₂ leads to global warming and ocean acidification.  
Reducing emissions improves air quality and climate stability.
""",
        "🌳 How much CO₂ does one tree absorb?": """
A mature tree can absorb **20–30 kg CO₂** per year.  
It varies by species, age, and environment.
""",
        "🆘 Why is CO₂ harmful to the planet?": """
Excess CO₂ causes extreme weather, ice melting, and rising sea levels.  
It disrupts ecosystems and biodiversity.
""",
        "⚖️ Carbon footprint vs sequestration": """
Carbon footprint = CO₂ **you emit**  
Carbon sequestration = CO₂ **trees remove** from the air.
""",
        "👣 Average person’s CO₂ emissions": """
One person emits around **4–5 tonnes of CO₂** every year.  
In cities, it's higher due to cars, electricity, and industry.
""",
        "📐 CO₂ sequestration by trees": """
**Formula**:  
CO₂ = CO₂/year × tree_age × survival_rate × growth_factor  
This helps estimate carbon capture over time.
""",
    },

    "🌎 Climate Topics": {
        "🌲 How do trees fight climate change?": """
They remove CO₂, release oxygen, and cool the planet.  
Forests also protect against floods and droughts.
""",
        "🪴 What is afforestation?": """
Planting trees in a new area where there was no previous forest.  
Helps increase green cover and reduce carbon levels.
""",
        "🌳 What is reforestation?": """
Replanting trees in deforested areas to restore biodiversity.  
It brings life back to damaged ecosystems.
""",
        "🧲 What is a carbon sink?": """
A place that absorbs more carbon than it releases.  
Forests, oceans, and wetlands are natural carbon sinks.
""",
        "🐾 Why is biodiversity important?": """
More species means healthier ecosystems.  
Diverse forests resist diseases and adapt to climate better.
""",
        "🌤️ What is the greenhouse effect?": """
It keeps Earth warm by trapping heat using gases like CO₂.  
Too much CO₂ = global warming. Balance is key!
""",
        "🏙️ How do forests cool cities?": """
Trees provide shade and release water vapor.  
This cools the air and lowers heat in urban areas.
""",
        "💪 Climate-resilient trees": """
Trees like Neem, Pongamia, and Indian Almond can survive heat, drought, or floods.
""",
    },

    "🔥 Forest Fires": {
        "⚡ Why do forest fires occur?": """
They can start from lightning or human actions like campfires and waste burning.  
Dry leaves and wind help fires spread fast.
""",
        "🌫️ Impact of fires on CO₂": """
Fires release stored CO₂ and destroy green cover.  
Air pollution increases drastically.
""",
        "🛑 How to prevent forest fires?": """
Avoid burning waste near forests.  
Create firebreaks, plant fire-resistant trees, and spread awareness.
""",
        "🔥 Fire-resistant trees": """
Species like Neem, Banyan, and Tamarind resist fires better.  
Thick bark and moisture help them survive.
""",
    },

    "🌱 Tree Planting Tips": {
        "📍 Where should I plant trees?": """
Choose open spaces with sunlight, air, and water access.  
Avoid planting too close to buildings or cemented ground.
""",
        "⏰ Best time to plant trees?": """
The **monsoon (June–August)** is ideal in India.  
Rain helps young saplings grow strong roots.
""",
        "🌿 Why choose native trees?": """
They are adapted to your local climate and soil.  
Need less care and support local birds and animals.
""",
        "🛡️ How to care for young trees?": """
Water weekly, protect with guards, and remove weeds.  
First 2 years are crucial!
""",
        "🧪 Mixed species or single?": """
Mixed planting boosts biodiversity and reduces pest risks.  
Each tree plays a unique ecological role.
""",
    },

    "📈 Growth & Survival": {
        "✅ What is survival rate?": """
Percentage of trees that survive after planting.  
Higher rate = more CO₂ absorbed.
""",
        "📊 What is growth factor?": """
Shows how well a tree grows in a local environment.  
Used in CO₂ simulation formulas.
""",
        "🌱 Fast-growing trees": """
Casuarina, Pongamia, and Subabul grow quickly.  
They absorb CO₂ faster but may need more care.
""",
        "💧 What reduces survival?": """
Lack of water, animal grazing, and poor soil.  
Regular care and guards improve survival.
""",
        "🌤️ Why growth speed varies": """
Depends on sunlight, water, soil, and species genetics.  
Local trees usually grow better in their native soil.
""",
        "🧴 How to increase survival?": """
Use compost, mulch, and native species.  
Water regularly and protect from animals.
""",
    },

    "🧪 Soil & Locations": {
        "🏖️ What is sandy loam?": """
Mix of sand and silt. Drains well.  
Good for Amla and Neem trees.
""",
        "🧱 Best trees for red soil": """
Red soil suits Tamarind, Pongamia, and Indian Almond.  
Warm and dry climate helps them thrive.
""",
        "🌾 Soil for Teak": """
Teak prefers deep, black or red soil.  
Needs warmth and good drainage.
""",
        "🌊 Coastal planting tips": """
Use salt-tolerant species like Casuarina.  
They resist wind and protect land from erosion.
""",
        "🧪 What is soil pH?": """
Soil pH affects how well trees absorb nutrients.  
Ideal range: 6.0 to 7.5 for most trees.
""",
        "🧫 How to test soil?": """
Use a test kit or lab.  
Knowing soil type helps choose the right species.
""",
        "🪴 Which plant suits which soil?": """
Neem: sandy/loamy soil  
Banyan: well-drained fertile soil  
Peepal: clayey/alluvial soil  
Choose based on your local soil for best survival and CO₂ absorption.
""",
    }
        "🌿 Innovative Climate Solutions": {
        "🟢 What is Duckweed and how does it help?": """
Duckweed is a tiny floating aquatic plant that **grows extremely fast** — it can double in size every 2–3 days! 🌊  
It **absorbs CO₂ from water and air**, helps clean polluted water, and creates oxygen for aquatic life.

**Fun Fact**: Duckweed can absorb **5–10x more CO₂ per area** than trees in certain conditions.  
It is also used for biofuel, animal feed, and wastewater treatment.

🖼️ ![Duckweed](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Lemna_minor_2.jpg/640px-Lemna_minor_2.jpg)
""",

        "🌾 What is Vetiver Grass and how does it help the planet?": """
Vetiver is a **deep-rooted grass** known for preventing soil erosion and purifying water. Its roots can grow over 3 meters deep! 🌱  
It **stores carbon in the soil**, strengthens land, and improves groundwater recharge.

Vetiver is used in **slope protection, rainwater harvesting**, and even **aromatherapy** (essential oils).  
It is drought-tolerant, native-friendly, and used in eco-restoration worldwide.

🖼️ ![Vetiver](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Vetiver.jpg/800px-Vetiver.jpg)
""",

        "💡 Why include Duckweed & Vetiver in your afforestation model?": """
Including Duckweed and Vetiver gives your project a **unique, innovative edge**.  
These fast-growing, high-impact plants complement traditional tree planting.

- Duckweed works in **wetlands, ponds, polluted water**
- Vetiver is perfect for **slopes, erosion zones, drylands**

Together, they fight **climate change + water pollution + land degradation**.
""",
    }
}

# ✅ Display matching topics
for section, items in topics.items():
    filtered = {q: a for q, a in items.items() if search in q.lower() or search in a.lower()}
    if filtered:
        st.header(section)
        for question, answer in filtered.items():
            with st.expander(question):
                st.markdown(answer)
