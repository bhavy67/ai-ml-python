import ast

# Taking the input
today_ingredients = ast.literal_eval(input())
known_ingredients = ast.literal_eval(input())
recipe_book = ast.literal_eval(input())

def evaluate_pantry(today_ingredients, known_ingredients, recipe_book):

    # Convert to sets for easy comparison
    today_set = set(today_ingredients)
    known_set = set(known_ingredients)

    new_discoveries = sorted(list(today_set - known_set))

    brewable = []
    for potion, ingredients in recipe_book.items():
        if set(ingredients).issubset(today_set):
            brewable.append(potion)

    return [new_discoveries, brewable]

# Print the output
print(evaluate_pantry(today_ingredients, known_ingredients, recipe_book))
