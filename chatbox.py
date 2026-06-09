import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6Jh6GyUYv7sBsV0MMF0_jfwBmMcdG9_lBS7p0FKW06icw")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns)
    st.write(res.text)