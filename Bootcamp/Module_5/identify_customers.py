# Import literal_eval to safely evaluate the input string as a Python list
from ast import literal_eval

# Taking the input 
purchased = literal_eval(input())
subscribed = literal_eval(input())

def analyse_customers(purchased, subscribed):
    purchased_set = set(purchased)
    subscribed_set = set(subscribed)

    # Customers who purchased and subscribed
    loyalty = sorted(list(purchased_set & subscribed_set))

    # Subscribed but did not purchase
    leads = sorted(list(subscribed_set - purchased_set))

    # Purchased but not subscribed
    inactive = sorted(list(purchased_set - subscribed_set))

    return {
        'loyalty': loyalty,
        'leads': leads,
        'inactive': inactive
    }

# Print the output
print(analyse_customers(purchased, subscribed))