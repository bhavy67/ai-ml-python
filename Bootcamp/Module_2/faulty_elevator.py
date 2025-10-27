# Read inputs
u = int(input())
d = int(input())
target = int(input())

# Write your code here
curr_floor = 0
moves = 0

while curr_floor < target:
    curr_floor+=u
    moves+=1
    if curr_floor >= target:
        break
    curr_floor -= d

# Print the output
print(moves)