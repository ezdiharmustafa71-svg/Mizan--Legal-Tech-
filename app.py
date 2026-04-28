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

    # 🔍 Debug (مهم الآن فقط)
    st.write("DEBUG TEXT:")
    st.write(content)

    result = analyze_contract(content)
    st.write("### Results:")
    st.write(result)
