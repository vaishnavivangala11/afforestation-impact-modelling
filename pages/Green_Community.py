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
os.makedirs(os.path.dirname(feedback_file), exist_ok=True)

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

# 👥 Show Total Feedback
if os.path.exists(feedback_file):
    total_feedback = len(pd.read_csv(feedback_file))
    st.markdown(f"### 👥 Total Feedback Received: **{total_feedback}**")

# 🌿 Show Community Feedback
st.markdown("## 💬 Community Wall – What Others Are Saying")

if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    df = df.sort_values("Timestamp", ascending=False)

    for index, row in df.iterrows():
        st.markdown(f"""
        <div style='background-color:#f4fff4;padding:10px;border-radius:8px;margin-bottom:10px'>
            <strong>👤 {row['Name']}</strong><br>
            ⭐ <b>Rating:</b> {row['Rating']} / 5  
            <p>{row['Feedback']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

    # 🔐 Admin Delete Option
    with st.expander("🛠️ Admin: Delete All Feedback"):
        password = st.text_input("Enter Admin Password to Delete", type="password")
        if st.button("🗑️ Delete All Feedback"):
            if password == "Pikachu@05":
                os.remove(feedback_file)
                st.success("✅ All feedback has been deleted.")
            else:
                st.error("❌ Incorrect password. Access denied.")
else:
    st.info("No feedback yet. Be the first to share your thoughts!")
