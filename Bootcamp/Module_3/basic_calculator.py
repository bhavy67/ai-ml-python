# Taking input
x = int(input())
y = int(input())
op = input()

def calculator(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        return x/y

# Print the output
print(calculator(x, y, op))