# Taking input
s = input()

def count_vowels_and_consonants(s):
    vowels_set = "aeiouAEIOU"
    vowels = consonants = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
    
    return vowels, consonants

# Print the Output
vowels, consonants = count_vowels_and_consonants(s)
print(vowels)
print(consonants)
