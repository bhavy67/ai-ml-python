# Taking Input 
f = float(input())

class Temperature:
    def __init__(self, celsius):
        # Store the temperature in Celsius
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        # Apply the conversion formula: C = ((F - 32) * 5) / 9
        celsius_val = ((f - 32) * 5) / 9
        # Return a new instance of the class (Temperature object)
        return cls(round(celsius_val, 2))

# Create a Temperature object using the class method
temp_obj = Temperature.from_fahrenheit(f)

# Output the Temperature in Celsius
print(temp_obj.celsius)