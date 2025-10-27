# Taking input
days_late = int(input())

# Write your code here
if days_late <= 7:
    fine = 0
elif days_late <= 15:
    fine = (days_late-7)*2
else:
    fine = 16+(days_late-15)*5
# Print the output
print(fine)