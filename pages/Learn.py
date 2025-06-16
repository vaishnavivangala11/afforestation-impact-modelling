import streamlit as st

# ✅ Page setup
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")
st.title("📘 Learn: Trees, CO₂ & Climate Solutions")
st.markdown("Empower yourself with knowledge on how trees, duckweed, and vetiver help our planet. 🌍")

# ✅ Sidebar navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.markdown("[🏠 Home](./)")
st.sidebar.markdown("[📘 Learn](./Learn)")
st.sidebar.markdown("[🧠 Quiz](./Quiz)")
st.sidebar.markdown("[🌱 Green Community](./Green_Community)")

# ✅ Mobile-friendly sidebar tip
st.markdown("""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
    🔍 <strong>Tip:</strong> Tap the <strong>☰ menu</strong> at the top-left to navigate to <em>Learn</em>, <em>Quiz</em>, or <em>Green Community</em>!
</div>
""", unsafe_allow_html=True)

# ✅ Emoji Legend
with st.expander("🌟 Emoji Legend (Click to view)"):
    st.markdown("""
- 🌳 Tree, 🌿 Plant, 🌾 Grass  
- 💧 Water, 🌡️ Heat, 💨 Air  
- 🔥 Fire, 🐝 Wildlife, 📜 Law  
- 📊 Data, 🧮 Formula, 🧠 Quiz  
- 🪴 Duckweed, 📍 Location, 📘 Info  
""")

# ✅ Search bar
search = st.text_input("🔍 Search a topic...", "").lower()

# ✅ Educational topics grouped by category
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

# ✅ Show matching topics
for section, topics in lessons.items():
    filtered = {k: v for k, v in topics.items() if search in k.lower() or search in v.lower()}
    if filtered:
        st.subheader(section)
        for title, content in filtered.items():
            with st.expander(f"📘 {title}"):
                st.markdown(content)

# ✅ Footer & Back to Top
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; font-size: 18px; color: green;'>
🌿 Thank you for learning with us! Every tree you plant makes our planet greener.  
Let's grow knowledge and forests together. 💚
</div>
<br>
<a href='#Learn-Trees,-CO₂-&-Climate-Solutions' style='text-decoration: none;'>
⬆️ <strong>Back to Top</strong>
</a>
""", unsafe_allow_html=True)
