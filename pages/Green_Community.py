import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# 📁 File paths
chat_file = os.path.join(os.path.dirname(__file__), "..", "app", "community_chat.csv")
feedback_file = os.path.join(os.path.dirname(__file__), "..", "app", "community_feedback.csv")
os.makedirs(os.path.dirname(chat_file), exist_ok=True)
os.makedirs(os.path.dirname(feedback_file), exist_ok=True)

# 🌐 Page settings
st.set_page_config(page_title="💬 Green Community Chat", page_icon="🌿")
st.title("💬 Green Community Chat Wall")

# 🌱 Intro
st.markdown("""
<div style='background-color:#e8f5e9; padding: 15px; border-radius: 10px; border-left: 5px solid #66bb6a'>
    <h4>🌱 Let’s grow conversations like tree branches!</h4>
    <p>Every message adds a leaf to our community tree. 🌳💬<br>
    Feel free to express yourself and reply with love and knowledge. 🌿❤️</p>
</div>
""", unsafe_allow_html=True)

# 📝 Post new message
with st.form("main_chat_form", clear_on_submit=True):
    user = st.text_input("Your Name", placeholder="Type your name 😊", max_chars=30)
    message = st.text_area("Your Message", placeholder="Write something here... 🌱", max_chars=500)
    send = st.form_submit_button("📨 Post Message")

# Load messages
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
        st.experimental_rerun()
    else:
        st.warning("⚠️ Please fill in both name and message.")

# 🧵 Show messages + replies
def display_messages(df, parent_id="", level=0):
    messages = df[df["Parent_ID"] == parent_id].sort_values("Timestamp", ascending=False)
    for _, row in messages.iterrows():
        st.markdown(f"""
        <div style='background-color:#f0f8ff;padding:10px;border-radius:8px;margin-bottom:5px;margin-left:{level*20}px'>
            <strong>👤 {row['User']}</strong>  
            <p>{row['Message']}</p>
            <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"{'↪️' if level == 0 else '🔁'} Reply to {row['User']}"):
            with st.form(f"reply_form_{row['ID']}", clear_on_submit=True):
                reply_user = st.text_input("Your Name", placeholder="Your name 😊", key=f"user_{row['ID']}")
                reply_msg = st.text_area("Your Reply", placeholder="Write your reply here 🌿", key=f"msg_{row['ID']}")
                reply_submit = st.form_submit_button("Reply")
                if reply_submit:
                    if reply_user.strip() and reply_msg.strip():
                        reply_entry = pd.DataFrame([{
                            "ID": str(uuid.uuid4()),
                            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "User": reply_user.strip(),
                            "Message": reply_msg.strip(),
                            "Parent_ID": row["ID"]
                        }])
                        chat_df = pd.concat([chat_df, reply_entry], ignore_index=True)
                        chat_df.to_csv(chat_file, index=False)
                        st.success("✅ Reply posted!")
                        st.experimental_rerun()
                    else:
                        st.warning("⚠️ Name and reply cannot be empty.")

        display_messages(df, parent_id=row["ID"], level=level + 1)

# 🧱 Display community messages
if not chat_df.empty:
    st.markdown("## 🧱 Messages from the Community")
    display_messages(chat_df)
else:
    st.info("No messages yet. Be the first to start a conversation! 😊")

# ───────────────────────────────────────────────
# 🌿 Feedback Section
# ───────────────────────────────────────────────

st.markdown("---")
st.markdown("## 🌿 Help Us Grow – Share Your Thoughts About This Green App")

# 📊 Show feedback count
if os.path.exists(feedback_file):
    feedback_df = pd.read_csv(feedback_file)
    st.markdown(f"**🧾 Total feedback received: {len(feedback_df)}**")
else:
    feedback_df = pd.DataFrame(columns=["Timestamp", "Name", "Rating", "Feedback"])
    st.markdown("**🧾 Total feedback received: 0**")

# 📝 Feedback form
with st.form("rating_form", clear_on_submit=True):
    fb_name = st.text_input("Your Name (Optional)", placeholder="Enter your name")
    fb_rating = st.slider("How would you rate this app?", 1, 5, 5)
    fb_text = st.text_area("Feedback (Optional)", placeholder="Share your experience or suggestions...")
    fb_submit = st.form_submit_button("✅ Submit Feedback")

# 💾 Save feedback + confirmation
if fb_submit:
    fb_entry = pd.DataFrame([{
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Name": fb_name if fb_name.strip() else "Anonymous",
        "Rating": fb_rating,
        "Feedback": fb_text
    }])

    if os.path.exists(feedback_file):
        existing = pd.read_csv(feedback_file)
        all_feedback = pd.concat([existing, fb_entry], ignore_index=True)
    else:
        all_feedback = fb_entry

    all_feedback.to_csv(feedback_file, index=False)
    st.success("✅ Your feedback has been received and recorded. We truly appreciate your thoughts! 🌿")
    st.experimental_rerun()
