from ast import literal_eval

# Taking the input 
rgb_values = literal_eval(input())

def check_colour_validity(rgb_values):
    R, G, B = rgb_values
    errors = False

    if not (0 <= R <= 255):
        print("Invalid R value")
        errors = True

    if not (0 <= G <= 255):
        print("Invalid G value")
        errors = True

    if not (0 <= B <= 255):
        print("Invalid B value")
        errors = True

    if not errors:
        print("Valid RGB values")

check_colour_validity(rgb_values)