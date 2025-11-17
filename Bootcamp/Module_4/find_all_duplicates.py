# Import the literal_eval library to evaluate string input as Python safely 
from ast import literal_eval

# Taking input
lst = literal_eval(input())

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    result = []

    for s in lst:
        if s in seen and s not in duplicates:
            result.append(s)
            duplicates.add(s)   # ensure it's only added once
        else:
            seen.add(s)

    return result

# Print the output 
print(find_duplicates(lst))
