# Taking Inputs
name = input()
balance = float(input())

class BankAccount:
    def __init__(self, name, balance):
        # Initialize instance attributes
        self.name = name
        self.balance = balance

    def show_balance(self):
        # Print the formatted string using the instance attributes
        print(f"Name: {self.name}, Balance: {self.balance}")

# Create object
account = BankAccount(name, balance)

# Call the instance method to print the result
account.show_balance()