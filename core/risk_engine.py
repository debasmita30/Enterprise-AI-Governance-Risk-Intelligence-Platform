WEIGHTS = {
    "security": 0.30,
    "data_residency": 0.15,
    "compliance": 0.20,
    "cost": 0.15,
    "lock_in": 0.10,
    "sla": 0.10
}

def calculate_weighted_score(scores):
    total = 0
    for key in WEIGHTS:
        total += scores[key] * WEIGHTS[key]
    return round(total, 2)

def risk_category(score):
    if score <= 30:
        return "Low"
    elif score <= 60:
        return "Moderate"
    return "High"