# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input 
consonants = literal_eval(input())
vowels = literal_eval(input())

syllables = []

if consonants and vowels:
    for c in consonants:
        for v in vowels:
            syllables.append(c + v)

syllables.sort()

# Print the output in required format
print([len(syllables), syllables])