# Libraries (do not edit)
from ast import literal_eval

def claim_risk_exposure(p_fire, p_flood, p_theft, p_fire_flood, p_fire_theft, p_flood_theft, p_all_three):
    # Code here
    probability = (p_fire + p_flood + p_theft - p_fire_flood - p_fire_theft - p_flood_theft + p_all_three)
    return probability

# Input and output processing (do not edit)
print(round(claim_risk_exposure(*literal_eval(input())), 2))