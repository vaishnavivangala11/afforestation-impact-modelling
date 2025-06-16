import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# ✅ Page config
st.set_page_config(page_title="💬 Green Community", page_icon="🌿")

# ✅ File paths (shared across users)
chat_file = "app/community_chat.csv"
feedback_file = "app/community_feedback.csv"

# ✅ Make sure files exist
if not os.path.exists(chat_file):
    pd.DataFrame(columns=["ID", "Timestamp", "User", "Message", "Parent_ID"]).to_csv(chat_file, index=False)
if not os.path.exists(feedback_file):
    pd.DataFrame(columns=["Timestamp", "Name", "Rating", "Feedback"]).to_csv(feedback_file, index=False)

# ✅ Load data
chat_df = pd.read_csv(chat_file)
feedback_df = pd.read_csv(feedback_file)

# ✅ Title and intro
st.title("💬 Green Community Wall")
st.markdown("🌿 Share your thoughts, ideas, or questions with the community.")

# ✅ Message form
with st.form("post_form", clear_on_submit=True):
    name = st.text_input("Your Name", max_chars=30)
    message = st.text_area("Your Message", max_chars=300)
    submit = st.form_submit_button("📨 Post Message")
    if submit:
        if name.strip() and message.strip():
            new = pd.DataFrame([{
                "ID": str(uuid.uuid4()),
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "User": name.strip(),
                "Message": message.strip(),
                "Parent_ID": ""
            }])
            chat_df = pd.concat([chat_df, new], ignore_index=True)
            chat_df.to_csv(chat_file, index=False)
            st.success("✅ Message posted!")
            st.rerun()
        else:
            st.warning("Please enter both name and message.")

# ✅ Show messages
st.subheader("🧱 Community Messages")
if chat_df.empty:
    st.info("No messages yet. Be the first! 🌱")
else:
    for _, row in chat_df.sort_values("Timestamp", ascending=False).iterrows():
        st.markdown(f"""
        <div style='background-color:#e8f5e9;padding:10px;border-radius:8px;margin-bottom:5px'>
            <strong>👤 {row['User']}</strong><br>{row['Message']}<br>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

# ✅ Feedback section
st.markdown("---")
st.subheader("🌱 Share Feedback About the App")

with st.form("feedback_form", clear_on_submit=True):
    fb_name = st.text_input("Name (Optional)")
    fb_rating = st.slider("🌟 Rate this App", 1, 5, 5)
    fb_msg = st.text_area("Feedback (required)")
    fb_submit = st.form_submit_button("✅ Submit Feedback")

if fb_submit:
    if fb_msg.strip():
        entry = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": fb_name.strip() if fb_name else "Anonymous",
            "Rating": fb_rating,
            "Feedback": fb_msg.strip()
        }])
        feedback_df = pd.concat([feedback_df, entry], ignore_index=True)
        feedback_df.to_csv(feedback_file, index=False)
        st.success("🌿 Feedback received! Thank you!")
        st.rerun()
    else:
        st.warning("⚠️ Feedback message cannot be empty.")
