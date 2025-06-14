import streamlit as st

st.set_page_config(page_title="Green Community", page_icon="🌿")
st.title("🌿 Green Community")

st.caption("Share your thoughts, feedback, or appreciation about this project!")

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 🌱 Page Setup
st.set_page_config(page_title="Green Community – Feedback", page_icon="🌿")
st.title("🌱 Green Community – Share Your Thoughts")

st.markdown("""
We believe in growing **together** – like a forest. 🌳  
Your voice helps us improve and inspires others.  
Share your thoughts, feedback, or experience below. 💚
""")

# 📂 File to store feedback
feedback_file = os.path.join(os.path.dirname(__file__), "..", "app", "feedback.csv")

# 📝 Feedback Form
with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("Your Name (Optional)", placeholder="Enter your name or leave blank for Anonymous")
    feedback = st.text_area("💬 Share your feedback", placeholder="Write your thoughts here...")
    rating = st.slider("🌟 Rate this Web App (1 = Poor, 5 = Excellent)", 1, 5, 5)
    submit = st.form_submit_button("📩 Submit Feedback")

# 💾 Save Feedback
if submit:
    if feedback.strip() == "":
        st.warning("⚠️ Please enter some feedback before submitting.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([{
            "Timestamp": timestamp,
            "Name": name if name else "Anonymous",
            "Feedback": feedback,
            "Rating": rating
        }])

        if os.path.exists(feedback_file):
            existing = pd.read_csv(feedback_file)
            updated = pd.concat([existing, new_entry], ignore_index=True)
        else:
            updated = new_entry

        updated.to_csv(feedback_file, index=False)
        st.success("✅ Thank you! Your feedback has been added to the Green Community wall below.")

# 🌿 Show Community Feedback
st.markdown("## 💬 Community Wall – What Others Are Saying")

if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    df = df.sort_values("Timestamp", ascending=False)
    
    for _, row in df.iterrows():
        st.markdown(f"""
        <div style='background-color:#f4fff4;padding:10px;border-radius:8px;margin-bottom:10px'>
            <strong>👤 {row['Name']}</strong>  
            ⭐ **Rating**: {row['Rating']} / 5  
            <p>{row['Feedback']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No feedback yet. Be the first to share your experience!")
