#Taking input
num = int(input())

def is_armstrong(num):
    original = num
    total = 0
    
    while num > 0:
        digit = num % 10
        total += digit * digit * digit
        num //= 10
    
    if total == original:
        return "Yes"
    else:
        return "No"
     
# Print the output
print(is_armstrong(num))
