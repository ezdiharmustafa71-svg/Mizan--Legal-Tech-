from fastapi import FastAPI
from analyzer import analyze_text
from scoring import calculate_risk_score

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working 🚀"}

@app.post("/analyze")
def analyze_contract(text: str):
    clauses = analyze_text(text)
    score = calculate_risk_score(clauses)

    return {
        "risk_score": score,
        "clauses": clauses
    }
