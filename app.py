import streamlit as st

st.title("Contract Analyzer")

# 👇 إدخال النص
user_input = st.text_area("Paste your contract here")

# 👇 القواعد
CLAUSES = {
    "payment": "Payment terms",
    "termination": "Termination clause",
    "confidential": "Confidentiality clause",
    "liability": "Liability limitation",
    "governing law": "Governing law clause",
    "data": "Data ownership clause"
}

# 👇 التحليل
def analyze_contract(text):
    text = text.lower()
    results = []

    for key, label in CLAUSES.items():
        if key in text:
            results.append(f"⚠️ Detected: {label}")

    if not results:
        return "✅ No clauses detected."

    return "\n".join(results)

# 👇 زر التحليل
if st.button("Analyze"):
    content = user_input

    # def analyze_contract(text):
    text = text.lower()
    results = []

    for key, label in CLAUSES.items():
        if key in text:
            risk = "Medium"

            if key == "liability":
                risk = "High"
            elif key == "payment":
                risk = "Medium"
            elif key == "termination":
                risk = "High"
            elif key == "confidential":
                risk = "Low"

            results.append(f"⚠️ {label} — Risk: {risk}")

    if not results:
        return "✅ No clauses detected."

    return "\n".join(results)
    st.text(result)
