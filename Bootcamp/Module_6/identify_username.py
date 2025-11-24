import re

# Taking the input
text = input()

def extract_email_data(text):
    pattern = r'([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})'
    matches = re.findall(pattern, text)
    return matches

# Print the output
print(extract_email_data(text))
