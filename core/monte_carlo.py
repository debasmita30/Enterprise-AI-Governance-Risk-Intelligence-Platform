import numpy as np

def simulate_cost_risk(base_cost, budget, simulations=1000):
    simulated_scores = []
    for _ in range(simulations):
        fluctuation = np.random.normal(0, 0.1)
        simulated_cost = base_cost * (1 + fluctuation)
        ratio = simulated_cost / budget if budget > 0 else 1
        if ratio <= 0.5:
            simulated_scores.append(20)
        elif ratio <= 1:
            simulated_scores.append(50)
        else:
            simulated_scores.append(90)
    return np.mean(simulated_scores)