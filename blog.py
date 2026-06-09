import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6JPMAzY54tHq45dskKdaNW3JON2mqwXPAaMfluPSRr3uw")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"you are a Blog Post Generator. Give content for the given topic")
    st.write(res.text)