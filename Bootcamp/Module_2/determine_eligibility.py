# Taking input
age = int(input())
member = input()

# Write your code here
if age < 18 or age > 60:
    if member == 'Y':
        result = "20%"
    else:
        result = "10%"
else:
    if member == 'Y':
        result = "5%"
    else:
        result = "No Discount"

# Print the output
print(result)