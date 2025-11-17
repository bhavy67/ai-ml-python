# Import the literal_eval library to safely evaluate string input as a Python 
from ast import literal_eval

# Taking input
n = int(input())
arr = literal_eval(input())

def find_elements_twice(arr):
    freq = {}
    
    # Count occurrences
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Filter numbers that appear exactly twice and sort them
    result = sorted([num for num, count in freq.items() if count == 2])
    
    return result

# Print the output
print(find_elements_twice(arr))