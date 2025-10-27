# Taking input
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Write your code here
a = (a * b) + c

result = (a % d == 0) and (a > b) and (a > c)

# Print the output
print(result)