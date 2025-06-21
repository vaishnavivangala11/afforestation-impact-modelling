import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 🌿 Page Setup
st.set_page_config(page_title="Green Community – Feedback", page_icon="🌱")
st.title("🌱 Green Community – Share Your Thoughts")

# 🌸 Welcome Message (No background box)
st.markdown("""
🌼 **“Each voice is a leaf, each thought a bloom.”**

🍀 Your feedback is more than words — it’s the sunlight that helps this green app grow.  
✨ Tell us what you feel, what you dream, or what we could do better.  
💌 Whether it's a cheer, an idea, or a whisper — let it bloom here.  

❤️ *Join our forest of ideas and make a difference, one word at a time.* 🌳
""")

# 📂 Feedback CSV file path
feedback_file = os.path.join(os.path.dirname(__file__), "..", "app", "feedback.csv")
os.makedirs(os.path.dirname(feedback_file), exist_ok=True)

# 📝 Feedback Form
with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("Your Name (Optional)", placeholder="Enter your name or leave blank for Anonymous")
    feedback = st.text_area("💬 Share your feedback", placeholder="Write your thoughts here...")
    rating = st.slider("🌟 Rate this Web App (1 = Poor, 5 = Excellent)", 1, 5, 5)
    submit = st.form_submit_button("📩 Submit Feedback")

# 💾 Save feedback
if submit:
    if feedback.strip() == "":
        st.warning("⚠️ Please enter some feedback before submitting.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([{
            "Timestamp": timestamp,
            "Name": name.strip() if name.strip() else "Anonymous",
            "Feedback": feedback.strip(),
            "Rating": rating
        }])

        if os.path.exists(feedback_file):
            existing = pd.read_csv(feedback_file)
            updated = pd.concat([existing, new_entry], ignore_index=True)
        else:
            updated = new_entry

        updated.to_csv(feedback_file, index=False)
        st.success("✅ Thank you! Your feedback has been submitted.")
