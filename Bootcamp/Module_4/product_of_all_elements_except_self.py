# Import the literal_eval library to safely evaluate string input as a Python 
from ast import literal_eval

# Taking input
n = int(input())
arr = literal_eval(input())

def product_except_self(arr):
    if len(arr) == 1:
        return [1]
    
    n = len(arr)
    result = [1] * n
    
    # Step 1: Build prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]
    
    # Step 2: Multiply with suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]
    
    return result

# Print the output
print(product_except_self(arr))