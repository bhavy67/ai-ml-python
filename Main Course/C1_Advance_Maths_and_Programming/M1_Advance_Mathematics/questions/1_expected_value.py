import ast

# Input has been taken
data = ast.literal_eval(input())

# The outcomes and probabilities have been extracted from the input
outcomes, probabilities = data[0], data[1]

# Write your code below
if round(sum(probabilities), 10) != 1.0:
    print("Invalid input")
else:
    expected_value = sum(x * p for x, p in zip(outcomes, probabilities))
    print(round(float(expected_value), 2))