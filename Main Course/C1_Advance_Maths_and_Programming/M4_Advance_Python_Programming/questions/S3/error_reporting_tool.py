# Taking Input
s = str(input())

def extract_number(s):
    try:
        result = int(s)
    except ValueError:
        result = "Invalid input"
    finally:
        print("Attempted conversion")
    
    return result

# Print the output
print(extract_number(s))