# Taking input
n = int(input())

def digit_product(n):
    if n < 10:
        return n
    return (n%10) * digit_product(n//10)

# Print the output
print(digit_product(n))