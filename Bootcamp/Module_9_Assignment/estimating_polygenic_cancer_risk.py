# Libraries (do not edit)
from ast import literal_eval
from itertools import product

def polygenic_disease_risk(n, k, mutation_probs):
    total_prob = 0.0

    for combo in product([0, 1], repeat=n):
        if sum(combo) >= k:
            prob = 1.0
            for i in range(n):
                if combo[i] == 1:
                    prob *= mutation_probs[i]
                else:
                    prob *= (1 - mutation_probs[i])
            total_prob += prob

    return total_prob

# Input and output handling (do not edit)
print(round(polygenic_disease_risk(*literal_eval(input())), 4))