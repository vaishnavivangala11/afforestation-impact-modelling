import streamlit as st
import pandas as pd
from datetime import datetime
import pathlib

st.set_page_config(page_title="CO₂ Quiz – Afforestation", page_icon="🧠")

st.title("🧠 Mini Quiz: CO₂ & Trees")
st.caption("Test your knowledge about afforestation and carbon sequestration!")

# Initialize session states
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Ask user name
name = st.text_input("👤 Enter your name to begin the quiz:")
if not name:
    st.warning("Please enter your name to start the quiz.")
    st.stop()

if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
    else:
        st.stop()

# List of 15 quiz questions
questions = [
    {"q": "What gas do trees absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Carbon Dioxide"},
    {"q": "Which part of the tree is mainly responsible for photosynthesis?", "options": ["Roots", "Stem", "Leaves", "Bark"], "answer": "Leaves"},
    {"q": "Which gas do trees release during the day?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Methane"], "answer": "Oxygen"},
    {"q": "What is the basic formula for CO₂ absorption by a tree?", "options": ["CO₂/year × Age", "CO₂/year × Age × Survival Rate × Growth Factor", "CO₂/year + Height", "Photosynthesis × CO₂"], "answer": "CO₂/year × Age × Survival Rate × Growth Factor"},
    {"q": "Which tree absorbs the most CO₂?", "options": ["Bamboo", "Neem", "Banyan", "Mango"], "answer": "Banyan"},
    {"q": "If a tree absorbs 20 kg CO₂ per year, how much in 10 years?", "options": ["200 kg", "20 kg", "100 kg", "2,000 kg"], "answer": "200 kg"},
    {"q": "What role does tree survival rate play in CO₂ calculation?", "options": ["It reduces the total CO₂ based on live trees", "It doubles the CO₂ rate", "It increases tree height", "It affects only oxygen"], "answer": "It reduces the total CO₂ based on live trees"},
    {"q": "Growth factor in CO₂ calculation is used to:", "options": ["Account for local growing conditions", "Calculate rainfall", "Estimate seed germination", "Measure tree height"], "answer": "Account for local growing conditions"},
    {"q": "Which formula helps estimate total CO₂ of 1000 trees?", "options": ["Tree CO₂ × 1000", "Tree CO₂ × 1000 × Age", "CO₂/year × Age × 1000 × Survival × Growth", "CO₂ × Leaves"], "answer": "CO₂/year × Age × 1000 × Survival × Growth"},
    {"q": "Why do we simulate CO₂ for up to 200 years in this app?", "options": ["To show extreme future climate", "For trees like Banyan or Peepal that live very long", "To confuse users", "200 years is default"], "answer": "For trees like Banyan or Peepal that live very long"},
    {"q": "Which process in trees helps convert CO₂ to oxygen?", "options": ["Transpiration", "Photosynthesis", "Respiration", "Evaporation"], "answer": "Photosynthesis"},
    {"q": "What is the best time to plant trees for survival?", "options": ["Winter", "Summer", "Monsoon", "Autumn"], "answer": "Monsoon"},
    {"q": "Which of these increases a tree’s CO₂ absorption?", "options": ["Fertilizer", "Bigger leaves", "Older age", "Both B and C"], "answer": "Both B and C"},
    {"q": "How does afforestation fight climate change?", "options": ["Increases rain", "Reduces CO₂", "Spreads pollution", "Cools soil only"], "answer": "Reduces CO₂"},
    {"q": "How many trees are needed to absorb 1 ton of CO₂ per year?", "options": ["10", "50", "100", "Depends on species"], "answer": "Depends on species"},
]

st.markdown("### Choose the correct answer for each question:")

user_answers = {}
for i, q in enumerate(questions, 1):
    all_opts = ["Select an answer"] + q["options"]
    user_answers[i] = st.radio(f"Q{i}: {q['q']}", all_opts, key=f"q{i}")

# Submit button
if st.button("✅ Submit Quiz"):
    st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    st.markdown("---")
    correct_count = 0

    for i, q in enumerate(questions, 1):
        user_ans = user_answers[i]
        correct = q["answer"]

        if user_ans == correct:
            correct_count += 1
        elif user_ans == "Select an answer":
            st.warning(f"⚠️ Q{i}: Not answered. Correct: {correct}")
        else:
            st.info(f"Q{i} submitted.")

    # 🎯 Save name and timestamp only (not score)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = pd.DataFrame([{"Name": name, "Timestamp": timestamp}])

    quiz_log_file = pathlib.Path("app") / "quiz_results.csv"
    quiz_log_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        if quiz_log_file.exists():
            if quiz_log_file.stat().st_size > 0:
                existing = pd.read_csv(quiz_log_file)
                updated = pd.concat([existing, entry], ignore_index=True)
            else:
                updated = entry
        else:
            updated = entry

        updated.to_csv(quiz_log_file, index=False)
        st.success("📝 Your participation has been recorded. Thank you!")
    except Exception as e:
        st.error(f"Error saving your submission: {e}")

    st.balloons()
    st.markdown("✅ Thanks for participating! Explore the **Learn** section to improve your knowledge.")
