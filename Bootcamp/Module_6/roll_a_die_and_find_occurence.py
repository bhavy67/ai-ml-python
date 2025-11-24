from ast import literal_eval

# Taking the input
rolls = literal_eval(input())

def find_most_frequent_number(rolls):
    frequency = {i: 0 for i in range(1, 7)}
    
    for d1, d2 in rolls:
        frequency[d1] += 1
        frequency[d2] += 1
    
    most_frequent = max(frequency, key=lambda x: (frequency[x], -x))
    return most_frequent

# Print the output
print(find_most_frequent_number(rolls))
