import streamlit as st
import pandas as pd
import pathlib
from datetime import datetime

# ✅ This must be the first Streamlit command
st.set_page_config(page_title="CO₂ Quiz – Afforestation", page_icon="🧠")

# 🧠 Page Title
st.title("🧠 Mini Quiz: CO₂ & Trees")
st.caption("Test your knowledge about afforestation and carbon sequestration!")

# Session states
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Ask for name before quiz
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

# Quiz Questions
questions = [
    {
        "q": "What gas do trees absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
        "answer": "Carbon Dioxide"
    },
    {
        "q": "Which part of the tree is mainly responsible for photosynthesis?",
        "options": ["Roots", "Stem", "Leaves", "Bark"],
        "answer": "Leaves"
    },
    {
        "q": "Which gas do trees release during the day?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Methane"],
        "answer": "Oxygen"
    },
    {
        "q": "What is the basic formula for CO₂ absorption by a tree?",
        "options": [
            "CO₂/year × Age",
            "CO₂/year × Age × Survival Rate × Growth Factor",
            "CO₂/year + Height",
            "Photosynthesis × CO₂"
        ],
        "answer": "CO₂/year × Age × Survival Rate × Growth Factor"
    },
    {
        "q": "Which tree absorbs the most CO₂?",
        "options": ["Bamboo", "Neem", "Banyan", "Mango"],
        "answer": "Banyan"
    },
    {
        "q": "If a tree absorbs 20 kg CO₂ per year, how much in 10 years?",
        "options": ["200 kg", "20 kg", "100 kg", "2,000 kg"],
        "answer": "200 kg"
    },
    {
        "q": "What role does tree survival rate play in CO₂ calculation?",
        "options": [
            "It reduces the total CO₂ based on live trees",
            "It doubles the CO₂ rate",
            "It increases tree height",
            "It affects only oxygen"
        ],
        "answer": "It reduces the total CO₂ based on live trees"
    },
    {
        "q": "Growth factor in CO₂ calculation is used to:",
        "options": [
            "Account for local growing conditions",
            "Calculate rainfall",
            "Estimate seed germination",
            "Measure tree height"
        ],
        "answer": "Account for local growing conditions"
    },
    {
        "q": "Which formula helps estimate total CO₂ of 1000 trees?",
        "options": [
            "Tree CO₂ × 1000",
            "Tree CO₂ × 1000 × Age",
            "CO₂/year × Age × 1000 × Survival × Growth",
            "CO₂ × Leaves"
        ],
        "answer": "CO₂/year × Age × 1000 × Survival × Growth"
    },
    {
        "q": "Why do we simulate CO₂ for up to 200 years in this app?",
        "options": [
            "To show extreme future climate",
            "For trees like Banyan or Peepal that live very long",
            "To confuse users",
            "200 years is default"
        ],
        "answer": "For trees like Banyan or Peepal that live very long"
    },
    # ✅ Extra CO₂ Formula Questions
    {
        "q": "If a tree absorbs 25 kg CO₂/year, survives 80%, and growth factor is 1.2, how much in 10 years?",
        "options": ["240 kg", "2400 kg", "1000 kg", "240 kg × 1.2 × 0.8"],
        "answer": "240 kg × 1.2 × 0.8"
    },
    {
        "q": "What does 'Survival Rate' of 0.6 mean in a plantation of 1000 trees?",
        "options": ["600 trees survive", "60 trees survive", "400 trees survive", "100 trees survive"],
        "answer": "600 trees survive"
    },
    {
        "q": "Which value affects total CO₂ most in formula?",
        "options": ["Survival Rate", "Leaf color", "Rainfall", "Planting month"],
        "answer": "Survival Rate"
    },
    {
        "q": "If 1 tree absorbs 22 kg/year, what's total for 50 trees in 5 years?",
        "options": ["5500 kg", "220 kg", "550 kg", "None"],
        "answer": "5500 kg"
    },
    {
        "q": "In CO₂ formula, what is multiplied with CO₂/year, Age, Tree Count?",
        "options": ["Soil type", "Species", "Survival × Growth factor", "Sunlight"],
        "answer": "Survival × Growth factor"
    }
]

# Display Questions
st.markdown("### Choose the correct answer for each question:")
user_answers = {}
score = 0

for i, q in enumerate(questions, 1):
    all_options = ["Select an answer"] + q["options"]
    user_answers[i] = st.radio(f"Q{i}: {q['q']}", all_options, key=f"q{i}")

# Submit
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
            st.success(f"✅ Q{i}: Correct! ({correct})")
        elif user_ans == "Select an answer":
            st.warning(f"⚠️ Q{i}: Not answered. Correct answer: {correct}")
        else:
            st.error(f"❌ Q{i}: Incorrect. You chose '{user_ans}'. Correct is: {correct}")

    st.markdown("---")
    st.success(f"🎯 Your Score: **{score} out of {len(questions)}**")

    # Save participation if perfect score
    if score == len(questions):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = pd.DataFrame([{"Name": name, "Timestamp": timestamp}])
        quiz_log_file = pathlib.Path("app") / "quiz_results.csv"
        quiz_log_file.parent.mkdir(parents=True, exist_ok=True)

        if quiz_log_file.exists():
            existing = pd.read_csv(quiz_log_file)
            updated = pd.concat([existing, entry], ignore_index=True)
        else:
            updated = entry

        updated.to_csv(quiz_log_file, index=False)
        st.success("📝 Your participation has been recorded. Thank you!")
        st.balloons()
        st.markdown("🎉 Excellent! You're a CO₂ champion! 💚")
    elif score >= 10:
        st.markdown("👍 Good job! You know your trees and CO₂.")
    else:
        st.markdown("📘 Keep learning! Try the **Learn** section for more info.")

    # Retake option
    if st.button("🔁 Retake Quiz"):
        st.session_state.quiz_started = False
        st.session_state.quiz_submitted = False
        st.rerun()
