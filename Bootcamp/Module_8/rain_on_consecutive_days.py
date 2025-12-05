# Libraries (do not edit)
from ast import literal_eval

# Function to calculate consecutive rain probability
def calculate_consecutive_rain_probability(n):
    # Write your code here
    return 0.3 ** n
    

# Input and output processing (do not edit)
print(round(calculate_consecutive_rain_probability(literal_eval(input())), 4))