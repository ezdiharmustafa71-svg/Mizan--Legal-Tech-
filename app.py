import streamlit as st
from openai import OpenAI

# =========================
# 🔐 Secure API Key
# =========================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# =========================
# 🧠 Prompt
# =========================
SYSTEM_PROMPT = """
You are an expert legal contract analyst.

Analyze the contract and return a structured, simple report for non-lawyers.

Rules:
- Use simple language
- Use bullet points
- Highlight risks with ⚠️

Format:

## Key Clauses
- ...

## Payment Terms
- ...

## Termination Clause
- ...

## Confidentiality
- ...

## Key Risks ⚠️
- ...

## Governing Law
- ...

## Summary
- 3-5 simple lines
"""

# =========================
# 🤖 AI Function
# =========================
def analyze_contract(contract_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": contract_text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"

# =========================
# 🖥️ UI
# =========================
st.title("⚖️ Mizan AI Contract Analyzer")

contract = st.text_area("Paste your contract here:")

if st.button("Analyze"):
    if contract.strip():
        with st.spinner("Analyzing contract with AI..."):
            result = analyze_contract(contract)
        st.markdown(result)
    else:
        st.warning("Please paste a contract first.")
