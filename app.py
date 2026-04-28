CLAUSES = {
    "payment": "Payment terms",
    "termination": "Termination clause",
    "confidential": "Confidentiality clause",
    "liability": "Liability limitation",
    "governing law": "Governing law clause",
    "data": "Data ownership clause"
}

def analyze_contract(text):
    text = text.lower()
    results = []

    for key, label in CLAUSES.items():
        if key in text:
            results.append(f"Detected: {label}")

    if not results:
        return "No clauses detected."

    return "\n".join(results)
