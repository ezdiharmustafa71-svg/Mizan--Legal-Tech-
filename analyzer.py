def analyze_text(text):
    clauses = []

    text = text.lower()

    if "liability" in text:
        clauses.append({"type": "liability", "severity": "high"})

    if "payment" in text:
        clauses.append({"type": "payment_terms", "severity": "medium"})

    if "termination" in text:
        clauses.append({"type": "termination", "severity": "medium"})

    return clauses
