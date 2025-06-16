import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import os
from fpdf import FPDF

# ✅ This must be the first Streamlit command
st.set_page_config(page_title="Afforestation Impact – East Godavari", page_icon="🌳", layout="wide")

# ✅ Hide Streamlit’s default page links
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# ✅ Mobile users navigation tip
st.markdown("""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
    🔍 <strong>Tip:</strong> Tap the <strong>☰ menu</strong> (top-left) to access <em>Learn</em>, <em>Quiz</em>, and <em>Green Community</em> pages!
</div>
""", unsafe_allow_html=True)

# ✅ Title
st.title("🌿 Afforestation Impact Modelling")

# ✅ File path setup
file_path = os.path.join("app", "local_species.xlsx")

# ✅ Load the tree species data
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    st.error("🚫 Tree species file not found. Please make sure 'local_species.xlsx' is in the 'app/' folder.")
    st.stop()

# ✅ User inputs
tree = st.selectbox("Select a Tree Species", df['Tree'])
age = st.slider("Enter Tree Age (in Years)", 1, 200, 1)

# ✅ Get selected tree row
row = df[df['Tree'] == tree].iloc[0]

# ✅ Display CO₂ calculation
factor = row['Growth_Factor']
rate = row['Survival_Rate']
co2 = factor * rate * age * 26  # example formula

# ✅ Show outputs
st.markdown(f"📈 **Growth Factor**: {factor}")
st.markdown(f"💧 **Survival Rate**: {rate}")
st.success(f"🌳 A {tree} tree absorbs approx. **{co2:.1f} kg of CO₂** over {age} years.")

# ✅ Max age
if 'Max_Age' in row:
    st.info(f"🎯 Max Age for {tree}: **{row['Max_Age']} years**")

# ✅ Explanation
with st.expander("📘 How is this CO₂ value calculated? Click to see the formula"):
    st.markdown("""
    **Formula Used:**
    \n`CO₂ Absorbed = Growth Factor × Survival Rate × Age × Base CO₂`
    \nWhere base CO₂ = 26 kg/year.
    """)

# ✅ Soil and location info
st.markdown(f"🪴 **Soil Type**: {row['Soil_Type']}")
st.markdown(f"📍 **Best Place to Plant**: {row['Best_Place_to_Plant']}")
