# Taking input
N = int(input())

def print_pattern(N):
    odd = 1  # Start with the first odd number
    for i in range(1, N + 1):
        row = []
        for j in range(i):
            row.append(str(odd))
            odd += 2
        print(" ".join(row))

# Print the output
print_pattern(N)
