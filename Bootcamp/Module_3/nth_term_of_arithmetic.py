# Taking input
a = int(input())
d = int(input())
n_term = int(input())

def find_nth_arithmetic_term(a, d, n_term):
    return a + (n_term - 1) * d
         
# Print the result
print(find_nth_arithmetic_term(a, d, n_term))