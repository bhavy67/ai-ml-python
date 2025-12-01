# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
preferences = literal_eval(input())

def generate_valid_pairs(preferences):
    valid_pairs = []
    
    top_two = preferences[:2]
    
    for i in range(len(preferences)):
        for j in range(i + 1, len(preferences)):
            event1 = preferences[i]
            event2 = preferences[j]
            
            if event1 in top_two or event2 in top_two:
                pair = tuple(sorted((event1, event2)))
                valid_pairs.append(pair)
    
    valid_pairs.sort()
    
    return valid_pairs

# Print the output
result = generate_valid_pairs(preferences)
print(result)