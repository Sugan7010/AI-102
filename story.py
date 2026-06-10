import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6JuJCTqJsps0DYdYS9mDgHYsPHhM9LuhOEEmJmMUFA8GQ")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"Your the story teller.generate creative stories with genre selection and characters")
    st.write(res.text)