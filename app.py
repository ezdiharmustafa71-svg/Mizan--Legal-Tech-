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
