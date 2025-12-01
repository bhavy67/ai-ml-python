# Taking the input 
n = int(input())
identical_counts = list(map(int, input().split()))

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate the number of unique ways to arrange t-shirts
def calculate_arrangements(n, identical_counts):
    numerator = factorial(n)
    denominator = 1
    for count in identical_counts:
        denominator *= factorial(count)
    
    return float(numerator / denominator)

# Print the output 
print(calculate_arrangements(n, identical_counts))