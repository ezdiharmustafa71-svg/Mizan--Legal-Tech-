CLAUSE_WEIGHTS = {
    "liability": 0.4,
    "payment_terms": 0.2,
    "termination": 0.2
}

SEVERITY_SCORE = {
    "low": 1,
    "medium": 5,
    "high": 10
}

def calculate_risk_score(clauses):
    total = 0
    max_score = 0

    for c in clauses:
        weight = CLAUSE_WEIGHTS.get(c["type"], 0.1)
        score = SEVERITY_SCORE[c["severity"]]

        total += weight * score
        max_score += weight * 10

    if max_score == 0:
        return 0

    return round((total / max_score) * 10, 2)
