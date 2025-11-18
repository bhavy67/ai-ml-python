# Taking the input
s = input()

def count_characters(s):
    # Input validation: must be non-empty and alphabetic only
    if not s or not s.isalpha():
        return "Input must contain only alphabetic characters."
    
    s = s.lower()  # Convert to lowercase for case-insensitive counting
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    return freq

# Print the output
print(count_characters(s))
