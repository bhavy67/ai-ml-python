import math, ast
data = ast.literal_eval(input())
x, y = data

# The input tuple has been taken for you

# Write your code below
df_dx = 2 * x * y
df_dy = x**2 + 3 * (y**2)

raw_res = (round(float(df_dx), 2), round(float(df_dy), 2))
result = tuple(int(val) if val == int(val) else val for val in raw_res)

print(result)