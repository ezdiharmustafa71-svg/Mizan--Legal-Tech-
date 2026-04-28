import streamlit as st

st.set_page_config(page_title="Contract Analyzer", layout="centered")

st.title("📄 Contract Analyzer")
st.caption("AI-powered contract clause detection (MVP version)")

user_input = st.text_area("Paste your contract here")

CLAUSES = {
    "payment": "Payment Terms",
    "termination": "Termination Clause",
    "confidential": "Confidentiality Clause",
    "liability": "Liability Limitation",
    "governing law": "Governing Law Clause",
    "data": "Data Ownership Clause"
}

def analyze_contract(text):
    text = text.lower()
    results = []

    for key, label in CLAUSES.items():
        if key in text:
            results.append(f"⚠️ {label}")

    if not results:
        return ["✅ No clauses detected"]

    return results

if st.button("Analyze Contract"):
    result = analyze_contract(user_input)

    st.markdown("## 📊 Analysis Results")

    for item in result:
        if "⚠️" in item:
            st.error(item)
        else:
            st.success(item)
