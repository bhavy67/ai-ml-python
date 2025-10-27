# Taking input
n = int(input())

# Write your code here
original = n
rev = 0

while n > 0:
    digit=n%10
    rev = rev*10+digit
    n//=10

if rev == original:
    print("Palindrome")
else:
    print("Not Palindrome")