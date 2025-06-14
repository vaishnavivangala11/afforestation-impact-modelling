import streamlit as st
import pandas as pd
from datetime import datetime
import pathlib

# Page config
st.set_page_config(page_title="CO₂ Quiz – Afforestation", page_icon="🧠")

st.title("🧠 Mini Quiz: CO₂ & Trees")
st.caption("Test your knowledge about afforestation and carbon sequestration!")

# Session state initialization
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Ask for name before starting
name = st.text_input("👤 Enter your name to begin the quiz:")
if not name:
    st.warning("Please enter your name to start the quiz.")
    st.stop()

if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
    else:
        st.stop()

# Quiz Questions (15 total)
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
    {"q": "What does photosynthesis require besides CO₂?", "options": ["Sunlight and water", "Nitrogen", "Oxygen", "Heat only"], "answer": "Sunlight and water"},
    {"q": "What does deforestation lead to?", "options": ["More CO₂ in air", "Faster rain", "Bigger leaves", "Less oxygen"], "answer": "More CO₂ in air"},
    {"q": "What is a carbon sink?", "options": ["A system that absorbs more CO₂ than it emits", "A pipe that removes CO₂", "A tree hole", "A mountain lake"], "answer": "A system that absorbs more CO₂ than it emits"},
    {"q": "Which type of tree is best for coastal areas like Kakinada?", "options": ["Mangroves", "Cactus", "Pine", "Bamboo"], "answer": "Mangroves"},
    {"q": "What is one benefit of planting native tree species?", "options": ["Better survival and CO₂ capture", "They grow taller", "They are colorful", "They require fertilizers"], "answer": "Better survival and CO₂ capture"},
]

st.markdown("### Choose the correct answer for each question:")

user_answers = {}
score = 0

# Quiz UI
for i, q in enumerate(questions, 1):
    all_options = ["Select an answer"] + q["options"]
    user_answers[i] = st.radio(f"Q{i}: {q['q']}", all_options, key=f"q{i}")

# Submit Button
if st.button("✅ Submit Quiz"):
    st.session_state.quiz_submitted = True

# Result Logic
if st.session_state.quiz_submitted:
    st.markdown("---")
    for i, q in enumerate(questions, 1):
        user_ans = user_answers[i]
        correct = q["answer"]
        if user_ans == correct:
            score += 1
            st.success(f"✅ Q{i}: Correct!")
        elif user_ans == "Select an answer":
            st.warning(f"⚠️ Q{i}: Not answered. Correct answer: {correct}")
        else:
            st.error(f"❌ Q{i}: Incorrect. Correct answer: {correct}")

    # 🎯 Do not show score to user
    # st.success(f"🎯 Your Score: **{score} out of {len(questions)}**")

    # 📝 Save Submission
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = pd.DataFrame([{"Name": name, "Timestamp": timestamp}])
        quiz_log_file = pathlib.Path("app") / "quiz_results.csv"
        quiz_log_file.parent.mkdir(parents=True, exist_ok=True)

        if quiz_log_file.exists() and quiz_log_file.stat().st_size > 0:
            try:
                existing = pd.read_csv(quiz_log_file)
                updated = pd.concat([existing, entry], ignore_index=True)
            except pd.errors.EmptyDataError:
                updated = entry
        else:
            updated = entry

        updated.to_csv(quiz_log_file, index=False)
        st.success("📝 Your participation has been recorded. Thank you!")
    except Exception as e:
        st.error(f"Error saving your submission: {e}")

    st.balloons()
    st.markdown("🎉 Excellent! You're part of the green future!")
    st.write(f"Saving to: {quiz_log_file}")

