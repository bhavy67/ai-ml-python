# Taking input
sentence = input()

def longest_word(sentence):
    words = sentence.split()
    
    longest = words[0]  # Start with the first word
    
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    
    return longest

# Print the output
print(longest_word(sentence))
