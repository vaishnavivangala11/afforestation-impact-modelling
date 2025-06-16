import streamlit as st
import random

# ✅ Page setup – must be first
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")

# ✅ Mobile-friendly sidebar tip
st.markdown("""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
    🔍 <strong>Tip:</strong> Tap the <strong>☰ menu</strong> at the top-left to navigate to <em>Learn</em>, <em>Quiz</em>, or <em>Green Community</em>!
</div>
""", unsafe_allow_html=True)

# ✅ Title & Intro
st.title("📘 Learn: Trees, CO₂ & Climate Solutions")
st.markdown("Empower yourself with knowledge on how trees, duckweed, and vetiver help our planet. 🌍")

# ✅ Did You Know? – Fun Fact Box
fun_facts = [
    "🌳 A mature tree can absorb around 22 kg of CO₂ per year!",
    "🪴 Duckweed doubles its mass in less than 2 days, making it a super absorber of CO₂.",
    "🌾 Vetiver roots can grow over 3 meters deep, storing carbon underground.",
    "🌍 Forests absorb about 30% of the world’s CO₂ emissions annually.",
    "🌲 India’s Green India Mission aims to increase forest cover by 5 million hectares.",
    "🧒 School tree-planting campaigns have been shown to improve climate awareness by 70%.",
    "💧 Tree roots help prevent floods by improving soil water-holding capacity.",
    "🐝 Trees attract pollinators like bees, essential for food crops.",
    "🛰️ Satellites now track tree growth and CO₂ uptake across the world.",
    "🔥 Deforestation causes nearly 10% of global greenhouse gas emissions."
]
random_fact = random.choice(fun_facts)
st.markdown(f"""
<div style="background-color: #fff8e1; padding: 15px; border-left: 6px solid #ffb300; border-radius: 8px; margin-top: 10px; font-size: 18px;">
    🌟 <strong>Did you know?</strong><br>
    {random_fact}
</div>
""", unsafe_allow_html=True)

# ✅ Sidebar Navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/Learn.py", label="📘 Learn")
st.sidebar.page_link("pages/Quiz.py", label="🧠 Quiz")
st.sidebar.page_link("pages/Green_Community.py", label="💬 Green Community")

# ✅ Search Bar
search = st.text_input("🔍 Search a topic...", "", placeholder="e.g., duckweed, CO₂, afforestation").lower()

# ✅ Educational Topics
lessons = {
    "🌍 CO₂ & Climate Science": {
        "How trees help reduce CO₂ levels": "🌳 Trees absorb CO₂ through photosynthesis and store it in their biomass.",
        "The greenhouse effect and global warming": "🌡️ CO₂ traps heat, causing extreme weather and sea-level rise.",
        "Understanding CO₂ sequestration": "🧮 Trees, duckweed, and vetiver naturally capture and store carbon long-term.",
        "CO₂ Absorption Formula": "`CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor` — Example: 1 × 25 × 0.85 × 1.0 = 21.25 kg CO₂",
        "Why reducing CO₂ is urgent": "⏳ Too much CO₂ leads to climate disasters. Every tree makes a difference."
    },
    "🌱 Tree Planting & Afforestation": {
        "What is afforestation and reforestation": "🌲 Afforestation means planting trees where there were none before.",
        "Benefits of native species": "🪵 Neem, Peepal, and Pongamia grow well locally and support biodiversity.",
        "Tree growth and CO₂ capture": "🌿 Fast-growing trees absorb more CO₂. Long-living ones store it longer.",
        "Caring for saplings": "💧 Water regularly and protect young trees, especially in the first 2 years."
    },
    "🔥 Deforestation & Its Impact": {
        "What is deforestation?": "🪓 Cutting down forests for farming or roads removes vital carbon sinks.",
        "Main causes of deforestation": "🚜 Farming, 🛣️ urban growth, 🪵 logging, and 🔥 forest fires reduce tree cover.",
        "How deforestation affects climate": "🌡️ Fewer trees = more CO₂, less rain, hotter climate, and erosion.",
        "How afforestation helps reverse it": "🌱 Planting trees restores green cover and balances ecosystems."
    },
    "🪴 Duckweed – Tiny Plant, Big Impact": {
        "Duckweed and CO₂ removal": "🪴 Duckweed grows fast and absorbs CO₂ rapidly in water bodies.",
        "Duckweed’s climate role": "🌊 It purifies water, stores carbon, and makes biofuel.",
        "Where duckweed thrives": "🏞️ Freshwater ponds, tanks, and village lakes are ideal."
    },
    "🌾 Vetiver Grass – A Green Protector": {
        "Vetiver for CO₂ absorption": "🌾 Vetiver roots store CO₂ underground and stop soil erosion.",
        "Why vetiver is climate-smart": "🔥 Grows in drought, floods, and poor soils — ideal for India.",
        "Vetiver's extra uses": "💧 Used in perfumes, medicine, and water treatment near roads and canals."
    },
    "🧪 Soil & Growth Factors": {
        "Soil types and tree health": "🌱 Neem loves sandy loam; tamarind prefers red soil for strong roots.",
        "Understanding soil pH": "🧪 Ideal pH is 6.0–7.5 for healthy plant growth. Test your soil before planting.",
        "Survival & growth factor": "✅ Survival = how many live. Growth = how fast they grow. Both affect CO₂."
    },
    "🌿 Climate & Community Topics": {
        "Urban Heat Islands & Cooling Trees": "🌡️ Trees reduce local temperatures and make cities cooler.",
        "Air Quality & Trees": "💨 Trees trap dust and absorb pollutants like NO₂ and SO₂.",
        "Water Conservation & Tree Roots": "💧 Roots improve soil water retention and recharge groundwater.",
        "Biodiversity Boosters": "🐝 Trees provide food and shelter for birds, bees, and animals.",
        "Youth, Schools & Tree Missions": "🧒 Students planting trees build eco-awareness and green school yards.",
        "CO₂ Tracking with Technology": "📊 Apps and satellite tools track how much CO₂ trees absorb.",
        "Agroforestry: Trees + Farming": "🧭 Trees with crops improve yield and reduce soil erosion.",
        "Forest Fires – Causes & Prevention": "🔥 Vetiver and native trees reduce fire risk by acting as fire-breaks.",
        "Indian Forest Laws & Missions": "📜 CAMPA, Green India Mission support afforestation in India.",
        "Local Community & Job Creation": "🌾 Tree projects create jobs in nurseries, planting, and care."
    },
    "🌟 Why This Project Matters": {
        "Your role in climate action": "🧍 One tree planted = less CO₂, more oxygen, and a better future.",
        "Supporting the SDGs": "🎯 This project supports SDG 13 (Climate), SDG 15 (Life on Land), and more.",
        "East Godavari impact": "📍 Real tree data + local focus helps communities make informed green decisions."
    }
}

# ✅ Display Filtered Topics
for section, topics in lessons.items():
    filtered = {k: v for k, v in topics.items() if search in k.lower() or search in v.lower()}
    if filtered:
        st.subheader(section)
        for title, content in dict(sorted(filtered.items())).items():
            with st.expander(f"📘 {title}"):
                st.markdown(content)
        st.markdown("[🔝 Back to top](#learn-trees-co2--climate-solutions)")

# ✅ Emoji Legend (Optional)
with st.expander("🗺️ Emoji Legend"):
    st.markdown("""
    - 🌳 Trees  
    - 🪴 Duckweed  
    - 🌾 Vetiver  
    - 🔥 Forest Fires  
    - 💧 Water  
    - 🧪 Soil & pH  
    - 📊 CO₂ Tech  
    - 📜 Policies  
    """)

# ✅ Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px; font-size: 18px; color: #2e7d32; background-color:#e8f5e9; border-radius: 10px;'>
        🌿 <strong>Thank you for learning with us!</strong><br>  
        Every tree you plant makes our planet greener.  
        Let’s grow knowledge and forests together. 💚
    </div>
    """,
    unsafe_allow_html=True
)
