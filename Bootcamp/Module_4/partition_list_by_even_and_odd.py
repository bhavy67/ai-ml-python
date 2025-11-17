# Import the literal_eval library to safely evaluate string input as a Python 
from ast import literal_eval

# Taking input
n = int(input())
arr = literal_eval(input())

def partition_even_odd(arr):
    evens = []
    odds = []
    
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    return evens + odds

# Print the output
print(partition_even_odd(arr))
