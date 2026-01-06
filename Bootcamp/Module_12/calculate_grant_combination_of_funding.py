from ast import literal_eval
from math import comb

def calculate_grant_combinations(total_proposals, new_pi_proposals, established_pi_proposals,max_new_pi_grants, total_grants_to_award):
    total_ways = 0
    max_k = min(max_new_pi_grants, total_grants_to_award)
    
    for k in range(max_k + 1):
        if total_grants_to_award - k <= established_pi_proposals:
            total_ways += (
                comb(new_pi_proposals, k) *
                comb(established_pi_proposals, total_grants_to_award - k)
            )
    
    return total_ways


# (do not edit)
print(calculate_grant_combinations(*literal_eval(input())))