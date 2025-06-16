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

# 📂 Feedback file
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

# 🌿 Show Feedback Count
if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    st.markdown(f"### 👥 Total Feedback Received: **{len(df)}**")

# 🔐 Admin-only section (hidden until password entered)
delete_mode = False
admin_logged_in = False
if "admin_auth" not in st.session_state:
    st.session_state.admin_auth = False

# Ask for password if not already logged in
if not st.session_state.admin_auth:
    with st.expander("🔒 Admin Login"):
        admin_pass = st.text_input("Enter Admin Password", type="password")
        if admin_pass == "Pikachu@05":
            st.session_state.admin_auth = True
            st.success("🛡️ Admin mode activated.")
        elif admin_pass:
            st.error("❌ Incorrect password")

# 🌿 Show Feedback Wall
st.markdown("## 💬 Community Wall – What Others Are Saying")

if os.path.exists(feedback_file):
    df = pd.read_csv(feedback_file)
    df = df.sort_values("Timestamp", ascending=False)

    indexes_to_delete = []

    for index, row in df.iterrows():
        st.markdown(f"""
        <div style='background-color:#f4fff4;padding:10px;border-radius:8px;margin-bottom:10px'>
            <strong>👤 {row['Name']}</strong><br>
            ⭐ <b>Rating:</b> {row['Rating']} / 5  
            <p>{row['Feedback']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

        # ✅ Show delete button only if admin is authenticated
        if st.session_state.admin_auth:
            if st.button(f"🗑️ Delete this feedback", key=str(index)):
                indexes_to_delete.append(index)

    # ✅ Delete selected feedbacks (admin only)
    if indexes_to_delete:
        df.drop(index=indexes_to_delete, inplace=True)
        df.to_csv(feedback_file, index=False)
        st.success("✅ Selected feedback(s) deleted. Please refresh the page.")
else:
    st.info("No feedback yet. Be the first to share your thoughts!")
