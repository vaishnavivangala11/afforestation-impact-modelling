import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# 📄 File to store chat messages
chat_file = os.path.join(os.path.dirname(__file__), "..", "app", "community_chat.csv")
os.makedirs(os.path.dirname(chat_file), exist_ok=True)

# 🌐 Page configuration
st.set_page_config(page_title="💬 Community Chat Wall", page_icon="💭")
st.title("💬 Community Chat Wall")

st.markdown("""
Let's grow conversations like tree branches! 🌱  
Post your messages and reply to others — with emojis too! 😊🌳❤️  
""")

# 📝 Main message form
with st.form("main_chat_form", clear_on_submit=True):
    user = st.text_input("Your Name", placeholder="Type your name 😊", max_chars=30)
    message = st.text_area("Your Message", placeholder="Write something... use emojis like 🌳❤️🔥", max_chars=500)
    send = st.form_submit_button("📨 Post Message")

# 💾 Load or create chat DataFrame
if os.path.exists(chat_file):
    chat_df = pd.read_csv(chat_file)
else:
    chat_df = pd.DataFrame(columns=["ID", "Timestamp", "User", "Message", "Parent_ID"])

# 💾 Save new main message
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

# 🔁 Display messages and nested replies
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

        # Reply form under each message
        with st.expander(f"{'↪️' if level == 0 else '🔁'} Reply to {row['User']}"):
            with st.form(f"reply_form_{row['ID']}", clear_on_submit=True):
                reply_user = st.text_input("Your Name", placeholder="Your name 😊", key=f"user_{row['ID']}")
                reply_msg = st.text_area("Your Reply", placeholder="Write a reply with emojis! 💬🌱", key=f"msg_{row['ID']}")
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

        # 🔁 Recursively show replies
        display_messages(df, parent_id=row["ID"], level=level + 1)

# 💬 Show all community messages
if not chat_df.empty:
    st.markdown("## 🧱 Messages from the Community")
    display_messages(chat_df)
else:
    st.info("No messages yet. Be the first to start a conversation! 😊")
