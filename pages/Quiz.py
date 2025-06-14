import streamlit as st
import pandas as pd
from datetime import datetime
import pathlib

st.set_page_config(page_title="CO₂ Quiz – Afforestation", page_icon="🧠")
st.title("🧠 Mini Quiz: CO₂ & Trees")
st.caption("Test your knowledge about afforestation and carbon sequestration!")

# Session state setup
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Get user name
name = st.text_input("👤 Enter your name to begin the quiz:")
if not name:
    st.warning("Please enter your name to start the quiz.")
    st.stop()

# Start quiz button
if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
    else:
        st.stop()

# ✅ Quiz questions
questions = [
    {"q": "What gas do trees absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Carbon Dioxide"},
    {"q": "Which part of the tree is mainly responsible for photosynthesis?", "options": ["Roots", "Stem", "Leaves", "Bark"], "answer": "Leaves"},
    {"q": "Which gas do trees release during the day?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Methane"], "answer": "Oxygen"},
    {"q": "What is the formula for CO₂ absorption?", "options": ["CO₂/year × Age", "CO₂/year × Age × Survival × Growth", "CO₂/year + Height", "Photosynthesis × CO₂"], "answer": "CO₂/year × Age × Survival × Growth"},
    {"q": "Which tree absorbs the most CO₂?", "options": ["Bamboo", "Neem", "Banyan", "Mango"], "answer": "Banyan"},
    {"q": "How much CO₂ does a tree absorb in 10 years if it absorbs 20 kg/year?", "options": ["200 kg", "20 kg", "100 kg", "2,000 kg"], "answer": "200 kg"},
    {"q": "What does the survival rate affect?", "options": ["Doubles CO₂", "Only height", "Reduces CO₂ based on live trees", "Affects oxygen"], "answer": "Reduces CO₂ based on live trees"},
    {"q": "Growth factor in CO₂ calculation is for:", "options": ["Rainfall", "Germination", "Tree height", "Local conditions"], "answer": "Local conditions"},
    {"q": "Formula for 1000 trees CO₂?", "options": ["CO₂ × 1000", "CO₂ × 1000 × Age", "CO₂/year × Age × 1000 × Survival × Growth", "CO₂ × Leaves"], "answer": "CO₂/year × Age × 1000 × Survival × Growth"},
    {"q": "Why simulate CO₂ up to 200 years?", "options": ["Confuse users", "Long-living trees like Banyan", "Extreme climate", "200 years is default"], "answer": "Long-living trees like Banyan"},
    {"q": "What is afforestation?", "options": ["Cutting trees", "Planting new forests", "Burning trees", "None"], "answer": "Planting new forests"},
    {"q": "What is deforestation?", "options": ["Tree multiplication", "Saving trees", "Clearing forests", "Replanting"], "answer": "Clearing forests"},
    {"q": "Which SDG is related to Life on Land?", "options": ["SDG 13", "SDG 15", "SDG 10", "SDG 7"], "answer": "SDG 15"},
    {"q": "What’s one benefit of trees?", "options": ["Release CO₂", "Increase heat", "Give oxygen", "Make deserts"], "answer": "Give oxygen"},
    {"q": "How can communities support afforestation?", "options": ["Cut forests", "Burn leaves", "Organize plantation drives", "Ignore it"], "answer": "Organize plantation drives"},
]

st.markdown("### Choose the correct answer for each question:")
user_answers = {}
score = 0

# Show questions
for i, q in enumerate(questions, 1):
    options = ["Select an answer"] + q["options"]
    user_answers[i] = st.radio(f"Q{i}: {q['q']}", options, key=f"q{i}")

# Submit
if st.button("✅ Submit Quiz"):
    st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    for i, q in enumerate(questions, 1):
        if user_answers[i] == q["answer"]:
            score += 1

    # ✅ SHOW SCORE to user only
    st.markdown("---")
    st.success(f"🎯 Your Score: **{score} / {len(questions)}**")

    if score == len(questions):
        st.balloons()
        st.markdown("🎉 Excellent! You're a CO₂ champion! 💚")
    elif score >= 10:
        st.markdown("👍 Good job! You know your trees and CO₂.")
    else:
        st.markdown("📘 Keep learning! Visit the **Learn** section to improve your knowledge.")

    # ✅ SAVE ONLY NAME AND TIME (not score)
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = pd.DataFrame([{"Name": name, "Timestamp": timestamp}])
        log_file = pathlib.Path("app") / "quiz_results.csv"
        log_file.parent.mkdir(parents=True, exist_ok=True)

        if log_file.exists() and log_file.stat().st_size > 0:
            existing = pd.read_csv(log_file)
            updated = pd.concat([existing, entry], ignore_index=True)
        else:
            updated = entry

        updated.to_csv(log_file, index=False)
        st.success("📝 Your participation has been recorded.")
    except Exception as e:
        st.error("⚠️ Error saving your submission.")
