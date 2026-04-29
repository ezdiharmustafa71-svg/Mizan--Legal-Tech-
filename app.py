import streamlit as st
from openai import OpenAI

# =========================
# 🔐 OpenAI Client Setup
# =========================
client = OpenAI(api_key="PUT_YOUR_API_KEY_HERE")

# =========================
# 🧠 Prompt (System Brain)
# =========================
SYSTEM_PROMPT = """
You are an expert legal contract analyst.

Analyze the contract and return a structured, simple report for non-lawyers.

Rules:
- Use simple language
- Use bullet points
- Highlight risks with ⚠️
- Keep structure exactly

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
- 3–5 simple lines
"""

# =========================
# 🤖 AI Function
# =========================
def analyze_contract(contract_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": contract_text}
        ]
    )
    return response.choices[0].message.content


# =========================
# 🖥️ UI (Streamlit)
# =========================
st.title("Mizan AI Contract Analyzer")

contract = st.text_area("Paste your contract here:")

if st.button("Analyze"):
    if contract.strip():
        with st.spinner("Analyzing contract with AI..."):
            result = analyze_contract(contract)
        st.markdown(result)
    else:
        st.warning("Please paste a contract first.")
