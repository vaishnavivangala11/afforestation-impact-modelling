import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 🌱 Page Setup
st.set_page_config(page_title="Green Community – Feedback", page_icon="🌿")
st.title("🌱 Green Community – Share Your Thoughts")

# 💚 Intro Message
st.markdown("""
<div style="background-color:#e3fcef;padding:18px;border-radius:12px;border-left:5px solid #66bb6a;font-size:16px;line-height:1.6">
    🌼 <strong>“Each voice is a leaf, each thought a bloom.”</strong><br><br>

    🍀 Your feedback is more than words — it’s the sunlight that helps this green app grow.  
    ✨ Tell us what you feel, what you dream, or what we could do better.  
    💌 Whether it's a cheer, an idea, or a whisper — let it bloom here.  

    ❤️ <em>Join our forest of ideas and make a difference, one word at a time.</em> 🌳  
</div>
""", unsafe_allow_html=True)

# 📂 Feedback file path
feedback_file = os.path.join(os.path.dirname(__file__), "..", "app", "feedback.csv")
os.makedirs(os.path.dirname(feedback_file), exist_ok=True)

# 📝 Feedback Form
with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("👤 Your Name (Optional)", placeholder="Enter your name or leave blank for Anonymous")
    feedback = st.text_area("💬 Share your feedback", placeholder="Write your thoughts here... 💚")
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
        st.success("✅ Thank you! Your feedback has been added to the Green Community wall below. 🌿")
        st.rerun()

# 🌿 Show Feedback Count
if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    st.markdown(f"### 👥 Total Feedback Received: **{len(df)}** 💌")

# 💬 Feedback Wall
st.markdown("## 💬 Community Wall – What Others Are Saying")

if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    df = df.sort_values("Timestamp", ascending=False)

    for _, row in df.iterrows():
        st.markdown(f"""
        <div style='background-color:#f4fff4;padding:12px;border-radius:10px;margin-bottom:12px;border-left:5px solid #80cbc4'>
            <strong>👤 {row['Name']}</strong>  
            <br>⭐ <b>Rating:</b> {row['Rating']} / 5  
            <p style='margin-top:8px;'>{row['Feedback']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No feedback yet. Be the first to share your thoughts! 😊")
