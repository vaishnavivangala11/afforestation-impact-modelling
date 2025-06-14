import streamlit as st
import pandas as pd
import pathlib

st.set_page_config(page_title="View Quiz Submissions", page_icon="📄")

st.title("📄 Quiz Submissions Log")

# Path to the results CSV file
quiz_log_file = pathlib.Path("app") / "quiz_results.csv"

# Check if the file exists and is not empty
if quiz_log_file.exists() and quiz_log_file.stat().st_size > 0:
    try:
        df = pd.read_csv(quiz_log_file)
        st.dataframe(df)
    except Exception as e:
        st.error(f"⚠️ Couldn't read the file: {e}")
else:
    st.info("No submissions found yet.")
