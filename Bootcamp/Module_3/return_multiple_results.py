# Taking input
n = int(input())

def compute_values(n):
    return n**2, n**3, n*2
   
s, c, d = compute_values(n)

# Print the output
print(s, c, d)