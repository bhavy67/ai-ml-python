# Taking input
n = int(input())

def check_perfect_number(n):
    if n <= 1:
        return False

    sum_of_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n

# Print the result
print(check_perfect_number(n))