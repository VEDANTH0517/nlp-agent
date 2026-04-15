import streamlit as st
import requests

st.title("🤖 AI NLP Agent")

user_input = st.text_input("Enter text")

if st.button("Predict"):
    if user_input:
        response = requests.post(
            "http://127.0.0.1:8000/predict/",
            json={"text": user_input}
        )

        result = response.json()

        st.write(result)   # 👈 DEBUG LINE

        st.success(result["result"])