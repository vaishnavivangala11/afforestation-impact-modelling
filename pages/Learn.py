import streamlit as st

# Page setup
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")

st.title("📘 Learn: Trees, CO₂ & Climate Solutions")
st.markdown("Empower yourself with knowledge on how trees, duckweed, and vetiver help our planet. 🌍")

# Sidebar navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/Learn.py", label="📘 Learn")

# Search bar
search = st.text_input("🔍 Search a topic...", "").lower()

# Educational content grouped by themes
lessons = {
    "🌍 CO₂ & Climate Science": {
        "How trees help reduce CO₂ levels": """
🌳 Trees absorb carbon dioxide (CO₂) through photosynthesis and store it in their biomass. They are nature’s carbon sinks that help cool the planet.
""",
        "The greenhouse effect and global warming": """
🌡️ CO₂ traps heat in the atmosphere, warming the planet. Too much of it causes sea-level rise, extreme weather, and ecosystem imbalance.
""",
        "Understanding CO₂ sequestration": """
🧮 **CO₂ sequestration** means storing carbon for a long time. Trees, soil, duckweed, vetiver, and grasslands naturally capture and store carbon.
""",
        "CO₂ Absorption Formula": """
🧾 **Formula:**  
`CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor`  
📌 Example: A Neem tree with 1-year age: `1 × 25 × 0.85 × 1.0 = 21.25 kg CO₂`
""",
        "Why reducing CO₂ is urgent": """
⏳ High CO₂ levels lead to climate disasters. Every tree and plant reduces carbon burden and helps stabilize climate.
"""
    },

    "🌱 Tree Planting & Afforestation": {
        "What is afforestation and reforestation": """
🌲 **Afforestation** is planting trees where there were none before.  
🌳 **Reforestation** is replanting lost forests. Both restore ecosystems.
""",
        "Benefits of native species": """
🪵 Local species like Neem, Peepal, and Pongamia grow faster, survive better, and support biodiversity in East Godavari.
""",
        "Tree growth and CO₂ capture": """
🌿 Fast-growing trees like Subabul absorb more CO₂ quickly. Long-living trees like Banyan store carbon for decades.
""",
        "Caring for saplings": """
💧 Protect with guards, water regularly, and mulch around roots.  
🕊️ First 2 years are critical for healthy growth.
"""
    },
        "🔥 Deforestation & Its Impact": {
        "What is deforestation?": """
🪓 Deforestation is the cutting down of forests for farming, roads, or cities. It reduces biodiversity, harms the climate, and removes vital carbon sinks.
""",
        "Main causes of deforestation": """
🚜 Farming (like palm oil, soy, and cattle),  
🛣️ Urban expansion,  
🪵 Logging for timber,  
🔥 Forest fires — all reduce green cover.
""",
        "How deforestation affects climate": """
🌡️ Fewer trees = more CO₂ in the air.  
No forests = less rainfall, hotter temperatures, soil erosion, and more floods.
""",
        "How afforestation helps reverse it": """
🌱 Planting new trees in deforested areas helps restore balance. It brings back wildlife, cools the land, and stores carbon again.
"""
    },
    # 🌿 Climate & Community Topics
st.subheader("🌿 Climate & Community Topics")

with st.expander("🌡️ Urban Heat Islands & Cooling Trees"):
    st.markdown("""
Trees cool cities by shading surfaces and releasing moisture.  
More greenery means lower temperatures and healthier living.
""")

with st.expander("💨 Trees Improve Air Quality"):
    st.markdown("""
Leaves absorb pollutants and trap dust from the air.  
Neem and Peepal work like nature’s air purifiers.
""")

with st.expander("💧 Tree Roots Save Water"):
    st.markdown("""
Roots slow down water loss and boost groundwater.  
Forests protect rivers, lakes, and village tanks.
""")

with st.expander("🐝 Biodiversity from Tree Planting"):
    st.markdown("""
Trees give shelter to birds, bees, and small animals.  
Afforestation restores habitats and supports wildlife.
""")

with st.expander("🧒 Youth in Tree Missions"):
    st.markdown("""
Students planting trees build eco-awareness.  
Schools and rural paths make great planting zones.
""")

with st.expander("📊 CO₂ Monitoring with Tech"):
    st.markdown("""
Apps and GPS help track tree-based carbon capture.  
Digital tools make afforestation smarter and transparent.
""")

with st.expander("🧭 Agroforestry: Trees on Farms"):
    st.markdown("""
Farms with trees yield more and resist drought.  
Vetiver and native trees protect soil and boost income.
""")

with st.expander("🔥 Preventing Forest Fires"):
    st.markdown("""
Fires start due to dry weather and human activity.  
Planting fire-resistant species reduces risk naturally.
""")

with st.expander("📜 Forest Laws & Green Missions"):
    st.markdown("""
India supports afforestation through legal programs.  
Green India Mission and CAMPA offer tree-planting support.
""")

with st.expander("🌾 Jobs from Tree Planting"):
    st.markdown("""
Tree projects create rural employment in nurseries and care.  
Women, SHGs, and youth groups benefit the most.
""")
 "🪴 Duckweed – Tiny Plant, Big Impact": {
        "Duckweed and CO₂ removal": """
🪴 Duckweed is a super-fast-growing aquatic plant that absorbs CO₂ rapidly. It doubles every 1–2 days under good conditions.
""",
        "Duckweed’s climate role": """
🌊 Duckweed purifies water, stores carbon, and produces biofuel. It’s one of the most efficient natural CO₂ absorbers.
""",
        "Where duckweed thrives": """
🏞️ Duckweed grows in freshwater ponds, tanks, and lakes. It’s perfect for rural water bodies near farmlands.
"""
    },

    "🌾 Vetiver Grass – A Green Protector": {
        "Vetiver for CO₂ absorption": """
🌾 Vetiver’s deep roots capture CO₂ underground and prevent soil erosion. It improves land and stores carbon in the root zone.
""",
        "Why vetiver is climate-smart": """
🔥 Drought and flood resistant. Vetiver grows in degraded soils and harsh climates. Ideal for India's changing weather patterns.
""",
        "Vetiver's extra uses": """
💧 Used in perfumes, medicine, erosion control, and water treatment. Planted near roads, canals, and hills.
"""
    },

    "🧪 Soil & Growth Factors": {
        "Soil types and tree health": """
🌱 Soil affects root strength, water retention, and nutrient absorption. Neem loves sandy loam. Tamarind likes red soil.
""",
        "Understanding soil pH": """
🧪 Ideal soil pH is between 6.0–7.5. It helps nutrients flow to roots. Test your soil before large planting.
""",
        "Survival & growth factor": """
✅ Survival rate = how many trees survive.  
📈 Growth factor = how fast they grow. Both impact total CO₂ absorption.
"""
    },

    "🌿 Why This Project Matters": {
        "Your role in climate action": """
🧍 One tree planted = less CO₂, better air, more life.  
🌱 1,000 trees = real change in your school, village, or city.
""",
        "Supporting the SDGs": """
🎯 This project aligns with:  
- ✅ SDG 13: Climate Action  
- ✅ SDG 15: Life on Land  
- ✅ SDG 6: Clean Water  
- ✅ SDG 3: Health  
- ✅ SDG 1 & 8: No Poverty & Work
""",
        "East Godavari impact": """
📍 Using real local tree data, this app lets anyone—from students to farmers—understand their impact.  
From planting to carbon math — knowledge grows action.
"""
    }
}

# Show lessons based on search
for section, topics in lessons.items():
    filtered = {k: v for k, v in topics.items() if search in k.lower() or search in v.lower()}
    if filtered:
        st.subheader(section)
        for title, content in filtered.items():
            with st.expander(f"📘 {title}"):
                st.markdown(content)

# 🌟 Footer Message
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px; font-size: 18px; color: green;'>
        🌿 Thank you for learning with us! Every tree you plant makes our planet greener.  
        Let's grow knowledge and forests together. 💚  
        <br><br>
        — Your Tree Impact Team
    </div>
    """,
    unsafe_allow_html=True
)
