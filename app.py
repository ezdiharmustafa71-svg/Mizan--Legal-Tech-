import streamlit as st

st.title("Legal Contract Risk Analyzer")

uploaded_file = st.file_uploader("Upload Contract (txt)", type=["txt"])

def analyze_contract(text):
    text_lower = text.lower()

    findings = []
    risk_score = 0

    # Clause detection + scoring
    if "termination" in text_lower:
        findings.append(("Termination Clause", "Medium"))
        risk_score += 2

    if "liability" in text_lower:
        findings.append(("Liability Clause", "High"))
        risk_score += 3

    if "payment" in text_lower:
        findings.append(("Payment Terms Issue", "Medium"))
        risk_score += 2

    # Risk level classification
    if risk_score <= 2:
        level = "🟢 Low Risk"
    elif risk_score <= 5:
        level = "🟡 Medium Risk"
    else:
        level = "🔴 High Risk"

    return findings, risk_score, level


if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")

    st.write("## 📄 Contract Content")
    st.write(content)

    findings, score, level = analyze_contract(content)

    st.write("## 🧠 Analysis Report")
    st.write(f"### Overall Risk: {level}")
    st.write(f"### Risk Score: {score}")

    st.write("### Detected Clauses:")

    for item, severity in findings:
        if severity == "High":
            st.error(f"{item} → {severity} Risk")
        elif severity == "Medium":
            st.warning(f"{item} → {severity} Risk")
