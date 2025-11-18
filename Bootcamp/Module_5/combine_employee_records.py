# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
company_a = literal_eval(input())
company_b = literal_eval(input())

def merged_employees(company_a, company_b):
    # Combine both lists and remove duplicates using a set
    unique_employees = set(company_a) | set(company_b)
    
    # Return a sorted list
    return sorted(unique_employees)

# Print the output
print(merged_employees(company_a, company_b))
