import math, ast
data = ast.literal_eval(input())
u, v = data

# Input has been taken for you and the lists u and v have been extracted
# Write your code below
if len(u) != len(v):
    print("Invalid input")
else:
    mag_u = math.sqrt(sum(x**2 for x in u))
    mag_v = math.sqrt(sum(x**2 for x in v))
    
    dot_prod = sum(ui * vi for ui, vi in zip(u, v))

    result = (round(mag_u, 2), round(mag_v, 2), round(dot_prod, 2))
    print(result)