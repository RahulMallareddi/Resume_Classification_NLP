import streamlit as st
from streamlit.logger import get_logger

st.set_page_config(
    page_title="Welcome Screen",
    page_icon="👋",
)


st.markdown("<h1 style='text-align: center; color: white;'>Resume Classification</h1>", unsafe_allow_html=True)
st.image("img/animated-resume.jpg", caption="Analyzing Resumes")
st.write("Resume classification involves categorizing resumes based on certain criteria such as job titles, skills, experience levels, and industries. This process can help streamline the recruitment process by quickly identifying candidates who match specific job requirements.")

