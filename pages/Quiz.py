import streamlit as st
import pandas as pd
import pathlib
from datetime import datetime

# Page settings
st.set_page_config(page_title="CO₂ Quiz – Afforestation", page_icon="🧠")

# Title
st.title("🧠 Mini Quiz: CO₂ & Trees")
st.caption("Test your knowledge about afforestation and carbon sequestration!")

# Session states
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Name entry
name = st.text_input("👤 Enter your name to begin the quiz:")
if not name:
    st.warning("Please enter your name to start the quiz.")
    st.stop()

# Start button
if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
    else:
        st.stop()

# Quiz questions
questions = [
    {"q": "What gas do trees absorb from the atmosphere?",
     "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
     "answer": "Carbon Dioxide"},

    {"q": "Which part of the tree does photosynthesis?",
     "options": ["Roots", "Stem", "Leaves", "Bark"],
     "answer": "Leaves"},

    {"q": "Which gas is released by trees during the day?",
     "options": ["Carbon Dioxide", "Oxygen", "Methane", "Hydrogen"],
     "answer": "Oxygen"},

    {"q": "What is the formula for CO₂ absorption?",
     "options": ["CO₂/year × Age", "CO₂ × Height", "CO₂/year × Age × Survival × Growth", "CO₂ + Water"],
     "answer": "CO₂/year × Age × Survival × Growth"},

    {"q": "Which tree is best for CO₂ absorption?",
     "options": ["Bamboo", "Neem", "Banyan", "Peepal"],
     "answer": "Banyan"},

    {"q": "If a tree absorbs 20 kg CO₂/year, how much in 10 years?",
     "options": ["200 kg", "20 kg", "100 kg", "2,000 kg"],
     "answer": "200 kg"},

    {"q": "What does tree survival rate affect?",
     "options": ["Tree height", "Only oxygen", "Rainfall", "Live tree CO₂ count"],
     "answer": "Live tree CO₂ count"},

    {"q": "Growth factor is used to:",
     "options": ["Estimate seeds", "Calculate rainfall", "Adjust for conditions", "Measure diameter"],
     "answer": "Adjust for conditions"},

    {"q": "How do we calculate CO₂ for 1000 trees?",
     "options": ["Tree CO₂ × 1000", "CO₂ × Age", "CO₂ × 1000 × Growth", "CO₂/year × Age × 1000 × Survival × Growth"],
     "answer": "CO₂/year × Age × 1000 × Survival × Growth"},

    {"q": "Why simulate CO₂ for 200 years?",
     "options": ["Random default", "To confuse users", "For long-living trees", "Because it's a round number"],
     "answer": "For long-living trees"},

    {"q": "What is afforestation?",
     "options": ["Cutting forests", "Planting new forests", "Removing CO₂", "Creating buildings"],
     "answer": "Planting new forests"},

    {"q": "What causes deforestation?",
     "options": ["Urbanization", "Forest fire", "Logging", "All of the above"],
     "answer": "All of the above"},

    {"q": "How do trees help cool the earth?",
     "options": ["Shade", "Carbon absorption", "Transpiration", "All of the above"],
     "answer": "All of the above"},

    {"q": "What is photosynthesis?",
     "options": ["Tree respiration", "Process to absorb CO₂ and release O₂", "Tree aging", "Root growth"],
     "answer": "Process to absorb CO₂ and release O₂"},

    {"q": "What part of a tree stores most CO₂?",
     "options": ["Roots", "Leaves", "Wood/Biomass", "Bark"],
     "answer": "Wood/Biomass"},
]

# Show quiz
st.markdown("### Choose the correct answer for each question:")
user_answers = {}
score = 0

for i, q in enumerate(questions, 1):
    user_answers[i] = st.radio(
        f"Q{i}: {q['q']}",
        ["Select an answer"] + q["options"],
        key=f"q{i}"
    )

# Submit button
if st.button("✅ Submit Quiz"):
    st.session_state.quiz_submitted = True

# Results
if st.session_state.quiz_submitted:
    st.markdown("---")
    for i, q in enumerate(questions, 1):
        user_ans = user_answers[i]
        correct = q["answer"]
        if user_ans == correct:
            score += 1
        elif user_ans == "Select an answer":
            st.warning(f"⚠️ Q{i}: Not answered. Correct: {correct}")
        else:
            st.info(f"ℹ️ Q{i}: Correct Answer: {correct}")

    # 🎯 Don’t show score, just encouragement
    if score == len(questions):
        st.balloons()
        st.success("🎉 Excellent! You're a CO₂ champion!")
    elif score >= 10:
        st.success("👍 Good job! You know your trees and climate.")
    else:
        st.info("📘 Keep learning! Visit the **Learn** section for help.")

    # Save result without showing score
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = pd.DataFrame([{"Name": name, "Timestamp": timestamp}])

        quiz_log_file = pathlib.Path("app") / "quiz_results.csv"
        quiz_log_file.parent.mkdir(parents=True, exist_ok=True)

                if quiz_log_file.exists():
            if quiz_log_file.stat().st_size > 0:
                existing = pd.read_csv(quiz_log_file)
                updated = pd.concat([existing, entry], ignore_index=True)
            else:
                updated = entry  # File exists but is empty
        else:
            updated = entry  # File doesn't exist yet


        updated.to_csv(quiz_log_file, index=False)
        st.success("📝 Your participation has been recorded. Thank you!")

    except Exception as e:
        st.error("⚠️ Error saving your submission.")
        st.exception(e)
