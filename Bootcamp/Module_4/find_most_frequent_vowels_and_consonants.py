# Taking input 
s = input()

def max_vowel_consonant_sum(s):
    vowels = set("aeiou")
    
    vowel_max = 0
    consonant_max = 0
    
    freq = {}
    
    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Determine max vowel and consonant frequency
    for char, count in freq.items():
        if char in vowels:
            vowel_max = max(vowel_max, count)
        else:
            consonant_max = max(consonant_max, count)
    
    return vowel_max + consonant_max

# Print the output
print(max_vowel_consonant_sum(s))
