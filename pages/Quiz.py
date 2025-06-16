import streamlit as st
import pandas as pd
import datetime
import os

# ✅ Page config
st.set_page_config(page_title="🧠 Quiz – Tree Impact", page_icon="🧠", layout="wide")

# ✅ Mobile-friendly tip
st.markdown("""
<div style="background-color: #fff9e6; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
    🧠 <strong>Tip:</strong> Tap ☰ (menu) on mobile to access <em>Home, Learn, Quiz, or Community</em> pages!
</div>
""", unsafe_allow_html=True)

# ✅ Sidebar links (only show once)
with st.sidebar:
    st.title("🧠 Navigation")
    st.markdown("[🏠 Home](./)")
    st.markdown("[📘 Learn](./Learn)")
    st.markdown("[🧠 Quiz](./Quiz)")
    st.markdown("[🌱 Green Community](./Green_Community)")

# ✅ Quiz starts
st.title("🧠 CO₂ & Tree Knowledge Quiz")

name = st.text_input("Enter your name to begin:")
score = 0

questions = [
    {"q": "Which process do trees use to absorb CO₂?", "a": "Photosynthesis"},
    {"q": "What is the formula to estimate CO₂ absorbed by a tree?", "a": "CO₂ = Age × CO₂_per_year × Survival Rate × Growth Factor"},
    {"q": "Which fast-growing water plant absorbs CO₂?", "a": "Duckweed"},
    {"q": "What type of grass is used to control erosion and store CO₂?", "a": "Vetiver"},
    {"q": "Which mission supports tree planting in India?", "a": "Green India Mission"},
    {"q": "What do we call planting trees in barren areas?", "a": "Afforestation"},
    {"q": "Name one native CO₂-absorbing tree in East Godavari.", "a": "Neem"},
    {"q": "CO₂ is a major contributor to?", "a": "Global warming"},
    {"q": "What do tree roots help conserve?", "a": "Water"},
    {"q": "Which part of vetiver helps in carbon storage?", "a": "Roots"},
    {"q": "How many trees are needed to absorb 21,000 kg of CO₂ (using 21kg per tree)?", "a": "1000"},
    {"q": "What does the survival rate in the CO₂ formula indicate?", "a": "How many trees stay alive"},
    {"q": "What is a major source of deforestation?", "a": "Urban growth"},
    {"q": "Which aquatic plant helps clean ponds and absorbs CO₂?", "a": "Duckweed"},
    {"q": "Why is it important to plant native species?", "a": "They grow well and support biodiversity"}
]

user_answers = []
if name:
    st.markdown("### Answer all 15 questions below:")
    for i, q in enumerate(questions):
        answer = st.text_input(f"{i+1}. {q['q']}")
        user_answers.append(answer)

    if st.button("✅ Submit Quiz"):
        for i in range(len(questions)):
            if user_answers[i].strip().lower() == questions[i]["a"].strip().lower():
                score += 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {"Name": [name], "Score": [score], "Time": [timestamp]}
        df = pd.DataFrame(data)

        # ✅ Save to CSV
        filename = os.path.join(os.path.dirname(__file__), "..", "quiz_submissions.csv")
        if os.path.exists(filename):
            df_existing = pd.read_csv(filename)
            df_combined = pd.concat([df_existing, df], ignore_index=True)
        else:
            df_combined = df
        df_combined.to_csv(filename, index=False)

        st.success("✅ Quiz submitted successfully!")
        st.info("📄 Your result has been saved. Thanks for participating! 🎉")
