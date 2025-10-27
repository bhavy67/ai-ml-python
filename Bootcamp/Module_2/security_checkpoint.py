# Taking input
age = int(input())
clearance = int(input())

# Write your code here
if age >= 18 and clearance >= 3:
    result = "Access Granted"
elif 16 < age < 18 and clearance == 5:
    result = "Manual Verification Required"
else:
    result = "Access Denied"

# Print the output
print(result)