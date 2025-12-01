# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
ticket = literal_eval(input())
history = literal_eval(input())

def is_valid_ticket(ticket, history):
    
    for num in ticket:
        if num < 1 or num > 49:
            return False
    
    if len(ticket) != len(set(ticket)):
        return False

    sorted_ticket = tuple(sorted(ticket))
    
    if sorted_ticket in history:
        return False

    return True

# Print the output
print(is_valid_ticket(ticket, history))