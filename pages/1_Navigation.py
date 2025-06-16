import streamlit as st

st.set_page_config(page_title="Navigation – Afforestation App", page_icon="🧭")

st.title("🧭 Explore the App Easily")
st.markdown("Tap a section to visit 👇")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🌳 Home (Model)"):
        st.switch_page("streamlit_app.py")

    if st.button("🧠 Quiz"):
        st.switch_page("pages/Quiz.py")

with col2:
    if st.button("📘 Learn"):
        st.switch_page("pages/Learn.py")

    if st.button("🌱 Green Community"):
        st.switch_page("pages/Green_Community.py")

st.markdown("---")
st.info("📱 This page is designed for easy navigation, especially on mobile!")
