# ────────────────────────────────
# 🌿 Feedback Section
# ────────────────────────────────

st.markdown("---")
st.markdown("## 🌿 Help Us Grow – Share Your Thoughts About This Green App")

# 📁 Correct file path (outside the app folder, just in project root)
feedback_file = "feedback.csv"

# 🔁 Load existing feedback
if os.path.exists(feedback_file):
    feedback_df = pd.read_csv(feedback_file)
    st.markdown(f"**🧾 Total feedback received: {len(feedback_df)}**")
else:
    feedback_df = pd.DataFrame(columns=["Timestamp", "Name", "Rating", "Feedback"])
    st.markdown("**🧾 Total feedback received: 0**")

# 📝 Feedback form
with st.form("feedback_form", clear_on_submit=True):
    fb_name = st.text_input("Your Name (Optional)", placeholder="Type your name")
    fb_rating = st.slider("🌟 Rate this App", 1, 5, 5)
    fb_text = st.text_area("Your Feedback", placeholder="Tell us what you think...")
    fb_submit = st.form_submit_button("✅ Submit Feedback")

# 💾 Save feedback
if fb_submit:
    if fb_text.strip() == "":
        st.warning("⚠️ Please provide feedback before submitting.")
    else:
        new_entry = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": fb_name.strip() if fb_name.strip() else "Anonymous",
            "Rating": fb_rating,
            "Feedback": fb_text.strip()
        }])
        feedback_df = pd.concat([feedback_df, new_entry], ignore_index=True)
        feedback_df.to_csv(feedback_file, index=False)
        st.success("✅ Thank you! Your feedback was submitted.")
        st.rerun()

# 📬 Display past feedback
if not feedback_df.empty:
    st.markdown("### 📬 What People Are Saying")
    for _, row in feedback_df.sort_values("Timestamp", ascending=False).iterrows():
        st.markdown(f"""
        <div style='background-color:#f9fbe7; padding:10px; border-left: 4px solid #aed581; border-radius:5px; margin-bottom:8px'>
        <strong>👤 {row['Name']}</strong> – ⭐ {row['Rating']}<br>
        <i>{row['Feedback']}</i><br>
        <small>🕒 {row['Timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)
