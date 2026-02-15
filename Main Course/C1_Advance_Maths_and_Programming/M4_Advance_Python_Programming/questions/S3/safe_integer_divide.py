# Taking inputs
a = int(input())
b = int(input())

def safe_divide(a, b):
    try:
        result = float(a / b)
    except ZeroDivisionError:
        result = "Error: division by zero"
    finally:
        print("Operation attempted")
    
    return result

# Print the output
print(safe_divide(a, b))