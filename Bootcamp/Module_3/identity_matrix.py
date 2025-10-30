# Taking input
N = int(input())

# Write your code
for i in range(N):
    for j in range(N):
        if i == j:
            print(1)
        else:
            print(0)
    print()