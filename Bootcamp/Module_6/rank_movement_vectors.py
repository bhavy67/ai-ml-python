# Import literal_eval to safely evaluate string input
from ast import literal_eval

# Taking the input
vectors = literal_eval(input())

def sort_by_magnitude(vectors):
    return sorted(vectors, key=lambda v: (v[0]**2 + v[1]**2)**0.5, reverse=True)

# Print the output
print(sort_by_magnitude(vectors))