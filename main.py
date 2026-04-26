from fastapi import FastAPI
from scoring import calculate_risk_score

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working 🚀"}

@app.get("/risk")
def get_risk():
    score = calculate_risk_score()
    return {"risk_score": score}
