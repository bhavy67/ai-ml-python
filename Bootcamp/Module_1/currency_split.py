# Taking input
amount = int(input())

hundreds = amount // 100
amount = amount % 100

fifties = amount // 50
amount = amount % 50

tens = amount // 10
amount = amount % 10

ones = amount

# Print the result
print(hundreds, fifties, tens, ones)