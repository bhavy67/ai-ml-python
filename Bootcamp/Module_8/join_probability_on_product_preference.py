# Libraries (do not edit)
from ast import literal_eval

def calculate_joint_probability(products_and_probabilities):
    # Your code here
    joint_prob = 1.0
    for p in products_and_probabilities.values():
        joint_prob *= p
    return joint_prob

# Input and output processing (do not edit)
print(round(calculate_joint_probability(literal_eval(input())), 4))