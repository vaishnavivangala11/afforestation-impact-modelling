import streamlit as st
from fpdf import FPDF
import base64
import re

# --- Helper function to remove emojis and symbols not supported in PDF ---
def clean_text_for_pdf(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Page configuration
st.set_page_config(page_title="Learn", page_icon="📘", layout="wide")

st.title("📘 Learn: Trees, CO₂ & Climate Solutions")
st.markdown("Empower yourself with knowledge on how trees, duckweed, and vetiver help our planet. 🌍")

# Sidebar
st.sidebar.markdown("## 📚 Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
st.sidebar.page_link("pages/Learn.py", label="📘 Learn")

# Search bar
search = st.text_input("🔍 Search a topic...", "").lower()

# Educational topics
lessons = {
    "🌍 CO₂ & Climate Science": {
        "How trees help reduce CO₂ levels": """
Trees absorb carbon dioxide (CO₂) through photosynthesis. The gas is stored in their trunk, branches, leaves, and roots as biomass.
""",
        "CO₂ Absorption Formula": """
**Formula:**  
CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor  
**Example:** A Neem tree with 1-year age = 1 × 25 × 0.85 × 1.0 = 21.25 kg CO₂
"""
    },
    "🪴 Duckweed – Tiny Plant, Massive Impact": {
        "Duckweed and CO₂ removal": """
Duckweed is one of the world’s fastest-growing aquatic plants. It absorbs CO₂ and doubles in size every 1–2 days under ideal conditions.
""",
        "Where duckweed grows best": """
Duckweed thrives in still freshwater ponds, tanks, and lakes. It can be reused as animal feed or compost.
"""
    },
    "🌾 Vetiver Grass – A Green Protector": {
        "Vetiver for CO₂ absorption": """
Vetiver is a deep-rooted grass that captures CO₂ underground. It’s great for degraded lands and erosion control.
""",
        "Why vetiver is climate-smart": """
It survives drought, floods, and poor soil. Vetiver improves soil fertility and prevents erosion.
"""
    },
    "🌿 Why This Project Matters": {
        "Your tree, your climate action": """
Planting even one tree helps reduce CO₂, clean the air, and improve water cycles.
""",
        "Local impact in East Godavari": """
By using local species and simulating CO₂ absorption, this app empowers communities to take real action.
"""
    }
}

# Filter & display topics
pdf_text = ""
for section, topics in lessons.items():
    filtered = {k: v for k, v in topics.items() if search in k.lower() or search in v.lower()}
    if filtered:
        st.subheader(section)
        pdf_text += f"\n\n{section}\n"
        for title, content in filtered.items():
            with st.expander(f"📘 {title}"):
                st.markdown(content)
            clean_content = clean_text_for_pdf(content.strip())
            pdf_text += f"\n📘 {title}\n{clean_content}\n"

# PDF download
if pdf_text:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in pdf_text.split("\n"):
        pdf.multi_cell(0, 8, txt=line)
    pdf_output = pdf.output(dest="S").encode("latin-1", errors="ignore")
    b64 = base64.b64encode(pdf_output).decode("utf-8")
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Tree_Learnings.pdf">📄 Download PDF of This Page</a>'
    st.markdown("---")
    st.markdown(href, unsafe_allow_html=True)
