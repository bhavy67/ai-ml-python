# Taking input 
a = input()
b = input()

def merge_alternating(a, b):
    result = []
    i = 0
    
    # Iterate while either string still has characters
    while i < len(a) or i < len(b):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
        i += 1
    
    return "".join(result)

# Print the output 
print(merge_alternating(a, b))
