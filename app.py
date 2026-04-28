import streamlit as st

st.title("Contract Analyzer")

user_input = st.text_area("Paste your contract here")

def analyze_contract(text):
    # تحليل بسيط مبدئي
    if "payment" in text.lower():
        return "⚠️ This contract includes payment terms."
    elif "termination" in text.lower():
        return "⚠️ This contract includes termination clauses."
    else:
        return "✅ No major risks detected (basic scan)."

if st.button("Analyze"):
    if user_input:
        result = analyze_contract(user_input)
        st.write("### Analysis Result:")
        st.write(result)
    else:
        st.warning("Please enter contract text.")
