import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# ✅ Page config
st.set_page_config(page_title="💬 Green Community", page_icon="🌿")

# 📁 File paths
base_dir = os.path.dirname(__file__)
chat_file = os.path.join(base_dir, "..", "app", "community_chat.csv")
feedback_file = os.path.join(base_dir, "..", "app", "community_feedback.csv")
os.makedirs(os.path.dirname(chat_file), exist_ok=True)
os.makedirs(os.path.dirname(feedback_file), exist_ok=True)

# 🌿 Sidebar Tip
st.sidebar.markdown("🔗 **Navigation Tip:** Use the sidebar to explore 📘 Learn | 📝 Quiz | 💬 Green Community")

# 🌱 Welcome Box
st.markdown("""
<div style='background-color:#e6ffe6; padding: 15px; border-left: 5px solid #2e7d32; border-radius: 10px;'>
    <h3>🌿 Green Community Wall</h3>
    <p>“Every message is a leaf, every reply a branch — together we grow a forest of thoughts.” 🌳💬</p>
    <p>Let’s build an inspiring space for eco-conversations, questions, and love for nature. 🌱✨</p>
</div>
""", unsafe_allow_html=True)

# 📬 Post a Message
with st.form("main_chat_form", clear_on_submit=True):
    user = st.text_input("👤 Your Name", placeholder="Enter your name")
    message = st.text_area("🌿 Your Message", placeholder="Start the conversation...")
    send = st.form_submit_button("📨 Post")

# Load chat messages
if os.path.exists(chat_file):
    chat_df = pd.read_csv(chat_file)
else:
    chat_df = pd.DataFrame(columns=["ID", "Timestamp", "User", "Message", "Parent_ID"])

# Save new message
if send:
    if user.strip() and message.strip():
        new_entry = pd.DataFrame([{
            "ID": str(uuid.uuid4()),
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "User": user.strip(),
            "Message": message.strip(),
            "Parent_ID": ""
        }])
        chat_df = pd.concat([chat_df, new_entry], ignore_index=True)
        chat_df.to_csv(chat_file, index=False)
        st.success("✅ Message posted!")
        st.rerun()
    else:
        st.warning("⚠️ Please fill in both name and message.")

# 🌲 Display Messages
def display_messages(df, parent_id="", level=0):
    messages = df[df["Parent_ID"] == parent_id].sort_values("Timestamp", ascending=False)
    for _, row in messages.iterrows():
        st.markdown(f"""
        <div style='background-color:#f0f8ff;padding:10px;border-radius:8px;margin-bottom:5px;margin-left:{level*20}px'>
            <strong>👤 {row['User']}</strong><br>
            <p>{row['Message']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

        # Reply section
        with st.expander(f"💬 Reply to {row['User']}"):
            with st.form(f"reply_form_{row['ID']}", clear_on_submit=True):
                reply_user = st.text_input("Your Name", key=f"user_{row['ID']}")
                reply_msg = st.text_area("Reply Message", key=f"msg_{row['ID']}")
                reply_submit = st.form_submit_button("Reply")
                if reply_submit and reply_user.strip() and reply_msg.strip():
                    reply_entry = pd.DataFrame([{
                        "ID": str(uuid.uuid4()),
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "User": reply_user.strip(),
                        "Message": reply_msg.strip(),
                        "Parent_ID": row["ID"]
                    }])
                    df = pd.concat([df, reply_entry], ignore_index=True)
                    df.to_csv(chat_file, index=False)
                    st.success("✅ Reply posted!")
                    st.rerun()

        display_messages(df, parent_id=row["ID"], level=level+1)

# Show all messages
st.markdown("## 🧱 Community Messages")
if not chat_df.empty:
    display_messages(chat_df)
else:
    st.info("📭 No messages yet. Be the first leaf on our tree! 🌿")

# ─────────────────────────────
# 🌟 Feedback Section
# ─────────────────────────────
st.markdown("---")
st.markdown("## 🌼 Share Your Feedback")

# Load feedback
if os.path.exists(feedback_file):
    feedback_df = pd.read_csv(feedback_file)
else:
    feedback_df = pd.DataFrame(columns=["Timestamp", "Name", "Rating", "Feedback"])

# Show total and feedbacks
st.markdown(f"📊 **Total Feedback Received:** {len(feedback_df)}")
if not feedback_df.empty:
    for _, row in feedback_df.sort_values("Timestamp", ascending=False).iterrows():
        st.markdown(f"""
        <div style='background-color:#fffbe6;padding:10px;border-radius:8px;margin-bottom:5px'>
            <strong>🌟 {row['Name']}</strong> – ⭐️ {row['Rating']}/5<br>
            <em>{row['Feedback']}</em><br>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

# Feedback form
with st.form("feedback_form", clear_on_submit=True):
    fb_name = st.text_input("Your Name (Optional)")
    fb_rating = st.slider("🌟 Rate the App", 1, 5, 5)
    fb_text = st.text_area("Your Feedback", placeholder="Share your thoughts...")
    fb_submit = st.form_submit_button("✅ Submit Feedback")

if fb_submit:
    if not fb_text.strip():
        st.warning("⚠️ Please enter feedback before submitting.")
    else:
        entry = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": fb_name if fb_name.strip() else "Anonymous",
            "Rating": fb_rating,
            "Feedback": fb_text.strip()
        }])
        feedback_df = pd.concat([feedback_df, entry], ignore_index=True)
        feedback_df.to_csv(feedback_file, index=False)
        st.success("🌟 Thanks for your feedback!")
        st.rerun()
