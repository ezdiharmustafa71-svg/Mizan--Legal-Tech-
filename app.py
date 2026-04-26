import streamlit as st
import requests

st.title("📄 Contract Analyzer")

user_input = st.text_area("Paste contract text here:")

if st.button("Analyze"):
    if user_input:
        st.write("Analyzing...")
