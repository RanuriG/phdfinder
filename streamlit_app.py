import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os
from dotenv import load_dotenv
# load_dotenv()

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]
# openai_api_key = os.getenv("OPENAI_API_KEY")
# serper_api_key = os.getenv("SERPER_API_KEY")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

icon("🎓 Find your PhD")


with st.sidebar:
    st.header('Enter the Details')
    country = st.text_input("Country that you wish to do a PhD:")
    gpa = st.text_input("Your GPA:")
    research_areas = st.text_area("Research areas that you wish to work in your PhD:")

if st.button('Run Research'):
    if not country or not gpa or not research_areas:
        st.error("Please fill all the fields.")
    else:
        # inputs = f"Research country: {country}\nGPA: {gpa}\nResearch Areas: {research_areas}"
        inputs = [country, gpa, research_areas]
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Possible PhD Opportunities:")
        st.write(result)
