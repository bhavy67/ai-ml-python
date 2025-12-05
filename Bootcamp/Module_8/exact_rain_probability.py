# Libraries (do not edit)
from ast import literal_eval

# Function to calculate rain probability in a fortnight
def calculate_rain_probability_in_fortnight(n):
    # Write your code here
    import math
    
    p = 0.3
    q = 0.7
    total_days = 14

    nCr = math.comb(total_days, n)
    probability = nCr * (p ** n) * (q ** (total_days - n))

    return probability


# Input and output processing (do not edit)
print(round(calculate_rain_probability_in_fortnight(literal_eval(input())), 4))