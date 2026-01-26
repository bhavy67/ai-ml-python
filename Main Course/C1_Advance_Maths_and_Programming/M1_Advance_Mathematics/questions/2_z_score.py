import math, ast
data = ast.literal_eval(input())

# Input has been taken for you as a tuple

# Write your code below
x, mu, sigma = data

if sigma <= 0:
    print("Invalid input")
else:
    z_score = (x - mu) / sigma
    print(round(float(z_score), 2))