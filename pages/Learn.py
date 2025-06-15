import streamlit as st
from fpdf import FPDF
import base64
import re

# Page configuration
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")

st.title("📘 Learn: Trees, CO₂ & Climate Solutions")
st.markdown("Empower yourself with knowledge on how trees, duckweed, and vetiver help our planet. 🌍")

# Sidebar navigation
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/Learn.py", label="📘 Learn")

# Search bar
search = st.text_input("🔍 Search a topic...", "").lower()

# Educational content grouped by theme
lessons = {
    "🌍 CO₂ & Climate Science": {
        "How trees help reduce CO₂ levels": """
Trees absorb carbon dioxide (CO₂) through photosynthesis. The gas is stored in their trunk, branches, leaves, and roots as biomass. Planting trees directly removes CO₂ from the atmosphere and helps fight climate change.
""",
        "The greenhouse effect and global warming": """
CO₂ and other gases trap heat in Earth’s atmosphere. This natural greenhouse effect keeps Earth warm, but too much CO₂ causes excessive warming, sea-level rise, and extreme weather.
""",
        "Understanding CO₂ sequestration": """
Sequestration means long-term storage of CO₂. Trees, soil, wetlands, and grasslands act as carbon sinks. Growing more plants increases Earth’s ability to store carbon safely.
""",
        "Why reducing CO₂ is urgent": """
High CO₂ levels harm the planet by changing weather patterns, melting glaciers, and heating oceans. Every ton of CO₂ removed helps restore balance and protect life on Earth.
""",
        "CO₂ Absorption Formula": """
**Formula:**  
`CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor`  
**Example:** A Neem tree with 1-year age = `1 × 25 × 0.85 × 1.0 = 21.25 kg CO₂`  
This formula estimates CO₂ captured based on tree species and growth conditions.
"""
    },

    "🌱 Tree Planting & Afforestation": {
        "What is afforestation and reforestation": """
Afforestation means planting trees in areas where there were no forests before. Reforestation is restoring lost forests. Both play a major role in increasing green cover and reversing damage from deforestation.
""",
        "Benefits of planting native species": """
Native trees grow well in local conditions, need less water, and support local birds, insects, and soil. Neem, Peepal, Pongamia, and Indian Almond are good native choices in East Godavari.
""",
        "Tree growth and CO₂ absorption": """
Trees grow at different rates. Fast-growing trees like Subabul and Pongamia absorb more CO₂ quickly, while long-living trees like Banyan store carbon over many decades.
""",
        "How to care for saplings": """
Protect young trees with guards, water them regularly, and mulch the base to retain moisture. The first 2 years are crucial for survival and strong roots.
"""
    },

    "🪴 Duckweed – Tiny Plant, Massive Impact": {
        "Duckweed and CO₂ removal": """
Duckweed is one of the world’s fastest-growing aquatic plants. It absorbs CO₂ from both water and air and doubles in size every 1–2 days under ideal conditions.
""",
        "Duckweed as a climate solution": """
Duckweed grows on ponds and helps in carbon capture, water purification, and even biofuel production. It can absorb CO₂ like fast-growing trees in a fraction of the time.
""",
        "Where duckweed grows best": """
Duckweed thrives in still freshwater ponds, tanks, and village lakes. It can be grown near farms and reused as animal feed or compost.
"""
    },

    "🌾 Vetiver Grass – A Green Protector": {
        "Vetiver for CO₂ absorption": """
Vetiver is a deep-rooted grass that captures CO₂ underground in its long roots. It helps sequester carbon and stabilizes soil in degraded lands.
""",
        "Why vetiver is climate-smart": """
It survives drought, floods, and poor soil, making it ideal for India's changing climate. Vetiver improves soil fertility and prevents erosion.
""",
        "Uses beyond CO₂": """
Vetiver roots are used in perfumes, mats, and medicines. It filters wastewater and is often planted near highways, canals, and hillsides for protection.
"""
    },

    "🧪 Soil & Growth Factors": {
        "Importance of soil type in tree growth": """
The type of soil affects how well a tree absorbs water and nutrients. Sandy loam is ideal for Neem and Amla, while red soil suits Tamarind and Indian Almond.
""",
        "What is soil pH?": """
Soil pH affects how easily nutrients are absorbed by roots. Most trees grow well in slightly acidic to neutral soils (pH 6.0 to 7.5).
""",
        "Survival rate and growth factor": """
Survival rate measures how many trees remain alive after planting. Growth factor shows how quickly they grow. Both affect total CO₂ captured.
"""
    },

    "🌿 Why This Project Matters": {
        "Your tree, your climate action": """
Planting even one tree helps reduce CO₂, clean the air, and improve water cycles. Imagine the impact of 1,000 trees planted in your village or school!
""",
        "Supporting the SDGs": """
This project supports **Sustainable Development Goals** like:
- SDG 13: Climate Action  
- SDG 15: Life on Land  
- SDG 6: Clean Water  
- SDG 3: Good Health  
- SDG 1 & 8: No Poverty & Decent Work
""",
        "Local impact in East Godavari": """
By using local species data and simulating actual CO₂ absorption, this app empowers individuals, schools, and communities to take action.
From better air to better jobs — every tree counts.
"""
    }
}

# Show filtered content + build text for PDF
pdf_text = ""
for section, topics in lessons.items():
    filtered = {k: v for k, v in topics.items() if search in k.lower() or search in v.lower()}
    if filtered:
        st.subheader(section)
        pdf_text += f"\n\n{section}\n"
        for title, content in filtered.items():
            with st.expander(f"📘 {title}"):
                st.markdown(content)
            # Remove emojis from PDF text
            clean_title = re.sub(r"[^\x00-\x7F]+", "", title)
            clean_content = re.sub(r"[^\x00-\x7F]+", "", content)
            pdf_text += f"\n{clean_title}\n{clean_content.strip()}\n"

# PDF download section
if pdf_text:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in pdf_text.split("\n"):
        pdf.multi_cell(0, 10, txt=line)
    pdf_output = pdf.output(dest="S").encode("latin-1", errors="ignore")
    b64_pdf = base64.b64encode(pdf_output).decode("utf-8")
    st.markdown("---")
    st.markdown(
        f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="Learn_Tree_CO2_Education.pdf">📄 Click to Download this Page as PDF</a>',
        unsafe_allow_html=True
    )



