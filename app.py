import streamlit as st

st.title("Contract Analyzer MVP")

uploaded_file = st.file_uploader("Upload your contract (txt)", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")

    st.write("### Contract Content")
    st.write(content)

    st.write("### Simple Analysis")

    if "termination" in content.lower():
        st.warning("Found: Termination clause")

    if "liability" in content.lower():
        st.warning("Found: Liability clause")
