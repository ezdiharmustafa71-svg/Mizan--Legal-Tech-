import streamlit as st
import requests

st.title("📄 Contract Analyzer")

user_input = st.text_area("Paste contract text here:")

if st.button("Analyze"):
    if user_input:
    response = requests.post(
    "http://127.0.0.1:8000/analyze",
    params={"text": user_input}
)

result = response.json()

st.write("### Result")
st.write(result)
