# Taking input
n = int(input())

# Write your code here
for i in range(1, n + 1):
    if i % 3 == 0 and i % 4 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 4 == 0:
        print("Buzz")
    else:
        print(i)